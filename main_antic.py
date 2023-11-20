# @author: FuseFinder

import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import QEasingCurve, QTimer
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from sim_results import*
import test_loop as tl

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		loadUi('Interficie1_1.ui', self)

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

		# Cambiar paginas
		self.bt_1.clicked.connect(self.changeToPage1)
		self.bt_2.clicked.connect(self.changeToPage2)
		self.bt_3.clicked.connect(self.changeToPage3)
		self.bt_4.clicked.connect(self.changeToPage4)
		self.bt_5.clicked.connect(self.changeToPage5)
		self.bt_6.clicked.connect(self.changeToPage6)
		self.bt_7.clicked.connect(self.changeToPage7)
		self.bt_8.clicked.connect(self.changeToPage8)

		# Mostrar resultados
		self.timer = QTimer(self)
		self.increment = 0
		self.bt_start.clicked.connect(self.startOperation)
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
	def changeToPage1(self):
#		if self.currentIndex == 1:
		self.stackedWidget_info.setCurrentIndex(0)
#		elif self.currentIndex == 0:
	


	def changeToPage2(self):
		self.stackedWidget_info.setCurrentIndex(1)

	def changeToPage3(self):
		self.stackedWidget_info.setCurrentIndex(2)

	def changeToPage4(self):
		self.stackedWidget_info.setCurrentIndex(3)

	def changeToPage5(self):
		self.stackedWidget_info.setCurrentIndex(4)

	def changeToPage6(self):
		self.stackedWidget_info.setCurrentIndex(5)

	def changeToPage7(self):
		self.stackedWidget_info.setCurrentIndex(6)

	def changeToPage8(self):
		self.stackedWidget_info.setCurrentIndex(7)

	# Mostrar resultados
	def resumeOperation(self):
		if self.increment == 100:
			self.stackedWidget_1.setCurrentIndex(data1)
			self.label_1.setText(f"<font color='green'>{data1_2:.2f} V</font>")
			self.increment += 5
		
		elif self.increment == 200:
			self.stackedWidget_2.setCurrentIndex(data2)
			self.label_2_1.setText(f"Celda 1: {data2_2_1:.2f} V")
			self.label_2_2.setText(f"Celda 2: {data2_2_2:.2f} V")
			self.label_2_3.setText(f"Celda 3: {data2_2_3:.2f} V")
			self.increment += 5

		elif self.increment == 300:
			self.stackedWidget_3.setCurrentIndex(data3)
			self.label_3_1.setText(f"Celda 1: {data3_2_1:.2f} ºC")
			self.label_3_2.setText(f"Celda 2: {data3_2_2:.2f} ºC")
			self.label_3_3.setText(f"Celda 3: {data3_2_3:.2f} ºC")
			self.increment += 5

		elif self.increment == 400:
			self.stackedWidget_4.setCurrentIndex(data4)
			self.label_4.setText(f"{data4_2:.2f} V")
			self.increment += 5

		elif self.increment == 500:
			list_12V = tl.function_test_loop()
			self.stackedWidget_5.setCurrentIndex(list_12V[0])
			self.label_5.setText(f"{data5_2:.2f} V")
			self.increment += 5

		elif self.increment == 600:
			self.stackedWidget_6.setCurrentIndex(data6)
			self.label_6.setText(f"{data6_2:.2f} V")
			self.increment += 5

		elif self.increment == 700:
			self.stackedWidget_7.setCurrentIndex(data7)
			self.label_7.setText(f"{data7_2:.2f} V")
			self.increment += 5

		elif self.increment == 800:
			self.stackedWidget_8.setCurrentIndex(data8)
			self.label_8.setText(f"{data8_2:.2f} A")
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
		self.stackedWidget_1.setCurrentIndex(1)
		self.stackedWidget_2.setCurrentIndex(1)
		self.stackedWidget_3.setCurrentIndex(1)
		self.stackedWidget_4.setCurrentIndex(1)
		self.stackedWidget_5.setCurrentIndex(1)
		self.stackedWidget_6.setCurrentIndex(1)
		self.stackedWidget_7.setCurrentIndex(1)
		self.stackedWidget_8.setCurrentIndex(1)
		self.label_1.setText(f"-")
		self.label_2_1.setText(f"Celda 1: -")
		self.label_2_2.setText(f"Celda 2: -")
		self.label_2_3.setText(f"Celda 3: -")
		self.label_3_1.setText(f"Celda 1: -")
		self.label_3_2.setText(f"Celda 2: -")
		self.label_3_3.setText(f"Celda 3: -")
		self.label_4.setText(f"-")
		self.label_5.setText(f"-")
		self.label_6.setText(f"-")
		self.label_7.setText(f"-")
		self.label_8.setText(f"-")
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