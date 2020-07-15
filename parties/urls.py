from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test$', views.test_response, name='test_response'),  # todo: temporary url, remove after a while
    url(r'^$', views.index, name='index'),
]
