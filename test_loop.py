import bms_coms
import pandas as pd
import constants as c
from gpioconfig import *

def function_test_loop():

    #------------------------------------constants.py apart de les constants
    
    bat_info = get_bms_data_test()
    
    VoltMeanCells = []
    tempMeanCells = []

    VoltCells = []
    VoltMeanCCheck = []
    tempCells = []
    tempMeanCCheck = []
    
    Volt = pd.Series(bat_info.get_voltage())
    curr = pd.Series(bat_info.get_current())
    temp = pd.Series(bat_info.get_temperature())
    SoC = pd.Series(bat_info.get_soc())
    SoH = pd.Series(bat_info.get_soh())
    
    for i in range(24):
        VoltCells.append(pd.Series(bat_info.get_cell_voltage(i)))

    for i in range(4):
        tempCells.append(pd.Series(bat_info.get_cell_temperature(i)))

    #------------------------------------Definició de les series que rebem de bms_com

    VoltMean = Volt.mean
    currMean = curr.mean
    tempMean = temp.mean
    SoCMean = SoC.mean
    SoHMean = SoH.mean

    #------------------------------------Mitjana de cada serie de la bateria

    for i in range(24):
        VoltMeanCells.append(VoltCells[i].mean)

        if (VoltCells[i][VoltCells[i] < c.VoltMinCells].count() != 0 or VoltCells[i][VoltCells[i] > c.VoltMaxCells].count() != 0):
            VoltMeanCCheck[i] = 3 #cas en que mitjana és correcte però alguna de les lectures esta fora del rang (Warning)
            warningVC = 1
        if (VoltCells[i].count() < 5):
            VoltMeanCCheck[i] = 4 #cas en què el nombre de lectures és massa baix (Warning)
            warningVC = 1
      
    for i in range(4):
        tempMeanCells.append(tempCells[i].mean)

        if (tempCells[i][c.tempMinCells >= tempCells[i]] != 0 or tempCells[i][c.tempMaxCells <= tempCells[i]] != 0):
            tempMeanCCheck[i] = 3 #cas en que mitjana és correcte però alguna de les lectures esta fora del rang (Warning)
            warningTC = 1
        if (tempCells[i].count() < 5):
            tempMeanCCheck[i] = 4 #cas en què el nombre de lectures és massa baix (Warning)
            warningTC = 1

    #-----------------------------------------Càlcul de mitjanes i dels warnings (alguna mesura fora del rang i poques mesures) de totes les cel·les
    
    warningV = 0
    warningC = 0
    warningT = 0
    warningSoC = 0
    warningSoH = 0
    warningVC = 0
    warningTC = 0

    #-------------------------------------Variables per evitar que els warnings i errors es solapin

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
        
    #----------------------------------Mirem si alguna de les lectures de la llista que ens passen esta fora del rang de la bateria (Warning 1)

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
    
    #--------------------------------------Mirem si la quantitat de lectures no aberrants que té cada llista és suficient o no de la bateria (Warning 2)

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
        
#--------------------------------------------------Checks Bateria
 
    for i in range(24):
        if c.VoltMinCells >= VoltMeanCells[i] and warningVC == 0:
            VoltMeanCCheck[i] = 2 #Voltage de cel·les per sota mínims
        elif VoltMeanCells[i] >= c.VoltMaxCells and warningVC == 0:
            VoltMeanCCheck[i] = 1 #Voltage de cel·les per sobre màxims
        elif warningVC == 0:
            VoltMeanCCheck[i] = 0 #Voltage de cel·les dins de marges

    for j in range(4):
        if c.tempMinCells >= tempMeanCells[j] and warningTC == 0:
            tempMeanCCheck[j] = 2 #Temperatura de cel·les per sota mínims
        elif tempMeanCells[j] >= c.tempMaxCells and warningTC == 0:
            tempMeanCCheck[j] = 1 #Temperatura de cel·les per sobre màxims
        elif warningTC == 0:
            tempMeanCCheck[j] = 0 #Temperatura de cel·les dins dels marges

    #-------------------------------------------------Checks Cells Bateria

    Volt12Vline = GPIOValuesDict["GPIO17"]
    if (Volt12Vline == 0):
        Volt12VlineCheck = 1 #Voltage fora de rang (11V-16V)
    else:
        Volt12VlineCheck = 0 #Voltage dins de rang (11V-16V)

    #-----------------------------------------------Checks GPIOs
    
    TreatedDataReturnList = [Volt12VlineCheck,-1, VoltMeanCheck, VoltMean, currMeanCheck, currMean, tempMeanCheck, tempMean, SoCMeanCheck, SoCMean, SoHMeanCheck, SoHMean]
    for i in range(24):
        TreatedDataReturnList.append(VoltMeanCCheck[i])
        TreatedDataReturnList.append(VoltMeanCells[i])
    for j in range(4):
        TreatedDataReturnList.append(tempMeanCCheck[j])
        TreatedDataReturnList.append(tempMeanCells[j])

    #----------------------------------------------Creem la llista que passem a la UI amb tots els Checks i els seus valors
    
    return TreatedDataReturnList

def failed_connection(Volt, curr, temp, SoC, SoH, VoltCells, tempCells):
    cell_volt_empt = 0
    cell_temp_empt = 0
    for i in range (24):                        #busquem llistes buides a cell_voltage
        if len(VoltCells[i]) == 0:
            cell_volt_empt = 1
    for j in range (4):                         #busquem llistes buides a cell_temperature
        if len(tempCells[j]) == 0:
            cell_temp_empt = 1
    if len(Volt) == 0 and len(curr) and len(temp) and len(SoC) and len(SoH) and cell_temp_empt == 1 and cell_volt_empt == 1:
        return -1                       #no hem obtingut cap dada (fallida total de la connexió)
    else:
        return 0                        # hem rebut dades (comunicació funciona)
        
