from flask import Flask, render_template, redirect, request
from FroRpcReg import *
#from FroRpcMan import *
#from FroUtils import *

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
        if response.isCorrect == True and response.storedType == "Turista":      #tourist case
            return redirect("/"+response.name+" "+response.surname+"/home")
        elif response.isCorrect == True and response.storedType != "Turista":    #airline case
            return redirect("/"+response.storedType+"/"+response.name+" "+response.surname+"/airlineHome")
        else:
            return render_template("Accesso.html")

    return render_template("Accesso.html")
    
@app.route("/booking", methods=('GET','POST'))
def booking():
	giorno = request.form['giorno']
	print(giorno)
	mese = request.form['mese']
	print(mese)
	anno = request.form['anno']
	print(anno)
	partenza = request.form['aereoporto_partenza']
	print(partenza)
	arrivo = request.form['aereoporto_arrivo']
	print(arrivo)
	persone = request.form['persone']
	print(persone)
	return render_template("Booking.html", items = [1,2,3])

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

#here the airline adds a new flight
@app.route("/<string:airline>/<string:fullName>/airlineHome/addFlight", methods=('GET', 'POST'))
def addFlight(airline, fullName):
    if request.method == 'POST':

        flightId = request.form['inputId']
        departureAirport = request.form['inputDepartureAirport']
        arrivalAirport = request.form['inputArrivalAirport']
        price = request.form['inputPrice']

        #this function returns a string like "DD-MM-YYYY"
        date = getDate(request.form['dayDropdown'], request.form['monthDropdown'], request.form['yearDropdown'])

        #this function returns a string like "HH:MMAM" or "HH:MMPM"
        fullDepartureHour = getFullHour(request.form['departureHour'], request.form['departureMinute'])
        fullArrivalHour = getFullHour(request.form['arrivalHour'], request.form['arrivalMinute'])

        #TODO: chiamata gRPC e tutte cose
        #TODO: return

    return render_template("AddFlight.html", airline=airline, fullName=fullName)

#here the airline modifies the price of an existing flight
@app.route("/<string:airline>/<string:fullName>/airlineHome/modifyFlight", methods=('GET', 'POST'))
def modifyFlight(airline, fullName):
    return render_template("ModifyFlight.html", airline=airline, fullName=fullName)

#here the airline modifies the price for seat selection
@app.route("/<string:airline>/<string:fullName>/airlineHome/modifySeatsPrices", methods=('GET', 'POST'))
def modifySeatsPrices(airline, fullName):
    return render_template("ModifySeatsPrices.html", airline=airline, fullName=fullName)

#here the airline modifies the price of extra-services
@app.route("/<string:airline>/<string:fullName>/airlineHome/modifyServicesPrices", methods=('GET', 'POST'))
def modifyServicesPrices(airline, fullName):
    return render_template("ModifyServicesPrices.html", airline=airline, fullName=fullName)

if __name__ == "__main__":
    app.run()
