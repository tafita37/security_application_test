# 🔐 security_application_test

## 1. Overview

### 📝 Project description  
A Django-based web application intentionally designed to explore, exploit, and secure common web vulnerabilities including **Cross-Site Scripting (XSS)**, **SQL Injection**, and **Brute Force Attacks**.  
The app simulates real-world exploitation scenarios and implements defensive mechanisms, offering an educational playground for cybersecurity experimentation.

### 🎯 Objective  
To understand how XSS, SQL Injection, and Brute Force attacks work in practice, how attackers exploit them, and how developers can secure applications through proper countermeasures such as input validation, secure headers, and authentication hardening.

---

## 2. Features

### ✅ Features list

- User authentication system
- Article listing and commenting functionality (XSS vulnerability testbed)
- Simulated cookie theft and client-side botnet via XSS
- SQL-based login page with intentional injection flaw
- Session hijacking and database exposure demonstration
- Brute force password guessing using Python + `requests`
- Defensive mechanisms including:
  - Output escaping
  - Content Security Policy (CSP)
  - Prepared statements
  - Rate-limiting / IP blocking
  - Secure & HttpOnly cookies

---

## 3. Requirements

### 🛠️ Required environment

- **Operating System**: Windows / Linux / macOS
- **Languages & Frameworks**: Python 3.10+, Django 4.x
- **Libraries**:
  - `Django`
  - `requests`
  - `itertools`
  - `beautifulsoup4` (for some optional payload testing)
  - Any other dependencies listed in `requirements.txt`

---

## 4. Installation

### 📦 Clone the repository

```bash
git clone https://github.com/tafita37/security_application_test.git
cd security_application_test
```

### Setup the project in the Odoo modules directory, create a virtual environment, install dependencies, and run the project:

```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```