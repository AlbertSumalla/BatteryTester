import os
import can
import cantools

DBC_PATH = '/home/fusefinder/Descargas/FS-FUSION-ION_v449_DBC_v5_FF0.dbc'  #Ubicació del dbc de la bms 

CAN_BMS_FILTERS =   #Filtres del bus
    [
	{"can_id": db.get_message_by_name("VOLTAGE_INFO").frame_id , "can_mask": 0xfffffff, "extended": True},
	{"can_id": db.get_message_by_name("CURRENT").frame_id , "can_mask": 0xfffffff, "extended": True},
	{"can_id": db.get_message_by_name("TEMPERATURE_INFO_CELL").frame_id , "can_mask": 0xfffffff, "extended": True},
	{"can_id": db.get_message_by_name("TEMPERATURE_INFO_INTERNAL").frame_id , "can_mask": 0xfffffff, "extended": True},
	{"can_id": db.get_message_by_name("VOLTAGES_CELL").frame_id , "can_mask": 0xfffffff, "extended": True},
	{"can_id": db.get_message_by_name("TEMPERATURE_CELLS").frame_id , "can_mask": 0xfffffff, "extended": True},
	{"can_id": db.get_message_by_name("BATTERY_STATE").frame_id , "can_mask": 0xfffffff, "extended": True}
	#{"can_id": db.get_message_by_name("BATTERY_SERIAL_NUMBER").frame_id , "can_mask": 0xfffffff, "extended": True}
    ]


def setup_bus():    #Retorna el bus can configurat amb els filtres
    os.system('sudo ip link set can0 type can bitrate 500000')
    os.system('sudo ifconfig can0 up')

    return can.interface.Bus(channel = 'can0', interface = 'socketcan', fd = True)



def setup_db_bms():     #Retorna la database del bms
    return cantools.database.load_file(DBC_PATH)



def encode_keepalive():     #Retorna el misatge keepalive
    keepalive = db.get_message_by_name("BROADCAST_KEEP_ALIVE")
    data = keepalive.encode({})

    return can.Message(arbitration_id=keepalive.frame_id, data=data, is_extended_id=True)



def encode_ignition(CAN_ignition):     #Retorna el misatge ignite
    ignition = db.get_message_by_name("IGNITION_OVER_CAN")
    data = ignition.encode({CAN_ignition})

    return can.Message(arbitration_id=ignition.frame_id, data=data, is_extended_id=True)


def close_bus():    #Tanca el bus
    os.system('sudo ifconfig can0 down')