from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello this is main page <h1>Hell</h1>"

@app.route("/<jmeno>")
def user("name"): #cokoliv dam tady do spicatych tak se propise do funkce
    return f"Ahoj {jmeno}"

if __name__=="__main__":
    app.run()

