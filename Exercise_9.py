from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
            return render_template ("index_ex9.html")

@app.route("/guessing_game")
def ex9():
    return render_template("ex9.html")

@app.route("/guess", methods=["post"])
def guessing():
    vlozene_cislo = int(request.form["cislo"])
    guessed_number = int(10)
    if vlozene_cislo < guessed_number:
        return render_template("ex9_too_small_number.html")
    elif vlozene_cislo > guessed_number:
        return render_template("ex9_too_big_number.html")
    elif vlozene_cislo == guessed_number:
        return "Congratulations!"
    else:
        return "There is an error"

if __name__ =="__main__":
    app.run(debug=True, port=5000)

