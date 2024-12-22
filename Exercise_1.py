from flask import Flask

Exercise_1 = Flask(__name__)

@Exercise_1.route("/")

def hello():
    """Uvodni stranka pro cviceni z LMS"""
    return 'Hello user!'

@Exercise_1.route("/hello/Pepa")
def Pepa():
    return 'Pepa!'

if __name__ =="__main__":
    Exercise_1.run(debug=True)


