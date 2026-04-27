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

* [cite_start]**Secure Authentication:** User registration and login system using `Flask-Login` and `Werkzeug` for password hashing.
* [cite_start]**Customer Management:** Dedicated module to add and store customer details including names, emails, and phone numbers.
* [cite_start]**Invoice Lifecycle:** Create invoices for existing customers, track their status (Pending/Paid), and manage them from a central dashboard.
* [cite_start]**PDF Generation:** Generate professional, downloadable PDF invoices on demand using the `ReportLab` library.
* [cite_start]**User-Specific Data:** Multi-tenant architecture where users only see their own customers and invoices.
* [cite_start]**Responsive UI:** Clean, modern interface styled with custom CSS for ease of use.

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone [https://github.com/yourusername/invoice-management-system.git](https://github.com/yourusername/invoice-management-system.git)
cd invoice-management-system

🛠️ Installation & Setup
1. Clone the repository
Bash
git clone https://github.com/yourusername/invoice-management-system.git
cd invoice-management-system
2. Set up a Virtual Environment
Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Initialize Database & Run
The database will automatically initialize on the first run.

Bash
python app.py
Visit http://127.0.0.1:5000 in your browser.

📁 Project Structure
app.py: The main application entry point containing routes, models, and business logic.

templates/: Jinja2 HTML templates for the frontend.

static/: CSS and styling assets.


requirements.txt: List of Python packages required for the project.

start.sh: A shell script to launch the application using the Gunicorn production server.

📝 Database Schema
The application uses three primary models:

User: Manages authentication credentials.

Customer: Stores client contact information linked to a specific user.

Invoice: Records transaction details, amounts, and statuses.

📄 License
This project is open-source and available under the MIT License.
<img width="1853" height="713" alt="{41727AEF-3053-4205-8372-F97E029918F5}" src="https://github.com/user-attachments/assets/8fc15b4f-c8d7-4bff-b49a-3092b935f207" />
<img width="1864" height="656" alt="{2C2B04BD-6FD5-4D21-84D0-123B925D6C62}" src="https://github.com/user-attachments/assets/3b19b265-d886-42ef-817b-9afbca49d348" />
