# @author: FuseFinder

import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QInputDialog
from PyQt5.QtCore import QEasingCurve, QTimer
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from sim_results import*

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		loadUi('Interficie1.1.ui', self)

		# Inicializar full screen
		self.showMaximized()

		# Control barra de titulos
		self.bt_close.clicked.connect(lambda: self.close())
		self.bt_max.clicked.connect(self.control_bt_max)
		self.bt_window.clicked.connect(self.control_bt_rest)
		self.bt_min.clicked.connect(self.control_bt_min)
		self.bt_window.hide()

		# Eliminar barra de titulo
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setWindowOpacity(1)

		# SizeGrip
		self.gripSize = 10
		self.grip = QtWidgets.QSizeGrip(self)
		self.grip.resize(self.gripSize, self.gripSize)

		# Mover ventana
		self.frame_superior.mouseMoveEvent = self.move_window

		#Missatges per defecte
		self.label_info1.setText(f"")
		self.label_info2_1.setText(f"")
		self.label_info2_2.setText(f"")
		self.label_info2_3.setText(f"")
		self.label_info3.setText(f"")
		self.label_info4_1.setText(f"")
		self.label_info4_2.setText(f"")
		self.label_info4_3.setText(f"")
		self.label_info5.setText(f"")
		self.label_info6.setText(f"")
		self.label_info7.setText(f"")
		self.label_info8.setText(f"")
		self.label_info9.setText(f"")
		self.label_info10.setText(f"")
		self.label_info11.setText(f"")
		self.label_info12.setText(f"")
		self.label_info13.setText(f"")

		# Cambiar paginas
		self.bt_1.clicked.connect(self.changeToPage1)
		self.bt_2.clicked.connect(self.changeToPage2)
		self.bt_3.clicked.connect(self.changeToPage3)
		self.bt_4.clicked.connect(self.changeToPage4)
		self.bt_5.clicked.connect(self.changeToPage5)
		self.bt_6.clicked.connect(self.changeToPage6)
		self.bt_7.clicked.connect(self.changeToPage7)
		self.bt_8.clicked.connect(self.changeToPage8)
		self.bt_9.clicked.connect(self.changeToPage9)
		self.bt_10.clicked.connect(self.changeToPage10)
		self.bt_11.clicked.connect(self.changeToPage11)
		self.bt_12.clicked.connect(self.changeToPage12)
		self.bt_13.clicked.connect(self.changeToPage13)

		# Mostrar resultados
		self.timer = QTimer(self)
		self.increment = 0
		self.bt_start.clicked.connect(self.show_serial_number_dialog)
		#self.bt_start.clicked.connect(self.run)
		self.bt_stop.clicked.connect(self.stopOperation)
		self.bt_replay.clicked.connect(self.replayOperation)
		
	# Control barra de titulos
	def control_bt_max(self):
		self.showMaximized()
		self.bt_max.hide()
		self.bt_window.show()

	def control_bt_rest(self):
		self.showNormal()
		self.bt_window.hide()
		self.bt_max.show()

	def control_bt_min(self):
		self.showMinimized()

	# SizeGrip
	def resizeEvent(self, event):
		rect = self.rect()
		self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

	# Mover ventana
	def mousePressEvent(self, event):
		self.clickPosition = event.globalPos()

	def move_window(self, event):
		if self.isMaximized() == False:
			if event.buttons() == QtCore.Qt.LeftButton:
				self.move(self.pos() + event.globalPos() - self.clickPosition)
				self.clickPosition = event.globalPos()
				event.accept()
		if event.globalPos().y() <= 10:
			self.showMaximized()
			self.bt_max.hide()
			self.bt_window.show()
		else:
			self.showNormal()
			self.bt_window.hide()
			self.bt_max.show

	# Cambiar paginas

