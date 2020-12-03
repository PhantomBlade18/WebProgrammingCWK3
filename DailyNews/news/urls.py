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
    path('profile/updateCategory/', views.updateCategory, name='updateCategory'),
    path('profile/updateImage/', views.updateImage, name='updateImage'),
    path('profile/removeImage/', views.removeImage, name='removeImage'),
    path('MyNews/', views.myNews, name='myNews'),
    path('likeArticle/', views.LikeArticle, name='LikeArticle'),
    path('MyNews/likeArticle/', views.LikeArticle, name='LikeArticle'),
    path('addComment/', views.addComment, name='AddComment'),
    path('addReply/', views.addReply, name='AddReply'),
]
