import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort

app = Flask(__name__)
# generate secret key
app.config['SECRET_KEY'] = '09c5d474925c3e4c306ee95fe8f3a3ef95eaec2e6e34ba8e'


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
# connection to database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_shoes(shoes_id):
    conn = get_db_connection()
    shoes = conn.execute("SELECT * FROM shoes WHERE id = ?", (shoes_id,)).fetchone()
    conn.close()
    # validate the post id exists
    if shoes is None:
        abort(404)
    # when post is found
    return shoes


@app.route('/')
def index():
    conn = get_db_connection()
    shoes = conn.execute('SELECT * FROM shoes').fetchall()
    conn.close()
    return render_template('index.html', shoes=shoes)


@app.route('/create/', methods=('GET', 'POST'))
def add():
    if request.method == "POST":
        name = request.form['name']
        image = request.form['image']
        price = request.form['price']
        if not name:
            flash("please enter name")
        elif not price:
            flash("please enter price")
        elif not image:
            flash("please enter image")
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO shoes (name, image, price) VALUES (?, ?, ?)', (name, image, price))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    shoes = get_shoes(id)
    if request.method == 'POST':
        name = request.form["name"]
        image = request.form["image"]
        price = request.form["price"]

        if not name:
            flash('Name required')
        elif not image:
            flash("Image URL required")
        elif not price:
            flash("Price requires")

        else:
            conn = get_db_connection()
            conn.execute('UPDATE shoes SET name = ?, image = ?, price = ?'
                         ' WHERE id = ?',
                         (name, image, price, id))
            conn.commit()
            return redirect(url_for('index'))

    return render_template("edit.html", shoes=shoes)


@app.route('/<int:id>/delete/', methods=('GET', 'POST'))
def delete(id):
    shoes = get_shoes(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM shoes WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    if shoes is not None:
        flash('"{}" was successfully deleted!'.format(shoes['name']))
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