#Lecturas de BMS

	#Tension total
	def changeToPage1(self):
		if self.increment >= 100:
			self.stackedWidget_info.setCurrentIndex(0)
			if data1 == 0:
				self.label_info1.setText(f"Total voltage read is <font color='green'>{data1v:.2f} V</font> which is between the boundaries.")
			elif data1 == 1:
				self.label_info1.setText(f"The total voltage is <font color='red'>{data1v:.2f} V</font> over the maximum. Overvoltage causes excessive current flow that may lead to overheating and lithium plating leading to battery failure.")
			elif data1 == 2:
				self.label_info1.setText(f"The total voltage is <font color='red'>{data1v:.2f} V</font> under the minimum. Undervoltage may be caused from storing the battery for a long time without use leading to a breakdown in the anodes and cathodes.")
			elif data1 == 3:
				self.label_info1.setText(f"The calculated average is within the correct range of values, but there are measurements that are outside of this range. It is recommended to redo the validation.")
			elif data1 == 4:
				self.label_info1.setText(f"The number of outlier measurements is too high, and the usable readings are few. It is recommended to redo the validation.")
			else:
				self.label_info1.setText(f"No valid data input.")

	#Tensiones de celdas
	def changeToPage2(self):
		if self.increment >= 200:
			self.stackedWidget_info.setCurrentIndex(1)
			#Cell 1
			if data2_1 == 0:
				self.label_info2_1.setText(f"Cell 1 voltage is <font color='green'>{data2_1v:.2f} V</font> which are between the boundaries.")
			elif data2_1 == 1:
				self.label_info2_1.setText(f"Cell 1 voltage is <font color='red'>{data2_1v:.2f} V</font> which is over the maximum. Overvoltage causes excessive current flow that may lead to overheating and lithium plating leading to battery failure.")
			elif data2_1 == 2:
				self.label_info2_1.setText(f"Cell 1 voltage is <font color='red'>{data2_1v:.2f} V</font> which is under the minimum.Undervoltage may be caused from storing the battery for a long time without use leading to a breakdown in the anodes and cathodes.")
			elif data2_1 == 3:
				self.label_info2_1.setText(f"The calculated average is within the correct range of values, but there are measurements that are outside of this range. It is recommended to redo the validation.")
			elif data2_1 == 4:
				self.label_info2_1.setText(f"The number of outlier measurements is too high, and the usable readings are few. It is recommended to redo the validation.")
			else:
				self.label_info2_1.setText(f"No valid data input.")

			#Cell 2
			if data2_2 == 0:
				self.label_info2_2.setText(f"Cell 2 voltage is <font color='green'>{data2_2v:.2f} V</font> which are between the boundaries.")
			elif data2_2 == 1:
				self.label_info2_2.setText(f"Cell 2 voltage is <font color='red'>{data2_2v:.2f} V</font> which is over the maximum. Overvoltage causes excessive current flow that may lead to overheating and lithium plating leading to battery failure.")
			elif data2_2 == 2:
				self.label_info2_2.setText(f"Cell 2 voltage is <font color='red'>{data2_2v:.2f} V</font> which is under the minimum.Undervoltage may be caused from storing the battery for a long time without use leading to a breakdown in the anodes and cathodes.")
			elif data2_2 == 3:
				self.label_info2_2.setText(f"The calculated average is within the correct range of values, but there are measurements that are outside of this range. It is recommended to redo the validation.")
			elif data2_2 == 4:
				self.label_info2_2.setText(f"The number of outlier measurements is too high, and the usable readings are few. It is recommended to redo the validation.")
			else:
				self.label_info2_2.setText(f"No valid data input.")

			#Cell 3
			if data2_3 == 0:
				self.label_info2_3.setText(f"Cell 3 voltage is <font color='green'>{data2_3v:.2f} V</font> which are between the boundaries.")
			elif data2_3 == 1:
				self.label_info2_3.setText(f"Cell 3 voltage is <font color='red'>{data2_3v:.2f} V</font> which is over the maximum. Overvoltage causes excessive current flow that may lead to overheating and lithium plating leading to battery failure.")
			elif data2_3 == 2:
				self.label_info2_3.setText(f"Cell 3 voltage is <font color='red'>{data2_3v:.2f} V</font> which is under the minimum.Undervoltage may be caused from storing the battery for a long time without use leading to a breakdown in the anodes and cathodes.")
			elif data2_3 == 3:
				self.label_info2_3.setText(f"The calculated average is within the correct range of values, but there are measurements that are outside of this range. It is recommended to redo the validation.")
			elif data2_3 == 4:
				self.label_info2_3.setText(f"The number of outlier measurements is too high, and the usable readings are few. It is recommended to redo the validation.")
			else:
				self.label_info2_3.setText(f"No valid data input.")

	#Estado de carga
	def changeToPage3(self):
		if self.increment >= 300:
			self.stackedWidget_info.setCurrentIndex(2)
			if data3 == 0:
				self.label_info3.setText(f"No errors")
			elif data3 == 1:
				self.label_info3.setText(f"The SoC percentage value read is under the minimum. Working outside the boundaries will reduce the battery cells life.")
			elif data3 == 2:
				self.label_info3.setText(f"The calculated average is within the correct range of values, but there are measurements that are outside of this range. It is recommended to redo the validation.")
			elif data3 == 3:
				self.label_info3.setText(f"The number of outlier measurements is too high, and the usable readings are few. It is recommended to redo the validation.")
			else:
				self.label_info3.setText(f"No valid data input.")

	#Temperatura de celdas
	def changeToPage4(self):
		if self.increment >= 400:
			self.stackedWidget_info.setCurrentIndex(3)
			#Cell 1
			if data4_1 == 0:
				self.label_info4_1.setText(f"Cell 1 temperature is <font color='green'>{data4_1v:.2f} ºC</font> which are between the boundaries.")
			elif data4_1 == 1:
				self.label_info4_1.setText(f"Cell 1 temperature is <font color='red'>{data4_1v:.2f} ºC</font> which is over the maximum. Overvoltage causes excessive current flow that may lead to overheating and lithium plating leading to battery failure.")
			elif data4_1 == 2:
				self.label_info4_1.setText(f"Cell 1 temperature is <font color='red'>{data4_1v:.2f} ºC</font> which is under the minimum.Undervoltage may be caused from storing the battery for a long time without use leading to a breakdown in the anodes and cathodes.")
			elif data4_1 == 3:
				self.label_info4_1.setText(f"The calculated average is within the correct range of values, but there are measurements that are outside of this range. It is recommended to redo the validation.")
			elif data4_1 == 4:
				self.label_info4_1.setText(f"The number of outlier measurements is too high, and the usable readings are few. It is recommended to redo the validation.")
			else:
				self.label_info4_1.setText(f"No valid data input.")

			#Cell 2
			if data4_2 == 0:
				self.label_info4_2.setText(f"Cell 2 temperature is <font color='green'>{data4_2v:.2f} ºC</font> which are between the boundaries.")
			elif data4_2 == 1:
				self.label_info4_2.setText(f"Cell 2 tempreature is <font color='red'>{data4_2v:.2f} ºC</font> which is over the maximum. Overvoltage causes excessive current flow that may lead to overheating and lithium plating leading to battery failure.")
			elif data4_2 == 2:
				self.label_info4_2.setText(f"Cell 2 tempreature is <font color='red'>{data4_2v:.2f} ºC</font> which is under the minimum.Undervoltage may be caused from storing the battery for a long time without use leading to a breakdown in the anodes and cathodes.")
			elif data4_2 == 3:
				self.label_info4_2.setText(f"The calculated average is within the correct range of values, but there are measurements that are outside of this range. It is recommended to redo the validation.")
			elif data4_2 == 4:
				self.label_info4_2.setText(f"The number of outlier measurements is too high, and the usable readings are few. It is recommended to redo the validation.")
			else:
				self.label_info4_2.setText(f"No valid data input.")

			#Cell 3
			if data4_3 == 0:
				self.label_info4_3.setText(f"Cell 3 temperature is <font color='green'>{data4_3v:.2f} ºC</font> which are between the boundaries.")
			elif data4_3 == 1:
				self.label_info4_3.setText(f"Cell 3 temperature is <font color='red'>{data4_3v:.2f} ºC</font> which is over the maximum. Working over the recommended temperature at the battery leads to the condition known as Arrhenius effect which will drain higher power from the battery. Higher temperature also generates higher currents creating high heat generation.")
			elif data4_3 == 2:
				self.label_info4_3.setText(f"Cell 3 temperature is <font color='red'>{data4_3v:.2f} ºC</font> which is under the minimum. Working under the recommended temperature at the battery may cause a reduction in the current carrying capacity for both the charging and discharging process.")
			elif data4_3 == 3:
				self.label_info4_3.setText(f"The calculated average is within the correct range of values, but there are measurements that are outside of this range. It is recommended to redo the validation.")
			elif data4_3 == 4:
				self.label_info4_3.setText(f"The number of outlier measurements is too high, and the usable readings are few. It is recommended to redo the validation.")
			else:
				self.label_info4_3.setText(f"No valid data input.")

	#Temperatura de placa
	def changeToPage5(self):
		if self.increment >= 500:
			self.stackedWidget_info.setCurrentIndex(4)
			if data5 == 0:
				self.label_info5.setText(f"No error")
			elif data5 == 1:
				self.label_info5.setText(f"The temperature of the board is <font color='red'>{data5v:.2f} ºC</font> which is over the maximum. Working over the recommended temperature on the board may cause: loss of structural integrity, disruption of circuit lines, incompatible rates of material expansion or oxidation. The reason for the overheating may be caused by: component malfunction causing dissipation, through-hole interference, surface-mount device distance, lead-free solder…")
			elif data5 == 2:
				self.label_info5.setText(f"The temperature of the board is <font color='red'>{data5v:.2f} ºC</font> which is under the minimum.")
			elif data5 == 3:
				self.label_info5.setText(f"The calculated average is within the correct range of values, but there are measurements that are outside of this range. It is recommended to redo the validation.")
			elif data5 == 4:
				self.label_info5.setText(f"The number of outlier measurements is too high, and the usable readings are few. It is recommended to redo the validation.")
			else:
				self.label_info5.setText(f"No valid data input.")

	#Corriente bateria
	def changeToPage6(self):
		if self.increment >= 600:
			self.stackedWidget_info.setCurrentIndex(5)
			if data6 == 0:
				self.label_info6.setText(f"Total current read is <font color='green'>{data6v:.2f} A</font> which is between the boundaries.")
			elif data6 == 1:
				self.label_info6.setText(f"Total current read is <font color='green'>{data6v:.2f} A</font> which is not between the boundaries.")
			elif data6 == 3:
				self.label_info6.setText(f"The calculated average is within the correct range of values, but there are measurements that are outside of this range. It is recommended to redo the validation.")
			elif data6 == 4:
				self.label_info6.setText(f"The number of outlier measurements is too high, and the usable readings are few. It is recommended to redo the validation.")
			else:
				self.label_info6.setText(f"No valid data input.")


