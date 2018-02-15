from django.urls import path

from . import views

urlpatterns = [
    path('', views.PollList.as_view()),
    path('<pk>/', views.Poll.as_view()),
    path('answer', views.Answer.as_view())
]