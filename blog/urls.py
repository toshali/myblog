from django.conf.urls import url
from . import views 

## dot (.) means from self import view 

urlpatterns = [

    url(r'^$', views.post_list, name='post_list'),

]
