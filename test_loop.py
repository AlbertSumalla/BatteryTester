import bms_coms
import pandas as pd
import constants

#Càlcul de mitjanes
VoltMean = 1 #s.mean
currMean = 1
tempMean = 1
SoCMean = 1
SoHMean = 1
VoltMeanCells = 1
tempMeanCells = 1

#--------------------.py apart de les constants----------------------


#-------------------------------------------------------------------
#Checks Bateria
if VoltMin >= VoltMean:
    VoltMeanCheck = 2 #Voltage per sota mínims
elif VoltMean >= VoltMax:
    VoltMeanCheck = 1 #Voltage per sobre màxims
else:
    VoltMeanCheck = 0 #Voltage dins de marges

if (currExpect - RangecurrMin < currMean < currExpect + RangecurrMax):
    currMeanCheck = 0 #Corrent dins de marges
else:
    currMeanCheck = 1 #Corrent fora de l'esperat

if tempMin >= tempMean:
    tempMeanCheck = 2 #Temperatura per sota mínims
elif tempMean >= tempMax:
    tempMeanCheck = 1 #Temperatura per sobre màxims
else:
    tempMeanCheck = 0 #Temperatura dins de marges

if SoCMin >= SoCMean:
    SoCMeanCheck = 1 #SoC per sota del mínim
else:
    SoCMeanCheck = 0 #SoC dins dels marges

if SoHMin >= SoHMean:
    SoHMeanCheck = 1 #SoH per sota del mínim
else:
    SoHMeanCheck = 0 #SoH dins dels marges


#Checks Cells Bateria
if VoltMinCells >= VoltMeanCells:
    VoltMeanCCheck = 2 #Voltage de cel·les per sota mínims
elif VoltMeanCells >= VoltMaxCells:
    VoltMeanCCheck = 1 #Voltage de cel·les per sobre màxims
else:
    VoltMeanCCheck = 0 #Voltage de cel·les dins de marges

if tempMinCells >= tempMeanCells:
    tempMeanCCheck = 2 #Temperatura de cel·les per sota mínims
elif tempMeanCells >= tempMaxCells:
    tempMeanCCheck = 1 #Temperatura de cel·les per sobre màxims
else:
    tempMeanCCheck = 0 #Temperatura de cel·les dins dels marges


