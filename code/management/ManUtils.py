from datetime import datetime, date

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

def roundPrice(initialPrice):

    if not initialPrice.isdigit():      #questo è il caso in cui abbiamo una virgola all'interno del prezzo
        for i in range(0,len(initialPrice)):

            if initialPrice[i] == '.' and i == len(initialPrice)-1:
                return initialPrice[0:i]
            elif initialPrice[i] == '.' and i <= len(initialPrice)-2 and i >= len(initialPrice)-3:
                return initialPrice
            elif initialPrice[i] == '.' and i <= len(initialPrice)-4:
                return initialPrice[0:i+3]

    else:                               #questo è il caso in cui il prezzo è intero
        return initialPrice
