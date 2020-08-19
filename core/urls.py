from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^welcome$', views.welcome, name='welcome'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^login$', views.login, name='login'),
    url(r'^party$', views.party, name='party'),  # todo: add the following pattern '/party/{id}'
]
