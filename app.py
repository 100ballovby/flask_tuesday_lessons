from flask import Flask


app = Flask(__name__)
# связываю сайт с главным файлом проекта
app.config['SECRET_KEY'] = 'try-to-guess'

from routes import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
