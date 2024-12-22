from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index_ex10.html")

@app.route("/post")
def ex10():
    return render_template("ex10.html")

@app.route("/post", methods=["POST"])
def postmetoda():
            return "You have sent a POST"

@app.route("/get", methods=["GET"])
def user():
        return "You have sent a GET"

if __name__ =="__main__":
    app.run(debug=True, port=5000)

