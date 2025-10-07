from foodconapp import views
from django.urls import path


urlpatterns = [
    path('public_home/', views.public_home, name='public_home'),
    path('public_login/', views.public_login, name='public_login'),
    path('public_recipe/', views.public_recipe, name='public_recipe'),
    path('public_reg/', views.public_reg, name='public_reg'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('public_chefreg/', views.public_chefreg, name='public_chefreg'),

    
    
    # path('success/', views.registration_success, name='registration_success'),  # Example success page
]
