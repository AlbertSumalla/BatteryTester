import os
import can
import cantools
from config_can import *
a
db = setup_db_bms()

bat_info = Battery_full()

with setup_bus() as can0: # socketcan_native
	can0.set_filters(get_bms_filters(db))
	
	can0.send(encode_keepalive(db))

	for i in range(30): 

		msg_received = can0.recv(1)

		try:
			decoded_frame = db.decode_message(msg_received.arbitration_id, msg_received.data)
		except Exception:
			continue

		match msg_received.arbitration_id:

			case get_id_db(db, "VOLTAGE_INFO"):
				bat_info.add_voltage(decoded_frame['Battery_Voltage'])

			case get_id_db(db, "CURRENT"):
				bat_info.add_current(decoded_frame['Battery_Current'])

			case get_id_db(db, "TEMPERATURE_INFO_CELL"):
				bat_info.add_current(decoded_frame['Temperature_internal_Mean'])

			case get_id_db(db, "VOLTAGES_CELL"):
				i = decoded_frame['Index_of_cell']

				bat_info.cells[i].add_voltage(decoded_frame['Cell_voltage_at_Index_plus_0'])
				bat_info.cells[i + 1].add_voltage(decoded_frame['Cell_voltage_at_Index_plus_1'])
				bat_info.cells[i + 2].add_voltage(decoded_frame['Cell_voltage_at_Index_plus_2'])

			case get_id_db(db, "TEMPERATURE_CELLS"):
				i = decoded_frame['NTC_Index']

				bat_info.cells[i].add_temperature(decoded_frame['Temperature_at_NTC_index_plus_0'])
				bat_info.cells[i + 1].add_temperature(decoded_frame['Temperature_at_NTC_index_plus_1'])
				bat_info.cells[i + 2].add_temperature(decoded_frame['Temperature_at_NTC_index_plus_2'])


			case get_id_db(db, "BATTERY_STATE"):
				bat_info.add_soc(decoded_frame['State_of_Charge'])
				bat_info.add_soh(decoded_frame['State_of_Health'])		



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
