from django.urls import path
from users.views import usersView

urlpatterns = [
    path('users/', usersView.as_view()),
]