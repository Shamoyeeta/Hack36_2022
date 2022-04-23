from django.urls import path

from . import views

urlpatterns = [
    path('', views.personListAPIView.as_view(),),
]
