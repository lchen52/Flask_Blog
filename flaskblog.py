from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Le Chen',
        'title': 'Blog Post 1',
        'content': 'First Content',
        'date_posted': '2019-10-09'
    },
    {
        'author': 'Le Chen',
        'title': 'Blog Post 2',
        'content': 'Second Content',
        'date_posted': '2019-10-09'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'about')

if __name__ == '__main__':
    app.run(debug = True)

