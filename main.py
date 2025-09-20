from flask import Flask, render_template, url_for, redirect
import os

# app = Flask("Website") 
app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/") 
def home(): 
    return render_template("tutorial.html") 

@app.route("/about/") 
def about(): 
    return render_template("about.html") 

# @app.route("/")
# def index():
#     return redirect(url_for("home"))

# @app.route("/home")
# def home():
#     return render_template("tutorial.html")

# @app.route("/about/")
# def about():
#     return render_template("about.html")

# if __name__ == "__main__":
#     print("CWD:", os.getcwd())
#     print("static exists:", os.path.exists("static"))
#     print("static files:", os.listdir("static") if os.path.exists("static") else "no dir")
#     print("tutorial.html:", os.path.exists("templates/tutorial.html"))
#     app.run(debug=True)

# print("CWD:", os.getcwd())
# print("templates/tutorial.html:", os.path.exists("templates/tutorial.html"))
# print("static/cat.png:", os.path.exists("static/cat.png"))
app.run(debug=True) 
