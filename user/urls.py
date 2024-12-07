from django.urls import path
from . import views

urlpatterns = [

    path('',views.base1, name = 'base1'),
    path('login/',views.login_view, name = 'login'),
    path('logout/',views.logout, name = 'logout'),
    path('register/',views.register, name = 'register'),
]
