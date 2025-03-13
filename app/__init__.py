from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.blueprints.admin import admin

    app.register_blueprint(admin)

    from app.blueprints.main import main

    app.register_blueprint(main)

    return app
