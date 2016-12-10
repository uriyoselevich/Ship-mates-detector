from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Department, Soldier


def index(request):
    all_departments = Department.objects.all()
    return render(request, 'ship/index.html', {'all_departments': all_departments})


def detail(request, department_id):
    # album = Album.objects.get(pk=department_id)
    department = get_object_or_404(Department, pk=department_id)
    return render(request, 'ship/detail.html',{ 'department': department,})


def baknaz_team(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    try:
        selected_soldier=department.soldier_set.get(pk=request.POST['soldier'])
    except(KeyError, Soldier.DoesNotExist):
        return render(request, 'ship/detail.html',
                      {'department': department, 'error_message': "You did not select a valid soldier"})
    else:
        selected_soldier.is_baknaz_team=True
        selected_soldier.save()
        return render(request, 'ship/detail.html', {'department': department, })

