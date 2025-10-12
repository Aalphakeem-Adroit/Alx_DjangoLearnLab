from django.urls import path
from .views import RegisterView, LoginView, UserDetailView, follow_user, unfollow_user
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('users', UserDetailView)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserDetailView.as_view(), name='user-detail'),
    path('follow/<int:user_id>/', follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),
]
