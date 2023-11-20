import bms_coms
import pandas as pd
import constants as c
from gpioconfig import *

def function_test_loop():

    bat_info = get_bms_data_test()
    
    #Càlcul de mitjanes
    VoltMean = 1 #s.mean
    currMean = 1
    tempMean = 1
    SoCMean = 1
    SoHMean = 1
    VoltMeanCells = 1
    tempMeanCells = 1

    VoltCells = []
    tempCells = []
    
    """-----------------------------------posar-ho darrere de Checks Cells Bateria
    Volt = pd.Series(bat_info.get_voltage())
    curr = pd.Series(bat_info.get_current())
    temp = pd.Series(bat_info.get_temperature())
    SoC = pd.Series(bat_info.get_soc())
    SoH = pd.Series(bat_info.get_soh())
    
    for i in range(24):
        VoltCells.append(pd.Series(bat_info.get_cell_voltage(i)))

    for i in range(4):
        tempCells.append(pd.Series(bat_info.get_cell_temperature(i)))
    #------------------------------------definició de les series que rebem

    VoltMean = Volt.mean
    currMean = curr.mean
    tempMean = temp.mean
    SoCMean = SoC.mean
    SoHMean = SoH.mean
    VoltMeanCells = VoltCells.mean
    tempMeanCells = tempCells.mean
    #------------------------------------mitjana de cada serie
    warningV = 0
    warningC = 0
    warningT = 0
    warningSoC = 0
    warningSoH = 0
    warningVC = 0
    warningTC = 0
    #-------------------------------------variables per evitar que els warnings i errors es solapin

    if (Volt[Volt < c.VoltMin].count() != 0 or Volt[Volt > c.VoltMax].count() != 0):
        VoltMeanCheck = 3 #cas en que mitjana és correcte però alguna de les lectures esta fora del rang (Warning)
        warningV = 1
    if (curr[c.currExpect - c.RangecurrMin < curr].count() != 0 or curr[curr < c.currExpect - c.RangecurrMin].count() != 0):
        currMeanCheck = 3 #cas en que mitjana és correcte però alguna de les lectures esta fora del rang (Warning)
        warningC = 1
    if (temp[c.tempMin >= temp] != 0 or temp[c.tempMax <= temp] != 0):
        tempMeanCheck = 3 #cas en que mitjana és correcte però alguna de les lectures esta fora del rang (Warning)
        warningT = 1
    if (SoC[c.SoCMin >= SoC] != 0):
        SoCMeanCheck = 3 #cas en que mitjana és correcte però alguna de les lectures esta fora del rang (Warning)
        warningSoC = 1
    if (SoH[c.SoHMin >= SoH] != 0):
        SoHMeanCheck = 3 #cas en que mitjana és correcte però alguna de les lectures esta fora del rang (Warning)
        warningSoH = 1
    if (VoltCells[VoltCells < c.VoltMinCells].count() != 0 or VoltCells[VoltCells > c.VoltMaxCells].count() != 0):
        VoltMeanCCheck = 3 #cas en que mitjana és correcte però alguna de les lectures esta fora del rang (Warning)
        warningVC = 1
    if (tempCells[c.tempMinCells >= tempCells] != 0 or tempCells[c.tempMaxCells <= tempCells] != 0):
        tempMeanCCheck = 3 #cas en que mitjana és correcte però alguna de les lectures esta fora del rang (Warning)
        warningTC = 1
    #----------------------------------mirem si alguna de les lectures de la llista que ens passen esta fora del rang

    if (Volt.count() < 5):
        VoltMeanCheck = 4 #cas en què el nombre de lectures és massa baix (Warning)
        warningV = 1
    if (curr.count() < 5):
        currMeanCheck = 4 #cas en què el nombre de lectures és massa baix (Warning)
        warningC = 1
    if (temp.count() < 5):
        tempMeanCheck = 4 #cas en què el nombre de lectures és massa baix (Warning)
        warningT = 1
    if (SoC.count() < 5):
        SoCMeanCheck = 4 #cas en què el nombre de lectures és massa baix (Warning)
        warningSoC = 1
    if (SoH.count() < 5):
        SoHMeanCheck = 4 #cas en què el nombre de lectures és massa baix (Warning)
        warningSoH = 1
    if (VoltCells.count() < 5):
        VoltMeanCCheck = 4 #cas en què el nombre de lectures és massa baix (Warning)
        warningVC = 1
    if (tempCells.count() < 5):
        tempMeanCCheck = 4 #cas en què el nombre de lectures és massa baix (Warning)
        warningTC = 1
    #----------------------------------mirem si la quantitat de lectures no aberrants que té cada llista és suficient o no
    """


    #--------------------constants.py apart de les constants----------------------


    #-------------------------------------------------------------------
    #Checks Bateria
    if c.VoltMin >= VoltMean and warningV == 0:
        VoltMeanCheck = 2 #Voltage per sota mínims
    elif VoltMean >= c.VoltMax and warningV == 0:
        VoltMeanCheck = 1 #Voltage per sobre màxims
    elif warningV == 0:
        VoltMeanCheck = 0 #Voltage dins de marges

    if (c.currExpect - c.RangecurrMin < currMean < c.currExpect + c.RangecurrMax) and warningC == 0:
        currMeanCheck = 0 #Corrent dins de marges
    elif warningV == 0:
        currMeanCheck = 1 #Corrent fora de l'esperat

    if c.tempMin >= tempMean and warningT == 0:
        tempMeanCheck = 2 #Temperatura per sota mínims
    elif tempMean >= c.tempMax and warningT == 0:
        tempMeanCheck = 1 #Temperatura per sobre màxims
    elif warningT == 0:
        tempMeanCheck = 0 #Temperatura dins de marges

    if c.SoCMin >= SoCMean and warningSoC == 0:
        SoCMeanCheck = 1 #SoC per sota del mínim
    elif warningSoC == 0:
        SoCMeanCheck = 0 #SoC dins dels marges

    if c.SoHMin >= SoHMean and warningSoH == 0:
        SoHMeanCheck = 1 #SoH per sota del mínim
    elif warningSoH == 0:
        SoHMeanCheck = 0 #SoH dins dels marges


    #Checks Cells Bateria
    if c.VoltMinCells >= VoltMeanCells and warningVC == 0:
        VoltMeanCCheck = 2 #Voltage de cel·les per sota mínims
    elif VoltMeanCells >= c.VoltMaxCells and warningVC == 0:
        VoltMeanCCheck = 1 #Voltage de cel·les per sobre màxims
    elif warningVC:
        VoltMeanCCheck = 0 #Voltage de cel·les dins de marges

    if c.tempMinCells >= tempMeanCells and warningTC == 0:
        tempMeanCCheck = 2 #Temperatura de cel·les per sota mínims
    elif tempMeanCells >= c.tempMaxCells and warningTC == 0:
        tempMeanCCheck = 1 #Temperatura de cel·les per sobre màxims
    elif warningTC == 0:
        tempMeanCCheck = 0 #Temperatura de cel·les dins dels marges

    #Checks GPIOs
    Volt12Vline = GPIOValuesDict["GPIO17"]
    if (Volt12Vline == 0):
        Volt12VlineCheck = 1; #Voltage fora de rang (11V-16V)
    else:
        Volt12VlineCheck = 0; #Voltage dins de rang (11V-16V)

    TreatedDataReturnList = [Volt12VlineCheck,-1]
    return TreatedDataReturnList
