from flask import Flask
import datetime


Exercise_2 = Flask(__name__)

@Exercise_2.route("/time")
def cas():
    aktualni_cas=datetime.datetime.now()
    return f"now is {aktualni_cas.hour}:{aktualni_cas.minute}"

if __name__ =="__main__":
    Exercise_2.run(debug=True)

