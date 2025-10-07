from user import views
from django.urls import path


urlpatterns = [
    path('user_chat_message/', views.user_chat_message, name='user_chat_message'),
    path('user_edit_profile/', views.user_edit_profile, name='user_edit_profile'),
    path('user_header/', views.user_header, name='user_header'),
    path('user_home/', views.user_home, name='user_home'),
    path('user_registration/', views.user_registration, name='user_registration'),
    path('footer/', views.footer, name='footer'),
    path('user_view_recipe/', views.user_view_recipe, name='user_view_recipe'),


]