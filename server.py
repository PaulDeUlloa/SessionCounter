from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "keep counter secret, keep it safe!"


# Have the root route render a template that displays the number of times the client
@app.route("/")
def index():
    if "counter" not in session:
        session["counter"] = 1
    else:
        session["counter"] += 1
    return render_template("index.html")


# Add a "/destroy_session" route that clears the session and redirects to the root route.
@app.route("/destroy_session")
def destroy_session():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8008)
