from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListPoll),
    path('<pk>/', views.Poll),
    # path('<int:pk>/', views.DetailPoll.as_view())
]