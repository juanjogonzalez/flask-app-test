from flask import Flask

def create_app():

    # Create the Flask application instance
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
        static_url_path="/",
    )

    # Set current_app context
    with app.app_context():

        # Register blueprints or routes
        from app.routes import main_bp

        app.register_blueprint(main_bp)

    return app