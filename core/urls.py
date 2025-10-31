from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('news/', views.news_home, name='news'),
    path('news/<str:unique_id>/', views.news_detail, name='news_detail'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team_view, name='team'),
    path('career/', views.job_list_view, name='career'),
    path('career/<str:unique_id>/', views.job_detail_view, name='career'),
    path('hostel/', views.hostel_view, name='hostel'),
    path('hostel/booking/<str:unique_id>/', views.hostel_booking, name='hostel_booking'),
]
