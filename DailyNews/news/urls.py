from django.urls import path
from . import views

urlpatterns = [
    #path('DeleteMovie/<int:mid>/',views.DeleteMovie, name = 'DeleteMovie'), EXAMPLE

    path('registerUser', views.registerUserView, name = 'registerUserView'),
    path('', views.index, name='index'),

]
