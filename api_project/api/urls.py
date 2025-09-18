from django.urls import path,include
from .views import BookList
from rest_framework import routers
from .views import BookViewSet
from .views import ListUsers
from .views import CustomAuthToken

router=routers.DefaultRouter()

router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/',BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)), # This includes all routes registered with the router

    path('users/',ListUsers.as_view(), name = 'api-token-authentication'),
    path('token/auth/',CustomAuthToken.as_view())
]
