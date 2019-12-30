from flask import Flask, render_template,redirect,url_for,flash 
from app import app
from app.forms import LoginForm

@app.route('/home')
@app.route('/')
def home():
	user = {'username': 'Anas'}

	posts = [
		{
			'author' : {'username': 'jhon'},
			'body' : 'it is a beautiful movie'


		},


		{
			'author' : {'username': 'Bob'},
			'body' : 'Yes it is...!!!'


		},

	]
	return render_template('home.html', title='home', user= user, posts= posts)

@app.route('/product')
def product():
	return render_template('product.html')



@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'] )
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for the user {}'.format(form.username.data))


		return redirect(url_for('home'))
	return render_template('login.html', title='Sign In Here', form=form)
 