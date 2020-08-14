from django.urls import path
from .views import login_view, welcome

urlpatterns = [
    path('', login_view, name='login'),
    path('welcome', welcome, name='welcome')
]
