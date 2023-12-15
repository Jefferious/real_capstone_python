from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# @app.route("/")
# def homepage():
#     """View homepage."""

#     return render_template("homepage.html")

@app.route("/scores")
def normal_tic():
    normal = crud.get_normal()

    return render_template("normal.html", normal=normal)

@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(email, password, wins, losses, draws)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")



@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}!")

    return redirect("/")

@app.route('/scores')
def scores():
    # Assuming you have a user object stored in 'current_user'
    user_wins = get_user_wins(current_user.user_id)
    user_losses = get_user_losses(current_user.user_id)
    user_draws = get_user_draws(current_user.user_id)

    return render_template('scores.html', current_user=current_user, user_wins=user_wins, user_losses=user_losses, user_draws=user_draws)

@app.route("/homepage.html")
def homepage():
    homepage = crud.get_home()

    return render_template("hompeage.html", homepage=homepage)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)