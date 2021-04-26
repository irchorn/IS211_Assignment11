from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import url_for

app = Flask(__name__)

todo_list = [
    ("Read Tutorial", "is@cuny.edu", "High"),
    ("Do Homework", "bb@cgmail.com", "High"),
    ("Optional Reading", "ww@gmail.com", "Low"),
]


@app.route('/')
def display_list():
    things_todo = todo_list

    return render_template('todo.html', things_todo=things_todo)


@app.route('/submit', methods=["POST"])
def submit():
    global todo_list
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']
    todo_list.append((task, email, priority))
    return redirect(url_for('display_list'))


@app.route('/clear', methods=["DELETE"])
def clear():
    global todo_list

    todo_list = []
    return redirect(url_for('display_list'))


if __name__ == '__main__':
    app.run(debug=True)
