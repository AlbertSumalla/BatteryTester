import os
import can
import cantools
from statistics import mean
from decimal import Decimal, getcontext


DBC_PATH = '/home/fusefinder/Descargas/FS-FUSION-ION_v449_DBC_v5_FF0.dbc'  #Ubicació del dbc de la bms 

# Constant declaration
MAX_OUTLIER_ERROR = 0.0

# Decimal floating point declaration
getcontext().prec = 4 

def get_bms_filters(db):    #Filtres del bus
    CAN_BMS_FILTERS =[
	{"can_id": get_id_db(db, "VOLTAGE_INFO") , "can_mask": 0xfffffff, "extended": True},
	{"can_id": get_id_db(db, "CURRENT") , "can_mask": 0xfffffff, "extended": True},
	{"can_id": get_id_db(db, "TEMPERATURE_INFO_INTERNAL") , "can_mask": 0xfffffff, "extended": True},
	{"can_id": get_id_db(db, "VOLTAGES_CELL") , "can_mask": 0xfffffff, "extended": True},
	{"can_id": get_id_db(db, "TEMPERATURE_CELLS") , "can_mask": 0xfffffff, "extended": True},
	{"can_id": get_id_db(db, "BATTERY_STATE") , "can_mask": 0xfffffff, "extended": True},
    {"can_id": get_id_db(db, "BATTERY_SERIAL_NUMBER") , "can_mask": 0xfffffff, "extended": True}
    ]

    return CAN_BMS_FILTERS

def get_id_db(db, name):
    return db.get_message_by_name(name).frame_id


def setup_bus():    #Retorna el bus can configurat amb els filtres
    os.system('sudo ip link set can0 type can bitrate 500000')
    os.system('sudo ifconfig can0 up')

    return can.interface.Bus(channel = 'can0', interface = 'socketcan', fd = True)



def setup_db_bms():     #Retorna la database del bms
    return cantools.database.load_file(DBC_PATH)



def encode_keepalive(db):     #Retorna el misatge keepalive
    keepalive = db.get_message_by_name("BROADCAST_KEEP_ALIVE")
    data = keepalive.encode({})

    return can.Message(arbitration_id=keepalive.frame_id, data=data, is_extended_id=True)



def encode_ignition(db ,CAN_ignition):     #Retorna el misatge ignite
    ignition = db.get_message_by_name("IGNITION_OVER_CAN")
    data = ignition.encode({CAN_ignition})

    return can.Message(arbitration_id=ignition.frame_id, data=data, is_extended_id=True)


def close_bus():    #Tanca el bus
    os.system('sudo ifconfig can0 down')

def remove_outliers(list):  #treu els valors aberrants
    
	if list == 0:
		list.pop(0)

    return list

	"""
class Battery_cell:     #per enmagatzemar totes les dades d'una cel·la
    def __init__(self):
        self.voltage = []
        self.temperature = []

    def __str__(self):
        return "Tensions = " + str(self.voltage) + " Temperatures = " + str(self.temperature)

    def add_voltage(self, voltage):
        self.voltage.append(voltage)

    def add_temperature(self, temperature):
        self.temperature.append(temperature)

    def remove_outliers(self):

        self.voltage = remove_outliers(self.voltage, MAX_OUTLIER_ERROR)
        self.temperature = remove_outliers(self.temperature, MAX_OUTLIER_ERROR)
	"""

class Battery_full:     #per enmagatzemar totes les dades de la bateria
    def __init__(self):
        self.voltage = []
        self.temperature = []
        self.current = []
        self.soc = []
        self.soh = []
        self.cell_voltage = []
        self.cell_temperature = []
        self.serial = []               # el num de serie té 32 caracters que guardo a una lista per fer més facil l'ordre
        
    def init_cells(self):

        for _ in range(24):
            self.cell_voltage.append([])

        for _ in range(4):
            self.cell_temperature.append([])

        for _ in range(32):
            self.serial.append(0)

    def print_class(self):
        print(self.voltage)
        print(self.temperature)
        print(self.current)
        print(self.soc)
        print(self.soh)
        print(self.serial)

        for i in range(24):
            print("Cell voltage " + str(i) + " " + str(self.cell_voltage[i]))

        for i in range(4):
            print("Cell temperature " + str(i) + " " + str(self.cell_temperature[i]))

    def add_voltage(self, voltage):
        self.voltage.append(voltage)

    def add_temperature(self, temperature):
        self.temperature.append(temperature)

    def add_current(self, current):
        self.current.append(current)

    def add_soc(self, soc):
        self.soc.append(Decimal(soc))

    def add_soh(self, soh):
        self.soh.append(Decimal(soh))

    def add_cell_voltage(self, i, voltage):
        self.cell_voltage[i].append(Decimal(voltage))

    def add_cell_temperature(self, i, temperature):
        self.cell_temperature[i].append(Decimal(temperature))

    def set_serial(self, i, serial):
        self.serial[i] = serial

    def get_voltage(self):
        return self.voltage

    def get_temperature(self):
        return self.temperature

    def get_current(self):
        return self.current

    def get_soc(self):
        return self.soc

    def get_soh(self):
        return self.soh

    def get_cell_voltage(self, i):
        return self.cell_voltage[i]

    def get_cell_temperature(self, i):
        return self.cell_temperature[i]
    
    def get_serial(self):
        return self.serial

    def remove_outliers(self):
	"""
        self.voltage = remove_outliers(self.voltage, MAX_OUTLIER_ERROR)

        self.temperature = remove_outliers(self.temperature, MAX_OUTLIER_ERROR)

        self.current = remove_outliers(self.current, MAX_OUTLIER_ERROR)

        self.soc = remove_outliers(self.soc, MAX_OUTLIER_ERROR)

        self.soh = remove_outliers(self.soh, MAX_OUTLIER_ERROR)
	"""
        for i in range(24):
            self.cell_voltage[i] = remove_outliers(self.cell_voltage[i])

        for i in range(4):
            self.cell_temperature[i] = remove_outliers(self.cell_temperature[i])

