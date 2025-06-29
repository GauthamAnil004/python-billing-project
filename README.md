# Python Billing System

This project contains two versions of a billing system written in Python and backed by MySQL:

## Versions

### 1. CLI Version (`billing_project.py`)
- Feature-rich and designed for advanced control.
- Includes role-based menus, product stock management, bill updates, and per-user bill tables.
- Still under development — some features may contain bugs or incomplete logic.
- Suitable for testing core functionality and database operations.

### 2. GUI Version (`gui_billing_app.py`)
- Built using Tkinter for a clean and user-friendly interface.
- Supports user registration and login.
- Enables adding products, viewing products, and creating bill entries.
- Supports basic role-based access (admin, staff, customer, guest).
- Easier to use than the CLI version, but with fewer features.
- Ideal for users who prefer simplicity and graphical interfaces.

---

You can run either version depending on your preference for simplicity or advanced functionality.

---

# Billing System (CLI Version)

This is a command-line billing system developed in Python with MySQL as the backend. It includes user authentication, role-based access control, billing management, stock management, and audit features.

## Features

- Role-based login system with support for:
  - Super Admin
  - Admin
  - Customer
  - Guest
  - Cashier
  - Accountant
- User registration, login, and deletion
- Generate and update bills
- Add and manage stock
- View stock, check parent/child product types
- Track date of purchase
- View and delete customer bills

---

# Billing System (GUI Version)

This version uses Tkinter to provide a graphical interface for basic billing operations.

## Features

- Login and account registration
- User designations (admin, staff, customer, guest)
- Add products to stock
- View product list in a table
- Add products to bill with timestamp
- Basic dashboard for navigation

---

## Technologies Used

- Python 3.x
- MySQL
- `mysql-connector-python` (for MySQL connectivity)
- Tkinter (comes with standard Python installation)

---

## Setup Instructions

1. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
