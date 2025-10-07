from chef import views
from django.urls import path

urlpatterns = [
    path('chef_add_comment/', views.chef_add_comment, name='chef_add_comment'),
    path('chef_add_rating/', views.chef_add_rating, name='chef_add_rating'),
    path('chef_header/', views.chef_header, name='chef_header'),
    path('chef_home/', views.chef_home, name='chef_home'),
    path('chef_upload_recipe/', views.chef_upload_recipe, name='chef_upload_recipe'),
    path('chef_view_comment/', views.chef_view_comment, name='chef_view_comment'),
    path('chef_view_other_recipe/', views.chef_view_other_recipe, name='chef_view_other_recipe'),
    path('chef_view_rating/', views.chef_view_rating, name='chef_view_rating'),
    path('chef_view_recipe_detail/', views.chef_view_recipe_detail, name='chef_view_recipe_detail'),
    path('footer/', views.footer, name='footer'),

]
