from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .models import ClientProfile
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
            return render(request, 'account/registration_done.html', {'new_user': new_user})
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
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home', kwargs={}))


class ClientProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = ClientProfile
    fields = ['avatar', 'phone', 'telegram']
    template_name_suffix = '_update_form'


class CabinetView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'account/cabinet.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(CabinetView, self).get_context_data(**kwargs)
        if self.object.type == 'client':
            context['client_tenders'] = Tender.objects.filter(author=self.object)
        return context

