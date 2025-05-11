from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from .models import Department, Position

def homework_querysets(request):
    qs1 = (
        Department.objects
        .filter(position__name__icontains='manager')
        .distinct()
        .order_by('name')
    )

    active_count = Position.objects.filter(is_active=True).count()

    qs3 = Position.objects.filter(
        Q(is_active=True) |
        Q(department__name='HR')
    )

    qs4 = (
        Department.objects
        .filter(position__name__icontains='manager')
        .values('name')
        .distinct()
    )

    qs5 = Position.objects.order_by('name').values('name', 'is_active')

    data = {
        '1_departments_with_managers': list(qs1.values('id', 'name')),
        '2_active_positions_count': active_count,
        '3_active_or_hr_positions': list(qs3.values('id', 'name', 'is_active', 'department__name')),
        '4_department_names_with_managers': list(qs4),
        '5_positions_name_and_active': list(qs5),
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 2})