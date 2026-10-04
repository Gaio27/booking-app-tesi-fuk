cat << 'EOF' > app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = 'tesi_fuk_secret_key_dili'

DB_NAME = 'booking.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS agendamentu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            naran TEXT NOT NULL,
            telemovel TEXT NOT NULL,
            servisu TEXT NOT NULL,
            data TEXT NOT NULL,
            oras TEXT NOT NULL,
            status TEXT DEFAULT 'Pendente'
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin_user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute("SELECT * FROM admin_user WHERE username = 'admin'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO admin_user (username, password) VALUES (?, ?)",
                       ('admin', generate_password_hash('password123')))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agendar', methods=['POST'])
def agendar():
    naran = request.form.get('naran')
    telemovel = request.form.get('telemovel')
    servisu = request.form.get('servisu')
    data = request.form.get('data')
    oras = request.form.get('oras')

    if not all([naran, telemovel, servisu, data, oras]):
        flash('Favór preenxe dadus hotu-hotu!')
        return redirect(url_for('index'))

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO agendamentu (naran, telemovel, servisu, data, oras)
        VALUES (?, ?, ?, ?, ?)
    ''', (naran, telemovel, servisu, data, oras))
    conn.commit()
    conn.close()

    flash('Agendamentu susesu tiha ona!')
    return redirect(url_for('index'))

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admin_user WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[2], password):
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Username ka password sala!')

    return render_template('login.html')

@app.route('/admin')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM agendamentu ORDER BY id DESC")
    lista_agendamentu = cursor.fetchall()
    conn.close()

    return render_template('admin.html', lista=lista_agendamentu)

@app.route('/admin/status/<int:id>/<string:status>')
def altera_status(id, status):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE agendamentu SET status = ? WHERE id = ?", (status, id))
    conn.commit()
    conn.close()
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
EOF
