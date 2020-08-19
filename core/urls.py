from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.home, name='home'),
]

# /welcome
# /signup
# /login
# /home
# /party/{id}
