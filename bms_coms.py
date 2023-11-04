import os
import can
import cantools

os.system('sudo ip link set can0 type can bitrate 500000')
os.system('sudo ifconfig can0 up')

db = cantools.database.load_file('/home/fusefinder/Descargas/FS-FUSION-ION_v449_DBC_v5_FF0.dbc')

filters =[
	{"can_id": db.get_message_by_name("VOLTAGE_INFO").frame_id , "can_mask": 0xfffffff, "extended": True},
	{"can_id": db.get_message_by_name("CURRENT").frame_id , "can_mask": 0xfffffff, "extended": True},
	{"can_id": db.get_message_by_name("TEMPERATURE_INFO_CELL").frame_id , "can_mask": 0xfffffff, "extended": True},
	{"can_id": db.get_message_by_name("TEMPERATURE_INFO_INTERNAL").frame_id , "can_mask": 0xfffffff, "extended": True},
	{"can_id": db.get_message_by_name("VOLTAGES_CELL").frame_id , "can_mask": 0xfffffff, "extended": True},
	{"can_id": db.get_message_by_name("TEMPERATURE_CELLS").frame_id , "can_mask": 0xfffffff, "extended": True},
	{"can_id": db.get_message_by_name("BATTERY_STATE").frame_id , "can_mask": 0xfffffff, "extended": True}
	#{"can_id": db.get_message_by_name("BATTERY_SERIAL_NUMBER").frame_id , "can_mask": 0xfffffff, "extended": True}
]

keepalive = db.get_message_by_name("BROADCAST_KEEP_ALIVE")
data = keepalive.encode({})


ign_message = can.Message(arbitration_id=keepalive.frame_id, data=data, is_extended_id=True)

msg_list = {}
with can.interface.Bus(channel = 'can0', interface = 'socketcan', fd=True, can_filters=filters) as can0:# socketcan_native
#with can.interface.Bus(channel = 'can0', bustype = 'socketcan', fd=True) as can0:# socketcan_native
	can0.send(ign_message)
	for i in range(30): 
		msg_list[i] = can0.recv(1)
		
for i in range(30): 
	print(i)
	print(msg_list[i])
	try:
		decode_frame = db.decode_message(msg_list[i].arbitration_id, msg_list[i].data)
		print(decode_frame)
	except Exception:
		print('Invalid frame')

os.system('sudo ifconfig can0 down')
