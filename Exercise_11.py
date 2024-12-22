from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["POST"])
def login():
        return

@app.route("/<prirozene>", methods=["GET"])
def user(name,surname):
    return f"<h1>Vlozeno cislo {prirozene}</h1>"

if __name__ =="__main__":
    app.run(debug=True, port=5000)

