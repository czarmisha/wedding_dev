from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from tender.models import Tender
from django.template.loader import render_to_string
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from .models import ClientProfile, BlockList
from .forms import LoginForm, UserRegistrationForm, ClientEditForm, ChangePasswordForm

User = get_user_model()



def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Запрос на сброс пароля"
					email_template_name = "account/password/password_reset.txt"
					c = {
					"email":user.email,
					'domain':'https://toypoy.uz', #toypoy.uz
					'site_name': 'Toypoy', #
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http', #https
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'toypoy.uz@gmail.com', [user.email])
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="account/password/password_reset.html", context={"password_reset_form":password_reset_form})


def hascyr(s):
    lower = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    return lower.intersection(s.lower()) != set()


def user_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            if(User.objects.filter(email=new_user.email).exists()):
                messages.error(request, 'Пользователь с такой почтой уже зарегистрирован')
                return render(request, 'account/registration.html', {'user_form': user_form})
            if(BlockList.objects.filter(email=new_user.email).exists()):
                messages.error(request, 'Эта почта заблокирована')
                return render(request, 'account/registration.html', {'user_form': user_form})
            if hascyr(new_user.username):
                messages.error(request, 'Имя пользователя должно быть на латинице')
                return render(request, 'account/registration.html', {'user_form': user_form})
             # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            subject = "Верификация почты"
            email_template_name = "account/verify_email.txt"
            c = {
            "email":new_user.email,
            'domain':'toypoy.uz', #toypoy.uz
            'site_name': 'Toypoy', #
            "user": new_user,
            'token': default_token_generator.make_token(new_user),
            'protocol': 'https',
            }
            email = render_to_string(email_template_name, c)
            try:
                send_mail(subject, email, 'toypoy.uz@gmail.com', [new_user.email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # Create profile for user
            new_client = ClientProfile(user=new_user, phone=123)
            new_client.save()
            new_user.clientprofile = new_client
            # Save the User object
            new_user.save()
            login(request, new_user)

            return HttpResponseRedirect(new_user.get_cabinet_url())
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/registration.html', {'user_form': user_form})

def verify_email_confirm(request, *args, **kwargs):
    user = User.objects.get(pk=kwargs.get('pk'))
    if default_token_generator.check_token(user, kwargs.get('token')):
        user.clientprofile.is_active=True
        user.clientprofile.save()
        user.save()
    return HttpResponseRedirect(user.get_cabinet_url())

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(user.get_cabinet_url())
                else:
                    messages.error(request, 'Вы пытаетесь зайти в отключенный аккаунт')
            else:
                messages.error(request, 'Вы ввели неверный логин или пароль')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home', kwargs={}))


def change_password(request):
    u = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = request.POST.get("old_password")
            new_pass = request.POST.get("new_password")
            new_pass_rep = request.POST.get("new_password_rep")
            if check_password(old_password,u.password):
                if(new_pass==new_pass_rep):
                    u.set_password(new_pass)
                    u.save()
                    return HttpResponseRedirect(reverse('home', kwargs={}))
                else:
                    messages.error(request, 'Новый пароль и Повтор пароль не совпадают')
            else:
                messages.error(request, 'Вы ввели неверный старый пароль')
    else:
            form = ChangePasswordForm()

    return render(request, 'account/change_password.html',
              {'form': form})


@login_required
def client_edit(request):
    if request.user.type == 'client':
        if request.method == 'POST':
            form = ClientEditForm(request.POST, request.FILES)
            if form.is_valid():
                cd = form.cleaned_data
                try:
                    client = ClientProfile.objects.get(user=request.user)
                except:
                    messages.error(request,
                                   'Вы пытаетесь редактировать несуществующий аккаунт. Пожалуйста,'
                                   ' обратитесь к администартору сайта'
                                   )
                client.user.first_name = cd['first_name']
                client.user.last_name = cd['last_name']
                if cd['avatar']:
                    client.avatar = cd['avatar']
                client.phone = cd['phone']
                client.telegram = cd['telegram']
                # TODO: telegram/ если ошибка редирект на эту ше форму с сообщением об ишибке
                client.user.save()
                client.save()
                return HttpResponseRedirect(reverse('account:cabinet', kwargs={'pk': client.user.pk}))
        else:
            initial_dict = {
                "avatar": request.user.clientprofile.avatar if request.user.clientprofile.avatar else None,
                'first_name': request.user.first_name if request.user.first_name else None,
                'last_name': request.user.last_name if request.user.last_name else None,
                'phone': request.user.clientprofile.phone if request.user.clientprofile.phone else None,
                'telegram': request.user.clientprofile.telegram if request.user.clientprofile.telegram else None,
            }
            form = ClientEditForm(initial=initial_dict)
    else:
        messages.error(request,
                       'Вы не являетесь молодоженом! Здесь какая-то ошибка, обратитесь к администратору сайта.')
    return render(request, 'account/clientprofile_update_form.html', {'form': form})


class ClientProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = ClientProfile
    fields = ['avatar', 'phone', 'telegram', ]
    template_name_suffix = '_update_form'


class CabinetView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'account/cabinet.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(CabinetView, self).get_context_data(**kwargs)
        # if self.object.type == 'client':
        #     context['client_tenders'] = Tender.objects.filter(author=self.object)
        return context


@login_required
def my_tenders(request):
    if request.user.type == 'client':
        tenders = Tender.objects.filter(author=request.user).all()
        return render(request, 'account/my_tenders.html', {'tenders': tenders})
    else:
        return render(request, 'wedding/home.html')
        
    
