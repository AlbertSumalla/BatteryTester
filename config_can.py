import os
import can
import cantools

DBC_PATH = '/home/fusefinder/Descargas/FS-FUSION-ION_v449_DBC_v5_FF0.dbc'  #Ubicació del dbc de la bms 



def get_bms_filters(db):    #Filtres del bus
    CAN_BMS_FILTERS =[
	{"can_id": get_id_db(db, "VOLTAGE_INFO") , "can_mask": 0xfffffff, "extended": True},
	{"can_id": get_id_db(db, "CURRENT") , "can_mask": 0xfffffff, "extended": True},
	{"can_id": get_id_db(db, "TEMPERATURE_INFO_CELL") , "can_mask": 0xfffffff, "extended": True},
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

    def add_voltage(self, voltage):
        self.voltage.append(voltage)

    def add_temperature(self, temperature):
        self.temperature.append(temperature)

class Battery_full:     #per enmagatzemar totes les dades de la bateria
    def __init__(self):
        self.voltage = []
        self.temperature = []
        self.current = []
        self.soc = []
        self.soh = []
        self.cells = [Battery_cell()]*24

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



