# Flask CRM Application

A simple Customer Relationship Management (CRM) application built using Flask.

## Index

1. [Description](#description)
2. [Features](#features)
3. [TechStack](#techstack)
4. [Dependencies](#dependencies)
5. [Screenshots](#screenshots)
6. [Installation](#installation)
7. [Usage](#usage)

## Description

This Flask application provides basic functionalities for managing customers and their communications.

## Features

- **User Authentication**: Users can register, login, and logout.
- **Customer Management**: Add, view, update, and delete customer information.
- **Communication Log**: Add communication logs for each customer.
- **Reminder Frequency**: Set reminder frequency for customers.

## TechStack

- **Backend Framework**: Flask
- **Database**: SQLite
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Session Management**: Flask-Session
- **Password Hashing**: Werkzeug Security

## Dependencies

- Flask
- Flask-Session
- Werkzeug

## Screenshots

**Register:**

[![register](https://i.postimg.cc/7bV2Qr1D/register.png)](https://postimg.cc/7bV2Qr1D)

**Invalid Login Handling:**

[![invalid-login-handling](https://i.postimg.cc/yghZHwwm/invalid-login-handling.png)](https://postimg.cc/yghZHwwm)

**Login Email & Password Check in Database:**

[![login-email-pass-check-database](https://i.postimg.cc/bDRsM1tL/login-email-pass-check-database.png)](https://postimg.cc/bDRsM1tL)

**Valid Login:**

[![valid-login](https://i.postimg.cc/9zV9pQ7J/valid-login.png)](https://postimg.cc/9zV9pQ7J)

**Add customer:**

[![add-cust](https://i.postimg.cc/xkMkvwjw/add-cust.png)](https://postimg.cc/xkMkvwjw)

**Add communication:**

[![add-comm](https://i.postimg.cc/Jt1yXYfF/add-comm.png)](https://postimg.cc/Jt1yXYfF)

**After deleting the customer with ID 1, it is removed from the customer information:**

[![delete-cust](https://i.postimg.cc/RNScMZCN/delete-cust.png)](https://postimg.cc/RNScMZCN)

**Customer Info:**

[![cust-info](https://i.postimg.cc/4mxhD2wc/cust-info.png)](https://postimg.cc/4mxhD2wc)

**View CRM:**

[![crm](https://i.postimg.cc/zyLHBLsX/crm.png)](https://postimg.cc/zyLHBLsX)

**Update customer:**

[![update-cust](https://i.postimg.cc/9479x4bN/update-cust.png)](https://postimg.cc/9479x4bN)


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/abinetha/Contact_CRM.git
   ```
   
2. Install dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```
   
3. Run the application:
   
   ```bash
   python app.py
   ```

## Usage

1. Navigate to [http://localhost:5000](url) in your web browser.
2. **Customer Information:** Access this route at [http://127.0.0.1:5000/customer_info](url) to view a list of all customers and their details. Use this route to retrieve information about customers stored in the database.
3. **Login:** Access this route at [http://127.0.0.1:5000/login](url) to log in to the application. This route is used for user authentication, allowing registered users to access the application's features.
4. **Logout:** Access this route at [http://127.0.0.1:5000/logout](url) to log out of the application. Use this route when you want to end your current session and log out securely.
5. **Registration:** Access this route at [http://127.0.0.1:5000/register](url) to create a new user account. This route is used for user registration, allowing new users to sign up and access the application.
6. **Add Customer:** Access this route at [http://127.0.0.1:5000/add_customer](url) to add a new customer to the database. Use this route when you need to enter details for a new customer into the system.
7. **Delete Customer:** Access this route at [http://127.0.0.1:5000/delete_customer/int:customer_id](url) to delete a customer from the database. Provide the customer_id of the customer you want to delete as part of the URL.
8. **Update Customer:** Access this route at [http://127.0.0.1:5000/update_customer/int:customer_id](url) to update the details of a customer in the database. Provide the customer_id of the customer you want to update as part of the URL.
9. **Add Communication:** Access this route at [http://127.0.0.1:5000/add_communication/int:customer_id](url) to add a communication log for a specific customer. Provide the customer_id of the customer for whom you want to add a communication log as part of the URL.
10. **CRM:** Access this route at [http://127.0.0.1:5000/crm/int:customer_id](url) to view customer details and communication logs in a CRM (Customer Relationship Management) interface. Provide the customer_id of the customer you want to view as part of the URL. Use this route to access detailed information and communication history for a specific customer.
