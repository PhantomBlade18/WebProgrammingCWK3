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
    path('profile/updateEmail/', views.updateEmail, name='updateEmail'),
    path('profile/updatePassword/', views.updatePassword, name='updatePassword'),
    path('profile/updateImage/', views.updateImage, name='updateImage'),
    path('profile/removeImage/', views.removeImage, name='removeImage'),
    path('MyNews/', views.myNews, name='myNews'),
    path('likeArticle/', views.LikeArticle, name='LikeArticle'),
    path('MyNews/likeArticle/', views.LikeArticle, name='LikeArticle'),
    path('addComment/', views.addComment, name='AddComment'),
    path('addReply/', views.addReply, name='AddReply'),
    path('deleteComment/', views.deleteComment, name='DeleteComment'),
    path('deleteReply/', views.deleteReply, name='DeleteReply'),
    path('updateComment/', views.updateComment, name='UpdateComment'), #No need for Update Reply as they are identical in what happens
    path('MyNews/addComment/', views.addComment, name='AddComment'),
    path('MyNews/addReply/', views.addReply, name='AddReply'),
    path('MyNews/deleteComment/', views.deleteComment, name='DeleteComment'),
    path('MyNews/deleteReply/', views.deleteReply, name='DeleteReply'),
    path('MyNews/updateComment/', views.updateComment, name='UpdateComment'),
    path('login/likeArticle/', views.LikeArticle, name='LikeArticle'),
    path('login/addComment/', views.addComment, name='AddComment'),
    path('login/addReply/', views.addReply, name='AddReply'),
    path('login/deleteComment/', views.deleteComment, name='DeleteComment'),
    path('login/deleteReply/', views.deleteReply, name='DeleteReply'),
    path('login/updateComment/', views.updateComment, name='UpdateComment')
]
