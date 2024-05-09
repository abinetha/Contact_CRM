from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3, time

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random string

# Database Initialization
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            address TEXT,
            gst_no TEXT,
            reminder_frequency INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS communications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            communication TEXT,
            FOREIGN KEY(customer_id) REFERENCES customers(id)
        )
    ''')
    conn.commit()
    conn.close()


# Routes
@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('customer_info'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()
        if user and user[3] == password:  # Check if user exists and password matches
            session['username'] = user[1]
            return redirect(url_for('customer_info'))
        else:
            print('hi')
            flash('Email or password does not exist in our database')
            time.sleep(1)
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
        conn.commit()
        conn.close()
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/customer_info')
def customer_info():
    if 'username' not in session:
        return redirect(url_for('login'))
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers')
    customers = cursor.fetchall()
    conn.close()
    return render_template('customer_info.html', customers=customers)

@app.route('/crm/<int:customer_id>')
def crm(customer_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers WHERE id = ?', (customer_id,))
    customer = cursor.fetchone()
    cursor.execute('SELECT * FROM communications WHERE customer_id = ? ORDER BY timestamp DESC', (customer_id,))
    communications = cursor.fetchall()
    conn.close()
    return render_template('crm.html', customer=customer, communications=communications)

@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        gst_no = request.form['gst_no']
        reminder_frequency = request.form['reminder_frequency']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO customers (name, email, phone, address, gst_no, reminder_frequency)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, email, phone, address, gst_no, reminder_frequency))
        conn.commit()
        conn.close()
        flash('Customer added successfully', 'success')
        return redirect(url_for('customer_info'))
    return render_template('add_customer.html')

@app.route('/delete_customer/<int:customer_id>')
def delete_customer(customer_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM customers WHERE id = ?', (customer_id,))
    conn.commit()
    conn.close()
    flash('Customer deleted successfully', 'success')
    return redirect(url_for('customer_info'))

@app.route('/update_customer/<int:customer_id>', methods=['GET', 'POST'])
def update_customer(customer_id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        gst_no = request.form['gst_no']
        reminder_frequency = request.form['reminder_frequency']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE customers
            SET name = ?, email = ?, phone = ?, address = ?, gst_no = ?, reminder_frequency = ?
            WHERE id = ?
        ''', (name, email, phone, address, gst_no, reminder_frequency, customer_id))
        conn.commit()
        conn.close()
        flash('Customer updated successfully', 'success')
        return redirect(url_for('customer_info'))
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers WHERE id = ?', (customer_id,))
    customer = cursor.fetchone()
    conn.close()
    return render_template('update_customer.html', customer=customer)

@app.route('/add_communication/<int:customer_id>', methods=['GET', 'POST'])
def add_communication(customer_id):
    if request.method == 'POST':
        communication = request.form['communication']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO communications (customer_id, communication)
            VALUES (?, ?)
        ''', (customer_id, communication))
        conn.commit()
        conn.close()
        flash('Communication added successfully', 'success')
        return redirect(url_for('customer_info'))
    return render_template('add_communication.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