#Funcionamiento resolver

	#Alimentación 5 VDC
	def changeToPage7(self):
		if self.increment >= 700:
			self.stackedWidget_info.setCurrentIndex(6)
			if data7 == 0:
				self.label_info7.setText(f"No error")
			elif data7 == 1:
				self.label_info7.setText(f"The power supply voltage of the resolver is not the expected voltage.")
			else:
				self.label_info7.setText(f"No valid data input.")
	
	#Sin
	def changeToPage8(self):
		if self.increment >= 800:
			self.stackedWidget_info.setCurrentIndex(7)
			if data8 == 0:
				self.label_info8.setText(f"No error")
			elif data8 == 1:
				self.label_info8.setText(f"The sine wave of the resolver is not working correctly. The common issues to consider include:\n- Electrical connection problems, like loose or damaged wiring or terminals. If all the cables are in good condition, you could try shielding them.\n- Electromagnetic interference or noise in the electrical system.\n- Physical damage to the resolver unit.\n- Calibration issues.\n- Power supply problems.")
			else:
				self.label_info8.setText(f"No valid data input.")
	
	#Cos
	def changeToPage9(self):
		if self.increment >= 900:
			self.stackedWidget_info.setCurrentIndex(8)
			if data9 == 0:
				self.label_info9.setText(f"No error")
			elif data9 == 1:
				self.label_info9.setText(f"The cosine wave of the resolver is not working correctly. The common issues to consider include:\n- Electrical connection problems, like loose or damaged wiring or terminals. If all the cables are in good condition, you could try shielding them.\n- Electromagnetic interference or noise in the electrical system.\n- Physical damage to the resolver unit.\n- Calibration issues.\n- Power supply problems.")
			else:
				self.label_info9.setText(f"No valid data input.")

