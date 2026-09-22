<div align="center">

# 🐍 Bloom AI — Backend

### ✨ The little backend that makes Bloom bloom ✨

<img src="https://img.shields.io/badge/Django-Backend-59633B?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
<img src="https://img.shields.io/badge/Django_REST_Framework-API-E9A0A8?style=for-the-badge&logo=django&logoColor=white" alt="DRF" />
<img src="https://img.shields.io/badge/Google_Gemini-AI-FFF4E8?style=for-the-badge&logo=google&logoColor=59633B" alt="Google Gemini" />
<img src="https://img.shields.io/badge/SQLite-Database-59633B?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />

<br />

<img src="https://img.shields.io/badge/JWT-Authentication-E9A0A8?style=flat-square" alt="JWT" />
<img src="https://img.shields.io/badge/Python-3.x-59633B?style=flat-square&logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Status-In_Development-E9A0A8?style=flat-square" alt="Status" />

<br /><br />

🌸 🧸 🌿 🛍️ ✨ 🌷

### Products • Authentication • Cart • AI

</div>

---

## 🌷 About

**Bloom AI Backend** is the Django REST API powering the Bloom AI e-commerce application.

It provides the backend services required by the React frontend, including:

- 🛍️ Product management
- 👤 User authentication
- 🔐 JWT authentication
- 🛒 Cart management
- 🤖 Gemini-powered AI chatbot
- 📦 Product stock information
- 🔌 REST API endpoints

The backend is designed to work together with the **Bloom AI React frontend**.

> 🌿 *The frontend is where Bloom looks beautiful.  
> The backend is where everything works behind the scenes.*

---

## 💕 Frontend Repository

Looking for the React frontend?

### 🌸 Bloom AI — Frontend

<a href="https://github.com/Neahans/bloom-ai-ecommerce">
  <img src="https://img.shields.io/badge/🌸_View_Frontend_Repository-59633B?style=for-the-badge" alt="Frontend Repository" />
</a>

🔗 **Frontend Repository:**  
https://github.com/Neahans/bloom-ai-ecommerce

---

## 🪴 Full Project

