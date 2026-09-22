import os

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)

from dotenv import load_dotenv

from routes.auth import auth
from routes.crud import crud, get_posts


# Load .env before reading environment variables
load_dotenv()


app = Flask(__name__)

# Flask session secret
app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")


# Register blueprints
app.register_blueprint(auth)
app.register_blueprint(crud)


# -------------------------
# Public pages
# -------------------------

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects")
def projects():
    return render_template("project.html")


# -------------------------
# Community
# -------------------------

@app.route("/community")
def community():

    posts = get_posts()

    return render_template(
        "community.html",
        posts=posts
    )


# -------------------------
# Run application
# -------------------------

if __name__ == "__main__":
    app.run(
        port=8080,
        debug=True
    )