#Otros

	#Funcionament DC-CD (lectura 12V) (no podem rebre valor)
	def changeToPage10(self):
		if self.increment >= 1000:
			self.stackedWidget_info.setCurrentIndex(9)
			if data10 == 0:
				self.label_info10.setText(f"No error")
			elif data10 == 1:
				self.label_info10.setText(f"The battery voltage is not within the expected range of values, which is between 11V and 16V.")
			else:
				self.label_info10.setText(f"No valid data input.")

	#Comunicación CAN con el INVERSOR
	def changeToPage11(self):
		if self.increment >= 1100:
			self.stackedWidget_info.setCurrentIndex(10)
			if data11 == 0:
				self.label_info11.setText(f"No error.")
			elif data11 == 1:
				self.label_info11.setText(f"Error.")
			else:
				self.label_info11.setText(f"No valid data input.")

	#Funcionamiento Acelerador 12 VDC
	def changeToPage12(self):
		if self.increment >= 1200:
			self.stackedWidget_info.setCurrentIndex(11)
			if data12 == 0:
				self.label_info12.setText(f"No error.")
			elif data12 == 1:
				self.label_info12.setText(f"Error.")
			else:
				self.label_info12.setText(f"No valid data input.")

	#Termistor motor
	def changeToPage13(self):
		if self.increment >= 1300:
			self.stackedWidget_info.setCurrentIndex(12)
			if data13 == 0:
				self.label_info13.setText(f"No error.")
			elif data13 == 1:
				self.label_info13.setText(f"The termistor motor is not working properly. The main problems that can cause this malfunction are:\n- The instantaneous current through the thermistor is too high, and the resistance coil is damaged.\n- The thermistor's resistance wire is insulated and protected, creating a short circuit between the coils.\n- The line voltage is unstable and fluctuating, and the instantaneous voltage exceeds the thermistor's safety rating.")
			else:
				self.label_info13.setText(f"No valid data input.")

	# Mostrar resultados
	def resumeOperation(self):
