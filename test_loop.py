import bms_coms
import pandas as pd
import constants as c
import gpioconfig

def function_test_loop():
    #Càlcul de mitjanes
    VoltMean = 1 #s.mean
    currMean = 1
    tempMean = 1
    SoCMean = 1
    SoHMean = 1
    VoltMeanCells = 1
    tempMeanCells = 1

    """-----------------------------------posar-ho darrere de Checks Cells Bateria
    Volt = pd.Series('llista que ens passin')
    curr = pd.Series('llista que ens passin')
    temp = pd.Series('llista que ens passin')
    SoC = pd.Series('llista que ens passin')
    SoH = pd.Series('llista que ens passin')
    VoltCells = pd.Series('llista que ens passin')
    tempCells = pd.Series('llista que ens passin')
    #------------------------------------definició de les series que rebem

    VoltMean = Volt.mean
    currMean = curr.mean
    tempMean = temp.mean
    SoCMean = SoC.mean
    SoHMean = SoH.mean
    VoltMeanCells = VoltCells.mean
    tempMeanCells = tempCells.mean
    #------------------------------------mitjana de cada serie

    if (Volt[Volt < c.VoltMin].count() != 0 or Volt[Volt > c.VoltMax].count() != 0):
        VoltMeanCheck = 3 #cas en que mitjana és correcte però alguna de les lectures esta fora del rang (Warning)
    if (curr[c.currExpect - c.RangecurrMin < curr].count() != 0 or curr[curr < c.currExpect - c.RangecurrMin].count() != 0):
        currMeanCheck = 3 #cas en que mitjana és correcte però alguna de les lectures esta fora del rang (Warning)
    if (temp[c.tempMin >= temp] != 0 or temp[c.tempMax <= temp] != 0):
        tempMeanCheck = 3 #cas en que mitjana és correcte però alguna de les lectures esta fora del rang (Warning)
    if (SoC[c.SoCMin >= SoC] != 0):
        SoCMeanCheck = 3 #cas en que mitjana és correcte però alguna de les lectures esta fora del rang (Warning)
    if (SoH[c.SoHMin >= SoH] != 0):
        SoHMeanCheck = 3 #cas en que mitjana és correcte però alguna de les lectures esta fora del rang (Warning)
    if (VoltCells[VoltCells < c.VoltMinCells].count() != 0 or VoltCells[VoltCells > c.VoltMaxCells].count() != 0):
        VoltMeanCCheck = 3 #cas en que mitjana és correcte però alguna de les lectures esta fora del rang (Warning)
    if (tempCells[c.tempMinCells >= tempCells] != 0 or tempCells[c.tempMaxCells <= tempCells] != 0):
        tempMeanCCheck = 3 #cas en que mitjana és correcte però alguna de les lectures esta fora del rang (Warning)
    #----------------------------------mirem si alguna de les lectures de la llista que ens passen esta fora del rang

    if (Volt.count() < 5):
        VoltMeanCheck = 4 #cas en què el nombre de lectures és massa baix (Warning)
    if (curr.count() < 5):
        currMeanCheck = 4 #cas en què el nombre de lectures és massa baix (Warning)
    if (temp.count() < 5):
        tempMeanCheck = 4 #cas en què el nombre de lectures és massa baix (Warning)
    if (SoC.count() < 5):
        SoCMeanCheck = 4 #cas en què el nombre de lectures és massa baix (Warning)
    if (SoH.count() < 5):
        SoHMeanCheck = 4 #cas en què el nombre de lectures és massa baix (Warning)
    if (VoltCells.count() < 5):
        VoltMeanCCheck = 4 #cas en què el nombre de lectures és massa baix (Warning)
    if (tempCells.count() < 5):
        tempMeanCCheck = 4 #cas en què el nombre de lectures és massa baix (Warning)
    #----------------------------------mirem si la quantitat de lectures no aberrants que té cada llista és suficient o no
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

    #Checks GPIOs
    Volt12Vline = GPIOValuesDict["GPIO17"]
    if (Volt12Vline = 0):
        Volt12VlineCheck = 1; #Voltage fora de rang (11V-16V)
    else:
        Volt12VlineCheck = 0; #Voltage dins de rang (11V-16V)

    GPIOReturnDict = []
    return GPIOReturnDict