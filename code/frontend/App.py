from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/", methods=('GET','POST'))
def menu():
    return render_template("Menu.html")

@app.route("/accedi", methods=('GET','POST'))
def accesso():
    if request.method == 'POST':
        email = request.form['inputEmail']
        return redirect("/"+email+"/home")

    return render_template("Accesso.html")

@app.route("/iscriviti", methods=('GET','POST'))
def iscrizione():
    if request.method == 'POST':

        email = request.form['inputEmail']
        name = request.form['inputName']
        surname = request.form['inputSurname']
        password = request.form['inputPassword']
        passwordConfirm = request.form['inputPasswordConfirm']
        userType = request.form['flexRadioDefault']
        airline = request.form['airlineDropdown']

        return redirect("/"+name+" "+surname+"/home")

    return render_template("Iscrizione.html")

@app.route("/<string:email>/home", methods=('GET','POST'))
def home(email):
    return render_template("Home.html", email=email)

if __name__ == "__main__":
    app.run()
