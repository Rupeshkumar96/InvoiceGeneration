# 🧾 Invoice Management System

A professional, full-stack Invoice Management System built with **Python** and **Flask**. This application allows users to register, manage customer databases, generate invoices, and export them as high-quality PDF documents.

---

## 🛠️ Tech Stack

<table border="0">
  <tr>
    <td align="center" width="96">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="48" height="48" alt="Python" />
      <br />Python
    </td>
    <td align="center" width="96">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/flask/flask-original.svg" width="48" height="48" alt="Flask" />
      <br />Flask
    </td>
    <td align="center" width="96">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/sqlite/sqlite-original.svg" width="48" height="48" alt="SQLite" />
      <br />SQLite
    </td>
    <td align="center" width="96">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg" width="48" height="48" alt="HTML5" />
      <br />HTML5
    </td>
    <td align="center" width="96">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original.svg" width="48" height="48" alt="CSS3" />
      <br />CSS3
    </td>
  </tr>
</table>

---

## ✨ Features

* Secure Authentication:** User registration and login system using `Flask-Login` and `Werkzeug` for password hashing.
* Customer Management:** Dedicated module to add and store customer details including names, emails, and phone numbers.
* Invoice Lifecycle:** Create invoices for existing customers, track their status (Pending/Paid), and manage them from a central dashboard.
* PDF Generation:** Generate professional, downloadable PDF invoices on demand using the `ReportLab` library.
* User-Specific Data:** Multi-tenant architecture where users only see their own customers and invoices.
* Responsive UI:** Clean, modern interface styled with custom CSS for ease of use.

---


## Installation & Setup
1. Clone the repository
Bash
git clone https://github.com/yourusername/invoice-management-system.git

cd invoice-management-system

2. Set up a Virtual Environment
Bash
python -m venv venv
source venv/bin/activate 

On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Initialize Database & Run

The database will automatically initialize on the first run.

Run :- python app.py

Visit http://127.0.0.1:5000 in your browser.


📁INVOICE-GENERATION/
│
├── .gitignore              # Files to ignore (like __pycache__, .env, venv/)
├── README.md               # Project description, setup guide, and screenshots
├── requirements.txt        # Python dependencies (Flask, SQLAlchemy, etc.)
├── app.py                  # Main application entry point
├── start.sh                # Shell script to run the app
│
├── static/                 # CSS, JS, and image assets
│   ├── css/
│   │   └── style.css
│   ├── js/                 # (Optional) For any frontend logic
│   └── img/                # Logos or background images
│
├── templates/              # HTML files for Flask/Jinja2
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── invoices.html
│   ├── create_invoice.html
│   ├── add_customer.html
│   └── invoice_pdf.html
│
└── instance/               # (Auto-generated) For your SQLite database
    └── database.db

📝 Database Schema
The application uses three primary models:

User: Manages authentication credentials.

Customer: Stores client contact information linked to a specific user.

Invoice: Records transaction details, amounts, and statuses.

📄 License
This project is open-source and available under the MIT License.
<img width="1853" height="713" alt="{41727AEF-3053-4205-8372-F97E029918F5}" src="https://github.com/user-attachments/assets/8fc15b4f-c8d7-4bff-b49a-3092b935f207" />
<img width="1864" height="656" alt="{2C2B04BD-6FD5-4D21-84D0-123B925D6C62}" src="https://github.com/user-attachments/assets/3b19b265-d886-42ef-817b-9afbca49d348" />
