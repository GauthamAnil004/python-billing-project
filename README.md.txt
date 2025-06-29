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

## Technologies Used

- Python 3.x
- MySQL
- `mysql-connector-python` (for MySQL connectivity)

## Setup Instructions

1. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