#Lecturas del BMS
		#Tension total
		if self.increment == 100:
			if data1 == 0:
				self.stackedWidget_1.setCurrentIndex(0)
			elif data1 == 1 or data1 == 2:
				self.stackedWidget_1.setCurrentIndex(2)
			elif data1 == 3 or data1 == 4:
				self.stackedWidget_1.setCurrentIndex(3)
			else:
				self.stackedWidget_1.setCurrentIndex(2)
			self.increment += 5
		
		#Tension de celdas
		elif self.increment == 200:
			if data2_1 == 0 and data2_2 == 0 and data2_3 == 0:
				self.stackedWidget_2.setCurrentIndex(0)
			elif (data2_1 == 1 or data2_1 == 2) or (data2_2 == 1 or data2_2 == 2) or (data2_3 == 1 or data2_3 == 2):
				self.stackedWidget_2.setCurrentIndex(2)
			elif (data2_1 == 3 or data2_1 == 4) or (data2_2 == 3 or data2_2 == 4) or (data2_3 == 3 or data2_3 == 4):
				self.stackedWidget_2.setCurrentIndex(3)
			else:
				self.stackedWidget_2.setCurrentIndex(2)
			self.increment += 5
		
		#Estado de carga
		elif self.increment == 300:
			if data3 == 0:
				self.stackedWidget_3.setCurrentIndex(0)
			elif data3 == 1:
				self.stackedWidget_3.setCurrentIndex(2)
			elif data3 == 2 or data3 == 3:
				self.stackedWidget_3.setCurrentIndex(3)
			else:
				self.stackedWidget_3.setCurrentIndex(2)
			self.increment += 5
		
		#Temperatura de celdas
		elif self.increment == 400:
			if data4_1 == 0 and data4_2 == 0 and data4_3 == 0:
				self.stackedWidget_4.setCurrentIndex(0)
			elif (data4_1 == 1 or data4_1 == 2) or (data4_2 == 1 or data4_2 == 2) or (data4_3 == 1 or data4_3 == 2):
				self.stackedWidget_4.setCurrentIndex(2)
			elif (data4_1 == 3 or data4_1 == 4) or (data4_2 == 3 or data4_2 == 4) or (data4_3 == 3 or data4_3 == 4):
				self.stackedWidget_4.setCurrentIndex(3)
			else:
				self.stackedWidget_4.setCurrentIndex(2)
			self.increment += 5
		
		#Temperatura de placa
		elif self.increment == 500:
			if data5 == 0:
				self.stackedWidget_5.setCurrentIndex(0)
			elif data5 == 1 or data5 == 2:
				self.stackedWidget_5.setCurrentIndex(2)
			elif data5 == 3 or data5 == 4:
				self.stackedWidget_5.setCurrentIndex(3)
			else:
				self.stackedWidget_5.setCurrentIndex(2)
			self.increment += 5
		
		#Corriente total
		elif self.increment == 600:
			if data6 == 0:
				self.stackedWidget_6.setCurrentIndex(0)
			elif data6 == 1:
				self.stackedWidget_6.setCurrentIndex(2)
			elif data6 == 2 or data6 == 3:
				self.stackedWidget_6.setCurrentIndex(3)
			else:
				self.stackedWidget_6.setCurrentIndex(2)
			self.increment += 5

