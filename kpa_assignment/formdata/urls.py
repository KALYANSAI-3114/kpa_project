# formdata/urls.py

from django.urls import path
from .views import WheelSpecificationListCreateAPIView
from .login_api import LoginView

urlpatterns = [
    path('forms/wheel-specifications', WheelSpecificationListCreateAPIView.as_view(), name='wheel-specifications-list-create'),
    path('users/login/', LoginView.as_view(), name='login'),
]