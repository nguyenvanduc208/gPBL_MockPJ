from django.urls import path
from .views import index, add, save


urlpatterns = [
    path('', index, name='prd_index'),
    path('add/', add, name='prd_add'),
    path('save/', save, name='prd_save'),
]