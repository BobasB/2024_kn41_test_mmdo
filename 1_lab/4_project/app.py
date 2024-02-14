from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '<p>Вітаємо, це мій перший веб сайт на Flask!</p>'

@app.route('/help')
def help():
    count =+ 1
    return f"""
    <body style="background-color:powderblue;">
    <p>Це сторінка з документацією. Поки що вона є пуста.</p>
    <p>Сайт запущений на {os.environ["OS"]}</p>
    <p>Ви відвідали цю сторінку {count} разів</p>
    """

if __name__ == '__main__':
    app.run(debug=True)