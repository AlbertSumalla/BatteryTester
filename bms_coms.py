import os
import can
import cantools
import config_can

db = setup_db()

msg_list = {}

with setup_bus() as can0: # socketcan_native
	can0.set_filters(CAN_BMS_FILTERS)
	
	can0.send(encode_keepalive())
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

close_bus()
