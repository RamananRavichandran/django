from django.urls import path
from . import views

urlpatterns = [
    path('', views.ase_form),
    path('list/',views.ase_list),
    path('form/',views.ase_form)
]
