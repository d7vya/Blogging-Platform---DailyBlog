from django.urls import path
from Home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('blogs',views.blogs,name='blogs'),
    path('addBlog',views.addBlog,name='addBlog'),
    path('login',views.login_,name='login'),
    path('register' , views.register,name='register'),
    path('logout',views.logout_,name='login'),
    path('blogpost/<int:blogid>',views.blogpost,name='blogpost'),
    path('comment/<int:blogid>',views.comment,name='comment'),
    path('restriction/<str:username>',views.restrictuser,name='restriction'),
    path('blog',views.blog,name='blog'),
    path('userpage',views.userpage,name='userpage')
    
    
]
