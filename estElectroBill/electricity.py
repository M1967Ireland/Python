###########
#
# estElectroBill v.2
# adding to and from dates
#
###############
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication ,QLabel,QLineEdit,QMainWindow,QPushButton, QWidget)
from PyQt5.QtCore import (QRect, Qt)

from datetime import datetime
startvalue = str(0)


		

class Ui_MainWindow(QMainWindow):

		######### Program
	def setupUi(self, MainWindow):
		MainWindow.resize(550, 400)
		self.centralwidget = QWidget(MainWindow) #centralwidget start
		self.label = QLabel(self.centralwidget)
		self.label.setGeometry(QRect(30, 50, 67, 17))

		self.textLabels()
		self.leftSide()
		self.rightSide()
		self.dateFrom()
		self.datesTo()
		self.pushButtons()
		
		MainWindow.setCentralWidget(self.centralwidget) 


	def textLabels(self):
		self.labelIntro = QLabel(self.centralwidget)
		self.labelIntro.setGeometry(QRect(75, 20, 400, 17))
		self.labelIntro.setText ('Please Enter Old value, New value and Days') 
		
		self.labelEnd = QLabel(self.centralwidget)
		self.labelEnd.setGeometry(QRect(180, 330, 400, 17))
		self.labelEnd.setText ('Pay with VAT is estimate, no discount added') 

	def pushButtons(self):
		self.button = QPushButton("Calculate Days",self.centralwidget)
		self.button.move(250, 300)
		self.button.setStyleSheet("background-color : yellow")
		self.button.clicked.connect(self.daysCounted)

		self.button = QPushButton("Calculate Total Sum",self.centralwidget)
		self.button.move(240, 350)
		self.button.clicked.connect(self.on_Calculate)		
	
	def leftSide(self):
		self.labelOldValue = QLabel(self.centralwidget)
		self.labelOldValue.setGeometry(QRect(50, 70, 85, 17))
		self.labelOldValue.setText ('Old Reading') 
		self.OldValueInn = QLineEdit(self.centralwidget)
		self.OldValueInn.setGeometry(QRect(140, 70, 75, 20))
		self.OldValueInn.insert(startvalue)
		self.OldValueInn.setAlignment(Qt.AlignCenter)
		
		self.labelNewValue = QLabel(self.centralwidget)
		self.labelNewValue.setGeometry(QRect(50, 90, 90, 17))
		self.labelNewValue.setText ('New Reading') 
		self.newValueInn = QLineEdit(self.centralwidget)
		self.newValueInn.setGeometry(QRect(140, 90, 75, 20))
		self.newValueInn.insert(startvalue)
		self.newValueInn.setAlignment(Qt.AlignCenter)
		
		
		self.labelDifference = QLabel(self.centralwidget)
		self.labelDifference.setGeometry(QRect(50, 110, 75, 17))
		self.labelDifference.setText ('Used') 
		self.differenceValue= QLineEdit(self.centralwidget)
		self.differenceValue.setGeometry(QRect(140, 110, 75, 20))
		self.differenceValue.setAlignment(Qt.AlignCenter)
		
		self.labelUnitUsageUnitPrice = QLabel(self.centralwidget)
		self.labelUnitUsageUnitPrice.setGeometry(QRect(50, 130, 75, 17))
		self.labelUnitUsageUnitPrice.setText ('Basic €') 
		self.unitUsageUnitPrice= QLineEdit(self.centralwidget)
		self.unitUsageUnitPrice.setGeometry(QRect(140, 130, 75, 20))
		self.unitUsageUnitPrice.setAlignment(Qt.AlignCenter)

	def rightSide(self):
				# Right side
		self.labelDays= QLabel(self.centralwidget)
		self.labelDays.setGeometry(QRect(250, 70, 75, 17))
		self.labelDays.setText ('Days') 
		self.Days= QLineEdit(self.centralwidget)
		self.Days.setGeometry(QRect(380, 70, 75, 20))
		self.Days.insert(startvalue)
		self.Days.setAlignment(Qt.AlignCenter)

		self.labelStandingCharge= QLabel(self.centralwidget)
		self.labelStandingCharge.setGeometry(QRect(250, 90, 150, 17))
		self.labelStandingCharge.setText ('Standing Charge') 
		self.StandingCharge= QLineEdit(self.centralwidget)
		self.StandingCharge.setGeometry(QRect(380, 90, 75, 20))
		self.StandingCharge.setAlignment(Qt.AlignCenter)

		self.labelBeforeVat= QLabel(self.centralwidget)
		self.labelBeforeVat.setGeometry(QRect(250, 110, 150, 17))
		self.labelBeforeVat.setText ('Charge before VAT') 
		self.BeforeVat= QLineEdit(self.centralwidget)
		self.BeforeVat.setGeometry(QRect(380, 110, 75, 20))
		self.BeforeVat.setAlignment(Qt.AlignCenter)
		
		self.labelWithVat= QLabel(self.centralwidget)
		self.labelWithVat.setGeometry(QRect(250, 130, 150, 17))
		self.labelWithVat.setText ('To Pay with VAT') 
		self.WithVat= QLineEdit(self.centralwidget)
		self.WithVat.setGeometry(QRect(380, 130, 75, 20))
		self.WithVat.setAlignment(Qt.AlignCenter)

	def dateFrom(self):
		self.labelFromDate = QLabel(self.centralwidget)
		self.labelFromDate.setGeometry(QRect(100, 200,75,17))
		self.labelFromDate.setText('From Date')

		self.labelFromDateDay= QLabel(self.centralwidget)
		self.labelFromDateDay.setGeometry(QRect(190, 180, 150, 17))
		self.labelFromDateDay.setText ('Day ') 
		self.fromDateDay= QLineEdit(self.centralwidget)
		self.fromDateDay.setGeometry(QRect(180, 200, 50, 25))
		self.fromDateDay.insert(startvalue)
		self.fromDateDay.setAlignment(Qt.AlignCenter)
		
		self.labelFromDateMonth= QLabel(self.centralwidget)
		self.labelFromDateMonth.setGeometry(QRect(280, 180, 150, 17))
		self.labelFromDateMonth.setText ('Month') 
		self.fromDateMonth= QLineEdit(self.centralwidget)
		self.fromDateMonth.setGeometry(QRect(270, 200, 50, 25))
		self.fromDateMonth.insert(startvalue)
		self.fromDateMonth.setAlignment(Qt.AlignCenter)
		
		self.labelFromDateYear= QLabel(self.centralwidget)
		self.labelFromDateYear.setGeometry(QRect(360, 180, 150, 17))
		self.labelFromDateYear.setText ('Year') 
		self.fromDateYear= QLineEdit(self.centralwidget)
		self.fromDateYear.setGeometry(QRect(350, 200, 50, 25))
		self.fromDateYear.insert(startvalue)
		self.fromDateYear.setAlignment(Qt.AlignCenter)

	def datesTo(self):
		self.labelToDate = QLabel(self.centralwidget)
		self.labelToDate.setGeometry(QRect(100, 275,75,17))
		self.labelToDate.setText('To Date')
		
		self.labelToDateDay= QLabel(self.centralwidget)
		self.labelToDateDay.setGeometry(QRect(190, 250, 150, 17))
		self.labelToDateDay.setText ('Day') 
		self.toDateDay= QLineEdit(self.centralwidget)
		self.toDateDay.setGeometry(QRect(180, 270, 50, 25))
		self.toDateDay.insert(startvalue)
		self.toDateDay.setAlignment(Qt.AlignCenter)
		
		self.labelToDateMonth= QLabel(self.centralwidget)
		self.labelToDateMonth.setGeometry(QRect(280, 250, 150, 17))
		self.labelToDateMonth.setText ('Month ') 
		self.toDateMonth= QLineEdit(self.centralwidget)
		self.toDateMonth.setGeometry(QRect(270, 270, 50, 25))
		self.toDateMonth.insert(startvalue)
		self.toDateMonth.setAlignment(Qt.AlignCenter)

		self.labelToDateYear= QLabel(self.centralwidget)
		self.labelToDateYear.setGeometry(QRect(360, 250, 150, 17))
		self.labelToDateYear.setText ('Year') 
		self.toDateYear= QLineEdit(self.centralwidget)
		self.toDateYear.setGeometry(QRect(350, 270, 50, 25))
		self.toDateYear.insert(startvalue)
		self.toDateYear.setAlignment(Qt.AlignCenter)		


	def daysCounted(self):
		
		fromDay= int(self.fromDateDay.text())
		fromMonth = int(self.fromDateMonth.text())
		fromYear = int(self.fromDateYear.text())
		
		toDay= int(self.toDateDay.text())+1 # +1 includes last day
		toMonth = int(self.toDateMonth.text())
		toYear = int(self.toDateYear.text())
		
		try:
			date1 = datetime(day = fromDay, month = fromMonth, year = fromYear)
			date2 = datetime(day = toDay, month = toMonth, year = toYear)
		except ValueError as ve:
			return
		timedelta = date2 - date1
		amountDays = str(timedelta.days)
		self.Days.clear()
		self.Days.insert(amountDays)
	####### Day calculation end


	# 	
	def on_Calculate(self):
		
		self.StandingCharge.clear()
		self.unitUsageUnitPrice.clear()
		self.differenceValue.clear()
		self.BeforeVat.clear()
		self.WithVat.clear()
		
		
		valueNew = int(self.newValueInn.text())
		valueOld = int(self.OldValueInn.text())
		differentValue = str(valueNew - valueOld)
		self.differenceValue.insert(differentValue)
		differentValue=float(differentValue)
		amount = str(round(differentValue *0.1753 ,2))
		self.unitUsageUnitPrice.insert(amount)
		

		daysInserted = int(self.Days.text())

		daysChargeShow = str(round(daysInserted*0.5517 ,2))
		self.StandingCharge.insert(daysChargeShow)
		
		chargeBeforeVat = round(daysInserted*0.5517 ,2)+ round(differentValue *0.1753 ,2)
		chargeBeforeVat = str(round(chargeBeforeVat,2))
		self.BeforeVat.insert(chargeBeforeVat)
		
		
		if daysInserted== 0 or differentValue == 0:
			pso = 0
		else: 
			pso = 6.52


		chargeWithVat = ((((daysInserted*0.5517)+ (differentValue *0.1753))+pso) *1.13)
		chargeWithVat = str(round(chargeWithVat, 2))
		self.WithVat.insert(chargeWithVat)
				
if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	MainWindow = QMainWindow()
	MainWindow.setWindowIcon(QIcon('helpIcon.png')) 
	ui = Ui_MainWindow()
	#ui.__init__(MainWindow)
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec())
