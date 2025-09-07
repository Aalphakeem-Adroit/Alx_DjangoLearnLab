from django.shortcuts import render,redirect
from django.views.generic import DetailView
from models import Book, Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required

def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"

def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"

def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")



@permission_required("relationship_app.can_add_book")
def add_book(request):
    return render(request, "relationship_app/add_book.html")

@permission_required("relationship_app.can_change_book")
def edit_book(request):
    return render(request, "relationship_app/edit_book.html")

@permission_required("relationship_app.can_delete_book")
def delete_book(request):
    return render(request, "relationship_app/delete_book.html")



# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})

# Class-based view: library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"


# Registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})
