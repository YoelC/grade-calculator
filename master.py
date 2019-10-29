# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Main(QtWidgets.QWidget):
    clicked = QtCore.pyqtSignal

    def __init__(self):
        super(Main, self).__init__()

        self.setBaseSize(500, 400)
        self.center()

        self.setWindowTitle("Calculator")
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.tabwidget = QtWidgets.QTabWidget()

        self.tab1 = tab1()
        self.tabwidget.addTab(self.tab1, "Add Grades")
        self.tabwidget.setTabBarAutoHide(True)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPixelSize(15)
        self.setFont(font)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.tabwidget)

        self.setLayout(vbox)

        # INFO SHARE

    def center(self):
        qr = self.frameGeometry()

        cp = QtWidgets.QDesktopWidget().availableGeometry().center()

        qr.moveCenter(cp)

        self.move(qr.topLeft())


class tab1(QtWidgets.QMainWindow):

    def __init__(self):
        super(tab1, self).__init__()
        self.isOpened = False
        self.F1text = ""
        self.F2text = ""
        self.Stext = ""
        self.SMtext = ""

        self.setWindowTitle("Calculator")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.centralwidget = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2 = QtWidgets.QGridLayout()

        # 'Semestral' label
        self.label_4 = QtWidgets.QLabel()
        self.label_4.setText("Semestral")
        self.gridLayout_2.addWidget(self.label_4, 11, 0, 1, 1)

        # 'F1' lineEdit
        self.lineEdit = QtWidgets.QDoubleSpinBox()
        self.lineEdit.clear()
        self.lineEdit.setMaximum(9999.99)
        self.lineEdit.valueChanged.connect(lambda: self.on_modify(1))
        self.gridLayout_2.addWidget(self.lineEdit, 4, 1, 1, 1)

        # 'Semestral' lineEdit
        self.lineEdit_4 = QtWidgets.QDoubleSpinBox()
        self.lineEdit_4.clear()
        self.lineEdit_4.setMaximum(9999.99)
        self.lineEdit_4.valueChanged.connect(lambda: self.on_modify(4))
        self.gridLayout_2.addWidget(self.lineEdit_4, 11, 1, 1, 1)

        # 'Summative' lineEdit
        self.lineEdit_3 = QtWidgets.QDoubleSpinBox()
        self.lineEdit_3.clear()
        self.lineEdit_3.setMaximum(9999.99)
        self.lineEdit_3.valueChanged.connect(lambda: self.on_modify(3))
        self.gridLayout_2.addWidget(self.lineEdit_3, 9, 1, 1, 1)

        # 'F2' lineEdit
        self.lineEdit_2 = QtWidgets.QDoubleSpinBox()
        self.lineEdit_2.clear()
        self.lineEdit_2.setMaximum(9999.99)
        self.lineEdit_2.valueChanged.connect(lambda: self.on_modify(2))
        self.gridLayout_2.addWidget(self.lineEdit_2, 6, 1, 1, 1)

        # 'Summative' label
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setText("Summative")
        self.gridLayout_2.addWidget(self.label_2, 9, 0, 1, 1)

        # 'F1' label
        self.label_3 = QtWidgets.QLabel()
        self.label_3.setText("F1")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)

        # 'F2' label
        self.label = QtWidgets.QLabel()
        self.label.setText("F2")
        self.gridLayout_2.addWidget(self.label, 6, 0, 1, 1)

        # Spacers and grids
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 5, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 7, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 10, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 12, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 14, 4, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 14, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 4, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 4, 4, 1, 1)

        # Groupboxed
        groupbox = QtWidgets.QGroupBox()
        vbox = QtWidgets.QVBoxLayout()
        groupbox.setLayout(vbox)
        self.gridLayout_2.addWidget(groupbox, 1, 0, 1, 5)

        # 'Grade:' label
        self.label_5 = QtWidgets.QLabel()
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setText("Final Grade:")
        vbox.addWidget(self.label_5)

        # GradeNumber label
        self.label_6 = QtWidgets.QLabel()
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setFont(QtGui.QFont("Segoe UI", 25))
        self.label_6.setText("Not set")
        vbox.addWidget(self.label_6)

        # F1 '...' pushButton
        self.pushButton_2 = QtWidgets.QPushButton()
        self.pushButton_2.setText("...")
        self.pushButton_2.clicked.connect(lambda: self.open_window(1))
        self.gridLayout_2.addWidget(self.pushButton_2, 4, 3, 1, 1)

        # F2 '...' pushButton
        self.pushButton_3 = QtWidgets.QPushButton()
        self.pushButton_3.setText("...")
        self.pushButton_3.clicked.connect(lambda: self.open_window(2))
        self.gridLayout_2.addWidget(self.pushButton_3, 6, 3, 1, 1)

        # Summative '...' pushButton
        self.pushButton_4 = QtWidgets.QPushButton()
        self.pushButton_4.setText("...")
        self.pushButton_4.clicked.connect(lambda: self.open_window(3))
        self.gridLayout_2.addWidget(self.pushButton_4, 9, 3, 1, 1)

        # Semestral '...' pushButton
        self.pushButton_5 = QtWidgets.QPushButton()
        self.pushButton_5.setText("...")
        self.pushButton_5.clicked.connect(lambda: self.open_window(4))
        self.gridLayout_2.addWidget(self.pushButton_5, 11, 3, 1, 1)

        '''
        # 'Save' pushButton
        self.pushButton_6 = QtWidgets.QPushButton()
        self.pushButton_6.setText("Save Changes")
        self.gridLayout_2.addWidget(self.pushButton_6, 13, 1, 1, 3)
        '''

        # F1 'Clear' pushButton
        self.clearPushButton = QtWidgets.QPushButton()
        self.clearPushButton.setText("Clear")
        self.clearPushButton.clicked.connect(lambda: self.clear_func(1))
        self.gridLayout_2.addWidget(self.clearPushButton, 4, 4, 1, 1)

        # F2 'Clear' pushButton
        self.clearPushButton_2 = QtWidgets.QPushButton()
        self.clearPushButton_2.setText("Clear")
        self.clearPushButton_2.clicked.connect(lambda: self.clear_func(2))
        self.gridLayout_2.addWidget(self.clearPushButton_2, 6, 4, 1, 1)

        # S 'Clear' pushButton
        self.clearPushButton_3 = QtWidgets.QPushButton()
        self.clearPushButton_3.setText("Clear")
        self.clearPushButton_3.clicked.connect(lambda: self.clear_func(3))
        self.gridLayout_2.addWidget(self.clearPushButton_3, 9, 4, 1, 1)

        # SM 'Clear' pushButton
        self.clearPushButton_4 = QtWidgets.QPushButton()
        self.clearPushButton_4.setText("Clear")
        self.clearPushButton_4.clicked.connect(lambda: self.clear_func(4))
        self.gridLayout_2.addWidget(self.clearPushButton_4, 11, 4, 1, 1)

        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)

    def open_window(self, number):

        newWindow = Ui_Dialog()
        newWindow.setModal(True)
        newWindow.show()

        # Saves previous text stored in F1text, F2text, Stext and SMtext depending on the number defined in the call
        self.isOpened = True

        if number == 1:
            if self.F1text == "":
                newWindow.plainTextEdit.setPlainText(self.lineEdit.text())
            else:
                newWindow.plainTextEdit.setPlainText(self.F1text)

        elif number == 2:
            if self.F2text == "":
                newWindow.plainTextEdit.setPlainText(self.lineEdit_2.text())
            else:
                newWindow.plainTextEdit.setPlainText(self.F2text)
        elif number == 3:
            if self.Stext == "":
                newWindow.plainTextEdit.setPlainText(self.lineEdit_3.text())
            else:
                newWindow.plainTextEdit.setPlainText(self.Stext)
        elif number == 4:
            if self.SMtext == "":
                newWindow.plainTextEdit.setPlainText(self.lineEdit_4.text())
            else:
                newWindow.plainTextEdit.setPlainText(self.SMtext)

        if newWindow.exec_():

            if number == 1:
                self.F1text = newWindow.plainTextEdit.toPlainText().strip(" ")
            elif number == 2:
                self.F2text = newWindow.plainTextEdit.toPlainText().strip(" ")
            elif number == 3:
                self.Stext = newWindow.plainTextEdit.toPlainText().strip(" ")
            elif number == 4:
                self.SMtext = newWindow.plainTextEdit.toPlainText().strip(" ")

            text = newWindow.plainTextEdit.toPlainText()
            text_list = text.split()
            final_grade = 0

            for grade in text_list:
                try:
                    grade = float(grade)
                except ValueError:
                    self.warning("Grades have to be numbers")
                    if number == 1:
                        self.F1text = ""

                    if number == 2:
                        self.F2text = ""

                    if number == 3:
                        self.Stext = ""

                    if number == 4:
                        self.SMtext = ""
                    return

                final_grade += grade

            try:
                final_grade = final_grade / len(text_list)
            except ZeroDivisionError:
                return
            if number == 1:
                self.lineEdit.setValue(round(final_grade, 2))

            elif number == 2:
                self.lineEdit_2.setValue(round(final_grade, 2))

            elif number == 3:
                self.lineEdit_3.setValue(round(final_grade, 2))

            elif number == 4:
                self.lineEdit_4.setValue(round(final_grade, 2))

            self.isOpened = False

    def calc(self):
        F1 = self.lineEdit.value()

        if F1 != 0:
            F1_weight = 10
        else:
            F1_weight = 0

        F2 = self.lineEdit_2.value()
        if F2 != 0:
            F2_weight = 25
        else:
            F2_weight = 0

        S = self.lineEdit_3.value()
        if S != 0:
            S_weight = 40
        else:
            S_weight = 0

        SM = self.lineEdit_4.value()
        if SM != 0:
            SM_weight = 25
        else:
            SM_weight = 0

        weight = F1_weight + F2_weight + S_weight + SM_weight
        if weight != 0:
            grade = (F1*F1_weight + F2*F2_weight + S*S_weight + SM*SM_weight)/weight
            self.label_6.setText(str(round(grade, 2)))
        else:
            self.label_6.setText("No establecida")

        if F1 == 0:
            self.lineEdit.clear()
        if F2 == 0:
            self.lineEdit_2.clear()
        if S == 0:
            self.lineEdit_3.clear()
        if SM == 0:
            self.lineEdit_4.clear()

    def on_modify(self, number):
        self.calc()

        if not self.isOpened:
            if number == 1:
                self.F1text = str(self.lineEdit.value())

            if number == 2:
                self.F2text = str(self.lineEdit_2.value())

            if number == 3:
                self.Stext = str(self.lineEdit_3.value())

            if number == 4:
                self.SMtext = str(self.lineEdit_4.value())

    def average(self, string):
        string = string.split()
        final_val = 0
        for number in string:
            final_val += float(number)

        final_val = final_val/len(string)

        return number

    def warning(self, text):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setWindowIcon(QtGui.QIcon("icon.png"))
        self.msg.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.msg.setText(text)
        self.msg.setWindowTitle("Error")
        self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        self.retval = self.msg.exec_()

    def clear_func(self, number):
        if number == 1:
            self.lineEdit.setValue(0)
            self.lineEdit.clear()
            self.F1text = ""

        elif number == 2:
            self.lineEdit_2.setValue(0)
            self.lineEdit_2.clear()
            self.F2text = ""

        elif number == 3:
            self.lineEdit_3.setValue(0)
            self.lineEdit_3.clear()
            self.Stext = ""

        elif number == 4:
            self.lineEdit_4.setValue(0)
            self.lineEdit_4.clear()
            self.SMtext = ""

        self.label_6.setText("Not set")
        self.calc()


class Ui_Dialog(QtWidgets.QDialog):

    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.setWindowTitle("Details")
        self.setFixedSize(300, 300)
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.gridLayout = QtWidgets.QGridLayout()

        self.buttonBox = QtWidgets.QDialogButtonBox()
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.gridLayout.addWidget(self.buttonBox, 1, 2, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)

        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setPlaceholderText('''100 20 60 80...''')
        font = QtGui.QFont("Segoe UI", 16)
        self.plainTextEdit.setFont(font)
        self.gridLayout.addWidget(self.plainTextEdit, 0, 1, 1, 3)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)

        self.setLayout(self.gridLayout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    GUI = Main()
    app.setStyle('Fusion')

    # Dark Mode
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(240, 240, 240))
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(45, 45, 45))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtGui.QColor(200, 200, 200))
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(200, 200, 200))
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)

    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(37, 110, 217))
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)

    app.setPalette(palette)
    GUI.show()
    sys.exit(app.exec_())