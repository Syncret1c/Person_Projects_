from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

@views.route("/")
@login_required
def home():
    return render_template("home.html", user = current_user)

@views.route("/new_post", methods=["GET", "POST"])
@login_required
def new_post():
    return render_template("new_post.html", user = current_user)