from django.urls import path
from .views import login_handle, register, log_out


urlpatterns = [
    path('login/', login_handle, name='login'),
    path('register/', register, name='register'),
    path('logout/', log_out, name='logout'),
]
