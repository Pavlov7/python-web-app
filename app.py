from forms import LoginForm
from flask import Flask
from flask import render_template
from config import Config

app = Flask("app")
app.config.from_object(Config)

@app.route("/")
def home():
  title = "home"
  songs = [
    {
      'name': 'himna',
      'duration': 3
    },
    {
      'name': 'vetrove',
      'duration': 5
    }
  ]
  customer = { 'username': 'Ivan' }
  return render_template('index.html', user=customer, title=title, songs=songs)

@app.route("/users")
def users():
  users = ['Ivan', 'Mark', 'sndnbnja']
  return render_template('users.html', users=users, title='users')

@app.route("/about")
def about():
  return render_template('about.html', about='about text', title='about')

@app.route("/login")
def login():
  form = LoginForm()
  return render_template('login.html', form=form)

app.run()
