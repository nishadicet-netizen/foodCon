from adminapp import views
from django.urls import path

urlpatterns = [
    path('admin_header/', views.admin_header, name='admin_header'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('admin_send_replay/', views.admin_send_replay, name='admin_send_replay'),
    path('admin_view_chef/', views.admin_view_chef, name='admin_view_chef'),
    path('admin_view_complaint/', views.admin_view_complaint, name='admin_view_complaint'),
    path('admin_view_rating/', views.admin_view_rating, name='admin_view_rating'),
    path('admin_view_recipe/', views.admin_view_recipe, name='admin_view_recipe'),
    path('admin_view_user/', views.admin_view_user, name='admin_view_user'),
    path('footer/', views.footer, name='footer'),
]