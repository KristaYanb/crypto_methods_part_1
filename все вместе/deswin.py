# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deswin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog16(object):
    def setupUi(self, Dialog16):
        Dialog16.setObjectName("Dialog16")
        Dialog16.resize(1100, 700)
        Dialog16.setMinimumSize(QtCore.QSize(1100, 700))
        Dialog16.setMaximumSize(QtCore.QSize(1100, 700))
        self.but_clear = QtWidgets.QPushButton(Dialog16)
        self.but_clear.setGeometry(QtCore.QRect(880, 600, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.but_clear.setFont(font)
        self.but_clear.setObjectName("but_clear")
        self.key_gen = QtWidgets.QPushButton(Dialog16)
        self.key_gen.setGeometry(QtCore.QRect(720, 120, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.key_gen.setFont(font)
        self.key_gen.setObjectName("key_gen")
        self.down_file = QtWidgets.QPushButton(Dialog16)
        self.down_file.setGeometry(QtCore.QRect(60, 550, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.down_file.setFont(font)
        self.down_file.setObjectName("down_file")
        self.label_2 = QtWidgets.QLabel(Dialog16)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.key_from_file = QtWidgets.QPushButton(Dialog16)
        self.key_from_file.setGeometry(QtCore.QRect(580, 120, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.key_from_file.setFont(font)
        self.key_from_file.setObjectName("key_from_file")
        self.slova = QtWidgets.QPlainTextEdit(Dialog16)
        self.slova.setGeometry(QtCore.QRect(170, 50, 381, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.slova.setFont(font)
        self.slova.setObjectName("slova")
        self.key_to_file = QtWidgets.QPushButton(Dialog16)
        self.key_to_file.setGeometry(QtCore.QRect(910, 120, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.key_to_file.setFont(font)
        self.key_to_file.setObjectName("key_to_file")
        self.but_encr = QtWidgets.QPushButton(Dialog16)
        self.but_encr.setGeometry(QtCore.QRect(660, 470, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.but_encr.setFont(font)
        self.but_encr.setObjectName("but_encr")
        self.key = QtWidgets.QPlainTextEdit(Dialog16)
        self.key.setGeometry(QtCore.QRect(640, 50, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.key.setFont(font)
        self.key.setReadOnly(False)
        self.key.setObjectName("key")
        self.but_decr = QtWidgets.QPushButton(Dialog16)
        self.but_decr.setGeometry(QtCore.QRect(890, 470, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.but_decr.setFont(font)
        self.but_decr.setObjectName("but_decr")
        self.rez_encr = QtWidgets.QPlainTextEdit(Dialog16)
        self.rez_encr.setEnabled(True)
        self.rez_encr.setGeometry(QtCore.QRect(170, 170, 381, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.rez_encr.setFont(font)
        self.rez_encr.setReadOnly(True)
        self.rez_encr.setObjectName("rez_encr")
        self.up_file = QtWidgets.QPushButton(Dialog16)
        self.up_file.setGeometry(QtCore.QRect(400, 550, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.up_file.setFont(font)
        self.up_file.setObjectName("up_file")
        self.label_4 = QtWidgets.QLabel(Dialog16)
        self.label_4.setGeometry(QtCore.QRect(580, 0, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog16)
        self.label_5.setGeometry(QtCore.QRect(630, 180, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.progressBar = QtWidgets.QProgressBar(Dialog16)
        self.progressBar.setGeometry(QtCore.QRect(20, 640, 1061, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_6 = QtWidgets.QLabel(Dialog16)
        self.label_6.setGeometry(QtCore.QRect(430, 590, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog16)
        self.label_7.setGeometry(QtCore.QRect(210, 0, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog16)
        self.label_8.setGeometry(QtCore.QRect(240, 390, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog16)
        self.label_9.setGeometry(QtCore.QRect(90, 440, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(Dialog16)
        self.label_11.setGeometry(QtCore.QRect(420, 440, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.inp_file = QtWidgets.QPlainTextEdit(Dialog16)
        self.inp_file.setGeometry(QtCore.QRect(20, 470, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.inp_file.setFont(font)
        self.inp_file.setReadOnly(True)
        self.inp_file.setObjectName("inp_file")
        self.out_file = QtWidgets.QPlainTextEdit(Dialog16)
        self.out_file.setGeometry(QtCore.QRect(360, 470, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.out_file.setFont(font)
        self.out_file.setReadOnly(True)
        self.out_file.setObjectName("out_file")
        self.label_10 = QtWidgets.QLabel(Dialog16)
        self.label_10.setGeometry(QtCore.QRect(30, 160, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.rez_decr = QtWidgets.QPlainTextEdit(Dialog16)
        self.rez_decr.setEnabled(True)
        self.rez_decr.setGeometry(QtCore.QRect(170, 290, 381, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.rez_decr.setFont(font)
        self.rez_decr.setReadOnly(True)
        self.rez_decr.setObjectName("rez_decr")
        self.label_12 = QtWidgets.QLabel(Dialog16)
        self.label_12.setGeometry(QtCore.QRect(20, 280, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog16)
        self.label_13.setGeometry(QtCore.QRect(570, 270, 521, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.vect = QtWidgets.QPlainTextEdit(Dialog16)
        self.vect.setEnabled(False)
        self.vect.setGeometry(QtCore.QRect(630, 320, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.vect.setFont(font)
        self.vect.setUndoRedoEnabled(True)
        self.vect.setReadOnly(False)
        self.vect.setObjectName("vect")
        self.vect_gen = QtWidgets.QPushButton(Dialog16)
        self.vect_gen.setEnabled(False)
        self.vect_gen.setGeometry(QtCore.QRect(720, 390, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.vect_gen.setFont(font)
        self.vect_gen.setObjectName("vect_gen")
        self.ECBradioButton = QtWidgets.QRadioButton(Dialog16)
        self.ECBradioButton.setGeometry(QtCore.QRect(630, 230, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ECBradioButton.setFont(font)
        self.ECBradioButton.setChecked(True)
        self.ECBradioButton.setObjectName("ECBradioButton")
        self.CBCradioButton = QtWidgets.QRadioButton(Dialog16)
        self.CBCradioButton.setGeometry(QtCore.QRect(720, 230, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CBCradioButton.setFont(font)
        self.CBCradioButton.setObjectName("CBCradioButton")
        self.CFBradioButton = QtWidgets.QRadioButton(Dialog16)
        self.CFBradioButton.setGeometry(QtCore.QRect(820, 230, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CFBradioButton.setFont(font)
        self.CFBradioButton.setObjectName("CFBradioButton")
        self.OFBradioButton = QtWidgets.QRadioButton(Dialog16)
        self.OFBradioButton.setGeometry(QtCore.QRect(920, 230, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OFBradioButton.setFont(font)
        self.OFBradioButton.setObjectName("OFBradioButton")

        self.retranslateUi(Dialog16)
        QtCore.QMetaObject.connectSlotsByName(Dialog16)

    def retranslateUi(self, Dialog16):
        _translate = QtCore.QCoreApplication.translate
        Dialog16.setWindowTitle(_translate("Dialog16", "DES"))
        self.but_clear.setText(_translate("Dialog16", "???????????????? ??????"))
        self.key_gen.setText(_translate("Dialog16", "??????????????????????????"))
        self.down_file.setText(_translate("Dialog16", "?????????????? ????????"))
        self.label_2.setText(_translate("Dialog16", "?????????????? ??????????:"))
        self.key_from_file.setText(_translate("Dialog16", "??????????????????"))
        self.key_to_file.setText(_translate("Dialog16", "??????????????????"))
        self.but_encr.setText(_translate("Dialog16", "??????????????????????"))
        self.but_decr.setText(_translate("Dialog16", "????????????????????????"))
        self.up_file.setText(_translate("Dialog16", "?????????????? ????????"))
        self.label_4.setText(_translate("Dialog16", "???????????? (??????????????, ???????????????????????? ?????? ??????????????????):"))
        self.label_5.setText(_translate("Dialog16", "???????????????? ?????????? ???????????? ??????????????????:"))
        self.label_6.setText(_translate("Dialog16", "???????????????? ????????????????????:"))
        self.label_7.setText(_translate("Dialog16", "???????????? ?? ???????????? ?????? ??????????:"))
        self.label_8.setText(_translate("Dialog16", "???????????? ?? ??????????????:"))
        self.label_9.setText(_translate("Dialog16", "?????????????? ????????:"))
        self.label_11.setText(_translate("Dialog16", "???????????????? ????????:"))
        self.label_10.setText(_translate("Dialog16", "??????????????????????:"))
        self.label_12.setText(_translate("Dialog16", "????????????????????????:"))
        self.label_13.setText(_translate("Dialog16", "???????????? ?????????????????????????? (?????????????? ?????? ????????????????????????):"))
        self.vect_gen.setText(_translate("Dialog16", "??????????????????????????"))
        self.ECBradioButton.setText(_translate("Dialog16", "ECB"))
        self.CBCradioButton.setText(_translate("Dialog16", "CBC"))
        self.CFBradioButton.setText(_translate("Dialog16", "CFB"))
        self.OFBradioButton.setText(_translate("Dialog16", "OFB"))
