import bms_coms

#Càlcul de mitjanes

#Valors mínims i màxims acceptables de la bateria
voltageMin =
voltageMax =
currentMin = 
currentMax = 
temperatureMin =
temperatureMax =
SoCMin = 

#Valors mínims i màxims acceptables de les cel·les de la bateria
voltageMinCeldas =
voltageMaxCeldas =
temperatureMinCeldas =
temperatureMaxCeldas =

#Checks Bateria
if voltageMin >= voltageMitjana:
    voltageMitjanaCheck = 0 #Voltatge per sota mínims
elif voltageMitjana >= voltageMax:
    voltageMitjanaCheck = 1 #Voltatge per sobre màxims
else:
    voltageMitjanaCheck = 2 #Voltatge dins de marges

if currentMin <= currentMitjana <= currentMax:
    currentMitjanaCheck = True
else:
    currentMitjanaCheck = False

if temperatureMin <= temperatureMitjana <= temperatureMax:
    temperatureMitjanaCheck = True
else:
    temperatureMitjanaCheck = False

#Checks Celdas Bateria