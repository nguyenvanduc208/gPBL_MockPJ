from django.urls import path
from .views import login_handle, register, log_out, change_password


urlpatterns = [
    path('login/', login_handle, name='login'),
    path('register/', register, name='register'),
    path('logout/', log_out, name='logout'),
    path('change-password/', change_password, name='change_pass'),
]
