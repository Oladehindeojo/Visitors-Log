from django.urls import path
from . import views

app_name = 'logapp'

urlpatterns = [
    path('sign_in', views.visitor_sign_in, name='visitor_sign_in'),
    path('', views.visitor_list, name='visitor_list'),
]
