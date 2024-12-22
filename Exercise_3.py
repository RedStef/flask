from flask import Flask
import datetime


Exercise_3 = Flask(__name__)

@Exercise_3.route("/time")
def cas():
    aktualni_cas=datetime.datetime.now()
    return f"dnes je rok {aktualni_cas.year} a mesic {aktualni_cas.month}."

if __name__ =="__main__":
    Exercise_3.run(debug=True)

