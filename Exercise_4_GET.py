from flask import Flask, request

Exercise_4 = Flask(__name__)

@Exercise_4.route("/count/<number1>/<number2>", methods=["GET"])
def cislo_1(number1, number2):
    return f"{int(number1)+int(number2)}"

# GET PARAMETRY

if __name__ =="__main__":
    Exercise_4.run(debug=True, port=5000)

