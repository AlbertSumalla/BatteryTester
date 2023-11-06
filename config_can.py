import os
import can
import cantools
from statistics import mean

DBC_PATH = '/home/fusefinder/Descargas/FS-FUSION-ION_v449_DBC_v5_FF0.dbc'  #Ubicació del dbc de la bms 

MAX_OUTLIER_ERROR = 0.0

def get_bms_filters(db):    #Filtres del bus
    CAN_BMS_FILTERS =[
	{"can_id": get_id_db(db, "VOLTAGE_INFO") , "can_mask": 0xfffffff, "extended": True},
	{"can_id": get_id_db(db, "CURRENT") , "can_mask": 0xfffffff, "extended": True},
	{"can_id": get_id_db(db, "TEMPERATURE_INFO_INTERNAL") , "can_mask": 0xfffffff, "extended": True},
	{"can_id": get_id_db(db, "VOLTAGES_CELL") , "can_mask": 0xfffffff, "extended": True},
	{"can_id": get_id_db(db, "TEMPERATURE_CELLS") , "can_mask": 0xfffffff, "extended": True},
	{"can_id": get_id_db(db, "BATTERY_STATE") , "can_mask": 0xfffffff, "extended": True}
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



class Battery_cell:     #per enmagatzemar totes les dades d'una cel·la
    def __init__(self):
        self.voltage = []
        self.temperature = []

    def __str__(self):
        return "Tensions = " + str(self.voltage) + " Temperatures = " + str(self.voltage)

    def add_voltage(self, voltage):
        self.voltage.append(voltage)

    def add_temperature(self, temperature):
        self.temperature.append(temperature)

    def remove_outliers(self):
        for i in range(len(self.voltage)):
            if abs(self.voltage[i] - mean(self.voltage)) > MAX_OUTLIER_ERROR: 
                self.voltage.pop(i)

        for i in range(len(self.temperature)):
            if abs(self.temperature[i] - mean(self.temperature)) > MAX_OUTLIER_ERROR: 
                self.temperature.pop(i)



class Battery_full:     #per enmagatzemar totes les dades de la bateria
    def __init__(self):
        self.voltage = []
        self.temperature = []
        self.current = []
        self.soc = []
        self.soh = []
        self.cells = []
        
    def init_cells(self):
        for i in range(24):
            self.cells.append(Battery_cell())

    def print_class(self):
        print(self.voltage)
        print(self.temperature)
        print(self.current)
        print(self.soc)
        print(self.soh)

        for i in range(24):
            print(self.cells[i])

    def add_voltage(self, voltage):
        self.voltage.append(voltage)

    def add_temperature(self, temperature):
        self.temperature.append(temperature)

    def add_current(self, current):
        self.current.append(current)

    def add_soc(self, soc):
        self.soc.append(soc)

    def add_soh(self, soh):
        self.soh.append(soh)

    def remove_outliers(self):
        for i in range(len(self.voltage)-1):
            if abs(self.voltage[i] - mean(self.voltage)) > MAX_OUTLIER_ERROR: 
                self.voltage.pop(i)

        for i in range(len(self.temperature)-1):
            if abs(self.temperature[i] - mean(self.temperature)) > MAX_OUTLIER_ERROR: 
                self.temperature.pop(i)

        for i in range(len(self.current)-1):
            if abs(self.current[i] - mean(self.current)) > MAX_OUTLIER_ERROR: 
                self.current.pop(i)

        for i in range(len(self.soc)-1):
            if abs(self.soc[i] - mean(self.soc)) > MAX_OUTLIER_ERROR: 
                self.soc.pop(i)

        for i in range(len(self.soh)-1):
            if abs(self.soh[i] - mean(self.soh)) > MAX_OUTLIER_ERROR: 
                self.soh.pop(i)

        for i in range(24):
            self.cells[i].remove_outliers
