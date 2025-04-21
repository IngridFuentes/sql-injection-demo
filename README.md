# SQL Injection Vulnerability Demo

This project is a hands-on demonstration of a login system vulnerable to SQL injection, followed by a secure version using parameterized queries. It showcases my understanding of **web security**, **Python**, **Flask**, **SQLite**, and **best practices in secure coding**.


## Why This Project

- To demonstrate awareness of common security flaws
- To show how insecure SQL queries can be exploited
- To highlight my ability to identify and fix vulnerabilities


## Tech Stack

- Python
- Flask
- SQLite
- HTML

### Clone the repo

git clone https://github.com/IngridFuentes/sql-injection-demo.git

### Start the app

Then go to:

http://localhost:5000

### Try this vulnerability

- Username: admin

- Password: ' OR '1'='1

This input bypasses authentication using SQL injection.

###  Check the Secure login route

Check the /secure_login route to see the fix using parameterized queries.
