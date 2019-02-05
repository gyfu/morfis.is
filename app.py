from flask import Flask, request, url_for, render_template
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("base.html", title="MORFÍs")
@app.route('/about')
def about():
    return render_template("about.html", title="Um MORFÍs")
@app.route('/stjorn')
def stjorn():
    return render_template("stjorn.html", title="Stjórn MORFÍs")
@app.route('/log')
def log():
    return render_template("log.html", title="Lög MORFÍs")
@app.route('/domar')
def domar():
    with open("data/domarar.csv","r") as f:
        lines=csv.reader(f)
        listinn=[]
        for line in lines:
            listinn.append(line)
    return render_template("domar.html", title="Dómarar", listi=listinn)
@app.errorhandler(404)
def page_not_found(e):
    return "Page not found."

if __name__=="__main__":
    app.run(debug=True,use_reloader=True)
