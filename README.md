# 🗃️ Inventory Management System API

A backend system built with **FastAPI**, **SQLAlchemy**, and **MySQL**, designed to manage inventory — specifically **categories** and **products** — with clean API routes, validation, and a modular architecture.

---

 # 📌 Features

- ✅ Create, read, update, and delete categories
- ✅ Create, update, and delete products (linked to categories)
- ✅ Validation with Pydantic schemas
- ✅ Swagger UI for categories and products
- ✅ MySQL database connection using SQLAlchemy
- ✅ Environment configuration via `.env` file
- ✅ Tested using Postman

---

# 🧱 Project Structure

.
├── app/
│ ├── init.py
│ ├── main.py # FastAPI app instance
│ ├── database.py # SQLAlchemy DB setup
│ ├── models.py # Category & Product models
│ ├── schemas.py # Pydantic validation schemas
│ ├── routers/
│ │ ├── category.py # Category endpoints
│ │ └── product.py # Product endpoints
│ └── crud/
│ ├── crud_category.py # Category logic
│ └── crud_product.py # Product logic
├── .env # ← Environment variables (not tracked by Git)
├── requirements.txt
├── README.md # ← This file



---

1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/inventory-api.git
cd inventory-api

2️⃣ Set up a virtual environment
bash
python -m venv venv
source venv/bin/activate 
 
3️⃣ Install dependencies
bash
pip install -r requirements.txt

4️⃣ Create a .env file
Create a .env file in the root directory:
env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=sims

5️⃣ Update database.py to load .env
Make sure you're using python-dotenv in app/database.py:
python
from dotenv import load_dotenv
import os
load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
...

6️⃣ Run the application
bash
uvicorn app.main:app --reload

7️⃣ Access the docs
Visit: http://localhost:8000/docs

🔁 API Endpoints
📂 Categories
Method	Endpoint	Description
GET	/categories/	List all categories
GET	/categories/{id}	Get category by ID
POST	/categories/	Create a category
PUT	/categories/{id}	Update a category
DELETE	/categories/{id}	Delete a category

📦 Products
Method	Endpoint	Description
POST	/products/	Create a product
PUT	/products/{id}	Update a product
DELETE	/products/{id}	Delete a product

ℹ️ GET /products/ not implemented yet.

📥 Sample JSON: Create Category
json
{
  "cname": "MOUSE",
  "description": "ZEBRONICS,DELL..",
}

🛠 Tech Stack
FastAPI – API framework

SQLAlchemy – ORM for DB access

MySQL – Backend database

Pydantic – Data validation

Uvicorn – ASGI server

Postman – API testing

dotenv – Load environment variables

👤 Author
Merina Jaya George
Sreenandana M
Arya Pradeep
Nandana K
Aparna S S
Backend Developer | Python + FastAPI Projects

📜 License
This project is licensed under the MIT License.
