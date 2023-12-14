# @author: FuseFinder

import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QInputDialog
from PyQt5.QtCore import QEasingCurve, QTimer
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
#from sim_results import*

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
		self.bt_max.hide()

		# Eliminar barra de titulo
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setWindowOpacity(1)

		# SizeGrip
		# self.gripSize = 10
		# self.grip = QtWidgets.QSizeGrip(self)
		# self.grip.resize(self.gripSize, self.gripSize)

		# Mover ventana
		self.frame_superior.mouseMoveEvent = self.move_window

		#Missatges per defecte
		self.label_info1.setText(f"")
		self.label_info2.setText(f"")
		self.label_info3.setText(f"")
		self.label_info4_1.setText(f"")
		self.label_info4_2.setText(f"")
		self.label_info4_3.setText(f"")
		self.label_info4_4.setText(f"")
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
		self.timer.timeout.connect(self.resumeOperation)
		self.increment = 0
		self.bt_start.clicked.connect(self.startOperation)
		#self.bt_start.clicked.connect(self.run)
		self.bt_stop.clicked.connect(self.stopOperation)
		self.bt_replay.clicked.connect(self.replayOperation)
		#Valor resultado general de voltaje de celdas
		self.data2_tot = 0
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
	# def resizeEvent(self, event):
	# 	rect = self.rect()
	# 	self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

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
			if self.data1 == 0:
				self.label_info1.setText(f"<font color='#80FF80'><b>No error.<b></font> Total voltage read is <font color='#80FF80'><b>{self.data1v:.2f}<b> V</font> which is between the boundaries.")
			elif self.data1 == 1:
				self.label_info1.setText(f"<font color='red'><b>Error.<b></font> The total voltage is <font color='red'><b>{self.data1v:.2f} V<b></font> over the maximum. Overvoltage causes excessive current flow that may lead to overheating and lithium plating leading to battery failure.")
			elif self.data1 == 2:
				self.label_info1.setText(f"<font color='red'><b>Error.<b></font> The total voltage is <font color='red'><b>{self.data1v:.2f} V<b></font> under the minimum. Undervoltage may be caused from storing the battery for a long time without use leading to a breakdown in the anodes and cathodes.")
			elif self.data1 == 3:
				self.label_info1.setText(f"<font color='yellow'><b>Warning.</b></font> The calculated average is within the correct range of values, <font color='yellow'><b>{self.data1v:.2f} V</b></font>. However, there are measurements that are outside of this range. It is recommended to redo the validation.")
			elif self.data1 == 4:
				self.label_info1.setText(f"<font color='yellow'><b>Warning.<b></font> The number of outlier measurements is too high, and the usable readings are few. The value is <font color='yellow'><b>{self.data1v:.2f} V<b></font>. It is recommended to redo the validation.")
			else:
				self.label_info1.setText(f"<font color='red'><b>Error.<b></font> No valid data input.")
		self.label_info1.setWordWrap(True)
	#Tensiones de celdas
	def changeToPage2(self):
		if self.increment >= 200:
			self.stackedWidget_info.setCurrentIndex(1)
			if self.data2_tot == 0:
				self.label_info2.setText(f"<font color='#80FF80'><b>No error.<b></font> All cell's voltages between the boundaries.")
			elif self.data2_tot == 1:
				self.label_info2.setText(f"<font color='red'><b>Error.<b></font> All cell's voltages are not between the boundaries.")
			elif self.data2_tot == 3:
				self.label_info2.setText(f"<font color='yellow'><b>Warning.<b></font> At least one cell's average voltage is within the coorect range values, but there are measurements that are outside of this range.")
			elif self.data2_tot == 4:
				self.label_info2.setText(f"<font color='yellow'><b>Warning.<b></font> At least one cell's usable readings are few. It is recommended to redo the validation.")
			elif self.data2_tot == 5:
				self.label_info2.setText(f"<font color='yellow'><b>Warning.<b></font> At least one cell's average voltage is within the coorect range values, but there are measurements that are outside of this range. At least one cell's usable readings are few. It is recommended to redo the validation.")
			elif self.data2_tot == 2:
				self.label_info2.setText(f"<font color='red'><b>Error.<b></font> No valid data input for all cell's voltages.")
			self.label_info2.setWordWrap(True)
			#Cell 1
			if self.data2_1 == 0:
				self.label_c1.setText(f"Celda 1: <font color='#80FF80'><b>{self.data2_1v:.2f} V<b></font>")
			elif self.data2_1 == 1:
				self.label_c1.setText(f"Celda 1: <font color='red'><b>{self.data2_1v:.2f} V<b></font>")
			elif self.data2_1 == 2:
				self.label_c1.setText(f"Celda 1: <font color='red'><b>{self.data2_1v:.2f} V<b></font>")
			elif self.data2_1 == 3:
				self.label_c1.setText(f"Celda 1: <font color='yellow'><b>{self.data2_1v:.2f} V<b></font>")
			elif self.data2_1 == 4:
				self.label_c1.setText(f"Celda 1: <font color='yellow'><b>{self.data2_1v:.2f} V<b></font>")
			else:
				self.label_c1.setText(f"Celda 1: <font color='red'><b>{self.data2_1v:.2f} V<b></font>")
			self.label_c1.setWordWrap(True)
			#Cell 2
			if self.data2_2 == 0:
				self.label_c2.setText(f"Celda 2: <font color='#80FF80'><b>{self.data2_2v:.2f} V<b></font>")
			elif self.data2_2 == 1:
				self.label_c2.setText(f"Celda 2: <font color='red'><b>{self.data2_2v:.2f} V<b></font>")
			elif self.data2_2 == 2:
				self.label_c2.setText(f"Celda 2: <font color='red'><b>{self.data2_2v:.2f} V<b></font>")
			elif self.data2_2 == 3:
				self.label_c2.setText(f"Celda 2: <font color='yellow'><b>{self.data2_2v:.2f} V<b></font>")
			elif self.data2_2 == 4:
				self.label_c2.setText(f"Celda 2: <font color='yellow'><b>{self.data2_2v:.2f} V<b></font>")
			else:
				self.label_c1.setText(f"Celda 2: <font color='red'><b>{self.data2_2v:.2f} V<b></font>")
			self.label_c2.setWordWrap(True)
			#Cell 3
			if self.data2_3 == 0:
				self.label_c3.setText(f"Celda 3: <font color='#80FF80'><b>{self.data2_3v:.2f} V<b></font>")
			elif self.data2_3 == 1:
				self.label_c3.setText(f"Celda 3: <font color='red'><b>{self.data2_3v:.2f} V<b></font>")
			elif self.data2_3 == 2:
				self.label_c3.setText(f"Celda 3: <font color='red'><b>{self.data2_3v:.2f} V<b></font>")
			elif self.data2_3 == 3:
				self.label_c3.setText(f"Celda 3: <font color='yellow'><b>{self.data2_3v:.2f} V<b></font>")
			elif self.data2_3 == 4:
				self.label_c3.setText(f"Celda 3: <font color='yellow'><b>{self.data2_3v:.2f} V<b></font>")
			else:
				self.label_c3.setText(f"Celda 3: <font color='red'><b>{self.data2_3v:.2f} V<b></font>")
			self.label_c3.setWordWrap(True)
			#Cell 4
			if self.data2_4 == 0:
				self.label_c4.setText(f"Celda 4: <font color='#80FF80'><b>{self.data2_4v:.2f} V<b></font>")
			elif self.data2_4 == 1:
				self.label_c4.setText(f"Celda 4: <font color='red'><b>{self.data2_4v:.2f} V<b></font>")
			elif self.data2_4 == 2:
				self.label_c4.setText(f"Celda 4: <font color='red'><b>{self.data2_4v:.2f} V<b></font>")
			elif self.data2_4 == 3:
				self.label_c4.setText(f"Celda 4: <font color='yellow'><b>{self.data2_4v:.2f} V<b></font>")
			elif self.data2_4 == 4:
				self.label_c4.setText(f"Celda 4: <font color='yellow'><b>{self.data2_4v:.2f} V<b></font>")
			else:
				self.label_c4.setText(f"Celda 4: <font color='red'><b>{self.data2_4v:.2f} V<b></font>")
			self.label_c4.setWordWrap(True)
			#Cell 5
			if self.data2_5 == 0:
				self.label_c5.setText(f"Celda 5: <font color='#80FF80'><b>{self.data2_5v:.2f} V<b></font>")
			elif self.data2_5 == 1:
				self.label_c5.setText(f"Celda 5: <font color='red'><b>{self.data2_5v:.2f} V<b></font>")
			elif self.data2_5 == 2:
				self.label_c5.setText(f"Celda 5: <font color='red'><b>{self.data2_5v:.2f} V<b></font>")
			elif self.data2_5 == 3:
				self.label_c5.setText(f"Celda 5: <font color='yellow'><b>{self.data2_5v:.2f} V<b></font>")
			elif self.data2_5 == 4:
				self.label_c5.setText(f"Celda 5: <font color='yellow'><b>{self.data2_5v:.2f} V<b></font>")
			else:
				self.label_c5.setText(f"Celda 5: <font color='red'><b>{self.data2_5v:.2f} V<b></font>")
			self.label_c5.setWordWrap(True)
			#Cell 6
			if self.data2_6 == 0:
				self.label_c6.setText(f"Celda 6: <font color='#80FF80'><b>{self.data2_6v:.2f} V<b></font>")
			elif self.data2_6 == 1:
				self.label_c6.setText(f"Celda 6: <font color='red'><b>{self.data2_6v:.2f} V<b></font>")
			elif self.data2_6 == 2:
				self.label_c6.setText(f"Celda 6: <font color='red'><b>{self.data2_6v:.2f} V<b></font>")
			elif self.data2_6 == 3:
				self.label_c6.setText(f"Celda 6: <font color='yellow'><b>{self.data2_6v:.2f} V<b></font>")
			elif self.data2_6 == 4:
				self.label_c6.setText(f"Celda 6: <font color='yellow'><b>{self.data2_6v:.2f} V<b></font>")
			else:
				self.label_c6.setText(f"Celda 6: <font color='red'><b>{self.data2_6v:.2f} V<b></font>")
			self.label_c6.setWordWrap(True)
			#Cell 7
			if self.data2_7 == 0:
				self.label_c7.setText(f"Celda 7: <font color='#80FF80'><b>{self.data2_7v:.2f} V<b></font>")
			elif self.data2_7 == 1:
				self.label_c7.setText(f"Celda 7: <font color='red'><b>{self.data2_7v:.2f} V<b></font>")
			elif self.data2_7 == 2:
				self.label_c7.setText(f"Celda 7: <font color='red'><b>{self.data2_7v:.2f} V<b></font>")
			elif self.data2_7 == 3:
				self.label_c7.setText(f"Celda 7: <font color='yellow'><b>{self.data2_7v:.2f} V<b></font>")
			elif self.data2_7 == 4:
				self.label_c7.setText(f"Celda 7: <font color='yellow'><b>{self.data2_7v:.2f} V<b></font>")
			else:
				self.label_c7.setText(f"Celda 7: <font color='red'><b>{self.data2_7v:.2f} V<b></font>")
			self.label_c7.setWordWrap(True)
			#Cell 8
			if self.data2_8 == 0:
				self.label_c8.setText(f"Celda 8: <font color='#80FF80'><b>{self.data2_8v:.2f} V<b></font>")
			elif self.data2_8 == 1:
				self.label_c8.setText(f"Celda 8: <font color='red'><b>{self.data2_8v:.2f} V<b></font>")
			elif self.data2_8 == 2:
				self.label_c8.setText(f"Celda 8: <font color='red'><b>{self.data2_8v:.2f} V<b></font>")
			elif self.data2_8 == 3:
				self.label_c8.setText(f"Celda 8: <font color='yellow'><b>{self.data2_8v:.2f} V<b></font>")
			elif self.data2_8 == 4:
				self.label_c8.setText(f"Celda 8: <font color='yellow'><b>{self.data2_8v:.2f} V<b></font>")
			else:
				self.label_c8.setText(f"Celda 8: <font color='red'><b>{self.data2_8v:.2f} V<b></font>")
			self.label_c8.setWordWrap(True)
			#Cell 9
			if self.data2_9 == 0:
				self.label_c9.setText(f"Celda 9: <font color='#80FF80'><b>{self.data2_9v:.2f} V<b></font>")
			elif self.data2_9 == 1:
				self.label_c9.setText(f"Celda 9: <font color='red'><b>{self.data2_9v:.2f} V<b></font>")
			elif self.data2_9 == 2:
				self.label_c9.setText(f"Celda 9: <font color='red'><b>{self.data2_9v:.2f} V<b></font>")
			elif self.data2_9 == 3:
				self.label_c9.setText(f"Celda 9: <font color='yellow'><b>{self.data2_9v:.2f} V<b></font>")
			elif self.data2_9 == 4:
				self.label_c9.setText(f"Celda 9: <font color='yellow'><b>{self.data2_9v:.2f} V<b></font>")
			else:
				self.label_c9.setText(f"Celda 9: <font color='red'><b>{self.data2_9v:.2f} V<b></font>")
			self.label_c9.setWordWrap(True)
			#Cell 10
			if self.data2_10 == 0:
				self.label_c10.setText(f"Celda 10: <font color='#80FF80'><b>{self.data2_10v:.2f} V<b></font>")
			elif self.data2_10 == 1:
				self.label_c10.setText(f"Celda 10: <font color='red'><b>{self.data2_10v:.2f} V<b></font>")
			elif self.data2_10 == 2:
				self.label_c10.setText(f"Celda 10: <font color='red'><b>{self.data2_10v:.2f} V<b></font>")
			elif self.data2_10 == 3:
				self.label_c10.setText(f"Celda 10: <font color='yellow'><b>{self.data2_10v:.2f} V<b></font>")
			elif self.data2_10 == 4:
				self.label_c10.setText(f"Celda 10: <font color='yellow'><b>{self.data2_10v:.2f} V<b></font>")
			else:
				self.label_c10.setText(f"Celda 10: <font color='red'><b>{self.data2_10v:.2f} V<b></font>")
			self.label_c10.setWordWrap(True)
			#Cell 11
			if self.data2_11 == 0:
				self.label_c11.setText(f"Celda 11: <font color='#80FF80'><b>{self.data2_11v:.2f} V<b></font>")
			elif self.data2_11 == 1:
				self.label_c11.setText(f"Celda 11: <font color='red'><b>{self.data2_11v:.2f} V<b></font>")
			elif self.data2_11 == 2:
				self.label_c11.setText(f"Celda 11: <font color='red'><b>{self.data2_11v:.2f} V<b></font>")
			elif self.data2_11 == 3:
				self.label_c11.setText(f"Celda 11: <font color='yellow'><b>{self.data2_11v:.2f} V<b></font>")
			elif self.data2_11 == 4:
				self.label_c11.setText(f"Celda 11: <font color='yellow'><b>{self.data2_11v:.2f} V<b></font>")
			else:
				self.label_c11.setText(f"Celda 11: <font color='red'><b>{self.data2_11v:.2f} V<b></font>")
			self.label_c11.setWordWrap(True)
			#Cell 12
			if self.data2_12 == 0:
				self.label_c12.setText(f"Celda 12: <font color='#80FF80'><b>{self.data2_12v:.2f} V<b></font>")
			elif self.data2_12 == 1:
				self.label_c12.setText(f"Celda 12: <font color='red'><b>{self.data2_12v:.2f} V<b></font>")
			elif self.data2_12 == 2:
				self.label_c12.setText(f"Celda 12: <font color='red'><b>{self.data2_12v:.2f} V<b></font>")
			elif self.data2_12 == 3:
				self.label_c12.setText(f"Celda 12: <font color='yellow'><b>{self.data2_12v:.2f} V<b></font>")
			elif self.data2_12 == 4:
				self.label_c12.setText(f"Celda 12: <font color='yellow'><b>{self.data2_12v:.2f} V<b></font>")
			else:
				self.label_c12.setText(f"Celda 12: <font color='red'><b>{self.data2_12v:.2f} V<b></font>")
			self.label_c12.setWordWrap(True)
			#Cell 13
			if self.data2_13 == 0:
				self.label_c13.setText(f"Celda 13: <font color='#80FF80'><b>{self.data2_13v:.2f} V<b></font>")
			elif self.data2_13 == 1:
				self.label_c13.setText(f"Celda 13: <font color='red'><b>{self.data2_13v:.2f} V<b></font>")
			elif self.data2_13 == 2:
				self.label_c13.setText(f"Celda 13: <font color='red'><b>{self.data2_13v:.2f} V<b></font>")
			elif self.data2_13 == 3:
				self.label_c13.setText(f"Celda 13: <font color='yellow'><b>{self.data2_13v:.2f} V<b></font>")
			elif self.data2_13 == 4:
				self.label_c13.setText(f"Celda 13: <font color='yellow'><b>{self.data2_13v:.2f} V<b></font>")
			else:
				self.label_c13.setText(f"Celda 13: <font color='red'><b>{self.data2_13v:.2f} V<b></font>")
			self.label_c13.setWordWrap(True)
			#Cell 14
			if self.data2_14 == 0:
				self.label_c14.setText(f"Celda 14: <font color='#80FF80'><b>{self.data2_14v:.2f} V<b></font>")
			elif self.data2_14 == 1:
				self.label_c14.setText(f"Celda 14: <font color='red'><b>{self.data2_14v:.2f} V<b></font>")
			elif self.data2_14 == 2:
				self.label_c14.setText(f"Celda 14: <font color='red'><b>{self.data2_14v:.2f} V<b></font>")
			elif self.data2_14 == 3:
				self.label_c14.setText(f"Celda 14: <font color='yellow'><b>{self.data2_14v:.2f} V<b></font>")
			elif self.data2_14 == 4:
				self.label_c14.setText(f"Celda 14: <font color='yellow'><b>{self.data2_14v:.2f} V<b></font>")
			else:
				self.label_c14.setText(f"Celda 14: <font color='red'><b>{self.data2_14v:.2f} V<b></font>")
			self.label_c14.setWordWrap(True)
			#Cell 15
			if self.data2_15 == 0:
				self.label_c15.setText(f"Celda 15: <font color='#80FF80'><b>{self.data2_15v:.2f} V<b></font>")
			elif self.data2_15 == 1:
				self.label_c15.setText(f"Celda 15: <font color='red'><b>{self.data2_15v:.2f} V<b></font>")
			elif self.data2_15 == 2:
				self.label_c15.setText(f"Celda 15: <font color='red'><b>{self.data2_15v:.2f} V<b></font>")
			elif self.data2_15 == 3:
				self.label_c15.setText(f"Celda 15: <font color='yellow'><b>{self.data2_15v:.2f} V<b></font>")
			elif self.data2_15 == 4:
				self.label_c15.setText(f"Celda 15: <font color='yellow'><b>{self.data2_15v:.2f} V<b></font>")
			else:
				self.label_c15.setText(f"Celda 15: <font color='red'><b>{self.data2_15v:.2f} V<b></font>")
			self.label_c15.setWordWrap(True)
			#Cell 16
			if self.data2_16 == 0:
				self.label_c16.setText(f"Celda 16: <font color='#80FF80'><b>{self.data2_16v:.2f} V<b></font>")
			elif self.data2_16 == 1:
				self.label_c16.setText(f"Celda 16: <font color='red'><b>{self.data2_16v:.2f} V<b></font>")
			elif self.data2_16 == 2:
				self.label_c16.setText(f"Celda 16: <font color='red'><b>{self.data2_16v:.2f} V<b></font>")
			elif self.data2_16 == 3:
				self.label_c16.setText(f"Celda 16: <font color='yellow'><b>{self.data2_16v:.2f} V<b></font>")
			elif self.data2_16 == 4:
				self.label_c16.setText(f"Celda 16: <font color='yellow'><b>{self.data2_16v:.2f} V<b></font>")
			else:
				self.label_c16.setText(f"Celda 16: <font color='red'><b>{self.data2_16v:.2f} V<b></font>")
			self.label_c16.setWordWrap(True)
			#Cell 17
			if self.data2_17 == 0:
				self.label_c17.setText(f"Celda 17: <font color='#80FF80'><b>{self.data2_17v:.2f} V<b></font>")
			elif self.data2_17 == 1:
				self.label_c17.setText(f"Celda 17: <font color='red'><b>{self.data2_17v:.2f} V<b></font>")
			elif self.data2_17 == 2:
				self.label_c17.setText(f"Celda 17: <font color='red'><b>{self.data2_17v:.2f} V<b></font>")
			elif self.data2_17 == 3:
				self.label_c17.setText(f"Celda 17: <font color='yellow'><b>{self.data2_17v:.2f} V<b></font>")
			elif self.data2_17 == 4:
				self.label_c17.setText(f"Celda 17: <font color='yellow'><b>{self.data2_17v:.2f} V<b></font>")
			else:
				self.label_c17.setText(f"Celda 17: <font color='red'><b>{self.data2_17v:.2f} V<b></font>")
			self.label_c17.setWordWrap(True)
			#Cell 18
			if self.data2_18 == 0:
				self.label_c18.setText(f"Celda 18: <font color='#80FF80'><b>{self.data2_18v:.2f} V<b></font>")
			elif self.data2_18 == 1:
				self.label_c18.setText(f"Celda 18: <font color='red'><b>{self.data2_18v:.2f} V<b></font>")
			elif self.data2_18 == 2:
				self.label_c18.setText(f"Celda 18: <font color='red'><b>{self.data2_18v:.2f} V<b></font>")
			elif self.data2_18 == 3:
				self.label_c18.setText(f"Celda 18: <font color='yellow'><b>{self.data2_18v:.2f} V<b></font>")
			elif self.data2_18 == 4:
				self.label_c18.setText(f"Celda 18: <font color='yellow'><b>{self.data2_18v:.2f} V<b></font>")
			else:
				self.label_c18.setText(f"Celda 18: <font color='red'><b>{self.data2_18v:.2f} V<b></font>")
			self.label_c18.setWordWrap(True)
			#Cell 19
			if self.data2_19 == 0:
				self.label_c19.setText(f"Celda 19: <font color='#80FF80'><b>{self.data2_19v:.2f} V<b></font>")
			elif self.data2_19 == 1:
				self.label_c19.setText(f"Celda 19: <font color='red'><b>{self.data2_19v:.2f} V<b></font>")
			elif self.data2_19 == 2:
				self.label_c19.setText(f"Celda 19: <font color='red'><b>{self.data2_19v:.2f} V<b></font>")
			elif self.data2_19 == 3:
				self.label_c19.setText(f"Celda 19: <font color='yellow'><b>{self.data2_19v:.2f} V<b></font>")
			elif self.data2_19 == 4:
				self.label_c19.setText(f"Celda 19: <font color='yellow'><b>{self.data2_19v:.2f} V<b></font>")
			else:
				self.label_c19.setText(f"Celda 19: <font color='red'><b>{self.data2_19v:.2f} V<b></font>")
			self.label_c19.setWordWrap(True)
			#Cell 20
			if self.data2_20 == 0:
				self.label_c20.setText(f"Celda 20: <font color='#80FF80'><b>{self.data2_20v:.2f} V<b></font>")
			elif self.data2_20 == 1:
				self.label_c20.setText(f"Celda 20: <font color='red'><b>{self.data2_20v:.2f} V<b></font>")
			elif self.data2_20 == 2:
				self.label_c20.setText(f"Celda 20: <font color='red'><b>{self.data2_20v:.2f} V<b></font>")
			elif self.data2_20 == 3:
				self.label_c20.setText(f"Celda 20: <font color='yellow'><b>{self.data2_20v:.2f} V<b></font>")
			elif self.data2_20 == 4:
				self.label_c20.setText(f"Celda 20: <font color='yellow'><b>{self.data2_20v:.2f} V<b></font>")
			else:
				self.label_c20.setText(f"Celda 20: <font color='red'><b>{self.data2_20v:.2f} V<b></font>")
			self.label_c20.setWordWrap(True)
			#Cell 21
			if self.data2_21 == 0:
				self.label_c21.setText(f"Celda 21: <font color='#80FF80'><b>{self.data2_21v:.2f} V<b></font>")
			elif self.data2_21 == 1:
				self.label_c21.setText(f"Celda 21: <font color='red'><b>{self.data2_21v:.2f} V<b></font>")
			elif self.data2_21 == 2:
				self.label_c21.setText(f"Celda 21: <font color='red'><b>{self.data2_21v:.2f} V<b></font>")
			elif self.data2_21 == 3:
				self.label_c21.setText(f"Celda 21: <font color='yellow'><b>{self.data2_21v:.2f} V<b></font>")
			elif self.data2_21 == 4:
				self.label_c21.setText(f"Celda 21: <font color='yellow'><b>{self.data2_21v:.2f} V<b></font>")
			else:
				self.label_c21.setText(f"Celda 21: <font color='red'><b>{self.data2_21v:.2f} V<b></font>")
			self.label_c21.setWordWrap(True)
			#Cell 22
			if self.data2_22 == 0:
				self.label_c22.setText(f"Celda 22: <font color='#80FF80'><b>{self.data2_22v:.2f} V<b></font>")
			elif self.data2_22 == 1:
				self.label_c22.setText(f"Celda 22: <font color='red'><b>{self.data2_22v:.2f} V<b></font>")
			elif self.data2_22 == 2:
				self.label_c22.setText(f"Celda 22: <font color='red'><b>{self.data2_22v:.2f} V<b></font>")
			elif self.data2_22 == 3:
				self.label_c22.setText(f"Celda 22: <font color='yellow'><b>{self.data2_22v:.2f} V<b></font>")
			elif self.data2_22 == 4:
				self.label_c22.setText(f"Celda 22: <font color='yellow'><b>{self.data2_22v:.2f} V<b></font>")
			else:
				self.label_c22.setText(f"Celda 22: <font color='red'><b>{self.data2_22v:.2f} V<b></font>")
			self.label_c22.setWordWrap(True)
			#Cell 23
			if self.data2_23 == 0:
				self.label_c23.setText(f"Celda 23: <font color='#80FF80'><b>{self.data2_23v:.2f} V<b></font>")
			elif self.data2_23 == 1:
				self.label_c23.setText(f"Celda 23: <font color='red'><b>{self.data2_23v:.2f} V<b></font>")
			elif self.data2_23 == 2:
				self.label_c23.setText(f"Celda 23: <font color='red'><b>{self.data2_23v:.2f} V<b></font>")
			elif self.data2_23 == 3:
				self.label_c23.setText(f"Celda 23: <font color='yellow'><b>{self.data2_23v:.2f} V<b></font>")
			elif self.data2_23 == 4:
				self.label_c23.setText(f"Celda 23: <font color='yellow'><b>{self.data2_23v:.2f} V<b></font>")
			else:
				self.label_c23.setText(f"Celda 23: <font color='red'><b>{self.data2_23v:.2f} V<b></font>")
			self.label_c23.setWordWrap(True)
			#Cell 24
			if self.data2_24 == 0:
				self.label_c24.setText(f"Celda 24: <font color='#80FF80'><b>{self.data2_24v:.2f} V<b></font>")
			elif self.data2_24 == 1:
				self.label_c24.setText(f"Celda 24: <font color='red'><b>{self.data2_24v:.2f} V<b></font>")
			elif self.data2_24 == 2:
				self.label_c24.setText(f"Celda 24: <font color='red'><b>{self.data2_24v:.2f} V<b></font>")
			elif self.data2_24 == 3:
				self.label_c24.setText(f"Celda 24: <font color='yellow'><b>{self.data2_24v:.2f} V<b></font>")
			elif self.data2_24 == 4:
				self.label_c24.setText(f"Celda 24: <font color='yellow'><b>{self.data2_24v:.2f} V<b></font>")
			else:
				self.label_c24.setText(f"Celda 24: <font color='red'><b>{self.data2_24v:.2f} V<b></font>")
			self.label_c24.setWordWrap(True)
			'''
			#Cell 1
			if self.data2_1 == 0:
				self.label_info2_1.setText(f"<font color='#80FF80'><b>Cell 1 No error.<b></font> Cell 1 voltage is <font color='#80FF80'><b>{self.data2_1v:.2f}V<b></font> which is between the boundaries.")
			elif self.data2_1 == 1:
				self.label_info2_1.setText(f"<font color='red'><b>Cell 1 Error.<b></font> Cell 1 voltage is <font color='red'><b>{self.data2_1v:.2f} V<b></font> which is over the maximum. Overvoltage causes excessive current flow that may lead to overheating and lithium plating leading to battery failure.")
			elif self.data2_1 == 2:
				self.label_info2_1.setText(f"<font color='red'><b>Cell 1 Error.<b></font> Cell 1 voltage is <font color='red'><b>{self.data2_1v:.2f} V<b></font> which is under the minimum.Undervoltage may be caused from storing the battery for a long time without use leading to a breakdown in the anodes and cathodes.")
			elif self.data2_1 == 3:
				self.label_info2_1.setText(f"<font color='yellow'><b>Cell 1 Warning.<b></font> The calculated average is within the correct range of values, <font color='yellow'><b>{self.data2_1v:.2f} V</b></font>. However, there are measurements that are outside of this range. It is recommended to redo the validation.")
			elif self.data2_1 == 4:
				self.label_info2_1.setText(f"<font color='yellow'><b>Cell 1 Warning.<b></font> The number of outlier measurements is too high, and the usable readings are few. The value is <font color='yellow'><b>{self.data2_1v:.2f} V<b></font>. It is recommended to redo the validation.")
			else:
				self.label_info2_1.setText(f"<font color='red'><b>Cell 1 Error.<b></font> No valid data input.")
			self.label_info2_1.setWordWrap(True)
			#Cell 2
			if self.data2_2 == 0:
				self.label_info2_2.setText(f"<font color='#80FF80'><b>Cell 2 No error.<b></font> Cell 2 voltage is <font color='#80FF80'><b>{self.data2_2v:.2f} V<b></font> which is between the boundaries.")
			elif self.data2_2 == 1:
				self.label_info2_2.setText(f"<font color='red'><b>Cell 2 Error.<b></font> Cell 2 voltage is <font color='red'><b>{self.data2_2v:.2f} V<b></font> which is over the maximum. Overvoltage causes excessive current flow that may lead to overheating and lithium plating leading to battery failure.")
			elif self.data2_2 == 2:
				self.label_info2_2.setText(f"<font color='red'><b>Cell 2 Error.<b></font> Cell 2 voltage is <font color='red'><b>{self.data2_2v:.2f} V<b></font> which is under the minimum.Undervoltage may be caused from storing the battery for a long time without use leading to a breakdown in the anodes and cathodes.")
			elif self.data2_2 == 3:
				self.label_info2_2.setText(f"<font color='yellow'><b>Cell 2 Warning.<b></font> The calculated average is within the correct range of values, <font color='yellow'><b>{self.data2_2v:.2f} V</b></font>. However, there are measurements that are outside of this range. It is recommended to redo the validation.")
			elif self.data2_2 == 4:
				self.label_info2_2.setText(f"<font color='yellow'><b>Cell 2 Warning.<b></font> The number of outlier measurements is too high, and the usable readings are few. The value is <font color='yellow'><b>{self.data2_2v:.2f} V<b></font>. It is recommended to redo the validation.")
			else:
				self.label_info2_2.setText(f"<font color='red'><b>Cell 2 Error.<b></font> No valid data input.")
			self.label_info2_2.setWordWrap(True)
			#Cell 3
			if self.data2_3 == 0:
				self.label_info2_3.setText(f"<font color='#80FF80'><b>Cell 3 No error.<b></font> Cell 2 voltage is <font color='#80FF80'><b>{self.data2_3v:.2f} V<b></font> which is between the boundaries.")
			elif self.data2_3 == 1:
				self.label_info2_3.setText(f"<font color='red'><b>Cell 3 Error.<b></font> Cell 2 voltage is <font color='red'><b>{self.data2_3v:.2f} V<b></font> which is over the maximum. Overvoltage causes excessive current flow that may lead to overheating and lithium plating leading to battery failure.")
			elif self.data2_3 == 2:
				self.label_info2_3.setText(f"<font color='red'><b>Cell 3 Error.<b></font> Cell 2 voltage is <font color='red'><b>{self.data2_3v:.2f} V<b></font> which is under the minimum.Undervoltage may be caused from storing the battery for a long time without use leading to a breakdown in the anodes and cathodes.")
			elif self.data2_3 == 3:
				self.label_info2_3.setText(f"<font color='yellow'><b>Cell 3 Warning.<b></font> The calculated average is within the correct range of values, <font color='yellow'><b>{self.data2_3v:.2f} V</b></font>. However, there are measurements that are outside of this range. It is recommended to redo the validation.")
			elif self.data2_3 == 4:
				self.label_info2_3.setText(f"<font color='yellow'><b>Cell 3 Warning.<b></font> The number of outlier measurements is too high, and the usable readings are few. The value is <font color='yellow'><b>{self.data2_3v:.2f} V<b></font>. It is recommended to redo the validation.")
			else:
				self.label_info2_3.setText(f"<font color='red'><b>Cell 3 Error.<b></font> No valid data input.")
			self.label_info2_3.setWordWrap(True)
			'''
	#Estado de carga
	def changeToPage3(self):
		if self.increment >= 300:
			self.stackedWidget_info.setCurrentIndex(2)
			if self.data3 == 0:
				self.label_info3.setText(f"<font color='#80FF80'><b>No error.<b></font> SoC percentage value read is <font color='#80FF80'><b>{self.data3v:.2f}<b> %</font> which is between the boundaries.")
			elif self.data3 == 1:
				self.label_info3.setText(f"<font color='red'><b>Error.<b></font>The SoC percentage value read is <font color='red'><b>{self.data3v:.2f}<b> %</font> which is under the minimum. Working outside the boundaries will reduce the battery cells life.")
			elif self.data3 == 2:
				self.label_info3.setText(f"<font color='yellow'><b>Warning.<b></font> The calculated average is within the correct range of values, <font color='yellow'><b>{self.data3v:.2f}<b> %</font>, but there are measurements that are outside of this range. It is recommended to redo the validation.")
			elif self.data3 == 3:
				self.label_info3.setText(f"<font color='yellow'><b>Warning.<b></font> The number of outlier measurements is too high, and the usable readings are few. Value is <font color='yellow'><b>{self.data3v:.2f}<b> %</font>. It is recommended to redo the validation.")
			else:
				self.label_info3.setText(f"<font color='red'><b>Cell 3 Error.<b></font> No valid data input.")
		self.label_info3.setWordWrap(True)
	#Temperatura de celdas
	def changeToPage4(self):
		if self.increment >= 400:
			self.stackedWidget_info.setCurrentIndex(3)
			#Cell 1
			if self.data4_1 == 0:
				self.label_info4_1.setText(f"<font color='#80FF80'><b>Cell 1 No error.<b></font> Cell 1 temperature is <font color='#80FF80'><b>{self.data4_1v:.2f} ºC<b></font> which is between the boundaries.")
			elif self.data4_1 == 1:
				self.label_info4_1.setText(f"<font color='red'><b>Cell 1 Error.<b></font> Cell 1 temperature is <font color='red'><b>{self.data4_1v:.2f} ºC<b></font> which is over the maximum. Overvoltage causes excessive current flow that may lead to overheating and lithium plating leading to battery failure.")
			elif self.data4_1 == 2:
				self.label_info4_1.setText(f"<font color='red'><b>Cell 1 Error.<b></font> Cell 1 temperature is <font color='red'><b>{self.data4_1v:.2f} ºC<b></font> which is under the minimum.Undervoltage may be caused from storing the battery for a long time without use leading to a breakdown in the anodes and cathodes.")
			elif self.data4_1 == 3:
				self.label_info4_1.setText(f"<font color='yellow'><b>Cell 1 Warning.<b></font> The calculated average is within the correct range of values, <font color='yellow'><b>{self.data4_1v:.2f}<b> ºC</font> but there are measurements that are outside of this range. It is recommended to redo the validation.")
			elif self.data4_1 == 4:
				self.label_info4_1.setText(f"<font color='yellow'><b>Cell 1 Warning.<b></font> The number of outlier measurements is too high, and the usable readings are few. Value is <font color='yellow'><b>{self.data4_1v:.2f}<b> ºC</font>. It is recommended to redo the validation.")
			else:
				self.label_info4_1.setText(f"<font color='red'><b>Cell 1 Error.<b></font> No valid data input.")
			self.label_info4_1.setWordWrap(True)
			#Cell 2
			if self.data4_2 == 0:
				self.label_info4_2.setText(f"<font color='#80FF80'><b>Cell 2 No error.<b></font> Cell 2 temperature is <font color='#80FF80'><b>{self.data4_2v:.2f} ºC<b></font> which is between the boundaries.")
			elif self.data4_2 == 1:
				self.label_info4_2.setText(f"<font color='red'><b>Cell 2 Error.<b></font> Cell 2 temperature is <font color='red'><b>{self.data4_2v:.2f} ºC<b></font> which is over the maximum. Overvoltage causes excessive current flow that may lead to overheating and lithium plating leading to battery failure.")
			elif self.data4_2 == 2:
				self.label_info4_2.setText(f"<font color='red'><b>Cell 2 Error.<b></font> Cell 2 temperature is <font color='red'><b>{self.data4_2v:.2f} ºC<b></font> which is under the minimum.Undervoltage may be caused from storing the battery for a long time without use leading to a breakdown in the anodes and cathodes.")
			elif self.data4_2 == 3:
				self.label_info4_2.setText(f"<font color='yellow'><b>Cell 2 Warning.<b></font> The calculated average is within the correct range of values, <font color='yellow'><b>{self.data4_2v:.2f}<b> ºC</font> but there are measurements that are outside of this range. It is recommended to redo the validation.")
			elif self.data4_2 == 4:
				self.label_info4_2.setText(f"<font color='yellow'><b>Cell 2 Warning.<b></font> The number of outlier measurements is too high, and the usable readings are few. Value is <font color='yellow'><b>{self.data4_2v:.2f}<b> ºC</font>. It is recommended to redo the validation.")
			else:
				self.label_info4_2.setText(f"<font color='red'><b>Cell 2 Error.<b></font> No valid data input.")
			self.label_info4_2.setWordWrap(True)
			#Cell 3
			if self.data4_3 == 0:
				self.label_info4_3.setText(f"<font color='#80FF80'><b>Cell 3 No error.<b></font> Cell 3 temperature is <font color='#80FF80'><b>{self.data4_3v:.2f} ºC<b></font> which is between the boundaries.")
			elif self.data4_3 == 1:
				self.label_info4_3.setText(f"<font color='red'><b>Cell 3 Error.<b></font> Cell 3 temperature is <font color='red'><b>{self.data4_3v:.2f} ºC<b></font> which is over the maximum. Overvoltage causes excessive current flow that may lead to overheating and lithium plating leading to battery failure.")
			elif self.data4_3 == 2:
				self.label_info4_3.setText(f"<font color='red'><b>Cell 3 Error.<b></font> Cell 3 temperature is <font color='red'><b>{self.data4_3v:.2f} ºC<b></font> which is under the minimum.Undervoltage may be caused from storing the battery for a long time without use leading to a breakdown in the anodes and cathodes.")
			elif self.data4_3 == 3:
				self.label_info4_3.setText(f"<font color='yellow'><b>Cell 3 Warning.<b></font> The calculated average is within the correct range of values, <font color='yellow'><b>{self.data4_3v:.2f}<b> ºC</font> but there are measurements that are outside of this range. It is recommended to redo the validation.")
			elif self.data4_3 == 4:
				self.label_info4_3.setText(f"<font color='yellow'><b>Cell 3 Warning.<b></font> The number of outlier measurements is too high, and the usable readings are few. Value is <font color='yellow'><b>{self.data4_3v:.2f}<b> ºC</font>. It is recommended to redo the validation.")
			else:
				self.label_info4_3.setText(f"<font color='red'><b>Cell 3 Error.<b></font> No valid data input.")
			self.label_info4_3.setWordWrap(True)
			#Cell 4
			if self.data4_4 == 0:
				self.label_info4_4.setText(f"<font color='#80FF80'><b>Cell 4 No error.<b></font> Cell 4 temperature is <font color='#80FF80'><b>{self.data4_4v:.2f} ºC<b></font> which is between the boundaries.")
			elif self.data4_4 == 1:
				self.label_info4_4.setText(f"<font color='red'><b>Cell 4 Error.<b></font> Cell 4 temperature is <font color='red'><b>{self.data4_4v:.2f} ºC<b></font> which is over the maximum. Overvoltage causes excessive current flow that may lead to overheating and lithium plating leading to battery failure.")
			elif self.data4_4 == 2:
				self.label_info4_4.setText(f"<font color='red'><b>Cell 4 Error.<b></font> Cell 4 temperature is <font color='red'><b>{self.data4_4v:.2f} ºC<b></font> which is under the minimum.Undervoltage may be caused from storing the battery for a long time without use leading to a breakdown in the anodes and cathodes.")
			elif self.data4_4 == 3:
				self.label_info4_4.setText(f"<font color='yellow'><b>Cell 4 Warning.<b></font> The calculated average is within the correct range of values, <font color='yellow'><b>{self.data4_4v:.2f}<b> ºC</font> but there are measurements that are outside of this range. It is recommended to redo the validation.")
			elif self.data4_4 == 4:
				self.label_info4_4.setText(f"<font color='yellow'><b>Cell 4 Warning.<b></font> The number of outlier measurements is too high, and the usable readings are few. Value is <font color='yellow'><b>{self.data4_4v:.2f}<b> ºC</font>. It is recommended to redo the validation.")
			else:
				self.label_info4_4.setText(f"<font color='red'><b>Cell 4 Error.<b></font> No valid data input.")
			self.label_info4_4.setWordWrap(True)
	#Temperatura de placa
	def changeToPage5(self):
		if self.increment >= 500:
			self.stackedWidget_info.setCurrentIndex(4)
			if self.data5 == 0:
				self.label_info5.setText(f"<font color='#80FF80'><b>No error.<b></font> Temperature is <font color='#80FF80'><b>{self.data5v:.2f} ºC<b></font> which is between the boundaries.")
			elif self.data5 == 1:
				self.label_info5.setText(f"<font color='red'><b>Error.<b></font> The temperature of the board is <font color='red'><b>{self.data5v:.2f} ºC<b></font> which is over the maximum. Working over the recommended temperature on the board may cause: loss of structural integrity, disruption of circuit lines, incompatible rates of material expansion or oxidation. The reason for the overheating may be caused by: component malfunction causing dissipation, through-hole interference, surface-mount device distance, lead-free solder…")
			elif self.data5 == 2:
				self.label_info5.setText(f"<font color='red'><b>Error.<b></font> The temperature of the board is <font color='red'><b>{self.data5v:.2f} ºC<b></font> which is under the minimum.")
			elif self.data5 == 3:
				self.label_info5.setText(f"<font color='yellow'><b>Warning.<b></font> The calculated average is within the correct range of values, <font color='yellow'><b>{self.data5v:.2f}<b> ºC</font> but there are measurements that are outside of this range. It is recommended to redo the validation.")
			elif self.data5 == 4:
				self.label_info5.setText(f"<font color='yellow'><b>Warning.<b></font> The number of outlier measurements is too high, and the usable readings are few. Value is <font color='yellow'><b>{self.data5v:.2f} ºC<b></font>. It is recommended to redo the validation.")
			else:
				self.label_info5.setText(f"<font color='red'><b>Error.<b></font> No valid data input.")
		self.label_info5.setWordWrap(True)
	#Corriente total
	def changeToPage6(self):
		if self.increment >= 600:
			self.stackedWidget_info.setCurrentIndex(5)
			if self.data6 == 0:
				self.label_info6.setText(f"<font color='#80FF80'><b>No error.<b></font> Total current read is <font color='#80FF80'><b>{self.data6v:.2f} A<b></font> which is between the boundaries.")
			elif self.data6 == 1:
				self.label_info6.setText(f"<font color='red'><b>Error.<b></font> Total current read is <font color='#80FF80'><b>{self.data6v:.2f} A<b></font> which is not between the boundaries.")
			elif self.data6 == 2:
				self.label_info6.setText(f"<font color='yellow'><b>Warning.<b></font> The calculated average is within the correct range of values, <font color='yellow'><b>{self.data6v:.2f}<b> A</font> but there are measurements that are outside of this range. It is recommended to redo the validation.")
			elif self.data6 == 3:
				self.label_info6.setText(f"<font color='yellow'><b>Warning.<b></font> The number of outlier measurements is too high, and the usable readings are few. Value is <font color='yellow'><b>{self.data6v:.2f}<b> A</font>. It is recommended to redo the validation.")
			else:
				self.label_info6.setText(f"<font color='red'><b>Error.<b></font> No valid data input.")
		self.label_info6.setWordWrap(True)

