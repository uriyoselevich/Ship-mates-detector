from django.conf.urls import url
from . import views

app_name = 'ship'

urlpatterns = [
    # /ship/
    url(r'^$', views.index, name='index'),

    # /ship/<department.id>/
    url(r'^(?P<department_id>[0-9]+)/$', views.detail, name='detail'),

    # /ship/<department.id>/
    url(r'^(?P<department_id>[0-9]+)/baknaz_team/$', views.baknaz_team, name='baknaz_team'),
]