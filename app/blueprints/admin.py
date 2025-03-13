from flask import Blueprint, render_template

admin = Blueprint("admin", __name__, url_prefix="/admin")


@admin.route("/dashboard")
def dashboard():
    return render_template("/dashboard/index.html")
