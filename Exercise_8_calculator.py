from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
            return render_template ("index_calculator.html")

@app.route("/calculator")
def calculator_ex8():
    return render_template("calculator_ex8.html")

@app.route("/calculate", methods=["post"])
def calculate():
    prvni_cislo = int(request.form["prvni_cislo"])
    operator = request.form["operator"]
    druhe_cislo = int(request.form["druhe_cislo"])
    if operator == "plus":
        vysledek = prvni_cislo + druhe_cislo
        return str(vysledek)
    elif operator =="minus":
        vysledek = prvni_cislo - druhe_cislo
        return str(vysledek)
    elif operator == "multiply":
        vysledek = prvni_cislo * druhe_cislo
        return str(vysledek)
    elif operator == "divide":
        vysledek = prvni_cislo / druhe_cislo
        return str(vysledek)
    else:
        return "There is an error"

if __name__ =="__main__":
    app.run(debug=True, port=5000)

