# import flask
from flask import Flask, render_template
import os # imports the operating system module

app = Flask(__name__)

@app.route('/') # this decorate creates the home route
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('about.html', name=name, title='Home')

# creates a /about page
@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name=name, title='About Us')

@app.route('/post')
def post():
    name = 'Text Analyzer'
    return render_template('post.html', name=name, title=name)

if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host = '0.0.0.0', port=port) # to access website: go to 0.0.0.0:5000

