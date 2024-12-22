from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
            return render_template ("index_GG.html")

@app.route("/")
def Number_guessing_game():
    return render_template("Home_page_GG.html")

@app.route("/", methods=["GET", "POST"])
def guess_the_number():
    if request.method == "GET":
        return  render_template("Home_page_GG.html").format(0,1000)
    else:
        min_number = int(request.form.get("min"))
        max_number = int(request.form.get("max"))
        user_anser = int(request.form.get("user_anser"))
        gues = int(request.form.get("guess",500))

        if user_anser == "too big":
            max_number = guess
        elif user_answer == "too small":
            min_number = guess_the_number
        elif user_anser == "you win":
            return render_template("Hooray_GG.html").format(min_number,max_number)

        guess = (max_number - min_number) // 2 + min_number

        return render_template("Home_page_GG.html", guess=guess, min=min_number, max=max_number)

if __name__ =="__main__":
    app.run(debug=True, port=5000)

