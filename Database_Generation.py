##Database_Generation=name
##IFWPPS=group
##Sampling_Points_Vector_Layer=vector
##Administrative_Boundary_Category_Field=field Sampling_Points_Vector_Layer
##Plot_ID_Field=field Sampling_Points_Vector_Layer
##Volumetric_Equations_CSV_File=file
##Species_Column_Name=string NAME
##Database_File=output table

from osgeo import ogr
from PyQt4 import QtCore, QtGui
import sys, os, csv
import processing 
from qgis.core import QgsFeatureRequest 

progress.setText("Import Complete")

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout.addWidget(self.label_11)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.comboBox_5 = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.horizontalLayout_5.addWidget(self.comboBox_5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_8.addWidget(self.label_8)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_8.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_9.addWidget(self.label_9)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_9.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_10.addWidget(self.label_10)
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_10.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_12.addWidget(self.label_12)
        self.comboBox_7 = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_7.sizePolicy().hasHeightForWidth())
        self.comboBox_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_7.setFont(font)
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.horizontalLayout_12.addWidget(self.comboBox_7)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_11.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_11.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.comboBox, self.comboBox_2)
        MainWindow.setTabOrder(self.comboBox_2, self.comboBox_5)
        MainWindow.setTabOrder(self.comboBox_5, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.comboBox_7)
        MainWindow.setTabOrder(self.comboBox_7, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.comboBox)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "IFWPSS - Database Generation", None))
        self.label_11.setText(_translate("MainWindow", "IIRS FOREST WORKING PLAN PREPARATION SOFTWARE\n"
"SAMPLE POINT DATABASE GENERATION TOOL", None))
        self.label.setText(_translate("MainWindow", "Administrative Boundary ID\n"
"Division, Range, Block, Compartment etc.", None))
        self.label_2.setText(_translate("MainWindow", "Sampling Plot ID", None))
        self.label_5.setText(_translate("MainWindow", "Species Name", None))
        self.label_6.setText(_translate("MainWindow", "Local Name", None))
        self.label_8.setText(_translate("MainWindow", "Girth at Breast Height (GBH) in centimeters*", None))
        self.label_9.setText(_translate("MainWindow", "Bole Height in meters", None))
        self.label_10.setText(_translate("MainWindow", "Tree Height in meters", None))
        self.label_12.setText(_translate("MainWindow", "Timber Species", None))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "Yes", None))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "No", None))
        self.pushButton_2.setText(_translate("MainWindow", "Save and Close", None))
        self.pushButton_3.setText(_translate("MainWindow", "Save and Continue", None))

class WINDOW(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ui= Ui_MainWindow()
		self.ui.setupUi(self)
		self.setupSignals()
		self.reset()
		
	def reset(self):
		self.ui.comboBox.clear()
		for i in values:
			self.ui.comboBox.addItem(str(i))
		ListOfSpecies = []
		tf = open(Volumetric_Equations_CSV_File, "rb")
		r = csv.reader(tf)
		rownum = 0
		for row in r:
			if rownum == 0:
				header = row
				if Species_Column_Name in header:
					index = header.index(Species_Column_Name)
				else:
					progress.setText('Column name %s not found - ' %(Species_Column_Name))
			else:
				rowdata = row
				ListOfSpecies.append(rowdata[index])
			rownum += 1
		self.ui.comboBox_5.addItems(ListOfSpecies)

	def setupSignals(self):
		self.ui.comboBox.currentIndexChanged.connect(self.populateValues)
		self.ui.pushButton_2.clicked.connect(self.saveClose)
		self.ui.pushButton_3.clicked.connect(self.saveClear)
		
	def populateValues(self, index):
		vals = list(values)
		self.ui.comboBox_2.clear()
		plots = layer.getFeatures( QgsFeatureRequest().setFilterExpression \
				(""""%s" = '%s'""" %(Administrative_Boundary_Category_Field, str(vals[index]))))
		plotids = []
		for feature in plots:
			plotids.append(str(feature[Plot_ID_Field]))
		self.ui.comboBox_2.addItems(plotids)

	def saveClear(self):
		self.savedata()
		self.ui.lineEdit.clear()
		self.ui.lineEdit_2.clear()
		self.ui.lineEdit_3.clear()
		self.ui.lineEdit_4.clear()
		
	def saveClose(self):
		self.savedata()
		progress.setText("Database update complete")
		self.close()	
		
	def savedata(self):
		if str(self.ui.lineEdit_2.text()).strip() == "":
			QtGui.QMessageBox.information(self, "IFWPSS", "Please give GBH value to save the entry to database\nData not inserted")
			return
			
		header_row = ["ADMIN_ID", "PLOT_ID", "SPECIES_NAME", "LOCAL_NAME", "GBH", "BOLE_HT", "TREE_HT", "TIMBER", "STRATA"]
		line = []
		line.append(str(self.ui.comboBox.currentText()))
		line.append(str(self.ui.comboBox_2.currentText()))
		line.append(str(self.ui.comboBox_5.currentText()))
		line.append(str(self.ui.lineEdit.text()))
		line.append(str(self.ui.lineEdit_2.text()))
		line.append(str(self.ui.lineEdit_3.text()))
		line.append(str(self.ui.lineEdit_4.text()))
		line.append(str(self.ui.comboBox_7.currentText()))
		currentplot = layer.getFeatures(QgsFeatureRequest().setFilterExpression(""""%s" = %s""" %(Plot_ID_Field, str(self.ui.comboBox_2.currentText()))))
		for feature in currentplot:
			line.append(str(feature["STRATUM"]))
			break
		try:
			newfile = 0
			if not os.path.exists(Database_File):
				newfile = 1
			with open(Database_File, "ab") as csvfile:
				writer = csv.writer(csvfile, delimiter=',')
				if newfile:
					writer.writerow(header_row)
				writer.writerow(line)
			
			QtGui.QMessageBox.information(self, "IFWPSS", "%s - Data inserted" %(','.join(line)))
		except:
			QtGui.QMessageBox.information(self, "IFWPSS", "Data not inserted")

progress.setText("All set to run main logic")

ds = ogr.Open(Sampling_Points_Vector_Layer, False)
progress.setText('Opening file')
if ds == None:
    progress.setText('Unable to open file')

else:
    progress.setText('File open success')
    layer = processing.getObject(Sampling_Points_Vector_Layer)
    values = set()
    for feature in layer.getFeatures():
		values.add(feature[Administrative_Boundary_Category_Field])
    progress.setText('Initiating database update')
    dialog = WINDOW()
    dialog.show()
    progress.setText('\n...'*20)

