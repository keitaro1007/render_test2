# app.py
from flask import Flask, render_template_string
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="ja">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>おみくじアプリ</title>
        </head>
        <body>
            <h1>おみくじを引く</h1>
            <button onclick="fetch('/draw').then(response => response.text()).then(data => {
                document.getElementById('result').innerText = data;
            })">おみくじを引く</button>
            <h2 id="result"></h2>
        </body>
        </html>
    ''')

@app.route('/draw')
def draw():
    results = ["大吉", "吉", "凶"]
    return random.choice(results)

if __name__ == '__main__':
    app.run(debug=True)
