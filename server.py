from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/ninja')
def ninjas():
	return render_template("ninja.html")

@app.route('/ninja/<color>')
def turtle(color):
	return render_template('turtle.html', color=color)

app.run(debug=True)