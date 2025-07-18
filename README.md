Cloud Kitchen App

A simple cloud kitchen management app with a Python backend and a lightweight HTML/CSS/JS UI.
Supports managing products, orders, and units of measure with a MySQL database.

Project Structure

cloud-kitchen-app/
├── backend/     # Python Flask backend
├── ui/          # Frontend HTML, CSS, JS files
├── README.md
├── requirements.txt


Features

Backend:
Python Flask REST API.
MySQL database integration.
Manage:
Products
Orders
Units of measure.
SQL schema provided (cloud_kitchen.sql).

Frontend:
HTML/CSS/JavaScript UI.
Screens for:
Add/Manage Products
Place/View Orders


Tech Stack

Backend: Python, Flask
Database: MySQL
Frontend: HTML, CSS, JavaScript


Setup Instructions

Backend

Install dependencies:
cd backend
pip install -r requirements.txt

Set up the MySQL database:
Create a database (e.g., cloud_kitchen).
Run the provided SQL script:
sql
Copy
Edit
source cloud_kitchen.sql;

Run the server:
bash
Copy
Edit
python server.py
By default it runs at:
http://localhost:5000/

Frontend

Open the ui/index.html file in a browser.
It makes API calls to the Flask backend.


Files of Interest

Backend:

server.py — main Flask app.
sql_connection.py — DB connection helper.
order_dao.py — order-related DB ops.
products_dao.py — product-related DB ops.
uom_dao.py — unit of measure DB ops.

Frontend:

ui/index.html — Home page.
ui/manage-product.html — Manage products page.
ui/order.html — Order page.


Contributing

PRs and feedback welcome! Please open an issue or submit a pull request.

Maintainer

Dharun M