#Funcionamiento resolver

	#Alimentación 5 VDC
	def changeToPage7(self):
		if self.increment >= 700:
			self.stackedWidget_info.setCurrentIndex(6)
			if self.data7 == 0:
				self.label_info7.setText(f"<font color='#80FF80'><b>No error.<b></font> Voltage read is <font color='#80FF80'><b>{self.data7v:.2f} V<b></font>.")
			elif self.data7 == 1:
				self.label_info7.setText(f"<font color='red'><b>Error.<b></font>The power supply voltage of the resolver is not the expected voltage, <font color='red'><b>{self.data7v:.2f} V<b></font>")
			else:
				self.label_info7.setText(f"<font color='red'><b>Error.<b></font> No valid data input.")
		self.label_info7.setWordWrap(True)
	#Sin
	def changeToPage8(self):
		if self.increment >= 800:
			self.stackedWidget_info.setCurrentIndex(7)
			if self.data8 == 0:
				self.label_info8.setText(f"<font color='#80FF80'><b>No error.<b></font>")
			elif self.data8 == 1:
				self.label_info8.setText(f"<font color='red'><b>Error.<b></font> The sine wave of the resolver is not working correctly. The common issues to consider include: - Electrical connection problems, like loose or damaged wiring or terminals. If all the cables are in good condition, you could try shielding them. - Electromagnetic interference or noise in the electrical system. - Physical damage to the resolver unit. - Calibration issues. - Power supply problems.")
			else:
				self.label_info8.setText(f"<font color='red'><b>Error.<b></font> No valid data input.")
		self.label_info8.setWordWrap(True)
	#Cos
	def changeToPage9(self):
		if self.increment >= 900:
			self.stackedWidget_info.setCurrentIndex(8)
			if self.data9 == 0:
				self.label_info9.setText(f"<font color='#80FF80'><b>No error.<b></font>")
			elif self.data9 == 1:
				self.label_info9.setText(f"<font color='red'><b>Error.<b></font> The cosine wave of the resolver is not working correctly. The common issues to consider include: - Electrical connection problems, like loose or damaged wiring or terminals. If all the cables are in good condition, you could try shielding them. - Electromagnetic interference or noise in the electrical system. - Physical damage to the resolver unit. - Calibration issues. - Power supply problems.")
			else:
				self.label_info9.setText(f"<font color='red'><b>Error.<b></font> No valid data input.")
		self.label_info9.setWordWrap(True)
