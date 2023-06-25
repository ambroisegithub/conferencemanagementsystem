from django.urls import path
from . import views
#important urls
urlpatterns = [
    path('', views.conference_list, name='conference_list'),
    path('create/', views.conference_create, name='conference_create'),
    path('<int:pk>/', views.conference_detail, name='conference_detail'),
    path('<int:pk>/edit/', views.conference_edit, name='conference_edit'),
    path('<int:pk>/delete/', views.conference_delete, name='conference_delete'),
    path('<int:pk>/schedule/', views.conference_schedule, name='conference_schedule'),
]