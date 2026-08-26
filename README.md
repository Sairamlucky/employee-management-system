# Employee Management System

A web-based Employee Management System built using Python, Flask, PostgreSQL, HTML, and CSS.

This application allows users to manage employee records through a simple and responsive web interface.

## Features

- Dashboard
- Add new employees
- View all employees
- Search employees
- View employee details
- Edit employee information
- Delete employees
- Delete confirmation
- Form validation
- PostgreSQL database integration
- Flash messages for success/error notifications
- Responsive and modern UI
# Technologies used

# Backend
- Python
- Flask
- Psycopg

# frontend
- HTML5
- CSS3
# Database
- PostgreSQL
# Tools
- Git
- GitHub
- VS Code

#project Structure

employee-management-system/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── dashboard.html
│   ├── employee.html
│   ├── employees.html
│   ├── edit_employee.html
│   └── view_employee.html
│
├── .env
└── venv/     # Local only - not uploaded to GitHub

Installation
git clone https://github.com/Sairamlucky/employee-management-system.git

# Open the project
cd employee-management-system
# Create a virtual environment
python -m venv venv
# Install dependencies
pip install -r requirements.txt
# Environment Variables
Create a .env file in the project root
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
FLASK_SECRET_KEY=your_secret_key

# Run the Application
python app.py

browser-http://127.0.0.1:5000/

CRUD Operations

# The application supports complete CRUD functionality:

Create — Add a new employee
Read — View employee records
Update — Edit employee information
Delete — Remove employee records

>Future Improvements
>user authentication and login
>Employee profile photos
>Pagination
>Advanced search and filtering
>Department management
>Export employees to CSV/Excel
>REST API
>Cloud deployment

GitHub:
https://github.com/Sairamlucky