#Otros

	#Funcionament DC-CD (lectura 12V)
	def changeToPage10(self):
		if self.increment >= 1000:
			self.stackedWidget_info.setCurrentIndex(9)
			if self.data10 == 0:
				self.label_info10.setText(f"<font color='#80FF80'><b>No error.<b></font> Voltage read is <font color='#80FF80'><b>{self.data10v:.2f} V<b></font>")
			elif self.data10 == 1:
				self.label_info10.setText(f"<font color='red'><b>Error.<b></font> The battery voltage, <font color='#80FF80'><b>{self.data10v:.2f} V<b></font>, is over the maximum of 16V.")
			elif self.data10 == 2:
				self.label_info10.setText(f"<font color='red'><b>Error.<b></font> The battery voltage, <font color='#80FF80'><b>{self.data10v:.2f} V<b></font>, is under the minimum of 11 V.")
			else:
				self.label_info10.setText(f"<font color='red'><b>Error.<b></font> No valid data input.")
		self.label_info10.setWordWrap(True)
	#Comunicación CAN con el INVERSOR
	def changeToPage11(self):
		if self.increment >= 1100:
			self.stackedWidget_info.setCurrentIndex(10)
			if self.data11 == 0:
				self.label_info11.setText(f"<font color='#80FF80'><b>No error.<b></font>")
			elif self.data11 == 1:
				self.label_info11.setText(f"<font color='red'><b>Error.<b></font> ")
			else:
				self.label_info11.setText(f"<font color='red'><b>Error.<b></font> No valid data input.")
		self.label_info11.setWordWrap(True)
	#Funcionamiento Acelerador 12 VDC
	def changeToPage12(self):
		if self.increment >= 1200:
			self.stackedWidget_info.setCurrentIndex(11)
			if self.data12 == 0:
				self.label_info12.setText(f"<font color='#80FF80'><b>No error.<b></font>")
			elif self.data12 == 1:
				self.label_info12.setText(f"<font color='red'><b>Error.<b></font>")
			else:
				self.label_info12.setText(f"<font color='red'><b>Error.<b></font> No valid data input.")
		self.label_info12.setWordWrap(True)
	#Termistor motor
	def changeToPage13(self):
		if self.increment >= 1300:
			self.stackedWidget_info.setCurrentIndex(12)
			if self.data13 == 0:
				self.label_info13.setText(f"<font color='#80FF80'><b>No error.<b></font>")
			elif self.data13 == 1:
				self.label_info13.setText(f"<font color='red'><b>Error.<b></font> The termistor motor is not working properly. The main problems that can cause this malfunction are: - The instantaneous current through the thermistor is too high, and the resistance coil is damaged. - The thermistor's resistance wire is insulated and protected, creating a short circuit between the coils. - The line voltage is unstable and fluctuating, and the instantaneous voltage exceeds the thermistor's safety rating.")
			else:
				self.label_info13.setText(f"<font color='red'><b>Error.<b></font> No valid data input.")
		self.label_info13.setWordWrap(True)
	# Mostrar resultados
	def resumeOperation(self):
