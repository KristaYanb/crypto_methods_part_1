# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gammawin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog13(object):
    def setupUi(self, Dialog13):
        Dialog13.setObjectName("Dialog13")
        Dialog13.resize(1425, 733)
        Dialog13.setMinimumSize(QtCore.QSize(1425, 733))
        Dialog13.setMaximumSize(QtCore.QSize(1425, 733))
        self.rez_encr = QtWidgets.QPlainTextEdit(Dialog13)
        self.rez_encr.setEnabled(True)
        self.rez_encr.setGeometry(QtCore.QRect(350, 360, 561, 151))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.rez_encr.setFont(font)
        self.rez_encr.setReadOnly(True)
        self.rez_encr.setObjectName("rez_encr")
        self.label_2 = QtWidgets.QLabel(Dialog13)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.slova = QtWidgets.QPlainTextEdit(Dialog13)
        self.slova.setGeometry(QtCore.QRect(350, 10, 561, 151))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.slova.setFont(font)
        self.slova.setObjectName("slova")
        self.key = QtWidgets.QPlainTextEdit(Dialog13)
        self.key.setGeometry(QtCore.QRect(350, 250, 561, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.key.setFont(font)
        self.key.setReadOnly(False)
        self.key.setObjectName("key")
        self.but_encr = QtWidgets.QPushButton(Dialog13)
        self.but_encr.setGeometry(QtCore.QRect(130, 360, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.but_encr.setFont(font)
        self.but_encr.setObjectName("but_encr")
        self.dop_inf = QtWidgets.QPlainTextEdit(Dialog13)
        self.dop_inf.setGeometry(QtCore.QRect(940, 170, 441, 371))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.dop_inf.setFont(font)
        self.dop_inf.setReadOnly(True)
        self.dop_inf.setObjectName("dop_inf")
        self.label_3 = QtWidgets.QLabel(Dialog13)
        self.label_3.setGeometry(QtCore.QRect(60, 690, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.key_gen = QtWidgets.QPushButton(Dialog13)
        self.key_gen.setGeometry(QtCore.QRect(520, 210, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.key_gen.setFont(font)
        self.key_gen.setObjectName("key_gen")
        self.rez_decr = QtWidgets.QPlainTextEdit(Dialog13)
        self.rez_decr.setGeometry(QtCore.QRect(350, 530, 561, 151))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.rez_decr.setFont(font)
        self.rez_decr.setReadOnly(True)
        self.rez_decr.setObjectName("rez_decr")
        self.but_decr = QtWidgets.QPushButton(Dialog13)
        self.but_decr.setGeometry(QtCore.QRect(130, 530, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.but_decr.setFont(font)
        self.but_decr.setObjectName("but_decr")
        self.but_clear = QtWidgets.QPushButton(Dialog13)
        self.but_clear.setGeometry(QtCore.QRect(770, 690, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.but_clear.setFont(font)
        self.but_clear.setObjectName("but_clear")
        self.label_4 = QtWidgets.QLabel(Dialog13)
        self.label_4.setGeometry(QtCore.QRect(1020, 120, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog13)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Dialog13)
        self.label.setGeometry(QtCore.QRect(350, 170, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(Dialog13)
        self.label_6.setGeometry(QtCore.QRect(550, 170, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog13)
        self.label_7.setGeometry(QtCore.QRect(760, 170, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.down_file = QtWidgets.QPushButton(Dialog13)
        self.down_file.setGeometry(QtCore.QRect(130, 60, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.down_file.setFont(font)
        self.down_file.setObjectName("down_file")
        self.up_file = QtWidgets.QPushButton(Dialog13)
        self.up_file.setGeometry(QtCore.QRect(130, 420, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.up_file.setFont(font)
        self.up_file.setObjectName("up_file")
        self.gen_a = QtWidgets.QLineEdit(Dialog13)
        self.gen_a.setGeometry(QtCore.QRect(390, 170, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.gen_a.setFont(font)
        self.gen_a.setObjectName("gen_a")
        self.gen_b = QtWidgets.QLineEdit(Dialog13)
        self.gen_b.setGeometry(QtCore.QRect(590, 170, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.gen_b.setFont(font)
        self.gen_b.setObjectName("gen_b")
        self.gen_m = QtWidgets.QLineEdit(Dialog13)
        self.gen_m.setGeometry(QtCore.QRect(810, 170, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.gen_m.setFont(font)
        self.gen_m.setObjectName("gen_m")
        self.key_to_file = QtWidgets.QPushButton(Dialog13)
        self.key_to_file.setGeometry(QtCore.QRect(700, 310, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.key_to_file.setFont(font)
        self.key_to_file.setObjectName("key_to_file")
        self.key_from_file = QtWidgets.QPushButton(Dialog13)
        self.key_from_file.setGeometry(QtCore.QRect(350, 310, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.key_from_file.setFont(font)
        self.key_from_file.setObjectName("key_from_file")
        self.label_8 = QtWidgets.QLabel(Dialog13)
        self.label_8.setGeometry(QtCore.QRect(100, 560, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.but_proc_file = QtWidgets.QPushButton(Dialog13)
        self.but_proc_file.setGeometry(QtCore.QRect(130, 260, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.but_proc_file.setFont(font)
        self.but_proc_file.setObjectName("but_proc_file")

        self.retranslateUi(Dialog13)
        QtCore.QMetaObject.connectSlotsByName(Dialog13)

    def retranslateUi(self, Dialog13):
        _translate = QtCore.QCoreApplication.translate
        Dialog13.setWindowTitle(_translate("Dialog13", "?????????? ????????????????????????"))
        self.label_2.setText(_translate("Dialog13", "?????????????? ?????????? ?????? ????????????????????:"))
        self.but_encr.setText(_translate("Dialog13", "??????????????????????"))
        self.label_3.setText(_translate("Dialog13", "* ?????????????????????????? ?????????????? ???? ???????????? ???????????????????????????? ????????????"))
        self.key_gen.setText(_translate("Dialog13", "?????????????????????????? ????????"))
        self.but_decr.setText(_translate("Dialog13", "????????????????????????"))
        self.but_clear.setText(_translate("Dialog13", "???????????????? ??????"))
        self.label_4.setText(_translate("Dialog13", "???????????????????????????? ????????????????????:"))
        self.label_5.setText(_translate("Dialog13", "?????????????????? ?????? ?????????????????? ??????????:"))
        self.label.setText(_translate("Dialog13", "a = "))
        self.label_6.setText(_translate("Dialog13", "b = "))
        self.label_7.setText(_translate("Dialog13", "m = "))
        self.down_file.setText(_translate("Dialog13", "?????????????????? ???? ??????????"))
        self.up_file.setText(_translate("Dialog13", "?????????????????? ?? ????????"))
        self.key_to_file.setText(_translate("Dialog13", "?????????????????? ????????"))
        self.key_from_file.setText(_translate("Dialog13", "?????????????????? ????????"))
        self.label_8.setText(_translate("Dialog13", "* ??????????, ?????? ???????? ????????????????????????"))
        self.but_proc_file.setText(_translate("Dialog13", "???????????????????? ????????"))
