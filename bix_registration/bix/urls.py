from django.urls import path
from .views import BoatRegistrationView


urlpatterns = [
    path('register/', BoatRegistrationView.as_view(), name='register_boat'),
    # ...
]
