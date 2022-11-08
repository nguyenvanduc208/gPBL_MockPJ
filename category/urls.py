from django.urls import path

from category.views import add, save, index,edit,remove

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('save/', save, name='save'),
    path('save/<str:id>/', save, name='save'),
    path('edit/<str:id>/',edit , name='edit'),
    path('remove/<str:id>/',remove , name='remove'),
]
