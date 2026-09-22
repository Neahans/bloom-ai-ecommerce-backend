<div align="center">

# 🐍 Bloom AI — Backend

### ✨ The little backend that makes Bloom bloom ✨

<p>
  <img src="https://img.shields.io/badge/Django-Backend-59633B?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/DRF-REST_API-E9A0A8?style=for-the-badge&logo=django&logoColor=white" alt="Django REST Framework">
  <img src="https://img.shields.io/badge/Gemini-AI-FFF4E8?style=for-the-badge&logo=google&logoColor=59633B" alt="Google Gemini">
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.x-59633B?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/JWT-Authentication-E9A0A8?style=flat-square" alt="JWT">
  <img src="https://img.shields.io/badge/SQLite-Database-59633B?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite">
</p>

🌸 🧸 🌿 🛍️ ✨ 🌷

**Products · Authentication · Cart · AI**

</div>

---

## 🌷 About

**Bloom AI Backend** is the Django REST API powering the Bloom AI e-commerce application.

It provides the backend services used by the React frontend for:

* 🛍️ Product management
* 👤 User registration and authentication
* 🔐 JWT-based authorization
* 🛒 Shopping cart management
* 📦 Product stock information
* 🤖 Gemini-powered AI chatbot
* 🔌 REST API communication

> 🌿 **The frontend is where Bloom looks beautiful.
> The backend is where everything works behind the scenes.**

---

## 🌸 Bloom AI Project

Bloom AI is organized into two repositories:

