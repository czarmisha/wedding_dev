from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from .models import Tender
from .forms import TenderCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify


class TenderList(ListView):
    model = Tender
    context_object_name = 'tender_list'
    # paginate_by = 20


class TenderDetail(DetailView):
    model = Tender
    template_name = 'tender/tender_detail.html'
    context_object_name = 'tender'


class TenderUpdate(LoginRequiredMixin, UpdateView):
    model = Tender
    fields = ['on_date', 'budget', 'comment']
    template_name_suffix = '_update_form'

    # def form_valid(self, form):
    #     """If the form is valid, save the associated model."""
    #     tender = form.save(commit=False)
    #     tender.slug = slugify(tender.author.username + tender.service + tender(self.on_date))
    #     tender.save()
    #     return super().form_valid(form)


class TenderDelete(LoginRequiredMixin, DeleteView):
    model = Tender

    def get_success_url(self):
        return reverse_lazy('account:cabinet', args=[self.object.author.pk])


class TenderCreate(LoginRequiredMixin, CreateView):
    model = Tender
    template_name = 'tender/tender_create.html'

    def get_form(self, form_class=TenderCreateForm):
        form = super(TenderCreate, self).get_form(form_class)
        return form

    def form_valid(self, form):
        #TODO если тендер с таким сервисом уже есть - то не создаем
        tender = form.save(commit=False)
        tender.author = self.request.user
        tender.save()
        return HttpResponseRedirect(reverse_lazy('tender:detail', args=[tender.slug]))
