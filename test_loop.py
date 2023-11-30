from config_can import *
from bms_coms import *
import pandas as pd
from constants import *
from gpioconfig import *

def function_test_loop():
    
    #------------------------------------constants.py apart de les constants
    
    bat_info = get_bms_data_test()

    VoltMeanCells = []
    tempMeanCells = []

    VoltCells = []
    VoltMeanCCheck = [0]*24
    tempCells = []
    tempMeanCCheck = [0]*4
    
    Volt = pd.Series(bat_info.get_voltage())
    curr = pd.Series(bat_info.get_current())
    temp = pd.Series(bat_info.get_temperature())
    SoC = pd.Series(bat_info.get_soc())
    SoH = pd.Series(bat_info.get_soh())
    
    for i in range(24):
        VoltCells.append(pd.Series(bat_info.get_cell_voltage(i)))

    for i in range(4):
        tempCells.append(pd.Series(bat_info.get_cell_temperature(i)))

    #------------------------------------Definició de les series que rebem de bms_coms

    VoltMean = Volt.mean()
    currMean = curr.mean()
    tempMean = temp.mean()
    SoCMean = SoC.mean()
    SoHMean = SoH.mean()

    #------------------------------------Mitjana de cada serie de la bateria

    for i in range(24):
        VoltMeanCells.append(VoltCells[i].mean())

        if (VoltCells[i][VoltCells[i] < VoltMinCells].count() != 0 or VoltCells[i][VoltCells[i] > VoltMaxCells].count() != 0):
            VoltMeanCCheck[i] = 3 #cas en que mitjana és correcte però alguna de les lectures esta fora del rang (Warning)
            warningVC = 1
        if (VoltCells[i].count() < 5):
            VoltMeanCCheck[i] = 4 #cas en què el nombre de lectures és massa baix (Warning)
            warningVC = 1
      
    for i in range(4):
        tempMeanCells.append(tempCells[i].mean())

        if (tempCells[i][tempMinCells >= tempCells[i]].count() != 0 or tempCells[i][tempMaxCells <= tempCells[i]].count() != 0):
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

    if (Volt[Volt < VoltMin].count() != 0 or Volt[Volt > VoltMax].count() != 0):
        VoltMeanCheck = 3 #cas en que mitjana és correcte però alguna de les lectures esta fora del rang (Warning)
        warningV = 1
    if (curr[currExpect - RangecurrMin < curr].count() != 0 or curr[curr < currExpect - RangecurrMin].count() != 0):
        currMeanCheck = 3 #cas en que mitjana és correcte però alguna de les lectures esta fora del rang (Warning)
        warningC = 1
    if (temp[tempMin >= temp].count() != 0 or temp[tempMax <= temp].count() != 0):
        tempMeanCheck = 3 #cas en que mitjana és correcte però alguna de les lectures esta fora del rang (Warning)
        warningT = 1
    if (SoC[SoCMin >= SoC].count() != 0):
        SoCMeanCheck = 3 #cas en que mitjana és correcte però alguna de les lectures esta fora del rang (Warning)
        warningSoC = 1
    if (SoH[SoHMin >= SoH].count() != 0):
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

    if VoltMin >= VoltMean and warningV == 0:
        VoltMeanCheck = 2 #Voltage per sota mínims
    elif VoltMean >= VoltMax and warningV == 0:
        VoltMeanCheck = 1 #Voltage per sobre màxims
    elif warningV == 0:
        VoltMeanCheck = 0 #Voltage dins de marges

    if (currExpect - RangecurrMin < currMean < currExpect + RangecurrMax) and warningC == 0:
        currMeanCheck = 0 #Corrent dins de marges
    elif warningV == 0:
        currMeanCheck = 1 #Corrent fora de l'esperat

    if tempMin >= tempMean and warningT == 0:
        tempMeanCheck = 2 #Temperatura per sota mínims
    elif tempMean >= tempMax and warningT == 0:
        tempMeanCheck = 1 #Temperatura per sobre màxims
    elif warningT == 0:
        tempMeanCheck = 0 #Temperatura dins de marges

    if SoCMin >= SoCMean and warningSoC == 0:
        SoCMeanCheck = 1 #SoC per sota del mínim
    elif warningSoC == 0:
        SoCMeanCheck = 0 #SoC dins dels marges

    if SoHMin >= SoHMean and warningSoH == 0:
        SoHMeanCheck = 1 #SoH per sota del mínim
    elif warningSoH == 0:
        SoHMeanCheck = 0 #SoH dins dels marges
        
#--------------------------------------------------Checks Bateria
 
    for i in range(24):
        if VoltMinCells >= VoltMeanCells[i] and warningVC == 0:
            VoltMeanCCheck[i] = 2 #Voltage de cel·les per sota mínims
        elif VoltMeanCells[i] >= VoltMaxCells and warningVC == 0:
            VoltMeanCCheck[i] = 1 #Voltage de cel·les per sobre màxims
        elif warningVC == 0:
            VoltMeanCCheck[i] = 0 #Voltage de cel·les dins de marges

    for j in range(4):
        if tempMinCells >= tempMeanCells[j] and warningTC == 0:
            tempMeanCCheck[j] = 2 #Temperatura de cel·les per sota mínims
        elif tempMeanCells[j] >= tempMaxCells and warningTC == 0:
            tempMeanCCheck[j] = 1 #Temperatura de cel·les per sobre màxims
        elif warningTC == 0:
            tempMeanCCheck[j] = 0 #Temperatura de cel·les dins dels marges

    #-------------------------------------------------Checks Cells Bateria

   """
    db = setup_db_bms()

    with setup_bus() as can0: # socketcan_native
	
	can0.set_filters(get_inv_filters())
        
        inv_errors = get_inv_errors(can0, db)

        can0.set_filters(get_bms_filters(db))
    
        bat_info = get_bms_data_test(can0, db, 2)
    
    bat_info.remove_outliers()

    close_bus()

   """
   
    inv_errors = get_inv_errors_test()

    errors_inv = pd.Series(inv_errors)

    #--------------------------------------Definició de la serie d'errors del inversor que rebem de bms_coms

    if (errors_inv.count() == 0):
	    errors_inv_check = 0 #L'inversor no ens envia cap error
    else:
	    errors_inv_check = 1 #L'inversor ens envia algún error que enviarem a la UI

    #-------------------------------------Comprovem si l'inversor ens envia algún error o no

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
    TreatedDataReturnList.append(errors_inv_check)
    if (errors_inv_check == 1):
	    for k in range(errors_inv.count()):
		    TreatedDataReturnList.append(errors_inv[k])
    else:
	    TreatedDataReturnList.append(-1)

    #----------------------------------------------Creem la llista que passem a la UI amb tots els Checks i els seus valors (tant de bms com de l'inversor)
    
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
    if len(Volt) == 0 and len(curr) == 0 and len(temp) == 0 and len(SoC) == 0 and len(SoH) == 0 and cell_temp_empt == 1 and cell_volt_empt == 1:
        return -1                       #no hem obtingut cap dada (fallida total de la connexió)
    else:
        return 0                        # hem rebut dades (comunicació funciona)
        
