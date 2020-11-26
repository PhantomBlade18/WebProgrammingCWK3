from django.urls import path
from . import views

urlpatterns = [
    #path('DeleteMovie/<int:mid>/',views.DeleteMovie, name = 'DeleteMovie'), EXAMPLE
    path('', views.index, name='index'),
    path('registerUser/', views.registerUserView, name = 'registerUserView'),
    path('register/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.viewProfile, name='viewProfile'),

]
