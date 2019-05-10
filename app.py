from flask import Flask, request, url_for, render_template, g , session , redirect
import urllib, json, os, sqlite3
app = Flask(__name__)
app.secret_key=os.urandom(24)
DOMARAR="domarar.db"
ADGANGAR="adgangar.db"
def get_db(DATABASE):
    db=getattr(g,"_database",None)
    if db is None:
        db=g._database=sqlite3.connect(DATABASE)
    return db
@app.teardown_appcontext
def close_connection(exception):
    db=getattr(g,"_database",None)
    if db is not None:
        db.close()
@app.route('/login',methods=["GET","POST"])
def login():
    c=get_db(ADGANGAR).cursor()
    if request.method=="POST":
        test=request.form["user"]
        c.execute('''SELECT pass FROM users WHERE user=?''',(test,))
        password=c.fetchone()
        c.execute('''SELECT user FROM users WHERE user=?''',(test,))
        user=c.fetchone()
        session.pop("user",None)
        if request.form["password"]==password[0]:
            session['user']=user[0]
            return redirect(url_for("domar_edit"))
    return render_template("login.html",title="Login")
@app.route('/logout')
def logout():
    session.pop("user",None)
    return redirect(request.referrer)
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
    c=get_db(DOMARAR).cursor()
    data=[]
    for row in c.execute("SELECT DISTINCT * FROM domarar"):
        data.append(row)
    return render_template("domar.html",title='Dómarar',listi=data)
@app.route('/domar_edit',methods=["GET","POST"])
def domar_edit():
    c=get_db(DOMARAR).cursor()
    data=[]
    for row in c.execute("SELECT * FROM domarar"):
        data.append(row)
    if g.user:
        return render_template("domar_edit.html",title="Dómarar",listi=data)
        if request.method=="POST":
            nafn=request.form["nafn"]
            model=request.form["model"]
            skoli=request.form["skoli"]
            simi=request.form["simi"]   
            c.execute('''INSERT or ingore INTO domarar(
                nafn,
                model,
                skoli,
                simi
                )
                VALUES
                ?,
                ?,
                ?,
                ?
                );
                ''',(nafn,model,skoli,simi))
            get_db(DOMARAR).commit()
            redirect(url_for("domar_edit"))
    return render_template("domar.html",title="Dómarar",listi=data)
@app.before_request
def before_request():
    g.user=None
    if "user" in session:
        g.user=session["user"]
@app.errorhandler(404)
def page_not_found(e):
    return "Page not found."
if __name__=="__main__":
    #app.run(debug=True,use_reloader=True)
    app.run()
