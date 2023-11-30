import json

with open('constants_battery.json', 'r') as cnt_file:
    # Carga los datos desde el archivo JSON
    data = json.load(cnt_file)



#Valors mínims i màxims acceptables de la bateria
VoltMin = data["Total_Voltage"]["Value_MIN"]
VoltMax = data["Total_Voltage"]["Value_MAX"]
currExpect = 0
RangecurrMin = data["Total_Current"]["Value_MIN"]
RangecurrMax = data["Total_Current"]["Value_MAX"]
tempMin = data["Total_Temp"]["Value_MIN"]
tempMax = data["Total_Temp"]["Value_MAX"]
SoCMin = data["SoC_status"]["Value_MIN"]
SoHMin = data["SoH_status"]["Value_MIN"]

#Valors mínims i màxims acceptables de les cel·les de la bateria
VoltMinCells = data["Voltage_Cell"]["Value_MIN"]
VoltMaxCells = data["Voltage_Cell"]["Value_MAX"]
tempMinCells = data["Temp_Cell"]["Value_MIN"]
tempMaxCells = data["Temp_Cell"]["Value_MAX"]