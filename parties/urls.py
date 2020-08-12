from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test$', views.test_response, name='test_response'),  # todo: temporary url
    url(r'^home-page$', views.index, name='index'),
]