#Lecturas del BMS
		#Tension total
		if self.increment == 100:
			if self.data1 == 0:
				self.stackedWidget_1.setCurrentIndex(0)
				self.label_1v.setText(f"<font color='#80FF80'><b>{self.data1v:.2f}<b> V</font>")
			elif self.data1 == 1 or self.data1 == 2:
				self.stackedWidget_1.setCurrentIndex(2)
				self.label_1v.setText(f"<font color='red'><b>{self.data1v:.2f}<b> V</font>")
			elif self.data1 == 3 or self.data1 == 4:
				self.stackedWidget_1.setCurrentIndex(3)
				self.label_1v.setText(f"<font color='yellow'><b>{self.data1v:.2f}<b> V</font>")
			else:
				self.stackedWidget_1.setCurrentIndex(2)
				self.label_1v.setText(f"<font color='red'><b> -<b> V</font>")
			self.increment += 50
		
		#Tension de celdas
		elif self.increment == 200:
			data2_list = [self.data2_1,self.data2_2,self.data2_3,self.data2_4,self.data2_5,self.data2_6,self.data2_7,self.data2_8,self.data2_9,self.data2_10,self.data2_11,self.data2_12,self.data2_13,self.data2_14,self.data2_15,self.data2_16,self.data2_17,self.data2_18,self.data2_19,self.data2_20,self.data2_21,self.data2_22,self.data2_23,self.data2_24]
			if all(variable == 0 for variable in data2_list):
				self.data2_tot = 0
				self.stackedWidget_2.setCurrentIndex(0)
			elif all(variable in (1,2) for variable in data2_list):
				self.data2_tot = 1
				self.stackedWidget_2.setCurrentIndex(2)
			elif all(variable in (3,4) for variable in data2_list):
				if any(variable == 3 for variable in data2_list) and any(variable == 4 for variable in data2_list):
					self.data2_tot = 5
				elif any(variable == 3 for variable in data2_list):
					self.data2_tot = 3
				elif any(variable == 4 for variable in data2_list):
					self.data2_tot = 4
				self.stackedWidget_2.setCurrentIndex(3)
			else:
				self.data2_tot = 2
				self.stackedWidget_2.setCurrentIndex(2)
			
			self.increment += 50
		
		#Estado de carga
		elif self.increment == 300:
			if self.data3 == 0:
				self.stackedWidget_3.setCurrentIndex(0)
				self.label_3v.setText(f"<font color='#80FF80'><b>{self.data3v:.2f}<b> %</font>")
			elif self.data3 == 1:
				self.stackedWidget_3.setCurrentIndex(2)
				self.label_3v.setText(f"<font color='red'><b>{self.data3v:.2f}<b> %</font>")
			elif self.data3 == 2 or self.data3 == 3:
				self.stackedWidget_3.setCurrentIndex(3)
				self.label_3v.setText(f"<font color='yellow'><b>{self.data3v:.2f}<b> %</font>")
			else:
				self.stackedWidget_3.setCurrentIndex(2)
				self.label_3v.setText(f"<font color='red'><b> -<b> %</font>")
			self.increment += 50
		
		#Temperatura de celdas
		elif self.increment == 400:
			if self.data4_1 == 0 and self.data4_2 == 0 and self.data4_3 == 0 and self.data4_4 == 0:
				self.stackedWidget_4.setCurrentIndex(0)
			elif (self.data4_1 in(1,2)) or (self.data4_2 in(1,2)) or (self.data4_3 in (1,2)) or (self.data4_4 in (1,2)):
				self.stackedWidget_4.setCurrentIndex(2)
			elif (self.data4_1 in(3,4)) or (self.data4_2 in(3,4)) or (self.data4_3 in(3,4)) (self.data4_4 in (3,4)):
				self.stackedWidget_4.setCurrentIndex(3)
			else:
				self.stackedWidget_4.setCurrentIndex(2)
			self.increment += 50
		
		#Temperatura de placa
		elif self.increment == 500:
			if self.data5 == 0:
				self.stackedWidget_5.setCurrentIndex(0)
				self.label_5v.setText(f"<font color='#80FF80'><b>{self.data5v:.2f}<b> ºC</font>")
			elif self.data5 == 1 or self.data5 == 2:
				self.stackedWidget_5.setCurrentIndex(2)
				self.label_5v.setText(f"<font color='red'><b>{self.data5v:.2f}<b> ºC</font>")
			elif self.data5 == 3 or self.data5 == 4:
				self.stackedWidget_5.setCurrentIndex(3)
				self.label_5v.setText(f"<font color='yellow'><b>{self.data5v:.2f}<b> ºC</font>")
			else:
				self.stackedWidget_5.setCurrentIndex(2)
				self.label_5v.setText(f"<font color='red'><b> -<b> ºC</font>")
			self.increment += 50
		
		#Corriente total
		elif self.increment == 600:
			if self.data6 == 0:
				self.stackedWidget_6.setCurrentIndex(0)
				self.label_6v.setText(f"<font color='#80FF80'><b>{self.data6v:.2f}<b> A</font>")
			elif self.data6 == 1:
				self.stackedWidget_6.setCurrentIndex(2)
				self.label_6v.setText(f"<font color='red'><b>{self.data6v:.2f}<b> A</font>")
			elif self.data6 == 2 or self.data6 == 3:
				self.stackedWidget_6.setCurrentIndex(3)
				self.label_6v.setText(f"<font color='yellow'><b>{self.data6v:.2f}<b> A</font>")
			else:
				self.stackedWidget_6.setCurrentIndex(2)
				self.label_6v.setText(f"<font color='red'><b> -<b> A</font>")
			self.increment += 50

