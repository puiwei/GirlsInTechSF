from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Please create an endpoint with your name as the URL"


@app.route('/names/ed')
def ed():
    return "I'm Ed"

@app.route('/names/yasmine')
def yasmine():
	return "I'm not ed. I'm Yasmine. :)" 

