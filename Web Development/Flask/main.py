from random import randint
from flask import Flask, session, redirect, url_for
from db_scripts import get_question_after

def index():
    max_quiz = 3
     # atau jika siswa menulis get_quiz_count(), Anda dapat mengimpornya dan menentukan:
     # max_quiz = get_quiz_count[0]
    session['quiz'] = randint(1, max_quiz)
     # atau jika siswa menulis get_quiz_count(), Anda dapat mengimpornya dan menentukan:
     # session['quiz'] = get_random_quiz_id()
    session['last_question'] = 0
    return '<a href="/test">Test</a>'

def test():
    result = get_question_after(session['last_question'], session['quiz'])
    if result is None or len(result) == 0:
        return redirect(url_for('result'))
    else:
        session['last_question'] = result[0]
        # jika kita telah mengajarkan data base untuk mengembalikan Row atau dict, maka kita tidak boleh menulis result[0] dan sebaliknya menulis result['id']
        return '<h1>' + str(quiz) + '<br>' + str(result) + '</h1>'

def result():
    return "that's all folks!"

# membuat objek aplikasi web:
app = Flask(__name__)
app.add_url_rule('/', 'index', index) # membuat aturan untuk URL'/'
app.add_url_rule('/test', 'test', test) # membuat aturan untuk URL'/test'
app.add_url_rule('/result', 'result', result) # membuat aturan untuk URL'/test'

# Mengatur kunci enkripsi
app.config['SECRET_KEY'] = 'ThisIsSecretSecretSecretLife'

if __name__ == '__main__':
    # Memulai server web:
    app.run()