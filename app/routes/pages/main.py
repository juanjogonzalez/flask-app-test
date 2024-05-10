# Flask modules
from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__, url_prefix="/")

@main_bp.route("/")
def home_route():
    return render_template("pages/home.html")