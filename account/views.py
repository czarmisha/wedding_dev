from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm, ClientEditForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .models import ClientProfile
from django.contrib import messages
from tender.models import Tender

User = get_user_model()


def user_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            # Create profile for user
            new_client = ClientProfile(user=new_user, phone=123)
            new_client.save()
            new_user.clientprofile = new_client
            # Save the User object
            new_user.save()
            login(request, new_user)
            return HttpResponseRedirect(reverse('home', kwargs={}))
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/registration.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('home', kwargs={}))
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
        
    
