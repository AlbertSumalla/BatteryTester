import os
import can
import cantools
from config_can import *

db = setup_db_bms()

bat_info = Battery_full()

bat_info.init_cells()

with setup_bus() as can0: # socketcan_native
	
	can0.set_filters(get_bms_filters(db))

	can0.send(encode_keepalive(db))
	
	for i in range(100): 

		msg_received = can0.recv(1)
		if msg_received == None:
			can0.send(encode_keepalive(db))
			
		try:
			decoded_frame = db.decode_message(msg_received.arbitration_id, msg_received.data)
		except Exception:
			continue

		msg_id = msg_received.arbitration_id

		if msg_id == get_id_db(db, "VOLTAGE_INFO"):
			bat_info.add_voltage(decoded_frame['Battery_Voltage'])
			print("VOLTAGE_INFO")
				
		if msg_id == get_id_db(db, "CURRENT"):
			bat_info.add_current(decoded_frame['Battery_Current'])
			print("CURRENT")
	
		if msg_id == get_id_db(db, "TEMPERATURE_INFO_INTERNAL"):
			bat_info.add_temperature(decoded_frame['Temperature_internal_Mean'])
			print("TEMPERATURE_INFO_INTERNAL")
			
		if msg_id == get_id_db(db, "VOLTAGES_CELL"):
			i = decoded_frame['Index_of_cell']

			bat_info.cells[i].add_voltage(decoded_frame['Cell_voltage_at_Index_plus_0'])
			bat_info.cells[i + 1].add_voltage(decoded_frame['Cell_voltage_at_Index_plus_1'])
			bat_info.cells[i + 2].add_voltage(decoded_frame['Cell_voltage_at_Index_plus_2'])
			print("VOLTAGES_CELL " + str(i))

		if msg_id == get_id_db(db, "TEMPERATURE_CELLS"):
			i = decoded_frame['NTC_Index']

			bat_info.cells[i].add_temperature(decoded_frame['Temperature_at_NTC_index_plus_0'])
			bat_info.cells[i + 1].add_temperature(decoded_frame['Temperature_at_NTC_index_plus_1'])
			bat_info.cells[i + 2].add_temperature(decoded_frame['Temperature_at_NTC_index_plus_2'])
			print("TEMPERATURE_CELLS " + str(i))

		if msg_id == get_id_db(db, "BATTERY_STATE"):
			bat_info.add_soc(decoded_frame['State_of_Charge'])
			bat_info.add_soh(decoded_frame['State_of_Health'])	
			print("BATTERY_STATE")	

bat_info.print_class()
bat_info.remove_outliers()
bat_info.print_class()

"""
for i in range(30): 
	print(i)
	print(msg_list[i])
	try:
		decode_frame = db.decode_message(msg_list[i].arbitration_id, msg_list[i].data)
		print(decode_frame)
	except Exception:
		print('Invalid frame')
"""

close_bus()
