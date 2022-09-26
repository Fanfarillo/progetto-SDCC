from flask import Flask, render_template, redirect, request
from FroRpcReg import *

app = Flask(__name__)

#very first page
@app.route("/")
def menu():
    return render_template("Menu.html")

#sign in page
@app.route("/accedi", methods=('GET','POST'))
def accesso():
    if request.method == 'POST':

        email = request.form['inputEmail']
        password = request.form['inputPassword']

        response = sendCredentials(email, password)

        #if credentials are correct then go ahead; else they have to be changed before going to the next page
        if response.isCorrect == True and response.storedType == "Turista":         #tourist case
            return redirect("/"+response.name+" "+response.surname+"/home")
        elif response.isCorrect == True and response.storedType != "Turista":    #airline case
            return redirect("/"+response.storedType+"/"+response.name+" "+response.surname+"/airlineHome")
        else:
            return render_template("Accesso.html")

    return render_template("Accesso.html")

#sign up page
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

        isOk = sendSignUpInfo(email, name, surname, password, passwordConfirm, userType, airline)

        #if password==passwordConfirm then go ahead; else passwordConfirm has to be changed before going to the next page
        if isOk and userType == "Turista":
            return redirect("/"+name+" "+surname+"/home")
        elif isOk and userType != "Turista":
            return redirect("/"+airline+"/"+name+" "+surname+"/airlineHome")
        else:
            return render_template("Iscrizione.html")

    return render_template("Iscrizione.html")

#here the user specifies some information about the flight he wants to book
@app.route("/<string:fullName>/home", methods=('GET','POST'))
def home(fullName):
    return render_template("Home.html", fullName=fullName)

#here the airline specifies which information has to be managed
@app.route("/<string:airline>/<string:fullName>/airlineHome", methods=('GET', 'POST'))
def airlineHome(airline, fullName):
    return render_template("AirlineHome.html", airline=airline, fullName=fullName)

if __name__ == "__main__":
    app.run()
