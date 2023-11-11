import bms_coms
#-----------------------Fiqueu les variables en ingles, que hi havia un mix de catala i angles molt pocho

#Càlcul de mitjanes
# Inicialització de Mitjanes (mentres encara no hi ha el calcul)
VoltageMedian = 0
currentMedian = 0
temperatureMedian = 0
SoCMedian = 0
VoltageMedianCells = 0
temperatureMedianCells = 0

#Voltagealors mínims i màxims acceptables de la bateria
VoltageMin = 0
VoltageMax = 0
currentMin = 0
currentMax = 0
temperatureMin = 0
temperatureMax = 0
SoCMin = 0

#Voltagealors mínims i màxims acceptables de les cel·les de la bateria
VoltageMinCells = 0
VoltageMaxCells = 0
temperatureMinCells = 0
temperatureMaxCells = 0

#Checks Bateria
if VoltageMin >= VoltageMedian:
    VoltageMedianCheck = 0 #Voltage per sota mínims
elif VoltageMedian >= VoltageMax:
    VoltageMedianCheck = 1 #Voltage per sobre màxims
else:
    VoltageMedianCheck = 2 #Voltage dins de marges

if currentMin <= currentMedian <= currentMax:
    currentMedianCheck = True
else:
    currentMedianCheck = False

if temperatureMin >= temperatureMedian:
    temperatureMedianCheck = 0 #Temperatura per sota mínims
elif temperatureMedian >= temperatureMax:
    temperatureMedianCheck = 1 #Temperatura per sobre màxims
else:
    temperatureMedianCheck = 2 #Temperatura dins de marges

if SoCMin >= SoCMedian:
    SoCMedianCheck = False #SoC per sota del mínim
else:
    SoCMedianCheck = True #SoC dins dels marges

#Checks Cells Bateria

if VoltageMinCells >= VoltageMedianCells:
    VoltageMedianCellsCheck = 0 #Voltage de cel·les per sota mínims
elif VoltageMedianCells >= VoltageMaxCells:
    VoltageMedianCellsCheck = 1 #Voltage de cel·les per sobre màxims
else:
    VoltageMedianCellsCheck = 2 #Voltage de cel·les dins de marges

if temperatureMinCells >= temperatureMedianCells:
    temperatureMedianCellsCheck = 0 #Temperatura de cel·les per sota mínims
elif temperatureMedianCells >= temperatureMaxCells:
    temperatureMedianCellsCheck = 1 #Temperatura de cel·les per sobre màxims
else:
    temperatureMedianCellsCheck = 2 #Temperatura de cel·les dins dels marges


