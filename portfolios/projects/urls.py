from django.conf.urls import url

from .views import (
    user_detail,
    project_list,
    project_create,
    project_detail,
    project_update,
    project_delete,
)

urlpatterns = [
    url(r'^', project_list, name="list"),
    url(r'^create/', project_create),
    url(r'^user/(?P<user_id>\d+)/$', user_detail, name='user_detail'),
    url(r'^(?P<slug>[\w-]+)/$', project_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', project_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', project_delete),
]