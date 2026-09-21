from flask import session,Blueprint,request,redirect,url_for,render_template
import sqlalchemy as db
from database.model import engine,posts

crud=Blueprint('crud',__name__)

def get_posts():
    print(session)
    connection = engine.connect()

    result = connection.execute(
        db.select(posts)
    ).fetchall()

    connection.close()

    return result
        



@crud.route("/post", methods=["GET", "POST"])
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
            user_id=session['user_id'],
           
        ))

    connection.commit()
    connection.close()

    return render_template(
        "create_post.html",
        message="Post created successfully!"
    )

    # -------------------------
# Read one post
# -------------------------

@crud.route("/read/<int:id>")
def read(id):
    


    connection = engine.connect()

    post = connection.execute(
        db.select(posts).where(posts.c.id == id)
    ).fetchone()

    connection.close()
    if session['user_id']==post.user_id:
        print('hello')
        allowed=True
        return render_template(
        "read_post.html",
        post=post,allowed=allowed
        ) 

    return render_template(
        "read_post.html",
        post=post
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
    