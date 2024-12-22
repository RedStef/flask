
from flask import Flask, request

Exercise_5 = Flask(__name__)

@Exercise_5.route("/draw/<prvni>/<druhe>/<treti>", methods=["GET"])
def tri_cisla(prvni, druhe, treti):
    return f"{int(prvni), int(druhe), int(treti)}"

# GET PARAMETRY

if __name__ =="__main__":
    Exercise_5.run(debug=True, port=5000)



"""
from flask import Flask, request

Exercise_4 = Flask(__name__)

@Exercise_4.route("/draw", methods=["GET"])
def TWO_DIGITS():
    return "2 2 2"

# GET PARAMETRY

if __name__ =="__main__":
    Exercise_4.run(debug=True, port=5000)
"""