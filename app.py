from flask import Flask, request, url_for, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("base.html", title="MORFÍs")

@app.errorhandler(404)
def page_not_found(e):
    return "Page not found."

if __name__=="__main__":
    app.run(debug=True,use_reloader=True)
