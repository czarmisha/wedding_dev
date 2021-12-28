from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Tender
from .forms import TenderCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class TenderList(ListView):
    model = Tender
    context_object_name = 'tender_list'
    # paginate_by = 20

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context


class TenderDetail(DetailView):
    model = Tender
    template_name = 'tender/tender_detail.html'
    context_object_name = 'tender'


class TenderCreate(LoginRequiredMixin, CreateView):
    model = Tender
    template_name = 'tender/tender_create.html'

    def get_form(self, form_class=TenderCreateForm):
        form = super(TenderCreate, self).get_form(form_class)
        return form

    def form_valid(self, form):
        tender = form.save(commit=False)
        tender.author = self.request.user
        tender.save()
        return HttpResponseRedirect(reverse_lazy('tender:detail', args=[tender.slug]))
