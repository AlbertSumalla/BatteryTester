import os
import can
import cantools
import random
import string
from config_can import *

#############################################################################################################

def get_bms_data(can_bus,db,iterations): #retorna el data set amb el nombre de dades corresponent a les iteracions (1 iteracions = llegir despres d'enviar keep alive vins que deixi d'enviar) o -1 si no rep resopsta
	bat_info = Battery_full()
	bat_info.init_cells()

	n = 0
	e = 0
	
	can_bus.send(encode_keepalive(db))
	
	while n < iterations:	

		msg_received = can_bus.recv(0.5)

		
		if msg_received == None:
			
			if e == 1: return -1
			
			can_bus.send(encode_keepalive(db))
			n = n + 1
			e = 1

		try:
			decoded_frame = db.decode_message(msg_received.arbitration_id, msg_received.data)
		except Exception:
			continue

		e = 0
		
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
			
			if i == 0:
				bat_info.add_cell_temperature(i, decoded_frame['Temperature_at_NTC_index_plus_0'])
				bat_info.add_cell_temperature(i + 1, decoded_frame['Temperature_at_NTC_index_plus_1'])
				bat_info.add_cell_temperature(i + 2, decoded_frame['Temperature_at_NTC_index_plus_2'])
			else:
				bat_info.add_cell_temperature(3, decoded_frame['Temperature_at_NTC_index_plus_0'])

		if msg_id == get_id_db(db, "BATTERY_STATE"):
			bat_info.add_soc(decoded_frame['State_of_Charge'])
			bat_info.add_soh(decoded_frame['State_of_Health'])	

		if msg_id == get_id_db(db, "BATTERY_SERIAL_NUMBER"):
			i = decoded_frame['Sequence_number']

			if i < 5:
				bat_info.set_serial(i, decoded_frame['Char_at_seq_number_x_7_plus_0'])
				bat_info.set_serial(i + 1, decoded_frame['Char_at_seq_number_x_7_plus_1'])
				bat_info.set_serial(i + 2, decoded_frame['Char_at_seq_number_x_7_plus_2'])
				bat_info.set_serial(i + 3, decoded_frame['Char_at_seq_number_x_7_plus_3'])
				bat_info.set_serial(i + 4, decoded_frame['Char_at_seq_number_x_7_plus_4'])
				bat_info.set_serial(i + 5, decoded_frame['Char_at_seq_number_x_7_plus_5'])
				bat_info.set_serial(i + 6, decoded_frame['Char_at_seq_number_x_7_plus_6'])
			else:
				bat_info.set_serial(28, decoded_frame['Char_at_seq_number_x_7_plus_0'])
				bat_info.set_serial(29, decoded_frame['Char_at_seq_number_x_7_plus_1'])
				bat_info.set_serial(30, decoded_frame['Char_at_seq_number_x_7_plus_2'])
				bat_info.set_serial(31, decoded_frame['Char_at_seq_number_x_7_plus_3'])

	return bat_info

def get_inv_errors(can_bus,db):

	can_bus.send(encode_ignition(db, 0))

	can_bus.send(encode_ignition(db, 1))

	error_list = []

	msg_received = can_bus.recv(1)

	msg_received = can_bus.recv(1)
	
	while msg_received != None: 
		
		if msg_received.arbitration_id == 0x0081:
			
			bytes_data = msg_received.data
			
			error_list.append((bytes_data[4] << 8) + bytes_data[3])
			
		msg_received = can_bus.recv(1)
		
	return error_list
		

	

def get_bms_data_test():
	bat_data = Battery_full()
	bat_data.init_cells()
	random_serial = ''.join(random.choices(string.ascii_uppercase + string.digits,k = 32))
	
	voltage = [92.862,95.862,94.86,96.43546,95.562,95.738]
	current = [20,30,20.02,20,30,40,35,30.02,20,20,20,30,20,30,20,100,30,105,50,50.01,50]
	temperature = [28.3,28.3,28.3,28.3,28.3,28.3]
	soc = [68.51,68.51,68.51,68.51]
	soh = [99.9,99.8,99.88,99.89]
	cell_voltage = [
		[0, 3.911, 3.91, 3.91, 3.91, 3.911, 3.901, 3.911],
		[0, 3.91, 3.91, 3.91, 3.91, 3.9, 3.9, 3.911, 3.91],
		[0, 3.91, 3.91, 3.91, 3.91, 3.91, 3.9, 3.911, 3.911],
		[0, 3.91, 3.91, 3.91, 3.91, 3.9, 3.9, 3.911, 3.911],
		[0, 3.9, 3.91, 3.91, 3.91, 3.9, 3.9, 3.911, 3.911],
		[2.91, 2.91, 2.91, 2.91, 2.91, 2.9, 2.9, 2.911],
		[3.91, 3.91, 3.91, 3.91, 3.91, 3.9, 3.9, 3.91],
		[3.91, 3.91, 3.91, 3.91, 3.91, 3.9, 3.91, 3.91],
		[3.91, 3.91, 3.91, 3.91, 3.91, 3.9, 3.91, 3.911],
		[3.91, 3.91, 3.91, 3.91, 3.91, 3.9, 3.9, 3.911],
		[3.91, 3.91, 3.9, 3.91, 3.91, 3.9, 3.9, 3.91],
		[3.91, 3.91, 3.81, 3.91, 3.91, 3.9, 3.9, 3.91],
		[3.91, 3.91, 3.91, 0, 3.91, 3.9, 3.9, 3.91],
		[3.91, 3.91, 3.91, 0, 3.91, 3.9, 3.9, 3.91],
		[3.91, 3.91, 3.91, 3.91, 3.91, 3.9, 3.9, 3.91],
		[3.91, 3.911, 3.91, 3.91, 3.91, 3.9, 3.9, 3.91],
		[3.91, 3.91, 3.91, 3.91, 3.91, 3.9, 3.9, 3.911],
		[3.91, 3.91, 3.91, 3.91, 3.91, 3.9, 3.9, 3.911],
		[3.91, 3.911, 3.91, 3.91, 3.91, 3.9, 3.9, 3.91],
		[3.91, 3.9, 3.91, 3.91, 3.91, 3.9, 3.9, 3.911],
		[3.91, 3.91, 3.91, 3.911, 3.91, 3.9, 3.9, 3.911],
		[3.91, 3.91, 3.91, 3.91, 3.911, 3.9, 3.9, 3.911],
		[3.91, 3.91, 3.91, 3.91, 3.91, 3.9, 3.9, 3.911],
		[3.91, 3.91, 3.91, 3.91, 3.91, 3.9, 3.9, 3.911],

	]
	cell_temperature = [
		[31.1,31.11,31,30.11],
		[31.1,31.11,31,30.2],
		[31.1,31.1,31,30.2],
		[31.1,31.12,31,30.1]
	]

	bat_data.set_serial(0, random_serial)

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

def get_inv_errors_test():
	return [0x4dc3, 0x4d5d]
