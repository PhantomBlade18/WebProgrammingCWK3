from django.urls import path
from . import views

urlpatterns = [
    #path('DeleteMovie/<int:mid>/',views.DeleteMovie, name = 'DeleteMovie'), EXAMPLE

    path('registerUser/', views.registerUserView, name = 'registerUserView'),
    path('', views.index, name='index'),
    path('register/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<string:user>', views.viewProfile, name='viewprofile'),

]
