from flask import Flask


app = Flask(__name__)
# связываю сайт с главным файлом проекта

from routes import *

if __name__ == '__main__':
    app.run()
