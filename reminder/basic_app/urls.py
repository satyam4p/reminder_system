from django.conf.urls import url
from. import views


app_name='basic_app'


urlpatterns=[
    url(r'^(?P<pk>\d+)/$',views.Read,name='read'),



]