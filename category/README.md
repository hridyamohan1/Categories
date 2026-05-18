# Hierarchical Categories API

A Django REST Framework API system to dynamically create and retrieve hierarchical categories and subcategories.

---

# Features

- Create unlimited categories
- Create nested subcategories
- Unique category names
- Bulk category creation
- Retrieve category with:
  - Parent category
  - Subcategories (children)
- Search by category name
- Limit support
- Pagination support
- Optimized database queries

---

# Tech Stack

- Python
- Django
- Django REST Framework
- SQLite

---

# Project Structure

```text
category/
│
├── app1/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── pagination.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── category/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── requirements.txt


# API Endpoints

Base URL:

```text
http://127.0.0.1:8000/api/

1. Create Category
Endpoint
POST /api/categories/create/
Full URL
http://127.0.0.1:8000/api/categories/create/


2. Retrieve Categories
Endpoint
GET /api/categories/
Full URL
http://127.0.0.1:8000/api/categories/


3. Search Category by Name
Endpoint
GET /api/categories/?name=Electronics
Full URL
http://127.0.0.1:8000/api/categories/?name=Electronics


4. Limit Results
Endpoint
GET /api/categories/?limit=2
Full URL
http://127.0.0.1:8000/api/categories/?limit=2


5. Pagination
Endpoint
GET /api/categories/?page=1&page_size=5
Full URL
http://127.0.0.1:8000/api/categories/?page=1&page_size=5


6. Search + Limit
Endpoint
GET /api/categories/?name=Electronics&limit=1
Full URL
http://127.0.0.1:8000/api/categories/?name=Electronics&limit=1