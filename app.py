from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'tesifuk_secret_key_123'

def init_db():
    conn = sqlite3.connect('booking.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS agendamentu (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    naran TEXT,
                    telemovel TEXT,
                    servisu TEXT,
                    data TEXT,
                    oras TEXT,
                    status TEXT DEFAULT 'Pendente'
                )''')
    conn.commit()
    conn.close()

init_db()

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

    conn = sqlite3.connect('booking.db')
    c = conn.cursor()
    c.execute("INSERT INTO agendamentu (naran, telemovel, servisu, data, oras) VALUES (?, ?, ?, ?, ?)",
              (naran, telemovel, servisu, data, oras))
    conn.commit()
    conn.close()

    flash('Agendamentu Susesu Kria!')
    return redirect(url_for('index'))

@app.route('/admin/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin123':
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            flash('Username ka Password sala!')
    return render_template('login.html')

@app.route('/admin')
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    conn = sqlite3.connect('booking.db')
    c = conn.cursor()
    c.execute("SELECT * FROM agendamentu ORDER BY id DESC")
    lista = c.fetchall()
    conn.close()
    
    return render_template('admin.html', lista=lista)

@app.route('/admin/status/<int:id>/<string:status>')
def update_status(id, status):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    conn = sqlite3.connect('booking.db')
    c = conn.cursor()
    c.execute("UPDATE agendamentu SET status = ? WHERE id = ?", (status, id))
    conn.commit()
    conn.close()
    
    return redirect(url_for('admin'))

@app.route('/admin/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
