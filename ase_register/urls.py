from django.urls import path
from . import views

urlpatterns = [
    path('', views.ase_form,name='ase_insert'), #get and post request for insert operation
    path('<int:id>/', views.ase_form,name='ase_update'), #get and post request for update operation
    path('list/',views.ase_list,name='ase_list'), #get request to retrieve and display all records
    path('delete/<int:id>/',views.ase_delete,name='ase_delete')
]
