# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AiGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1362, 705)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Coding = QtWidgets.QLabel(Form)
        self.Coding.setGeometry(QtCore.QRect(30, 20, 141, 71))
        self.Coding.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.Coding.setAlignment(QtCore.Qt.AlignCenter)
        self.Coding.setObjectName("Coding")
        self.Title = QtWidgets.QLabel(Form)
        self.Title.setGeometry(QtCore.QRect(690, 10, 671, 71))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(24)
        self.Title.setFont(font)
        self.Title.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Title.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 0, 0);")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.arcLabelCenter = QtWidgets.QLabel(Form)
        self.arcLabelCenter.setGeometry(QtCore.QRect(480, 100, 411, 391))
        self.arcLabelCenter.setText("")
        self.arcLabelCenter.setPixmap(QtGui.QPixmap("GuiFinal/arc.gif"))
        self.arcLabelCenter.setAlignment(QtCore.Qt.AlignCenter)
        self.arcLabelCenter.setObjectName("arcLabelCenter")
        self.ExitButton = QtWidgets.QPushButton(Form)
        self.ExitButton.setGeometry(QtCore.QRect(1140, 630, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ExitButton.setFont(font)
        self.ExitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ExitButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ExitButton.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-color:  rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-width: 1px 1px 1px 1px;")
        self.ExitButton.setObjectName("ExitButton")
        self.FrameBtn = QtWidgets.QLabel(Form)
        self.FrameBtn.setGeometry(QtCore.QRect(10, -130, 111, 90))
        self.FrameBtn.setMaximumSize(QtCore.QSize(1110, 90))
        self.FrameBtn.setStyleSheet("background-color:transparent;")
        self.FrameBtn.setText("")
        self.FrameBtn.setPixmap(QtGui.QPixmap("GuiFinal/frame1_flip.png"))
        self.FrameBtn.setObjectName("FrameBtn")
        self.StartButton = QtWidgets.QPushButton(Form)
        self.StartButton.setEnabled(True)
        self.StartButton.setGeometry(QtCore.QRect(1140, 550, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.StartButton.setFont(font)
        self.StartButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.StartButton.setAccessibleDescription("")
        self.StartButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.StartButton.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-color:  rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-width: 1px 1px 1px 1px;")
        self.StartButton.setObjectName("StartButton")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 350, 621, 341))
        self.frame.setStyleSheet("background-color: transparent;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.EnterButton = QtWidgets.QPushButton(self.frame)
        self.EnterButton.setGeometry(QtCore.QRect(510, 290, 101, 31))
        self.EnterButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EnterButton.setMouseTracking(False)
        self.EnterButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.EnterButton.setStyleSheet("background-color:transparent;\n"
"color: rgb(255, 255, 255);\n"
"border-color:  rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-width: 1px 1px 1px 1px;")
        self.EnterButton.setObjectName("EnterButton")
        self.UserInput = QtWidgets.QLineEdit(self.frame)
        self.UserInput.setGeometry(QtCore.QRect(0, 290, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.UserInput.setFont(font)
        self.UserInput.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"\n"
"border-color:  rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-width: 1px 1px 1px 1px;")
        self.UserInput.setObjectName("UserInput")
        self.AiOutput = QtWidgets.QPlainTextEdit(self.frame)
        self.AiOutput.setGeometry(QtCore.QRect(0, 10, 441, 271))
        self.AiOutput.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"\n"
"border-color:  rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-width: 1px 1px 1px 1px;")
        self.AiOutput.setObjectName("AiOutput")
        self.Wave = QtWidgets.QLabel(Form)
        self.Wave.setGeometry(QtCore.QRect(20, 110, 441, 241))
        self.Wave.setText("")
        self.Wave.setPixmap(QtGui.QPixmap("GuiFinal/wave_natural_ai.gif"))
        self.Wave.setScaledContents(True)
        self.Wave.setAlignment(QtCore.Qt.AlignCenter)
        self.Wave.setObjectName("Wave")
        self.micLabel = QtWidgets.QLabel(Form)
        self.micLabel.setGeometry(QtCore.QRect(910, 110, 421, 241))
        self.micLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.micLabel.setText("")
        self.micLabel.setPixmap(QtGui.QPixmap("GuiFinal/mic.gif"))
        self.micLabel.setScaledContents(True)
        self.micLabel.setObjectName("micLabel")
        self.Earth = QtWidgets.QLabel(Form)
        self.Earth.setGeometry(QtCore.QRect(50, 100, 401, 241))
        self.Earth.setText("")
        self.Earth.setPixmap(QtGui.QPixmap("GuiFinal/LoadingEarth.gif"))
        self.Earth.setScaledContents(True)
        self.Earth.setObjectName("Earth")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Coding.setText(_translate("Form", "coding label"))
        self.Title.setText(_translate("Form", "SMART VIRTUAL ASSISTANT"))
        self.ExitButton.setText(_translate("Form", "EXIT"))
        self.StartButton.setText(_translate("Form", "START"))
        self.EnterButton.setText(_translate("Form", "ENTER"))
        self.UserInput.setText(_translate("Form", "Enter Command Here"))
        self.AiOutput.setPlainText(_translate("Form", "Terminal Output goes here"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