| 🌷 Part     | Repository                                                         |
| ----------- | ------------------------------------------------------------------ |
| 🎨 Frontend | [Bloom AI Frontend](https://github.com/Neahans/bloom-ai-ecommerce) |
| 🐍 Backend  | **Bloom AI Backend**                                               |

### 🎨 Frontend Repository

[![Open Frontend](https://img.shields.io/badge/🌸_Open_Bloom_AI_Frontend-59633B?style=for-the-badge)](https://github.com/Neahans/bloom-ai-ecommerce)

The React frontend provides the user interface for browsing products, viewing product details, interacting with the cart, and chatting with Bloom AI.

---

## 🪴 Architecture

```text
                    🌸 BLOOM AI
                         │
                         ▼
                ┌─────────────────┐
                │   React.js UI   │
                │                 │
                │  Home           │
                │  Shop           │
                │  Products       │
                │  Cart           │
                │  Bloom AI       │
                └────────┬────────┘
                         │
                         │ REST API
                         ▼
                ┌─────────────────┐
                │ Django Backend  │
                │                 │
                │ Products        │
                │ Authentication  │
                │ Cart            │
                │ Chatbot         │
                └────────┬────────┘
                         │
                    ┌────┴────┐
                    ▼         ▼
                🗄️ SQLite   🤖 Gemini
```

---

## 🎀 Features

### 🛍️ Product Management

The product API supports creating, viewing, updating, and deleting products.

```text
GET     /api/products/
GET     /api/products/<id>/
POST    /api/products/
PUT     /api/products/<id>/
DELETE  /api/products/<id>/
```

Each product contains information such as:

* Product name
* Description
* Price
* Category
* Image
* Stock
* Creation date

---

### 👤 Authentication

Bloom uses **JWT authentication** for protected API requests.

Supported features:

* 🌸 User registration
* 🔑 Login
* ♻️ Access token refresh
* 🛡️ Protected endpoints
* 👤 User-specific cart data

Authentication endpoints:

```text
POST /api/auth/register/
POST /api/auth/login/
POST /api/auth/refresh/
```

---

### 🛒 Shopping Cart

Authenticated users can manage their own cart.

```text
GET     /api/cart/
POST    /api/cart/
PUT     /api/cart/<id>/
DELETE  /api/cart/<id>/
```

Cart items contain:

* 🛍️ Product
* 🔢 Quantity
* 💰 Product price
* 👤 User

---

## 🤖 Bloom AI

Bloom includes an AI-powered shopping assistant using **Google Gemini**.

The chatbot communicates with the backend through a dedicated API endpoint.

```text
👩 User
   │
   │ "I need something under ₹1500."
   ▼
🌸 React Chatbot
   │
   │ POST /api/chat/
   ▼
🐍 Django REST API
   │
   ▼
🤖 Google Gemini
   │
   ▼
💬 AI Response
   │
   ▼
🌸 React Chatbot
```

### 💬 Chat Endpoint

```text
POST /api/chat/
```

Example request:

```json
{
  "message": "I need something under ₹1500."
}
```

Example response:

```json
{
  "reply": "..."
}
```

---

## 🧸 Tech Stack

| 🌷 Technology            | 🛠️ Purpose            |
| ------------------------ | ---------------------- |
| 🐍 Python                | Backend language       |
| 🌿 Django                | Web framework          |
| 🔌 Django REST Framework | REST APIs              |
| 🤖 Google Gemini         | AI chatbot             |
| 🔐 Simple JWT            | Authentication         |
| 🗄️ SQLite               | Database               |
| 🌱 python-dotenv         | Environment variables  |
| 🌸 django-cors-headers   | Frontend communication |

---

## 🌱 Project Structure

```text
bloom-ai-ecommerce-backend/
│
├── chatbot/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── ecommerce_backend/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── products/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── users/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Neahans/bloom-ai-ecommerce-backend.git
cd bloom-ai-ecommerce-backend
```

### 2️⃣ Create a virtual environment

On Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```powershell
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a `.env` file in the backend root:

```env
GEMINI_API_KEY=your_api_key_here
```

> 🔒 **Never commit your `.env` file or expose your Gemini API key.**

### 5️⃣ Run migrations

```powershell
python manage.py migrate
```

### 6️⃣ Start the development server

```powershell
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

---

## 🌸 Connect the React Frontend

Clone the frontend repository separately:

```bash
git clone https://github.com/Neahans/bloom-ai-ecommerce.git
```

Start the frontend:

```powershell
npm install
npm start
```

The React application runs at:

```text
http://localhost:3000/
```

The frontend communicates with the Django API running at:

```text
http://127.0.0.1:8000/
```

### 🔗 Repositories

**🎨 Frontend**

https://github.com/Neahans/bloom-ai-ecommerce

**🐍 Backend**

https://github.com/Neahans/bloom-ai-ecommerce-backend

---

## 🔐 Authentication

Protected API requests use a JWT access token.

Example:

```javascript
fetch("http://127.0.0.1:8000/api/cart/", {
  headers: {
    Authorization: `Bearer ${token}`
  }
});
```

---

## 🌸 CORS

During development, the backend allows requests from:

```text
http://localhost:3000
http://127.0.0.1:3000
```

This allows the React frontend to communicate with the Django REST API.

---

## 🧁 API Overview

| Endpoint              | Method | Purpose            |
| --------------------- | :----: | ------------------ |
| `/api/products/`      |   GET  | List products      |
| `/api/products/<id>/` |   GET  | Product details    |
| `/api/products/`      |  POST  | Create product     |
| `/api/products/<id>/` |   PUT  | Update product     |
| `/api/products/<id>/` | DELETE | Delete product     |
| `/api/auth/register/` |  POST  | Register user      |
| `/api/auth/login/`    |  POST  | Login              |
| `/api/auth/refresh/`  |  POST  | Refresh JWT        |
| `/api/cart/`          |   GET  | View cart          |
| `/api/cart/`          |  POST  | Add item to cart   |
| `/api/cart/<id>/`     |   PUT  | Update cart item   |
| `/api/cart/<id>/`     | DELETE | Remove cart item   |
| `/api/chat/`          |  POST  | Chat with Bloom AI |

---

## 🛡️ Security

Sensitive files are excluded from version control.

The project ignores:

```text
.env
.env.*
venv/
db.sqlite3
__pycache__/
*.pyc
```

### 🔒 Never expose

```text
GEMINI_API_KEY
```

Do not place API keys in:

* ❌ Source code
* ❌ Git commits
* ❌ README files
* ❌ Screenshots
* ❌ Public repositories

---

## 🌱 Future Improvements

Bloom is still growing ✨

Planned backend improvements include:

* 🛒 Complete checkout API
* 📦 Order management
* 🧾 Order history
* 💳 Payment integration
* ❤️ Wishlist API
* 🔎 Product search
* 🧠 Personalized AI recommendations
* 👤 User profile API
* 📊 Admin analytics
* 🏷️ Product reviews
* 📈 Inventory management

---

## 💌 Made With Love

<div align="center">

🌿 🧸 🌸 🛍️ ✨ 🌷

### Bloom AI

**React** ✦ **Django** ✦ **Gemini AI**

<br>

✨ *Keep growing. Keep creating. Keep blooming.* ✨

<br>

Made by **[Neaha N S](https://github.com/Neahans)**

</div>
