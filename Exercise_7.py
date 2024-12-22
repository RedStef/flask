from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user=request.form["nm"]
        return redirect(url_for("user", name=user))
    else:
        return render_template ("login.html")

@app.route("/<name>")
def user(name):
    return f"<h1>Hello {name}</h1>"

if __name__ =="__main__":
    app.run(debug=True, port=5000)

