from flask import Flask, render_template, request, redirect, make_response, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from reportlab.pdfgen import canvas
import io
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secret123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///invoice.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# ---------------- MODELS ----------------
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(100))
    amount = db.Column(db.Float)
    status = db.Column(db.String(20))
    date = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# ---------------- LOGIN ----------------
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect('/')
        else:
            flash("Invalid username or password")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if User.query.filter_by(username=request.form['username']).first():
            flash("Username already exists")
            return redirect('/register')
        hashed_pw = generate_password_hash(request.form['password'])
        u = User(username=request.form['username'], password=hashed_pw)
        db.session.add(u)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

# ---------------- APP ROUTES ----------------
@app.route('/')
@login_required
def dashboard():
    return render_template(
        'dashboard.html',
        customers=Customer.query.filter_by(user_id=current_user.id).count(),
        invoices=Invoice.query.filter_by(user_id=current_user.id).count()
    )

@app.route('/add_customer', methods=['GET', 'POST'])
@login_required
def add_customer():
    if request.method == 'POST':
        c = Customer(
            name=request.form['name'],
            email=request.form['email'],
            phone=request.form['phone'],
            user_id=current_user.id
        )
        db.session.add(c)
        db.session.commit()
        return redirect('/')
    return render_template('add_customer.html')

@app.route('/create_invoice', methods=['GET', 'POST'])
@login_required
def create_invoice():
    customers = Customer.query.filter_by(user_id=current_user.id).all()
    if request.method == 'POST':
        inv = Invoice(
            customer=request.form['customer'],
            amount=request.form['amount'],
            status='Pending',
            date=datetime.now().strftime('%d-%m-%Y'),
            user_id=current_user.id
        )
        db.session.add(inv)
        db.session.commit()
        return redirect('/invoices')
    return render_template('create_invoice.html', customers=customers)

@app.route('/invoices')
@login_required
def invoices():
    data = Invoice.query.filter_by(user_id=current_user.id).all()
    return render_template('invoices.html', invoices=data)

@app.route('/mark_paid/<int:id>')
@login_required
def mark_paid(id):
    inv = Invoice.query.get(id)
    if inv.user_id == current_user.id:
        inv.status = 'Paid'
        db.session.commit()
    return redirect('/invoices')

@app.route('/invoice_pdf/<int:id>')
@login_required
def invoice_pdf(id):
    invoice = Invoice.query.get(id)
    if invoice.user_id != current_user.id:
        return "Unauthorized", 403

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.setFont("Helvetica", 12)

    p.drawString(100, 800, "INVOICE")
    p.drawString(100, 760, f"Invoice No: {invoice.id}")
    p.drawString(100, 740, f"Date: {invoice.date}")
    p.drawString(100, 700, f"Customer: {invoice.customer}")
    p.drawString(100, 680, f"Amount: ₹{invoice.amount}")
    p.drawString(100, 660, f"Status: {invoice.status}")

    p.showPage()
    p.save()

    buffer.seek(0)
    response = make_response(buffer.read())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=invoice.pdf'
    return response

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
