from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)



@app.route("/<prirozene>", methods=["GET"])
def user(name,surname):
    natural_number=request.args.get("n")
    return f"<h1>Vlozeno cislo {prirozene}</h1>"

@app.route("/", methods=["POST"])
def login():
        user_name=request.form["nm"]
        return

if __name__ =="__main__":
    app.run(debug=True, port=5000)