#Funcionamiento resolver
		#Alimentacion 5 VDC
		elif self.increment == 700:
			if data7 == 0:
				self.stackedWidget_7.setCurrentIndex(0)
			elif data7 == 1:
				self.stackedWidget_7.setCurrentIndex(2)
			else:
				self.stackedWidget_6.setCurrentIndex(2)
			self.increment += 5
		
		#Sinus
		elif self.increment == 800:
			if data8 == 0:
				self.stackedWidget_8.setCurrentIndex(0)
			elif data8 == 1:
				self.stackedWidget_8.setCurrentIndex(2)
			else:
				self.stackedWidget_8.setCurrentIndex(2)
			self.increment += 5
		
		#Cosinus
		elif self.increment == 900:
			if data9 == 0:
				self.stackedWidget_9.setCurrentIndex(0)
			elif data9 == 1:
				self.stackedWidget_9.setCurrentIndex(2)
			else:
				self.stackedWidget_9.setCurrentIndex(2)
			self.increment += 5

#Otros
		#Funcionamiento DC-DC (voltage 12 V, no tenemos valor)
		elif self.increment == 1000:
			if data10 == 0:
				self.stackedWidget_10.setCurrentIndex(0)
			elif data10 == 1:
				self.stackedWidget_10.setCurrentIndex(2)
			else:
				self.stackedWidget_10.setCurrentIndex(2)
			self.increment += 5
		
		#Comunicación CAN con el INVERSOR
		elif self.increment == 1100:
			if data11 == 0:
				self.stackedWidget_11.setCurrentIndex(0)
			elif data11 == 1:
				self.stackedWidget_11.setCurrentIndex(2)
			else:
				self.stackedWidget_11.setCurrentIndex(2)
			self.increment += 5
		
		#Funcionamiento Acelerador 12V
		elif self.increment == 1200:
			if data12 == 0:
				self.stackedWidget_12.setCurrentIndex(0)
			elif data12 == 1:
				self.stackedWidget_12.setCurrentIndex(2)
			else:
				self.stackedWidget_12.setCurrentIndex(2)
			self.increment += 5
		
		#Termistor motor
		elif self.increment == 1300:
			if data13 == 0:
				self.stackedWidget_13.setCurrentIndex(0)
			elif data13 == 1:
				self.stackedWidget_13.setCurrentIndex(2)
			else:
				self.stackedWidget_13.setCurrentIndex(2)
			self.increment += 5
			self.timer.stop()
		
		else:
			self.increment += 5
			self.progressBar_1.setValue(self.increment)
			self.progressBar_2.setValue(self.increment-100)
			self.progressBar_3.setValue(self.increment-200)
			self.progressBar_4.setValue(self.increment-300)
			self.progressBar_5.setValue(self.increment-400)
			self.progressBar_6.setValue(self.increment-500)
			self.progressBar_7.setValue(self.increment-600)
			self.progressBar_8.setValue(self.increment-700)
			self.progressBar_9.setValue(self.increment-800)
			self.progressBar_10.setValue(self.increment-900)
			self.progressBar_11.setValue(self.increment-1000)
			self.progressBar_12.setValue(self.increment-1100)
			self.progressBar_13.setValue(self.increment-1200)

	def startOperation(self):
		'''
		Començarem start operation quan cliquem la tecla d'start
		La variable par és d'un altre codi, on quan sigui 1 es començarà a executar la interfície
		'''
		global par
		if par == 1:
			self.timer.timeout.connect(self.resumeOperation)
			self.timer.start(100)
		else:
			par = 0
		#self.timer.timeout.connect(self.resumeOperation)
		#self.timer.start(100)

	def stopOperation(self):
		self.timer.stop()

	def replayOperation(self):
		self.timer.stop()
		self.increment = 0
		self.progressBar_1.setValue(0)
		self.progressBar_2.setValue(0)
		self.progressBar_3.setValue(0)
		self.progressBar_4.setValue(0)
		self.progressBar_5.setValue(0)
		self.progressBar_6.setValue(0)
		self.progressBar_7.setValue(0)
		self.progressBar_8.setValue(0)
		self.progressBar_9.setValue(0)
		self.progressBar_10.setValue(0)
		self.progressBar_11.setValue(0)
		self.progressBar_12.setValue(0)
		self.progressBar_13.setValue(0)
		
		self.stackedWidget_1.setCurrentIndex(1)
		self.stackedWidget_2.setCurrentIndex(1)
		self.stackedWidget_3.setCurrentIndex(1)
		self.stackedWidget_4.setCurrentIndex(1)
		self.stackedWidget_5.setCurrentIndex(1)
		self.stackedWidget_6.setCurrentIndex(1)
		self.stackedWidget_7.setCurrentIndex(1)
		self.stackedWidget_8.setCurrentIndex(1)
		self.stackedWidget_9.setCurrentIndex(1)
		self.stackedWidget_10.setCurrentIndex(1)
		self.stackedWidget_11.setCurrentIndex(1)
		self.stackedWidget_12.setCurrentIndex(1)
		self.stackedWidget_13.setCurrentIndex(1)

		#Missatges per defecte
		self.label_info1.setText(f"")
		self.label_info2_1.setText(f"")
		self.label_info2_2.setText(f"")
		self.label_info2_3.setText(f"")
		self.label_info3.setText(f"")
		self.label_info4_1.setText(f"")
		self.label_info4_2.setText(f"")
		self.label_info4_3.setText(f"")
		self.label_info5.setText(f"")
		self.label_info6.setText(f"")
		self.label_info7.setText(f"")
		self.label_info8.setText(f"")
		self.label_info9.setText(f"")
		self.label_info10.setText(f"")
		self.label_info11.setText(f"")
		self.label_info12.setText(f"")
		self.label_info13.setText(f"")

	def show_serial_number_dialog(self):

		serial_number, ok = QInputDialog.getText(self, 'Introducir Número de Serie', 'Por favor, introduce el número de serie:')
        
		if ok:
			# Guardar el número de serie en un archivo
			with open('numeros_de_serie.txt', 'a') as file:
				file.write(serial_number)
			self.startOperation()

'''
	start = 0

	def run(self, start):
		if start == 1:
			print(f"start = {start}")
			self.startOperation()
		elif start == 0:
			print(f"hola start = {start}")
			start = 1
			return start
		else:
			print(f"no funciona = {start}")
'''
			
if __name__ == "__main__":
	app = QApplication(sys.argv)
	my_app = MainWindow()
	my_app.show()
	sys.exit(app.exec_())