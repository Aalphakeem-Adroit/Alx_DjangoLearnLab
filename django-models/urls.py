from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth import views as auth_views
from .views import register, admin_view, librarian_view, member_view, add_book, edit_book, delete_book

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
   
    # Authentication URLs
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("register/", register, name="register"),
    
    
]

urlpatterns += [
    path("admin-dashboard/", admin_view, name="admin_view"),
    path("librarian-dashboard/", librarian_view, name="librarian_view"),
    path("member-dashboard/", member_view, name="member_view"),
    path("add-book/", add_book, name="add_book"),
    path("edit-book/", edit_book, name="edit_book"),
    path("delete-book/", delete_book, name="delete_book"),
]

