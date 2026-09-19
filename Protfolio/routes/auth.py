from flask import (
    render_template,
    request,
    Blueprint,
    session,
    redirect,
    url_for
)

from config.supabse import spabase


auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        try:
            print('trying to save')
            response = spabase.auth.sign_up({
                "email": email,
                "password": password,
                "username":username
                
            })
            print(123)
            

            session['user_id']=response.user.id
            return redirect(url_for("auth.dashboard"))

        except Exception as e:
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

            if response.user is None:
                return render_template(
                    "sign_in.html",
                    message="Invalid email or password."
                )

            # User successfully authenticated
            session["user_id"] = response.user.id
            session["user_email"] = response.user.email

            return redirect(url_for("auth.dashboard"))

        except Exception:
            return render_template(
                "sign_in.html",
                message="Invalid email or password."
            )

    return render_template("sign_in.html")


@auth.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))
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