#Funcionamiento resolver
		#Alimentacion 5 VDC
		elif self.increment == 700:
			if self.data7 == 0:
				self.stackedWidget_7.setCurrentIndex(0)
				self.label_7v.setText(f"<font color='#80FF80'><b>{self.data7v:.2f}<b> V</font>")
			elif self.data7 == 1:
				self.stackedWidget_7.setCurrentIndex(2)
				self.label_7v.setText(f"<font color='red'><b>{self.data7v:.2f}<b> V</font>")
			else:
				self.stackedWidget_7.setCurrentIndex(2)
				self.label_7v.setText(f"<font color='red'><b> -<b> V</font>")
			self.increment += 50
		
		#Sinus
		elif self.increment == 800:
			if self.data8 == 0:
				self.stackedWidget_8.setCurrentIndex(0)
			elif self.data8 == 1:
				self.stackedWidget_8.setCurrentIndex(2)
			else:
				self.stackedWidget_8.setCurrentIndex(2)
			self.increment += 50
		
		#Cosinus
		elif self.increment == 900:
			if self.data9 == 0:
				self.stackedWidget_9.setCurrentIndex(0)
			elif self.data9 == 1:
				self.stackedWidget_9.setCurrentIndex(2)
			else:
				self.stackedWidget_9.setCurrentIndex(2)
			self.increment += 50

