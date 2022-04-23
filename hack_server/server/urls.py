from django.urls import path

from . import views

urlpatterns = [
    path('', views.personListAPIView.as_view()),
    path('signUp', views.personCreateAPIView.as_view()),
    path('login/<str:email>/<str:password>',
         views.personListAPIView.as_view()),
    path('itemListView/<int:id>', views.itemListAPIView.as_view()),
]
