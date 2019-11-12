# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(240, 360)
        MainWindow.setFixedSize(240, 360)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Pictures/images(2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(0, 60, 61, 61))
        self.pushButton_clear.setStyleSheet("background-color: rgb(79, 159, 239);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_percent = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_percent.setGeometry(QtCore.QRect(60, 60, 61, 61))
        self.pushButton_percent.setStyleSheet("background-color: rgb(79, 159, 239);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.pushButton_divide = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_divide.setGeometry(QtCore.QRect(180, 60, 61, 61))
        self.pushButton_divide.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    background-color: rgb(216, 0, 0);\n"
"    color: white;\n"
"    border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.pushButton_plusMinus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plusMinus.setGeometry(QtCore.QRect(120, 60, 61, 61))
        self.pushButton_plusMinus.setStyleSheet("background-color: rgb(79, 159, 239);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.pushButton_plusMinus.setObjectName("pushButton_plusMinus")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(120, 120, 61, 61))
        self.pushButton_9.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid gray;\n"
"\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_multiply.setGeometry(QtCore.QRect(180, 120, 61, 61))
        self.pushButton_multiply.setStyleSheet("QPushButton{\n"
"    background-color: rgb(216, 0, 0);\n"
"    color: white;\n"
"    border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(60, 120, 61, 61))
        self.pushButton_8.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid gray;\n"
"\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 120, 61, 61))
        self.pushButton_7.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid gray;\n"
"\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 180, 61, 61))
        self.pushButton_4.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid gray;\n"
"\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(180, 180, 61, 61))
        self.pushButton_minus.setStyleSheet("QPushButton{\n"
"    background-color: rgb(216, 0, 0);\n"
"    color: white;\n"
"    border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 180, 61, 61))
        self.pushButton_6.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid gray;\n"
"\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 180, 61, 61))
        self.pushButton_5.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid gray;\n"
"\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 240, 61, 61))
        self.pushButton_2.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid gray;\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 240, 61, 61))
        self.pushButton_3.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid gray;\n"
"\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(180, 240, 61, 61))
        self.pushButton_plus.setStyleSheet("QPushButton{\n"
"    background-color: rgb(216, 0, 0);\n"
"    color: white;\n"
"    border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 240, 61, 61))
        self.pushButton_1.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid gray;\n"
"\n"
"")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_zero = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_zero.setGeometry(QtCore.QRect(0, 300, 122, 61))
        self.pushButton_zero.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid gray;\n"
"\n"
"")
        self.pushButton_zero.setObjectName("pushButton_zero")
        self.pushButton_uquals = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_uquals.setGeometry(QtCore.QRect(180, 300, 61, 61))
        self.pushButton_uquals.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    background-color: rgb(216, 0, 0);\n"
"    color: white;\n"
"    border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_uquals.setObjectName("pushButton_uquals")
        self.pushButton_decimal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_decimal.setGeometry(QtCore.QRect(120, 300, 61, 61))
        self.pushButton_decimal.setStyleSheet("background-color: rgb(79, 159, 239);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid gray")
        self.pushButton_decimal.setObjectName("pushButton_decimal")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 240, 61))
        self.label.setStyleSheet("QLabel{\n"
"    qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"    border:1px solid gray;\n"
"    background-color: rgb(226, 226, 226);\n"
"    \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"background-color: white")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_clear.setText(_translate("MainWindow", "c"))
        self.pushButton_percent.setText(_translate("MainWindow", "%"))
        self.pushButton_divide.setText(_translate("MainWindow", "/"))
        self.pushButton_plusMinus.setText(_translate("MainWindow", "+/-"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_multiply.setText(_translate("MainWindow", "x"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_minus.setText(_translate("MainWindow", "-"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_zero.setText(_translate("MainWindow", "0"))
        self.pushButton_uquals.setText(_translate("MainWindow", "="))
        self.pushButton_decimal.setText(_translate("MainWindow", "."))
        self.label.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

