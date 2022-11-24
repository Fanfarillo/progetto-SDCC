from datetime import datetime, date, timedelta

class ServiziSelezionati:
    def __init__(self, bagaglioSpeciale, bagaglioStivaMedio, bagaglioStivaGrande, assicurazioneBagagli, animaleDomestico, neonato):
        self.bagaglioSpeciale = bagaglioSpeciale            #num bagagli speciali selezionati
        self.bagaglioStivaMedio = bagaglioStivaMedio        #num bagagli in stiva medi selezionati
        self.bagaglioStivaGrande = bagaglioStivaGrande      #num bagagli in stiva grandi selezionati
        self.assicurazioneBagagli = assicurazioneBagagli    #num assicurazione bagagli selezionati
        self.animaleDomestico = animaleDomestico            #num animali domestici selezionati
        self.neonato = neonato                              #num neonati selezionati


def getAmpm(initialHour):  
    intHour = int(initialHour)

    if intHour < 12:
        ampm = 'AM'
    else:
        ampm = 'PM'

    return ampm

#initialHour is a string like '0', '1', '2',..., '23', while hour is a string like '01', '02',..., '12'
#clearly, with AM / PM notation (used to store times in db), the value of the hour belongs to {1, 2,..., 12}
def getHour(initialHour):
    intHour = int(initialHour)

    if intHour == 0:
        hour = '12'
    elif intHour > 0 and intHour < 10:
        hour = '0'+initialHour
    elif intHour > 9 and intHour < 13:
        hour = initialHour
    elif intHour > 12 and intHour < 22:
        hour = '0'+str(intHour-12)
    else:
        hour = str(intHour-12)

    return hour

#initialString is a string like '0', '1', '2',..., '59', while twoDigitsString is a string like '00', '01', '02',..., '59'
def getTwoDigitsString(initialString):
    intValue = int(initialString)

    if intValue < 10:
        twoDigitsString = '0'+initialString
    else:
        twoDigitsString = initialString

    return twoDigitsString

def getFullHour(initialHour, initialMinute):
    ampm = getAmpm(initialHour)
    hour = getHour(initialHour)
    minute = getTwoDigitsString(initialMinute)
    
    return hour + ":" + minute + ampm

def getDate(initialDay, initialMonth, year):
    day = getTwoDigitsString(initialDay)
    month = getTwoDigitsString(initialMonth)
    
    return day + "-" + month + "-" + year

def getCurrentDateStr():
    today = date.today()
    return today.strftime("%d-%m-%Y")

def getFileSelezionate(postiSelezionati):
    fileSelezionate = [0]*5        #array che indicherà il numero di posti selezionati per ogni gruppo di posti; in prima battuta viene inizializzato a 0

    for posto in postiSelezionati:
        #bisogna anzitutto capire a quale fila appartiene ciascun posto in postiSelezionati; la lettera è una don't care
        if len(posto) == 2 and posto[1] == '1':     #caso fila 1
            fileSelezionate[0]+=1
        elif len(posto) == 2 and int(posto[1]) >= 2 and int(posto[1]) <= 5:     #caso file 2-5
            fileSelezionate[1]+=1
        elif (len(posto) == 2 and int(posto[1]) >= 6) or (len(posto) == 3 and posto[1] == '1' and int(posto[2]) <= 5):      #caso file 6-15
            fileSelezionate[2]+=1
        elif len(posto) == 3 and posto[1] == '1' and int(posto[2]) >= 6 and int(posto[2]) <= 7:     #caso file 16-17
            fileSelezionate[3]+=1
        else:       #caso file 18-26
            fileSelezionate[4]+=1
        
    return fileSelezionate

#this function checks if provided date exists
#not existing dates are 30/02, 31/02, 31/04, 31/06, 31/09, 31/11 and, for not leap years, 29/09
#NOTE: years that are multiple of 100 and are not multiple of 400 are NOT leap years
def checkDateExistance(dateStr):
    yearStr = dateStr[-4:]
    monthStr = dateStr[3:5]
    dayStr = dateStr[0:2]

    yearInt = int(yearStr)

    if (dayStr=='31' and (monthStr=='02' or monthStr=='04' or monthStr=='06' or monthStr=='09' or monthStr=='11')) or (dayStr=='30' and monthStr=='02'):
        return False
    elif dayStr=='29' and monthStr=='02' and (yearInt%4!=0 or (yearInt%100==0 and yearInt%400!=0)):
        return False
    else:
        return True

#this function checks if provided date is future (i.e. is greater than today)
def checkFutureDate(dateStr):
    dateObj = datetime.strptime(dateStr, '%d-%m-%Y').date()
    today = date.today()
    if dateObj > today:
        return True
    else:
        return False

#this function converts the number of days before a specific flight in the associated date (represented by a string)
def getConvenientDate(flightDate, numDaysBefore):
    flightDateObj = datetime.strptime(flightDate, '%d-%m-%Y')       #datetime object
    convenientDateObj = flightDateObj - timedelta(days=numDaysBefore)  #datetime object associated to the date in which is convenient to buy the tickets
    convenientDateStr = convenientDateObj.strftime('%d-%m-%Y')
    return convenientDateStr