```text
🌿 Bloom AI
│
├── 🎨 React Frontend
│   └── bloom-ai-ecommerce
│
└── 🐍 Django Backend
    └── bloom-ai-ecommerce-backend
🔗 Connect Both Repositories
🌸 Part	Repository
🎨 Frontend	Bloom AI Frontend
🐍 Backend	Bloom AI Backend
🎀 Features
🛍️ Product API

The backend provides product APIs for the React application.

GET /api/products/
GET /api/products/<id>/
POST /api/products/
PUT /api/products/<id>/
DELETE /api/products/<id>/

Product information includes:

Product name
Description
Price
Category
Image
Stock
Creation date
👤 Authentication

Bloom uses JWT-based authentication.

Features include:

🌸 User registration
🔐 Login
🔑 Access tokens
♻️ Refresh tokens
🛡️ Protected API requests

Authentication endpoints:

POST /api/auth/register/
POST /api/auth/login/
POST /api/auth/refresh/
🛒 Cart API

Users can manage their own shopping cart.

GET  /api/cart/
POST /api/cart/
PUT  /api/cart/<id>/
DELETE /api/cart/<id>/

Each cart item contains:

🛍️ Product
🔢 Quantity
💰 Product price
👤 User

Cart data is protected using authentication.

🤖 Bloom AI

Bloom includes an AI-powered shopping assistant using Google Gemini.

The React chatbot sends the user's message to the Django API:

React Chatbot
      │
      │ POST /api/chat/
      ▼
Django REST API
      │
      ▼
Google Gemini
      │
      ▼
AI Response
      │
      ▼
React Chatbot

Example:

User:
"I need something under ₹1500."

        ↓

Bloom AI:
"Sure! You could try the Blush Tote Bag..."
💬 Chat Endpoint
POST /api/chat/

Request:

{
  "message": "I need something under ₹1500."
}

Response:

{
  "reply": "..."
}
🧸 Tech Stack
🌷 Technology	🛠️ Purpose
🐍 Python	Backend language
🌿 Django	Web framework
🔌 Django REST Framework	REST APIs
🤖 Google Gemini	AI chatbot
🔐 Simple JWT	Authentication
🗄️ SQLite	Database
🌱 python-dotenv	Environment variables
🌸 django-cors-headers	Frontend API communication
🌱 Project Structure
bloom-ai-ecommerce-backend/
│
├── chatbot/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── ecommerce_backend/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── products/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── users/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── .gitignore
├── requirements.txt
└── README.md
🚀 Getting Started
1️⃣ Clone the backend
git clone https://github.com/Neahans/bloom-ai-ecommerce-backend.git
cd bloom-ai-ecommerce-backend
2️⃣ Create a virtual environment

Windows:

python -m venv venv

Activate it:

venv\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Configure environment variables

Create a .env file in the backend root:

GEMINI_API_KEY=your_api_key_here

🔒 Never commit .env to GitHub.

The .env file is already excluded through .gitignore.

5️⃣ Run migrations
python manage.py migrate
6️⃣ Start the Django server
python manage.py runserver

The backend will run at:

http://127.0.0.1:8000/
🌸 Connect With the React Frontend

Start the React frontend separately:

npm start

The frontend runs at:

http://localhost:3000/

The React application communicates with the Django backend through REST API endpoints.

┌──────────────────────┐
│   🌸 React Frontend  │
│   localhost:3000     │
└──────────┬───────────┘
           │
           │ REST API
           ▼
┌──────────────────────┐
│   🐍 Django Backend  │
│   127.0.0.1:8000     │
└──────────┬───────────┘
           │
      ┌────┴─────┐
      ▼          ▼
 🗄️ SQLite    🤖 Gemini
🔐 API Authentication

For protected endpoints, send the JWT access token in the request header:

Authorization: Bearer <access_token>

Example:

fetch("http://127.0.0.1:8000/api/cart/", {
  headers: {
    Authorization: `Bearer ${token}`
  }
});
🌿 CORS Configuration

The backend allows requests from the React development server:

http://localhost:3000
http://127.0.0.1:3000

This allows the React frontend to communicate with the Django REST API during development.

🧁 API Overview
🌷 Endpoint	🔧 Method	✨ Purpose
/api/products/	GET	List products
/api/products/<id>/	GET	Product details
/api/auth/register/	POST	Register user
/api/auth/login/	POST	Login
/api/auth/refresh/	POST	Refresh JWT
/api/cart/	GET	View cart
/api/cart/	POST	Add to cart
/api/chat/	POST	Chat with Bloom AI
🛡️ Environment & Security

Sensitive configuration should never be committed to GitHub.

The following files are ignored:

.env
.env.*
venv/
db.sqlite3
__pycache__/
*.pyc
🔒 Never expose:
GEMINI_API_KEY

in source code, screenshots, README files, or Git commits.

🧸 Future Improvements

Bloom is still growing 🌱

Planned backend improvements:

🛒 Complete checkout API
📦 Order management
🧾 Order history
💳 Payment integration
❤️ Wishlist API
🔎 Product search
🧠 AI product recommendations
👤 User profile API
📊 Admin analytics
🏷️ Product reviews
📈 Inventory management
🌸 Related Repository
<div align="center">
🎨 Bloom AI Frontend
<a href="https://github.com/Neahans/bloom-ai-ecommerce"> <img src="https://img.shields.io/badge/🌸_Open_Bloom_AI_Frontend-59633B?style=for-the-badge" alt="Open Frontend Repository" /> </a>

<br /><br />

🐍 Bloom AI Backend

You're here! ✨

</div>
💌 Made With Love
<div align="center">

🌿 🧸 🌸 🛍️ ✨ 🌷

Bloom AI

React ✦ Django ✦ Gemini AI

<br />

✨ Keep growing. Keep creating. Keep blooming. ✨

<br />

Made by Neaha N S

</div> ```
