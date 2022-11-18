class UpdateInfo:
    def __init__(self, updateExpression, expressionAttributeValues):
        self.updateExpression = updateExpression                        #string
        self.expressionAttributeValues = expressionAttributeValues      #dictionary


#initialString is a string like '0', '1', '2',..., '59', while twoDigitsString is a string like '00', '01', '02',..., '59'
def getTwoDigitsString(initialString):
    intValue = int(initialString)

    if intValue < 10:
        twoDigitsString = '0'+initialString
    else:
        twoDigitsString = initialString

    return twoDigitsString


#returns the first line of msg
def getIdFromMsg(msg):
    lines = msg.split("\n")
    return lines[0]


#returns the second line of msg
def getUsernameFromMsg(msg):
    lines = msg.split("\n")
    return lines[1]


#returns a list of selected seats from msg
def getSeatsFromMsg(msg):
    lines = msg.split("\n")
    seats = lines[2].split("-")
    return seats


#restituisce un oggetto di tipo UpdateInfo utile quando si deve aggiornare un elemento della tabella PostiOccupati
def getUpdateInfo(username, selectedSeats):
    expressionAttributeValues = {':u': username, }      #di fatto il dizionario è già pronto
    updateExpression = "set "

    for seat in selectedSeats:
        updateExpression = updateExpression + seat + "=:u, "

    #alla fine del ciclo bisogna eliminare l'ultima virgola e l'ultimo spazio
    updateExpression = updateExpression[:-2]

    #generazione dell'oggetto UpdateInfo da restituire al chiamante storeSelectedSeats()
    return UpdateInfo(updateExpression, expressionAttributeValues)
