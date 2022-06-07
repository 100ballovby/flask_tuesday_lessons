from app import app
from flask import render_template, redirect, url_for


@app.route('/')  # пишу функцию для главной страницы
def main_page():
    # функция просто генерирует пользователю шаблон главной страницы
    return render_template('index.html')
