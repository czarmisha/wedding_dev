from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Plan, Task

User = get_user_model()


@login_required
def plan_view(request):
    try:
        plan = Plan.objects.get(user=request.user)
        task_list = Task.objects.filter(plan=plan)
    except:
        plan = None
        task_list = None
    return render(request, template_name='plan/plan_list.html', context={'task_list': task_list})


@login_required
def plan_save(request):
    if request.method == 'POST':
        success = False
        err = ''
        if request.user.type == 'client':
            time = request.POST.get('time')
            action = request.POST.get('action')
            try:
                plan = Plan.objects.get(user=request.user)
            except:
                plan = Plan(user=request.user)
                plan.save()
            task = Task(plan=plan, time=time, action=action)
            task.save()
            success = True
        else:
            err = 'Эта услуга доступна только для молодоженов'

        resp = {
            'success': success,
            'error': err,
        }
        return JsonResponse(resp, safe=False)
    else:
        return JsonResponse({'success': False}, safe=False)


@login_required
def plan_delete(request):
    if request.method == 'POST':
        success = False
        err = ''
        if request.user.type == 'client':
            task_pk = request.POST.get('obj_pk')
            try:
                task = Task.objects.get(pk=task_pk)
            except:
                return JsonResponse({'success': False}, safe=False)
            task.delete()
            success = True
        else:
            err = 'Эта услуга доступна только для молодоженов'

        resp = {
            'success': success,
            'error': err,
        }
        return JsonResponse(resp, safe=False)
    else:
        return JsonResponse({'success': False}, safe=False)
