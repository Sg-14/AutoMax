from django.urls import path
from .views import login_view, home_view, RegisterView, logout_view, ProfileView

urlpatterns = [
    path('login/', login_view, name = 'login'),
    path('home/', home_view, name = 'home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name = 'logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]