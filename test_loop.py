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

if temperatureMin >= temperatureMitjana:
    temperatureMitjanaCheck = 0 #Temperatura per sota mínims
elif temperatureMitjana >= temperatureMax:
    temperatureMitjanaCheck = 1 #Temperatura per sobre màxims
else:
    temperatureMitjanaCheck = 2 #Temperatura dins de marges

if SoCMin >= SoCMitjana:
    SoCMitjanaCheck = False #SoC per sota del mínim
else:
    SoCMitjanaCheck = True #SoC dins dels marges

#Checks Celdas Bateria

if voltageMinCeldas >= voltageMitjanaCeldas:
    voltageMitjanaCeldasCheck = 0 #Voltatge de cel·les per sota mínims
elif voltageMitjanaCeldas >= voltageMaxCeldas:
    voltageMitjanaCeldasCheck = 1 #Voltatge de cel·les per sobre màxims
else:
    voltageMitjanaCeldasCheck = 2 #Voltatge de cel·les dins de marges

if temperatureMinCeldas >= temperatureMitjanaCeldas:
    temperatureMitjanaCeldasCheck = 0 #Temperatura de cel·les per sota mínims
elif temperatureMitjanaCeldas >= temperatureMaxCeldas:
    temperatureMitjanaCeldasCheck = 1 #Temperatura de cel·les per sobre màxims
else:
    temperatureMitjanaCeldasCheck = 2 #Temperatura de cel·les dins dels marges


