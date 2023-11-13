import bms_coms

#Càlcul de mitjanes
VoltMean = 1
currMean = 1
tempMean = 1
SoCMean = 1
VoltMeanCells = 1
tempMeanCells = 1

#Valors mínims i màxims acceptables de la bateria
VoltMin = 1
VoltMax = 2
currMin = 1
currMax = 2
tempMin = 1
tempMax = 2
SoCMin = 1

#Valors mínims i màxims acceptables de les cel·les de la bateria
VoltMinCells = 1
VoltMaxCells = 2
tempMinCells = 1
tempMaxCells = 2

#Checks Bateria
if VoltMin >= VoltMean:
    VoltMeanCheck = 0 #Voltage per sota mínims
elif VoltMean >= VoltMax:
    VoltMeanCheck = 1 #Voltage per sobre màxims
else:
    VoltMeanCheck = 2 #Voltage dins de marges

if currMin >= currMean:
    currMeanCheck = 0 #Corrent per sota mínims
elif currMean >= currMax:
    currMeanCheck = 1 #Corrent per sobre màxims
else:
    currMeanCheck = 2 #Corrent dins de marges

if tempMin >= tempMean:
    tempMeanCheck = 0 #Temperatura per sota mínims
elif tempMean >= tempMax:
    tempMeanCheck = 1 #Temperatura per sobre màxims
else:
    tempMeanCheck = 2 #Temperatura dins de marges

if SoCMin >= SoCMean:
    SoCMeanCheck = False #SoC per sota del mínim
else:
    SoCMeanCheck = True #SoC dins dels marges

#Checks Cells Bateria
if VoltMinCells >= VoltMeanCells:
    VoltMeanCCheck = 0 #Voltage de cel·les per sota mínims
elif VoltMeanCells >= VoltMaxCells:
    VoltMeanCCheck = 1 #Voltage de cel·les per sobre màxims
else:
    VoltMeanCCheck = 2 #Voltage de cel·les dins de marges

if tempMinCells >= tempMeanCells:
    tempMeanCCheck = 0 #Temperatura de cel·les per sota mínims
elif tempMeanCells >= tempMaxCells:
    tempMeanCCheck = 1 #Temperatura de cel·les per sobre màxims
else:
    tempMeanCCheck = 2 #Temperatura de cel·les dins dels marges


