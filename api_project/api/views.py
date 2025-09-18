from django.shortcuts import render
from rest_framework import generics,viewsets,authentication,permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class=BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset=Book.objects.all().order_by('-author')
    serializer_class=BookSerializer

class ListUsers(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,format=None):
        emails=[user.email for user in User.objects.all()]
        return Response(emails)

class CustomAuthToken(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        serializer=self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_id':user.pk,
            'email':user.email
        })
        

# In this API setup, authentication and permissions are managed using Django REST Framework (DRF). By default, DRF allows developers to configure global settings in the project’s settings.py file under the REST_FRAMEWORK dictionary. Authentication classes determine how users prove their identity when making requests to the API, while permission classes define what actions authenticated or unauthenticated users are allowed to perform.

# For authentication, common options include SessionAuthentication, which works with Django’s built-in login system and is suitable for web applications that use sessions and cookies, and BasicAuthentication, which uses HTTP Basic Authentication, sending the username and password with each request (mainly useful for testing). A more secure and scalable approach for production APIs is JWTAuthentication, provided by third-party packages such as djangorestframework-simplejwt, where users authenticate using JSON Web Tokens (JWT).

# Permissions build on authentication by controlling access to API endpoints. For example, AllowAny makes an endpoint publicly accessible, while IsAuthenticated restricts access to only logged-in users. Other built-in permissions such as IsAdminUser limit access to administrators, and DjangoModelPermissions tie API access to Django’s model-level permissions system. These permission classes can be set globally in the project settings or overridden on a per-view basis.

# In practice, this means you can configure an API view to allow only authenticated users to create or modify data, while still permitting unauthenticated users to read (view) the same data. For more advanced use cases, DRF also supports custom permission classes. For example, you could define a rule that only allows the creator of a resource to edit or delete it, while everyone else has read-only access. This flexibility makes it possible to enforce fine-grained control over how your API is consumed.