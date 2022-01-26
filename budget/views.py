from django.shortcuts import render
from django.http import JsonResponse
import json
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Budget

User = get_user_model()


@login_required
def budget_view(request):
    try:
        budget = Budget.objects.get(client=request.user)
    except Budget.DoesNotExist:
        budget = None
    return render(request, template_name='budget/budget.html', context={'json': json.loads(budget.budget_json) if budget else None,
                                                                        'budget': budget.budget_value if budget else None,
                                                                        'last_rel': budget.last_rel if budget else None,
                                                                        })


@login_required
def budget_save(request):
    if request.method == 'POST':
        json = request.POST.get('json')
        budget_value = request.POST.get('budget')
        last_rel = request.POST.get('last_rel')
        success = False
        err = ''
        if request.user.type == 'client':
            try:
                budget = Budget.objects.get(client=request.user)
            except Budget.DoesNotExist:
                budget = None
            if not budget:
                budget = Budget(client=request.user, budget_json=json, budget_value=budget_value, last_rel=last_rel)
            else:
                budget.budget_json = json
                budget.budget_value = budget_value
                budget.last_rel = last_rel
            budget.save()
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
