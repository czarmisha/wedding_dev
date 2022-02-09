from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from .models import Tender, Response
from .forms import TenderCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .filtres import TenderFilter
from django.contrib import messages
from django_filters.views import FilterView

User = get_user_model()


class TenderList(FilterView):
    model = Tender
    context_object_name = 'tender_list'
    template_name = 'tender/tender_list.html'
    filterset_class = TenderFilter


class TenderDetail(DetailView):
    model = Tender
    template_name = 'tender/tender_detail.html'
    context_object_name = 'tender'

    def get_context_data(self, **kwargs):
        context = super(TenderDetail, self).get_context_data(**kwargs)
        try:
            for response in self.request.user.responses.all():
                if response.tender == self.object:
                    context['responded'] = True
        except:
            print('anonymous user')
        return context


class TenderUpdate(LoginRequiredMixin, UpdateView):
    model = Tender
    fields = ['on_date', 'budget', 'comment']
    template_name_suffix = '_update_form'


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
        tender = form.save(commit=False)
        for user_tender in self.request.user.tender_set.all():
            if user_tender.service == tender.service:
                messages.error(self.request,
                               'У вас уже есть тендер на поиск этой услуги.')
                return super(TenderCreate, self).form_invalid(form)
        tender.author = self.request.user
        tender.save()
        return HttpResponseRedirect(reverse_lazy('tender:detail', args=[tender.slug]))


def create_response(request):
    if request.method == 'POST':
        tender_pk = request.POST.get('tender_pk')
        user_pk = request.POST.get('user_pk')
        tender = Tender.objects.get(pk=tender_pk)
        from_user = User.objects.get(pk=user_pk)
        response = Response(tender=tender, from_user=from_user)
        response.save()
        resp = {
            'success': True,
        }
        return JsonResponse(resp, safe=False)
    else:
        return JsonResponse({'success': False}, safe=False)
