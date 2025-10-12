# 🧩 Social Media API

A **Django REST API** project designed for user registration, authentication, and profile management.
This project demonstrates clean API design using Django REST Framework (DRF) and JWT authentication for secure access.

---

## 📖 Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Setup & Installation](#setup--installation)
5. [User Registration & Authentication](#user-registration--authentication)
6. [API Documentation](#api-documentation)

   * [User Endpoints](#user-endpoints)
   * [Authentication Endpoints](#authentication-endpoints)
7. [User Model Overview](#user-model-overview)
8. [Deployment (Coming Soon)](#deployment-coming-soon)
9. [License](#license)

---

## 🧠 Overview

This project provides a backend API for user management and authentication using Django REST Framework and JSON Web Tokens (JWT).
It allows new users to register, log in, and access protected resources once authenticated.

---

## 🚀 Features

* User Registration (via email and password)
* JWT-based Authentication (access & refresh tokens)
* Retrieve user profile information
* Secure API endpoints with authentication
* Modular and scalable code structure

---

## ⚙️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Authentication:** Simple JWT
* **Database:** MYSQL
* **Environment:** Python 3.10+

---

## 🧩 Setup & Installation

Follow the steps below to set up the project locally:

```bash
# 1️⃣ Clone the repository
git clone https://github.com/Aalphakeem-Adroit/Alx_DjangoLearnLab.git

# 2️⃣ Create a virtual environment
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Apply migrations
python manage.py migrate

# 5️⃣ Run the development server
python manage.py runserver
```

Once running, visit **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** to interact with the API.

---

## 👤 User Registration & Authentication

### 1️⃣ Register a User

**Endpoint:**

```
POST /api/register/
```

**Request Body:**

```json
{
  "username": "alphakeem",
  "email": "alphakeem@example.com",
  "password": "strongpassword123"
}
```

**Response:**

```json
{
  "message": "User registered successfully",
  "user": {
    "id": 1,
    "username": "alphakeem",
    "email": "alphakeem@example.com"
  }
}
```

---

### 2️⃣ Obtain Token (Login)

**Endpoint:**

```
POST /api/token/
```

**Request Body:**

```json
{
  "email": "alphakeem@example.com",
  "password": "strongpassword123"
}
```

**Response:**

```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

---

### 3️⃣ Refresh Token

**Endpoint:**

```
POST /api/token/refresh/
```

**Request Body:**

```json
{
  "refresh": "<refresh_token>"
}
```

**Response:**

```json
{
  "access": "<new_access_token>"
}
```

---

## 🧭 API Documentation

### 🧑‍💻 User Endpoints

| Method | Endpoint         | Description                         | Auth Required |
| ------ | ---------------- | ----------------------------------- | ------------- |
| `POST` | `/api/register/` | Register a new user                 | ❌             |
| `GET`  | `/api/users/`    | Retrieve list of all users          | ✅             |
| `GET`  | `/api/profile/`  | Retrieve authenticated user profile | ✅             |

---

### 🔐 Authentication Endpoints

| Method | Endpoint              | Description               | Auth Required |
| ------ | --------------------- | ------------------------- | ------------- |
| `POST` | `/api/token/`         | Obtain JWT tokens (login) | ❌             |
| `POST` | `/api/token/refresh/` | Refresh access token      | ❌             |

---

## 🧱 User Model Overview

The `User` model extends Django’s built-in `AbstractUser` and includes key fields:

| Field         | Type     | Description                           |
| ------------- | -------- | ------------------------------------- |
| `id`          | Integer  | Unique user identifier                |
| `username`    | String   | User's chosen display name            |
| `email`       | String   | Unique email address (used for login) |
| `password`    | String   | Securely hashed password              |
| `date_joined` | DateTime | Account creation date                 |

Custom user features can easily be added such as roles, bio, or profile image in future updates.

---

## 🚀 Deployment

This guide walks you through deploying your **Django REST API** to **Render** using **MySQL** as the production database.

---

## 🧩 1. Prerequisites

Before starting, ensure you have:

* ✅ A **Render account** — [https://render.com](https://render.com)
* ✅ A **GitHub repository** containing your Django project
* ✅ A **MySQL database** (you can use Render’s Managed MySQL or another provider like [PlanetScale](https://planetscale.com))
* ✅ `requirements.txt` file generated with

  ```bash
  pip freeze > requirements.txt
  ```

---

## ⚙️ 2. Prepare Your Django Project for Production

### **(a) Install required packages**

```bash
pip install gunicorn mysqlclient python-decouple whitenoise
```

Then update your `requirements.txt`:

```bash
pip freeze > requirements.txt
```

---

### **(b) Set Up Environment Variables**

In your project root, create a file called **`.env`**:

```env
DEBUG=False
SECRET_KEY=your-super-secret-key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=3306
ALLOWED_HOSTS=your-app-name.onrender.com
```

Make sure `.env` is listed in `.gitignore`:

```
.env
```

---

### **(c) Configure `settings.py`**

In your project’s `settings.py`, modify as follows:

```python
import os
from decouple import config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = [config('ALLOWED_HOSTS', default='*')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', default='3306'),
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Enable Whitenoise
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # other middlewares...
]

# Security
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
```

---

## 🏗️ 3. Create a `Procfile`

In your project root directory, create a file named **`Procfile`** (no extension):

```bash
web: gunicorn social_media_api.wsgi
```

---

## 🧰 4. Collect Static Files

Before deployment, run locally:

```bash
python manage.py collectstatic
```

Then commit and push changes to GitHub:

```bash
git add .
git commit -m "Prepare project for Render deployment"
git push origin main
```

---

## ☁️ 5. Deploy to Render

1. Go to [https://render.com](https://render.com)
2. Click **“New +” → “Web Service”**
3. Connect your **GitHub repository**
4. Fill in:

   * **Name:** `social-media-api`
   * **Environment:** `Python 3`
   * **Build Command:**

     ```
     pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
     ```
   * **Start Command:**

     ```
     gunicorn your_project_name.wsgi
     ```

---

## 🧑‍💻 6. Add Environment Variables in Render

In your Render dashboard:

1. Go to **Environment → Environment Variables**
2. Add all variables from your `.env` file manually:

   * `DEBUG=False`
   * `SECRET_KEY=...`
   * `DB_NAME=...`
   * `DB_USER=...`
   * `DB_PASSWORD=...`
   * `DB_HOST=...`
   * `DB_PORT=3306`
   * `ALLOWED_HOSTS=your-app-name.onrender.com`

---

## 🧮 7. Configure MySQL Database

If you haven’t yet:

1. Go to **Render → New → Database → MySQL**
2. Note the credentials:

   * **Host**
   * **Database name**
   * **User**
   * **Password**
3. Use those values in your environment variables.

Render automatically provides a connection URL you can also use.

---

## 🔐 8. Migrate & Create Superuser

In Render’s web service dashboard:

* Open the **“Shell”** (under “Deploys” or “Logs”)
  Then run:

```bash
python manage.py migrate
python manage.py createsuperuser
```

---

## 🌐 9. Verify Deployment

Visit your Render app URL, e.g.
👉 `https://social-media-api.onrender.com/api/`

Make sure:

* API endpoints work correctly
* Authentication is functional
* Admin dashboard loads properly

---

## 🧾 10. (Optional) Set Up Custom Domain and HTTPS

You can connect a **custom domain** in Render’s **Settings → Custom Domain**.
Render automatically provides **free HTTPS** via Let’s Encrypt.

---

## 🔍 11. Maintenance Tips

* Use `python-decouple` for all sensitive variables
* Use `render logs` or dashboard logs for debugging
* Schedule regular `pip install --upgrade` and migrations
* Monitor your app’s health via Render dashboard

---

## 📜 License

This project is licensed under the **MIT License** — free for personal and commercial use.
