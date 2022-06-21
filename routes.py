import sqlite3
from app import app
from flask import render_template, redirect, url_for, request, flash


def db_connect():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # выгружаю строки из базы данных
    return conn


@app.route('/')  # пишу функцию для главной страницы
def main_page():
    # функция просто генерирует пользователю шаблон главной страницы
    return render_template('index.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':  # если форма отправлена
        name = request.form['username']
        email = request.form['email']
        phone = request.form['phone']

        if not name:  # если имя не вписали
            flash('Поле "имя" обязательно!', 'warning')
        elif not email:
            flash('Поле email обязательно', 'warning')
        else:
            try:
                connection = db_connect()
                connection.execute('INSERT INTO users (name, email, phone) VALUES (?, ?, ?)',
                                   (name, email, phone))
                connection.commit()  # применить изменения в БД
                connection.close()
                flash('Форма успешно отправлена!', 'success')
                return redirect(url_for('about'))
            except sqlite3.IntegrityError:
                flash('Пользователь с таким email уже существует!', 'danger')
                return redirect(url_for('about'))
    return render_template('about.html')


@app.route('/admin')
def admin():
    connection = db_connect()
    users = connection.execute('SELECT * FROM users')
    return render_template('admin.html', users=users)
