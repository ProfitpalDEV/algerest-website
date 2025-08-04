from flask import Flask, render_template, request, redirect, url_for, flash, session
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Main routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Here you would typically send email or save to database
        flash('Thank you for your message! We will contact you soon.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')

# Employee system routes
@app.route('/employee/login', methods=['GET', 'POST'])
def employee_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Simple authentication (replace with proper auth later)
        if username == 'admin' and password == 'admin123':
            session['employee'] = username
            flash('Welcome to ALGEREST Employee Portal!', 'success')
            return redirect(url_for('employee_dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'error')

    return render_template('employee_login.html')

@app.route('/employee/dashboard')
def employee_dashboard():
    if 'employee' not in session:
        flash('Please sign in to access the employee portal.', 'error')
        return redirect(url_for('employee_login'))

    return render_template('employee_dashboard.html')

@app.route('/employee/drawings')
def employee_drawings():
    if 'employee' not in session:
        return redirect(url_for('employee_login'))

    return render_template('employee_drawings.html')

@app.route('/employee/logout')
def employee_logout():
    session.pop('employee', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)