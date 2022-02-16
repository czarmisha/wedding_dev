from django.http import JsonResponse
from services.models import *


def search_from_ajax(request):
    resp = {'success': False}
    if request.method == 'GET':
        service = request.GET.get('service')
        name = request.GET.get('name')
        if service == 'photographer':
            resp['queryset'] = search_by_name(Photographer, name)
        elif service == 'videographer':
            resp['queryset'] = search_by_name(Videographer, name)
        else:
            resp = {
            'error': 'unknown service type',
            'success': False,
            }
            return JsonResponse(resp, safe=False)

        if resp['queryset']:
            resp['success'] = True,
        return JsonResponse(resp, safe=False)
    else:
        resp = {
            'error': 'request type is not GET',
            'success': False,
        }
        return JsonResponse(resp, safe=False)

def search_by_name(Model, name):
    return list(Model.objects.filter(name=name))