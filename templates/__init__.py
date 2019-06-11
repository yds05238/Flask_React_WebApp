from flask import Flask
app = Flask(__name__,
 	static_folder = './public',
 	template_folder="./static")

from templates.messenger.views import messenger_blueprint
# register the blueprints
app.register_blueprint(messenger_blueprint)

