from flask import Flask, render_template, url_for, redirect
import os
import pandas as pd

# app = Flask("Website") 
# app = Flask(__name__, static_folder="static")
app = Flask(__name__) 

stations = pd.read_csv("data_small/stations.txt", skiprows=17) 
stations = stations[["STAID","STANAME                                 "]]

@app.route("/") 
def home(): 
    return render_template("home.html", data=stations.to_html()) 

@app.route("/api/v1/<station>/<date>") 
def about(station, date): 
    filename = "data_small\TG_STAID" +str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename,skiprows=20,parse_dates=["    DATE"]) 
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze()/10
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }

if __name__ == "__main__": 
    app.run(debug=True, port=5000) 


# @app.route("/api/v1/<word>") 
# def api(word): 
#     definition = word.upper() 
#     result_dictionary = {'word': word, 
#                          'definition': definition} 
#     return result_dictionary

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
