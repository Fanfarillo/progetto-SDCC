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
