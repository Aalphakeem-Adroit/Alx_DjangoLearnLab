# 📝 Django Blog Authentication System

This document explains how the **authentication system** for the `django_blog` project is set up, how it works, and how to test each part of it.

---

## 🔐 Features Implemented

* User Registration (extended `UserCreationForm`)
* User Login & Logout (Django built-in views)
* Profile Management (bio, profile picture, email updates)
* CSRF Protection
* Secure Password Storage (Django PBKDF2 hashing)
* Session Management

---

## ⚙️ How It Works

### 1. **Registration**

* Users register with username, email, password.
* On success → a `Profile` object is auto-created for the user.

### 2. **Login / Logout**

* Built-in Django `LoginView` and `LogoutView`.
* Invalid credentials → error message shown.

### 3. **Profile**

* Users can update their **username, email, bio, and profile picture**.
* Profile is linked to `User` with `OneToOneField`.

### 4. **Security**

* CSRF tokens on all forms.
* Passwords hashed (PBKDF2 + SHA256).
* Profile view protected by `@login_required`.

---

## 📂 Project Structure (Authentication Parts)

```
accounts/
│── forms.py       # Forms for registration, user update, and profile update
│── models.py      # Profile model extending Django’s User
│── urls.py        # Authentication URLs
│── views.py       # Registration & profile views
│── templates/
│    └── accounts/
│        ├── login.html
│        ├── logout.html
│        ├── register.html
│        └── profile.html
```

---

## 📜 Code Snippets

### 1. **Profile Model** (`accounts/models.py`)

```python
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
```

---

### 2. **Forms** (`accounts/forms.py`)

```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']
```

---

### 3. **Views** (`accounts/views.py`)

```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'accounts/profile.html', context)
```

---

### 4. **URLs** (`accounts/urls.py`)

```python
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile/', views.profile_view, name='profile'),
]
```

In `django_blog/urls.py` (main project):

```python
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
]
```

---

### 5. **Templates**

#### `register.html`

```html
{% load static %}
<h2>Register</h2>
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Register</button>
</form>
<p>Already have an account? <a href="{% url 'login' %}">Login</a></p>
```

#### `login.html`

```html
{% load static %}
<h2>Login</h2>
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>
<p>Don’t have an account? <a href="{% url 'register' %}">Register</a></p>
```

#### `logout.html`

```html
<h2>You have been logged out</h2>
<a href="{% url 'login' %}">Login again</a>
```

#### `profile.html`

```html
{% load static %}
<h2>Profile</h2>
<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ u_form.as_p }}
    {{ p_form.as_p }}
    <button type="submit">Update</button>
</form>
<a href="{% url 'logout' %}">Logout</a>
```

---

## 🧪 Testing Instructions

1. **Register a new user** at `/accounts/register/`.

   * Confirm user + profile created.

2. **Login** at `/accounts/login/`.

   * Try wrong password → error shown.

3. **Logout** at `/accounts/logout/`.

   * Session ends, redirected to login.

4. **Profile update** at `/accounts/profile/`.

   * Change email, username, upload profile picture.

---

## ⚡ Security Checklist

* [x] CSRF tokens included in all forms.
* [x] Passwords stored using hashing (Django default).
* [x] `@login_required` on profile view.
* [x] Session expires on logout.
