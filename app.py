from flask import Flask
from models.userModel import db
from config.config import Config
from controllers.authController import auth_bp
from controllers.profileController import profile_bp

def main_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_bp)
    app.register_blueprint(profile_bp)

    return app

if __name__ == '__main__':
    app = main_app()
    app.run(debug=True)