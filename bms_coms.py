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

			bat_info.add_cell_voltage(i, decoded_frame['Cell_voltage_at_Index_plus_0'])
			bat_info.add_cell_voltage(i + 1, decoded_frame['Cell_voltage_at_Index_plus_1'])
			bat_info.add_cell_voltage(i + 2, decoded_frame['Cell_voltage_at_Index_plus_2'])
			print("VOLTAGES_CELL " + str(i))

		if msg_id == get_id_db(db, "TEMPERATURE_CELLS"):
			i = decoded_frame['NTC_Index']

			bat_info.add_cell_temperature(i, decoded_frame['Temperature_at_NTC_index_plus_0'])
			bat_info.add_cell_temperature(i + 1, decoded_frame['Temperature_at_NTC_index_plus_1'])
			bat_info.add_cell_temperature(i + 2, decoded_frame['Temperature_at_NTC_index_plus_2'])
			print("TEMPERATURE_CELLS " + str(i))

		if msg_id == get_id_db(db, "BATTERY_STATE"):
			bat_info.add_soc(decoded_frame['State_of_Charge'])
			bat_info.add_soh(decoded_frame['State_of_Health'])	
			print("BATTERY_STATE")	

bat_info.print_class()
bat_info.remove_outliers()
bat_info.print_class()

close_bus()


#############################################################################################################

def get_bms_data(can_bus,db,iterations): #retorna el data set amb el nombre de dades corresponent a les iteracions (1 iteracions = llegir despres d'enviar keep alive vins que deixi d'enviar) o -1 si no rep resopsta
	bat_data = Battery_full()
	bat_data.init_cells()

	n = 0
	first_iteration = 1


	while n < iterations:

		if first_iteration:
			can_bus.send(encode_ignition(db, 1))

			msg_received = can_bus.recv(1)

			if msg_received == None:
				can_bus.send(encode_keepalive(db))

				msg_received = can_bus.recv(1)

				if msg_received == None: return -1

			first_iteration = 0 

		else:
			msg_received = can_bus.recv(1)

			if msg_received == None:
				can_bus.send(encode_keepalive(db))
				n + 1

			
		try:
			decoded_frame = db.decode_message(msg_received.arbitration_id, msg_received.data)
		except Exception:
			continue

		msg_id = msg_received.arbitration_id

		if msg_id == get_id_db(db, "VOLTAGE_INFO"):
			bat_info.add_voltage(decoded_frame['Battery_Voltage'])
				
		if msg_id == get_id_db(db, "CURRENT"):
			bat_info.add_current(decoded_frame['Battery_Current'])
	
		if msg_id == get_id_db(db, "TEMPERATURE_INFO_INTERNAL"):
			bat_info.add_temperature(decoded_frame['Temperature_internal_Mean'])
			
		if msg_id == get_id_db(db, "VOLTAGES_CELL"):
			i = decoded_frame['Index_of_cell']

			bat_info.add_cell_voltage(i, decoded_frame['Cell_voltage_at_Index_plus_0'])
			bat_info.add_cell_voltage(i + 1, decoded_frame['Cell_voltage_at_Index_plus_1'])
			bat_info.add_cell_voltage(i + 2, decoded_frame['Cell_voltage_at_Index_plus_2'])

		if msg_id == get_id_db(db, "TEMPERATURE_CELLS"):
			i = decoded_frame['NTC_Index']

			bat_info.add_cell_temperature(i, decoded_frame['Temperature_at_NTC_index_plus_0'])
			bat_info.add_cell_temperature(i + 1, decoded_frame['Temperature_at_NTC_index_plus_1'])
			bat_info.add_cell_temperature(i + 2, decoded_frame['Temperature_at_NTC_index_plus_2'])

		if msg_id == get_id_db(db, "BATTERY_STATE"):
			bat_info.add_soc(decoded_frame['State_of_Charge'])
			bat_info.add_soh(decoded_frame['State_of_Health'])	

	return bat_data



def get_bms_data_test():
	bat_data = Battery_full()

	voltage = []
	current = []
	temperature = []
	soc = []
	soh = []
	cell_voltage = [
		[],
		[],
		[],
		[],
		[],
		[],
		[],
		[],
		[],
		[],
		[],
		[],
		[],
		[],
		[],
		[],
		[],
		[],
		[],
		[],
		[],
		[],
		[],
		[]
	]
	cell_temperature = [
		[],
		[],
		[],
		[]
	]

	for values in voltage:
		bat_data.add_voltage(values)

	for values in current:
		bat_data.add_current(values)

	for values in temperature:
		bat_data.add_temperature(values)

	for values in soc:
		bat_data.add_soc(values)

	for values in soh:
		bat_data.add_soh(values)

	for i in range(24):
		for values in cell_voltage[i]:
			bat_data.add_cell_voltage(i ,values)

	for i in range(4):
		for values in cell_temperature[i]:
			bat_data.add_cell_temperature(i ,values)

	return bat_data