from flask import Flask, request
import random

Exercise_6 = Flask(__name__)

@Exercise_6.route("/lotto", methods=["GET"])
def LOTTO():
    list=[i for i in range(0,50)]
    vyherni_cisla = random.sample(list, 6)
    return vyherni_cisla

# GET PARAMETRY

if __name__ =="__main__":
    Exercise_6.run(debug=True, port=5000)

