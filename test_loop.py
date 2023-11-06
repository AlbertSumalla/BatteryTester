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
if voltageMin <= voltageMitjana <= voltageMax:
    voltageMitjanaCheck = True
else:
    voltageMitjanaCheck = False

if currentMin <= currentMitjana <= currentMax:
    currentMitjanaCheck = True
else:
    currentMitjanaCheck = False

if temperatureMin <= temperatureMitjana <= temperatureMax:
    temperatureMitjanaCheck = True
else:
    temperatureMitjanaCheck = False

#Checks Celdas Bateria