
from flask import (
    render_template,
    request,
    Blueprint,
    session,
    redirect,
    url_for
)
from database.model import engine, posts
import sqlalchemy as db
from config.supabse import spabase


auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        try:
            response = spabase.auth.sign_up({
                "email": email,
                "password": password,
                "options": {
                    "data": {
                        "username": username
                    }, "email_redirect_to": "https://8080-cs-13c5e34f-d659-4887-9d16-759d274b41ad.cs-asia-east1-vger.cloudshell.dev/dashboard"
                }
            })
            

            session["user_id"] = response.user.id

            

            session["username"] = response.user.user_metadata["username"]
            return render_template("massage.html",message='Go To Email to Confirm your mail')
            

        except Exception as e:
            print(e)
            return render_template(
                "register.html",
                message=e
            )

    return render_template("register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        try:
            response = spabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
            user = response.user





            if response.user is None:
                return render_template(
                    "sign_in.html",
                    message="Invalid email or password."
                )

            session["user_id"] = response.user.id
            session["username"] = response.user.user_metadata["username"]
            session["username"] = username
            session["user_email"] = response.user.email

            return redirect(url_for("auth.dashboard"))

        except Exception as e:
            print(e)
            return render_template(
                "sign_in.html",
                message=e
            )

    return render_template("sign_in.html")


@auth.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    connection = engine.connect()

    result = connection.execute(
        db.select(posts).where(
            posts.c.user_id == session["user_id"]
        )
    )

    return render_template("dashboard.html")


@auth.route("/logout")
def logout():

    session.clear()

    try:
        spabase.auth.sign_out()

    except Exception:
        pass

    return redirect(url_for("auth.login"))

