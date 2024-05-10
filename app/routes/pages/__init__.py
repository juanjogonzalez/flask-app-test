# Flask modules
from flask import Blueprint

# Import Blueprint modules
from .main import main_bp

pages_bp = Blueprint("pages", __name__, url_prefix="/")

pages_bp.register_blueprint(main_bp)