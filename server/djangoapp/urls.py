from django.urls import path
from . import views

urlpatterns = [
    path('get_cars/', views.get_cars, name='get_cars'),
    path('dealerships/', views.get_dealerships, name='dealerships'),
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),
    path('reviews/<int:dealer_id>/', views.get_dealer_reviews, name='dealer_reviews'),
    path('add_review/', views.add_review, name='add_review'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_request, name='logout_request'),
    path('registration/', views.registration, name='registration'),
]
