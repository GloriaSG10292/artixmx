from django.urls import path,include
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('',views.feed,name='feed'),
    path('profile/',views.profile,name='profile'),
    path('profile/<str:username>/',views.profile,name='profile'),
    path('register/',views.register,name='register'),
    path('login/',LoginView.as_view(template_name='social/login.html'),name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('post/', views.post, name='post'),
    path('follow/<str:username>/',views.follow,name='follow'),
    path('unfollow/<str:username>/',views.unfollow,name='unfollow'),
    path('add_to_favorites/<int:post_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:post_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('<str:username>/followers/', views.followers, name='followers'),
    path('<str:username>/following/', views.following, name='following'),
    path('favorites/', views.favorites, name='favorites'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('unlike_post/<int:post_id>/', views.unlike_post, name='unlike_post'),
    path('unlike_post_m/<int:post_id>/', views.unlike_post_m, name='unlike_post_m'),
    path('likes/<int:post_id>/', views.likes_list, name='likes_list'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_reset_request/', views.password_reset_request, name='password_reset_request'),
    path('password_reset_form/', views.password_reset_form, name='password_reset_form'),

]
