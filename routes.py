from app import app
from flask import render_template, redirect, url_for, request, flash

messages = []


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
            flash('Поле "имя" обязательно!')
        elif not email:
            flash('Поле email обязательно')
        else:
            messages.append({'username': name, 'email': email, 'phone': phone})
            return redirect(url_for('main_page'))
    return render_template('about.html')


@app.route('/admin')
def admin():
    return render_template('admin.html', user_messages=messages)
