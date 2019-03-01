from flask import Flask, render_template, request, redirect, url_for
import numpy as np

app = Flask(__name__)


def picked_up():
    """メッセージをランダムに表示するメソッド"""
    messages = [
        "こんにちは、あなたの名前を入力してください。",
        "やあ！お名前は何ですか？",
        "あなたの名前を教えてね"
    ]
    return np.random.choice(messages)


@app.route('/')
def index():
    title = 'ようこそ'
    message = picked_up()
    return render_template('index.html', message=message, title=title)


if __name__ == '__main__':
    app.debug = True
    app.run()
