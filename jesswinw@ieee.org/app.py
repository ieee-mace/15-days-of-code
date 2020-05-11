from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [{
    'author': 'Bob Vance',
    'title': 'Refridgerators affecting my Life',
    'content': 'asdhaskdhaskjhd daskjdhkjash kdjsah kdjhaskjdh kash dkjash dkjash k',
    'date': 'April 23,2020'
}, {
    'author': 'John Doe',
    'title': 'Everyody uses my name!!',
    'content': 'asdhaskdhaskjhd daskjdhkjash kdjsah kdjhaskjdh kash dkjash dkjash k',
    'date': 'April 22,2020'
}]


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return "<h1>This is the about page</h1>"


if __name__ == "__main__":
    app.run(debug=True)
