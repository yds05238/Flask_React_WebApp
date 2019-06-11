from flask import render_template, Blueprint
'''
hello_blueprint = Blueprint('hello',__name__)

@hello_blueprint.route('/')
@hello_blueprint.route('/hello')
def index():
	return render_template("index.html")
'''
messenger_blueprint = Blueprint('messenger',__name__)

@messenger_blueprint.route('/')
@messenger_blueprint.route('/messenger')
def index():
	return render_template("index.html")