from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.pair_list, name='pair_list'),
]
