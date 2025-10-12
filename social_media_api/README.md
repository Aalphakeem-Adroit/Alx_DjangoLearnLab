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

## 🚀 Deployment (Coming Soon)

Deployment instructions for production environments (e.g., on Render, Railway, or AWS) will be added later, including:

* Environment variable setup
* Secure database configuration
* JWT & SECRET_KEY management
* Production-ready server setup (Gunicorn/Nginx)

---

## 📜 License

This project is licensed under the **MIT License** — free for personal and commercial use.
