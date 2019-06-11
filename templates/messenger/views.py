from flask import render_template, Blueprint

messenger_blueprint = Blueprint('messenger',__name__)

@messenger_blueprint.route('/')
@messenger_blueprint.route('/messenger')
def index():
	return render_template("index.html")
