from flask import session, Blueprint, request, redirect, url_for, render_template
import sqlalchemy as db
from sqlalchemy import text

from database.model import engine, posts

crud = Blueprint("crud", __name__)


def get_posts():
    print(session)

    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT * FROM posts")
        )
        posts_data = result.fetchall()

    return posts_data


@crud.route("/post", methods=["GET", "POST"])
def post():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "GET":
        return render_template("create_post.html")

    title = request.form["title"]
    content = request.form["content"]

    with engine.begin() as connection:
        connection.execute(
            db.insert(posts).values(
                title=title,
                content=content,
                user_id=session["user_id"]
            )
        )

    return render_template(
        "create_post.html",
        message="Post created successfully!"
    )


@crud.route("/read/<int:id>")
def read(id):

    with engine.connect() as connection:
        post = connection.execute(
            db.select(posts).where(posts.c.id == id)
        ).fetchone()

    if post is None:
        return "Post not found", 404

    allowed = (
        "user_id" in session
        and session["user_id"] == post.user_id
    )

    return render_template(
        "read_post.html",
        post=post,
        allowed=allowed
    )


@crud.route("/delete/<int:post_id>", methods=["POST"])
def delete_post(post_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    with engine.begin() as connection:
        connection.execute(
            db.delete(posts).where(
                posts.c.id == post_id,
                posts.c.user_id == session["user_id"]
            )
        )

    return redirect(url_for("community"))