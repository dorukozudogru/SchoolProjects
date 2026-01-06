
from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

DATA_FILE = 'books.txt'

def read_books():
    books = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    books.append({'title': parts[0], 'author': parts[1], 'year': parts[2]})
    return books

def add_book(title, author, year):
    with open(DATA_FILE, 'a') as file:
        file.write(f"{title},{author},{year}\n")

@app.route('/')
def index():
    books = read_books()
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    author = request.form['author']
    year = request.form['year']

    if not title or not author or not year.isdigit() or len(year) != 4:
        flash("Invalid input. Please ensure all fields are filled correctly.")
    else:
        add_book(title, author, year)
        flash("Book added successfully!")
    return redirect(url_for('index'))

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query'].lower()
    books = [book for book in read_books() if query in book['title'].lower()]
    return render_template('index.html', books=books, query=query)

if __name__ == '__main__':
    app.run(debug=True)
