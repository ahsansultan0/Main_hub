import os

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)

import sqlalchemy as db
from dotenv import load_dotenv

from database.model import engine, posts
from routes.auth import auth


# Load .env BEFORE reading environment variables
load_dotenv()


app = Flask(__name__)

# Flask session secret
app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")


# Register authentication routes
app.register_blueprint(auth)


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

    connection = engine.connect()

    result = connection.execute(
        db.select(posts)
    ).fetchall()

    connection.close()

    return render_template(
        "community.html",
        posts=result
    )


# -------------------------
# Read one post
# -------------------------

@app.route("/read/<int:id>")
def read(id):
    if "user_id" not in session:
        return redirect(url_for('auth.login')) 


    connection = engine.connect()

    post = connection.execute(
        db.select(posts).where(posts.c.id == id)
    ).fetchone()

    connection.close()

    return render_template(
        "read_post.html",
        post=post
    )


# -------------------------
# Create post
# -------------------------

@app.route("/post", methods=["GET", "POST"])
def post():

    # Authentication check
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "GET":
        return render_template("create_post.html")

    title = request.form["title"]
    content = request.form["content"]

    connection = engine.connect()

    connection.execute(
        db.insert(posts).values(
            title=title,
            content=content,
            user_id=session['user_id']
        )
    )

    connection.commit()
    connection.close()

    return render_template(
        "create_post.html",
        message="Post created successfully!"
    )






# -------------------------
# Run application
# -------------------------

if __name__ == "__main__":
    app.run(
        port=8080,
        debug=True
    )