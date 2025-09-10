# 🍽️ Restaurant Management System  
 A web application built with Django and PostgreSQL that helps restaurants manage customers, orders, and menu items with full CRUD operations (Create, Read, Update, Delete). All records are securely stored in a relational database.  
## 🚀 Features

- Add, update, and delete customers, orders, and menu items

- PostgreSQL database integration with Django ORM  

- Organized workflows to simplify restaurant operations

- Secure data storage and management

## 🛠️ Tech Stack

- Backend: Python (Django)

- Frontend: HTML, CSS, Bootstrap

- Database: PostgreSQL

- Other: JavaScript, Django ORM

📂 Project Structure
```lua
restaurant-management/
│-- customers/         # Manage customers  
│-- orders/            # Manage orders  
│-- menu/              # Manage menu items  
│-- templates/         # HTML templates  
│-- static/            # CSS, JS, images  
│-- db.sqlite3 / PostgreSQL # Database  
│-- manage.py  
```
## ⚙️ Installation & Setup  
1. Clone the repository  
```bash
git clone https://github.com/YourUsername/restaurant-management.git
cd restaurant-management
```
2. Create and activate a virtual environment  
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```
3. Configure PostgreSQL database  

- Create a PostgreSQL database

- Update settings.py with your DB credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

5. Run migrations
```bash
python manage.py migrate
```
6. Create a superuser (optional for admin panel)
```bash
python manage.py createsuperuser
```

7. Run the server
```bash
python manage.py runserver
```

## 📌 What I Learned

- Building scalable web applications with Django

- Integrating PostgreSQL databases using Django ORM

- Implementing CRUD operations for real-world use cases

## 👨‍💻 Author  
<b>Mazen Eltelbany</b>  
📧 Email: [Mazeneltelbany383@gmail.com](mailto:Mazeneltelbany383@gmail.com)  
💼 LinkedIn: [LinkedIn](https://www.linkedin.com/in/mazen-eltelbany-b9641a326?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)

