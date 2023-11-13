import bms_coms
import pandas as pd
import constants as c

#Càlcul de mitjanes
VoltMean = 1 #s.mean
currMean = 1
tempMean = 1
SoCMean = 1
SoHMean = 1
VoltMeanCells = 1
tempMeanCells = 1

"""posar-ho darrere de Checks Cells Bateria
Volt = pd.Series('llista que ens passin')
curr = pd.Series('llista que ens passin')
temp = pd.Series('llista que ens passin')
SoC = pd.Series('llista que ens passin')
SoH = pd.Series('llista que ens passin')
VoltCells = pd.Series('llista que ens passin')
tempCells = pd.Series('llista que ens passin')
#definició de les series que rebem

VoltMean = Volt.mean
currMean = curr.mean
tempMean = temp.mean
SoCMean = SoC.mean
SoHMean = SoH.mean
VoltMeanCells = VoltCells.mean
tempMeanCells = tempCells.mean
#mitjana de cada serie

if (Volt[c.VoltMax < Volt < c.VoltMin].count() != 0 or Volt[Volt > c.VoltMax].count() != 0):
    VoltMeanCheck = 3 #cas en que mitjana és correcte però alguna de les lectures esta fora del rang (Warning)
if (curr[c.currExpect - c.RangecurrMin < curr < c.currExpect + c.RangecurrMax].count() != 0):
    currMeanCheck = 3

#mirem si alguna de les lectures de la llista que ens passen esta fora del rang, i la quantitat de lectures no aberrants té la llista

"""


#--------------------constants.py apart de les constants----------------------


#-------------------------------------------------------------------
#Checks Bateria
if c.VoltMin >= VoltMean:
    VoltMeanCheck = 2 #Voltage per sota mínims
elif VoltMean >= c.VoltMax:
    VoltMeanCheck = 1 #Voltage per sobre màxims
else:
    VoltMeanCheck = 0 #Voltage dins de marges

if (c.currExpect - c.RangecurrMin < currMean < c.currExpect + c.RangecurrMax):
    currMeanCheck = 0 #Corrent dins de marges
else:
    currMeanCheck = 1 #Corrent fora de l'esperat

if c.tempMin >= tempMean:
    tempMeanCheck = 2 #Temperatura per sota mínims
elif tempMean >= c.tempMax:
    tempMeanCheck = 1 #Temperatura per sobre màxims
else:
    tempMeanCheck = 0 #Temperatura dins de marges

if c.SoCMin >= SoCMean:
    SoCMeanCheck = 1 #SoC per sota del mínim
else:
    SoCMeanCheck = 0 #SoC dins dels marges

if c.SoHMin >= SoHMean:
    SoHMeanCheck = 1 #SoH per sota del mínim
else:
    SoHMeanCheck = 0 #SoH dins dels marges


#Checks Cells Bateria
if c.VoltMinCells >= VoltMeanCells:
    VoltMeanCCheck = 2 #Voltage de cel·les per sota mínims
elif VoltMeanCells >= c.VoltMaxCells:
    VoltMeanCCheck = 1 #Voltage de cel·les per sobre màxims
else:
    VoltMeanCCheck = 0 #Voltage de cel·les dins de marges

if c.tempMinCells >= tempMeanCells:
    tempMeanCCheck = 2 #Temperatura de cel·les per sota mínims
elif tempMeanCells >= c.tempMaxCells:
    tempMeanCCheck = 1 #Temperatura de cel·les per sobre màxims
else:
    tempMeanCCheck = 0 #Temperatura de cel·les dins dels marges


