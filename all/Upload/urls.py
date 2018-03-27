from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^result', views.result, name='result'),
    url(r'^', views.upload, name='upload'),

]
