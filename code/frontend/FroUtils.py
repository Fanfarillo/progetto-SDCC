def getAmpm(initialHour):  
    intHour = int(initialHour)

    if intHour < 12:
        ampm = 'AM'
    else:
        ampm = 'PM'

    return ampm

def getHour(initialHour):
    intHour = int(initialHour)

    if intHour == 0:
        hour = '12'
    else if intHour > 0 and intHour < 10:
        hour = '0'+initialHour
    else if intHour > 9 and intHour < 13:
        hour = initialHour
    else if intHour > 12 and intHour < 22:
        hour = '0'+str(intHour-12)
    else:
        hour = str(intHour-12)

    return hour

def getMinute(initialMinute):
    intMinute = int(initialMinute)

    if intMinute < 10:
        minute = '0'+initialMinute
    else:
        minute = initialMinute

    return minute

def getFullHour(initialHour, initialMinute):
    ampm = getAmpm(initialHour)
    hour = getHour(initialHour)
    minute = getMinute(initialMinute)à
    
    return hour + ":" + minute + ampm