#Otros
		#Funcionamiento DC-DC 
		elif self.increment == 1000:
			if self.data10 == 0:
				self.stackedWidget_10.setCurrentIndex(0)
				self.label_10v.setText(f"<font color='#80FF80'><b>{self.data10v:.2f}<b> V</font>")
			elif self.data10 == 1:
				self.stackedWidget_10.setCurrentIndex(2)
				self.label_7v.setText(f"<font color='red'><b>{self.data10v:.2f}<b> V</font>")
			elif self.data10 == 2:
				self.stackedWidget_10.setCurrentIndex(2)
				self.label_7v.setText(f"<font color='red'><b>{self.data10v:.2f}<b> V</font>")
			else:
				self.stackedWidget_10.setCurrentIndex(2)
				self.label_7v.setText(f"<font color='red'><b> -</font>")
			self.increment += 50
		
		#Comunicación CAN con el INVERSOR
		elif self.increment == 1100:
			if self.data11 == 0:
				self.stackedWidget_11.setCurrentIndex(0)
			elif self.data11 == 1:
				self.stackedWidget_11.setCurrentIndex(2)
			else:
				self.stackedWidget_11.setCurrentIndex(2)
			self.increment += 50
		
		#Funcionamiento Acelerador 12V
		elif self.increment == 1200:
			if self.data12 == 0:
				self.stackedWidget_12.setCurrentIndex(0)
			elif self.data12 == 1:
				self.stackedWidget_12.setCurrentIndex(2)
			else:
				self.stackedWidget_12.setCurrentIndex(2)
			self.increment += 50
		
		#Termistor motor
		elif self.increment == 1300:
			if self.data13 == 0:
				self.stackedWidget_13.setCurrentIndex(0)
			elif self.data13 == 1:
				self.stackedWidget_13.setCurrentIndex(2)
			else:
				self.stackedWidget_13.setCurrentIndex(2)
			self.increment += 50
		
		else:
			self.increment += 50
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
		
		#Posar al document .txt si la validació de cada bateria es correcte
		if self.increment == 1400:
			var = [self.data1,self.data2_tot,self.data3,self.data4_1 , self.data4_2 ,self.data4_3 , self.data4_4, self.data5 , self.data6 , self.data7 , self.data8 , self.data9 , self.data10 , self.data11 , self.data12 , self.data13]
			if all(variable == 0 for variable in var):	
				with open('numeros_de_serie.txt','a') as file:
						file.write(f"{self.serial_number} OK\n")
			elif ((self.data1 in (1,2)) or (self.data2_tot in (1,2)) or (self.data3 == 1) or (self.data4_1 in (1,2)) or (self.data4_2 in (1,2)) or (self.data4_3 in (1,2)) or (self.data5 in (1,2)) or (self.data6 == 1) or (self.data7 == 1) or (self.data8 == 1) or (self.data9 == 1) or (self.data10 == 1) or (self.data11 == 1) or (self.data12 == 1) or (self.data13 == 1)):
				with open('numeros_de_serie.txt','a') as file:
						file.write(f"{self.serial_number} ERROR\n")
			else:
				with open('numeros_de_serie.txt','a') as file:
							file.write(f"{self.serial_number} WARNING\n")
			self.timer.stop()

	def startOperation(self):
		'''
		Començarem start operation quan cliquem la tecla d'start
		La variable par és d'un altre codi, on quan sigui 1 es començarà a executar la interfície
		'''
		#valuelist = function_test_loop(serial_number)
		self.serial_number = 88
		self.data1 = 3
		self.data2_1 = 0
		self.data2_2 = 1
		self.data2_3 = 0
		self.data2_4 = 0
		self.data2_5 = 0
		self.data2_6 = 0
		self.data2_7 = 0
		self.data2_8 = 1
		self.data2_9 = 0
		self.data2_10 = 0
		self.data2_11 = 0
		self.data2_12 = 2
		self.data2_13 = 0
		self.data2_14 = 0
		self.data2_15 = 2
		self.data2_16= 0
		self.data2_17 = 0
		self.data2_18 = 0
		self.data2_19 = 0
		self.data2_20 = 1
		self.data2_21 = 0
		self.data2_22 = 0
		self.data2_23 = 0
		self.data2_24 = 2
		self.data3 = 0
		self.data4_1 = 0
		self.data4_2 = 1
		self.data4_3 = 2
		self.data4_4 = 0
		self.data5 = 0
		self.data6 = 2
		self.data7 = 0
		self.data8 = 1
		self.data9 = 2
		self.data10 = 0
		self.data11 = 2
		self.data12 = 0
		self.data13 = 2

		self.data1v = 5.6
		self.data2_1v = 15.21 
		self.data2_2v = 15.15
		self.data2_3v = 15.22
		self.data2_4v = 0
		self.data2_5v = 1
		self.data2_6v = 2
		self.data2_7v = 0
		self.data2_8v = 1
		self.data2_9v = 2
		self.data2_10v = 0
		self.data2_11v = 1
		self.data2_12v = 2
		self.data2_13v = 0
		self.data2_14v = 1
		self.data2_15v = 2
		self.data2_16v = 0
		self.data2_17v = 1
		self.data2_18v = 2
		self.data2_19v = 0
		self.data2_20v = 1
		self.data2_21v = 2
		self.data2_22v = 0
		self.data2_23v = 1
		self.data2_24v = 2
		self.data3v = 25.8
		self.data4_1v = 0.5
		self.data4_2v = 1.5
		self.data4_3v = 2.5
		self.data4_4v = 2.5
		self.data5v = 11.5
		self.data6v = 12
		self.data7v = 4
		self.data8v = 45 
		self.data9v = 21
		self.data10v = 21
		self.data11v = 56
		self.data12v = 8
		self.data13v = 86

		self.label_serie.setText(f"Nº de serie: {self.serial_number}")

		self.timer.timeout.disconnect(self.resumeOperation)
		self.timer.timeout.connect(self.resumeOperation)
		self.timer.start(100)

	def stopOperation(self):
		self.timer.stop()

	def replayOperation(self):
		self.timer.stop()
		self.data2_tot = 0
		self.label_serie.setText(f"Nº de serie:")
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
	
		#Missatges per defecte
		
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

		self.label_1v.setText(f"-")
		self.label_3v.setText(f"-")
		self.label_5v.setText(f"-")
		self.label_6v.setText(f"-")
		self.label_7v.setText(f"-")
		self.label_10v.setText(f"-")

		self.label_info1.setText(f"")
		self.label_info2.setText(f"")
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

		self.label_c1.setText(f"Celda 1: -")
		self.label_c2.setText(f"Celda 2: -")
		self.label_c3.setText(f"Celda 3: -")
		self.label_c4.setText(f"Celda 4: -")
		self.label_c5.setText(f"Celda 5: -")
		self.label_c6.setText(f"Celda 6: -")
		self.label_c7.setText(f"Celda 7: -")
		self.label_c8.setText(f"Celda 8: -")
		self.label_c9.setText(f"Celda 9: -")
		self.label_c10.setText(f"Celda 10: -")
		self.label_c11.setText(f"Celda 11: -")
		self.label_c12.setText(f"Celda 12: -")
		self.label_c13.setText(f"Celda 13: -")
		self.label_c14.setText(f"Celda 14: -")
		self.label_c15.setText(f"Celda 15: -")
		self.label_c16.setText(f"Celda 16: -")
		self.label_c17.setText(f"Celda 17: -")
		self.label_c18.setText(f"Celda 18: -")
		self.label_c19.setText(f"Celda 19: -")
		self.label_c20.setText(f"Celda 20: -")
		self.label_c21.setText(f"Celda 21: -")
		self.label_c22.setText(f"Celda 22: -")
		self.label_c23.setText(f"Celda 23: -")
		self.label_c24.setText(f"Celda 24: -")

'''
	def show_serial_number_dialog(self):

		serial_number, ok = QInputDialog.getText(self, 'Introducir Número de Serie', 'Por favor, introduce el número de serie:')
        
		if ok:
			# Guardar el número de serie en un archivo
			with open('numeros_de_serie.txt', 'a') as file:
				file.write(serial_number+' ')
				self.label_serie.setText(f"Nº de serie: {serial_number}")
			self.startOperation(serial_number)
'''
#serial_number
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