#questa funzione restituisce una stringa in formato POSTO1-POSTO2-...-POSTOn
def listToString(strList):
    finalString = ""

    for item in strList:
        finalString = finalString + item + "-"
    
    finalString = finalString[:-1]      #rimozione dell'ultimo carattere della stringa che, di fatto, è un trattino lasciato "a penzoloni"
    return finalString
    