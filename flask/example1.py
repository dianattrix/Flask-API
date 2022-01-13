from flask import Flask

app = Flask(__name__)

@app.route("/bye")
def bye():
    return "<h1>Bye!</h1>"

@app.route("/")
def principal():
    return "<h1>Hi there!</h1>"

@app.route("/greeting/<name>")
def greeting(name):
    return "<h1>Hi, {} !</h1>".format(name)

if __name__ == "__main__":
    #app.run()
    app.run(debug=True)
