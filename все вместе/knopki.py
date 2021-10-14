import sys
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
from math import sqrt
import pyecm
from sympy.ntheory import totient, isprime

from design import Ui_MainWindow
from cezarwin import Ui_Dialog
from atbashwin import Ui_Dialog2
from scitalawin import Ui_Dialog3
from polibiiwin import Ui_Dialog4
from albertiwin import Ui_Dialog8
from rishelwin import Ui_Dialog9
from vigenerwin import Ui_Dialog5
from gronsfwin import Ui_Dialog6
from pleifwin import Ui_Dialog7
from cardanowin import Ui_Dialog10
from hillwin import Ui_Dialog11
from vernamwin import Ui_Dialog12
from gammawin import Ui_Dialog13
from freqwin import Ui_Dialog14
from pol_alfwin import Ui_Dialog15
from deswin import Ui_Dialog16
from gostwin import Ui_Dialog17
from thofnumwin import Ui_Dialog18
from rsawin import Ui_Dialog19
from diffiewin import Ui_Dialog20
from shamirwin import Ui_Dialog21
from gamalwin import Ui_Dialog22

from atbash import codingAtbash
from scitala import codingScitala, decodingScitala
from cezar import codingCezar, decodingCezar
from polibii import codingPolibii, decodingPolibii
#from polibii2 import codingPolibii2, decodingPolibii2
from polibii3 import codingPolibii3, decodingPolibii3
from rishele import codingRishel, decodingRishel
from alberti import codingAlberti, decodingAlberti
from vigenere import codingVigener, decodingVigener
from gronsf import codingGronsf, decodingGronsf
from pleifer import codingPleif, decodingPleif
from cardano import codingCardano, decodingCardano, do_matr
from hill_new import codingHill, decodingHill
from vernam import codingVernam,decodingVernam
from gamma_new import codingGamma, codingGammaFile
from freq import decodingFreq, print_gist, zamena
from polalf import index_similar, kas, autocor, decodingVig, prepare, search_key_ind
from des import codingDES, decodingDES
from gost import codingGOST, decodingGOST
from thofnum import degree, NOD, invers, degree2, NOD2, invers2, IsPrime, PrimeFerma, gen_prime, PrimeFerma_big
from rsa import codingRSA, decodingRSA, NOD, degree, invers
from diffie import generate_q
from shamir import codingShamir
from gamal import codingGamal, decodingGamal

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)

        self.ui.simradioButton.toggled.connect(self._sim)
        self.ui.asimradioButton.toggled.connect(self._asim)

    def _sim(self):
        self.ui.simcomboBox.setEnabled(True)
        self.ui.asimcomboBox.setEnabled(False)

    def _asim(self):
        self.ui.simcomboBox.setEnabled(False)
        self.ui.asimcomboBox.setEnabled(True)

    def btnClicked(self):

        if self.ui.simradioButton.isChecked():

            if self.ui.simcomboBox.currentText() == "Атбаш":
                self.atb = atbashwindow()
                self.atb.show()

            if self.ui.simcomboBox.currentText() == "Цезарь":
                self.cez = cezarwindow()
                self.cez.show()

            if self.ui.simcomboBox.currentText() == "Сцитала":
                self.sci = scitalawindow()
                self.sci.show()

            if self.ui.simcomboBox.currentText() == "Квадрат Полибия":
                self.pol = polibiiwindow()
                self.pol.show()

            if self.ui.simcomboBox.currentText() == "Ришелье":
                self.rish = rishelwindow()
                self.rish.show()

            if self.ui.simcomboBox.currentText() == "Диск Альберти":
                self.alb = albertiwindow()
                self.alb.show()

            if self.ui.simcomboBox.currentText() == "Вижинер":
                self.vig = vigenerwindow()
                self.vig.show()

            if self.ui.simcomboBox.currentText() == "Гронсфельд":
                self.gron = gronsfwindow()
                self.gron.show()

            if self.ui.simcomboBox.currentText() == "Плейфер":
                self.pleif = pleifwindow()
                self.pleif.show()

            if self.ui.simcomboBox.currentText() == "Кардано":
                self.card = cardanowindow()
                self.card.show()

            if self.ui.simcomboBox.currentText() == "Хилл":
                self.hil = hillwindow()
                self.hil.show()

            if self.ui.simcomboBox.currentText() == "Вернам":
                self.vern = vernamwindow()
                self.vern.show()

            if self.ui.simcomboBox.currentText() == "Метод гаммирования":
                self.gam = gammawindow()
                self.gam.show()

            if self.ui.simcomboBox.currentText() == "Частотный криптоанализ":
                self.fre = freqwindow()
                self.fre.show()

            if self.ui.simcomboBox.currentText() == "Полиалфавитный криптоанализ":
                self.fre = pol_alfwindow()
                self.fre.show()

            if self.ui.simcomboBox.currentText() == "DES":
                self.des = deswindow()
                self.des.show()

            if self.ui.simcomboBox.currentText() == "ГОСТ 28147-89":
                self.gost = gostwindow()
                self.gost.show()

        if self.ui.asimradioButton.isChecked():

            if self.ui.asimcomboBox.currentText() == "Теория чисел":
                self.thofnum = thofnumwindow()
                self.thofnum.show()

            if self.ui.asimcomboBox.currentText() == "RSA":
                self.rsa = rsawindow()
                self.rsa.show()

            if self.ui.asimcomboBox.currentText() == "Диффи-Хеллман":
                self.diffie = diffiewindow()
                self.diffie.show()

            if self.ui.asimcomboBox.currentText() == "Шифр Шамира":
                self.shamir = shamirwindow()
                self.shamir.show()

            if self.ui.asimcomboBox.currentText() == "Шифр Эль-Гамаля":
                self.gamal = gamalwindow()
                self.gamal.show()

class atbashwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(atbashwindow, self).__init__()
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self)
        self.ui.but_encr.clicked.connect(self.but_encr)
        self.ui.but_decr.clicked.connect(self.but_decr)
        self.ui.but_clear.clicked.connect(self.but_clear)

    def but_encr(self):
        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        for i in range(0, len(self.ui.slova.toPlainText())):
            if ord((self.ui.slova.toPlainText())[i]) in range(15, 31) or ord((self.ui.slova.toPlainText())[i]) in range(128, 191):
                #ord((self.ui.slova.toPlainText())[i]) in range(0, 11) or
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите буквенный текст!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None
        self.ui.rez_encr.setPlainText(codingAtbash(self.ui.slova.toPlainText()))

    def but_decr(self):
        if (self.ui.rez_encr.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        for i in range(0, len(self.ui.slova.toPlainText())):
            if ord((self.ui.slova.toPlainText())[i]) in range(14, 31) or ord((self.ui.slova.toPlainText())[i]) in range(128, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите буквенный текст!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None
        self.ui.rez_decr.setPlainText(codingAtbash(self.ui.rez_encr.toPlainText()))

    def but_clear(self):
        self.ui.slova.clear()
        self.ui.rez_decr.clear()
        self.ui.rez_encr.clear()

class cezarwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(cezarwindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.but_encr.clicked.connect(self.but_encr)
        self.ui.but_decr.clicked.connect(self.but_decr)
        self.ui.but_clear.clicked.connect(self.but_clear)

    def but_encr(self):
        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        for i in range(0, len(self.ui.slova.toPlainText())):
            if ord((self.ui.slova.toPlainText())[i]) in range(14, 31) or ord((self.ui.slova.toPlainText())[i]) in range(128, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите буквенный текст!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None

        number = self.ui.key.text()
        try:
            number = int(number)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None

        self.ui.rez_encr.setPlainText(codingCezar(self.ui.slova.toPlainText(), int(self.ui.key.text())))

    def but_decr(self):
        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        for i in range(0, len(self.ui.slova.toPlainText())):
            if ord((self.ui.slova.toPlainText())[i]) in range(14, 31) or ord((self.ui.slova.toPlainText())[i]) in range(128, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите буквенный текст!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None

        number = self.ui.key.text()
        try:
            number = int(number)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None

        self.ui.rez_decr.setPlainText(decodingCezar(self.ui.rez_encr.toPlainText(), int(self.ui.key.text())))

    def but_clear(self):
        self.ui.key.clear()
        self.ui.slova.clear()
        self.ui.rez_decr.clear()
        self.ui.rez_encr.clear()

class scitalawindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(scitalawindow, self).__init__()
        self.ui = Ui_Dialog3()
        self.ui.setupUi(self)
        self.ui.but_encr.clicked.connect(self.but_encr)
        self.ui.but_decr.clicked.connect(self.but_decr)
        self.ui.but_clear.clicked.connect(self.but_clear)

    def but_encr(self):
        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        for i in range(0, len(self.ui.slova.toPlainText())):
            if (self.ui.slova.toPlainText())[i] == "*" or ord((self.ui.slova.toPlainText())[i]) in range(14, 31) or ord((self.ui.slova.toPlainText())[i]) in range(128, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите буквенный текст!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None

        number = self.ui.key.text()
        try:
            number = int(number)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if int(number) < 1:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число больше 0!", QtWidgets.QMessageBox.Ok)
            return None
        if int(number) > len(self.ui.slova.toPlainText()):
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Диаметр должен быть меньше длины сообщения!", QtWidgets.QMessageBox.Ok)
            return None

        rez = codingScitala(self.ui.slova.toPlainText(), int(self.ui.key.text()))
        self.ui.rez_encr.setPlainText(rez.replace("*", ""))

    def but_decr(self):
        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        for i in range(0, len(self.ui.slova.toPlainText())):
            if ord((self.ui.slova.toPlainText())[i]) in range(14, 31) or ord((self.ui.slova.toPlainText())[i]) in range(128, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите буквенный текст!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None

        number = self.ui.key.text()
        try:
            number = int(number)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if int(number) < 1:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число больше 0!", QtWidgets.QMessageBox.Ok)
            return None
        if int(number) > len(self.ui.slova.toPlainText()):
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Диаметр должен быть меньше длины сообщения!", QtWidgets.QMessageBox.Ok)
            return None

        rez = codingScitala(self.ui.slova.toPlainText(), int(self.ui.key.text()))
        while rez[len(rez)-1]=="*":
            count = len(rez)-1
            rez = rez[:count]
            print(rez)

        rez2 = decodingScitala(rez, int(self.ui.key.text()))
        self.ui.rez_decr.setPlainText(rez2.replace("*", ""))

    def but_clear(self):
        self.ui.key.clear()
        self.ui.slova.clear()
        self.ui.rez_decr.clear()
        self.ui.rez_encr.clear()

class polibiiwindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(polibiiwindow, self).__init__()
        self.ui = Ui_Dialog4()
        self.ui.setupUi(self)
        self.ui.but_encr.clicked.connect(self.but_encr)
        self.ui.but_decr.clicked.connect(self.but_decr)
        self.ui.but_clear.clicked.connect(self.but_clear)

    def but_encr(self):
        arr1_1 = "abcdefghijklmnopqrstuvwxyz"
        arr2_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        arr3_3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        arr4_4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0

        for i in self.ui.slova.toPlainText():
            if i in arr1_1:
                count1 += 1
            if i in arr2_2:
                count2 += 1
            if i in arr3_3:
                count3 += 1
            if i in arr4_4:
                count4 += 1
        if (count1 > 0 and count2 > 0) or (count1 > 0 and count3 > 0) or (count1 > 0 and count4 > 0) or (
                count2 > 0 and count3 > 0) or (count2 > 0 and count4 > 0) or (count3 > 0 and count4 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите текст, используя один алфавит!", QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        for i in range(0, len(self.ui.slova.toPlainText())):
            if ord((self.ui.slova.toPlainText())[i]) in range(14, 31) or ord((self.ui.slova.toPlainText())[i]) in range(128, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите буквенный текст!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None

        #для 2 и 3 методов
        rez1, rez2 = codingPolibii3(self.ui.slova.toPlainText())
        self.ui.rez_encr.setPlainText(rez2)

        #для 1 метода
        #rez = codingPolibii(self.ui.slova.toPlainText())
        #self.ui.rez_encr.setPlainText(rez)

    def but_decr(self):
        if (self.ui.rez_encr.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)

        #для 2 и 3 методов
        rez1, rez2 = codingPolibii3(self.ui.slova.toPlainText())
        arr1_1 = "abcdefghijklmnopqrstuvwxyz"
        arr2_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        arr3_3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        arr4_4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        for i in rez2:
            if i in arr1_1:
                count1 += 1
            if i in arr2_2:
                count2 += 1
            if i in arr3_3:
                count3 += 1
            if i in arr4_4:
                count4 += 1

        self.ui.rez_decr.setPlainText(decodingPolibii3(rez1, rez2,count1,count2,count3,count4))  #для 2 и 3 методов

        #для 1 метода
        #rez = codingPolibii(self.ui.slova.toPlainText())
        #self.ui.rez_decr.setPlainText(decodingPolibii(rez))

    def but_clear(self):
        self.ui.slova.clear()
        self.ui.rez_decr.clear()
        self.ui.rez_encr.clear()

class cardanowindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(cardanowindow, self).__init__()
        self.ui = Ui_Dialog10()
        self.ui.setupUi(self)
        self.ui.but_encr.clicked.connect(self.but_encr)
        self.ui.but_decr.clicked.connect(self.but_decr)
        self.ui.but_clear.clicked.connect(self.but_clear)
        self.ui.reshetka_btn.clicked.connect(self.reshetka_btn)

    def reshetka_btn(self):
        number = self.ui.key.text()
        try:
            number = int(number)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if int(number) < 1:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число больше 0!", QtWidgets.QMessageBox.Ok)
            return None
        #if int(number) % 2 == 1:
            #QtWidgets.QMessageBox.critical(self, "Ошибка", "Размер решетки должен быть четным числом!",
                                           #QtWidgets.QMessageBox.Ok)
            #return None

        arr = do_matr(self.ui.key.text())
        out = ''
        for i in arr:
            for item in i:
                out += item + ' '
            out += '\n'
        self.ui.reshetka.setPlainText(out)

    def but_encr(self):
        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        for i in range(0, len(self.ui.slova.toPlainText())):
            if ord((self.ui.slova.toPlainText())[i]) in range(14, 31) or ord((self.ui.slova.toPlainText())[i]) in range(128, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите буквенный текст!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None

        if self.ui.reshetka.toPlainText() == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Сгенерируйте решетку!", QtWidgets.QMessageBox.Ok)
            return None

        number = int(self.ui.key.text())

        if self.ui.comboBox.currentText() == "Без мусора":
            if len(self.ui.slova.toPlainText()) % (number * number * 4) != 0:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Размер текста должен быть кратен размеру решетки!",
                                               QtWidgets.QMessageBox.Ok)
                return None

            #if int(number) % 2 == 1:
                #QtWidgets.QMessageBox.critical(self, "Ошибка", "Размер решетки должен быть четным числом!", QtWidgets.QMessageBox.Ok)
                #return None
            self.ui.rez_encr.setPlainText(codingCardano(self.ui.slova.toPlainText(), self.ui.key.text(), self.ui.reshetka.toPlainText()))

        if self.ui.comboBox.currentText() == "С мусором":
            self.ui.rez_encr.setPlainText(codingCardano(self.ui.slova.toPlainText(), self.ui.key.text(), self.ui.reshetka.toPlainText()))

    def but_decr(self):

        if (self.ui.rez_encr.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Пустая строка результата шифрования!", QtWidgets.QMessageBox.Ok)
            return None

        if self.ui.reshetka.toPlainText() == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Сгенерируйте решетку!", QtWidgets.QMessageBox.Ok)
            return None

        number = int(self.ui.key.text())

        if self.ui.comboBox.currentText() == "Без мусора":
            #if int(number) % 2 == 1:
                #QtWidgets.QMessageBox.critical(self, "Ошибка", "Размер решетки должен быть четным числом!",
                                               #QtWidgets.QMessageBox.Ok)
                #return None
            if len(self.ui.rez_encr.toPlainText()) % (number * number * 4) != 0:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Размер текста должен быть кратен размеру решетки!",
                                               QtWidgets.QMessageBox.Ok)
                return None
            self.ui.rez_decr.setPlainText(decodingCardano(self.ui.rez_encr.toPlainText(), self.ui.key.text(), self.ui.reshetka.toPlainText()))

        if self.ui.comboBox.currentText() == "С мусором":
            self.ui.rez_decr.setPlainText(decodingCardano(self.ui.rez_encr.toPlainText(), self.ui.key.text(), self.ui.reshetka.toPlainText()))

    def but_clear(self):
        self.ui.key.clear()
        self.ui.slova.clear()
        self.ui.reshetka.clear()
        self.ui.rez_decr.clear()
        self.ui.rez_encr.clear()

class albertiwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(albertiwindow, self).__init__()
        self.ui = Ui_Dialog8()
        self.ui.setupUi(self)
        self.ui.but_encr.clicked.connect(self.but_encr)
        self.ui.but_decr.clicked.connect(self.but_decr)
        self.ui.but_clear.clicked.connect(self.but_clear)

    def but_encr(self):
        #arr = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"№;%:?*()_-+\\/.,@#$^&[]{}\'<>`~|\t\n '
        arr = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.key.text()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.key_2.text()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        for i in range(0, len(self.ui.slova.toPlainText())):
            if ord((self.ui.slova.toPlainText())[i]) in range(14, 31) or ord((self.ui.slova.toPlainText())[i]) in range(128, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите буквенный текст!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None

        """for i in (self.ui.slova.toPlainText()):
            if i not in arr:
                QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введен недопустимый символ!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                #self.ui.key.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None"""

        for i in (self.ui.key.text()):
            if i not in arr:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите буквенный текст!", QtWidgets.QMessageBox.Ok)
                #self.ui.slova.clear()
                self.ui.key.clear()
                #self.ui.rez_decr.clear()
                #self.ui.rez_encr.clear()
                return None

        for i in (self.ui.key_2.text()):
            if i not in arr:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите буквенный текст!", QtWidgets.QMessageBox.Ok)
                #self.ui.slova.clear()
                self.ui.key_2.clear()
                #self.ui.rez_decr.clear()
                #self.ui.rez_encr.clear()
                return None

        self.ui.rez_encr.setPlainText(codingAlberti(self.ui.slova.toPlainText(), self.ui.key.text(), self.ui.key_2.text()))

    def but_decr(self):
        #arr = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"№;%:?*()_-+\\/.,@#$^&[]{}\'<>`~|\t\n '
        arr = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

        if (self.ui.key.text()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.key_2.text()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        for i in (self.ui.key.text()):
            if i not in arr:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введен недопустимый символ!", QtWidgets.QMessageBox.Ok)
                # self.ui.slova.clear()
                self.ui.key.clear()
                #self.ui.rez_decr.clear()
                #self.ui.rez_encr.clear()
                return None

        for i in (self.ui.key_2.text()):
            if i not in arr:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введен недопустимый символ!", QtWidgets.QMessageBox.Ok)
                # self.ui.slova.clear()
                self.ui.key_2.clear()
                #self.ui.rez_decr.clear()
                #self.ui.rez_encr.clear()
                return None

        self.ui.rez_decr.setPlainText(decodingAlberti(self.ui.rez_encr.toPlainText(), self.ui.key.text(), self.ui.key_2.text()))

    def but_clear(self):
        self.ui.key.clear()
        self.ui.slova.clear()
        self.ui.rez_decr.clear()
        self.ui.rez_encr.clear()

class rishelwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(rishelwindow, self).__init__()
        self.ui = Ui_Dialog9()
        self.ui.setupUi(self)
        self.ui.but_encr.clicked.connect(self.but_encr)
        self.ui.but_decr.clicked.connect(self.but_decr)
        self.ui.but_clear.clicked.connect(self.but_clear)
        self.ui.risheleKeyValidator = QtGui.QRegExpValidator(QtCore.QRegExp("(\(([0-9]+\,)*[0-9]+\))+" ))
        # ("(\(([1-9]+\,{0,1})*[1-9]+\))+")
        self.ui.key.setValidator(self.ui.risheleKeyValidator)

    def but_encr(self):
        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.key.text()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите ключ!", QtWidgets.QMessageBox.Ok)
            return None

        key = re.findall('\(([\d,]*)\)', self.ui.key.text())
        parts = []
        for i in key:
            parts.append([int(j) for j in i.split(',')])

        key_len = 0
        for i in parts:
            key_len += len(i)

        if key_len > len(self.ui.slova.toPlainText()):
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Длина ключа должна быть <= длины текста!", QtWidgets.QMessageBox.Ok)
            return None

        for i in parts:
            for m in range(1, len(i) + 1):
                if m not in i:
                    QtWidgets.QMessageBox.critical(self, "Ошибка", "В записи ключа ошибка!", QtWidgets.QMessageBox.Ok)
                    return None

        self.ui.rez_encr.setPlainText(codingRishel(self.ui.slova.toPlainText(), key))

    def but_decr(self):
        if (self.ui.key.text()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите ключ!", QtWidgets.QMessageBox.Ok)
            return None

        try:
            key = re.findall('\(([\d,]*)\)', self.ui.key.text())
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Ошибка в записи ключа!", QtWidgets.QMessageBox.Ok)
            return None

        parts = []
        for i in key:
            parts.append([int(j) for j in i.split(',')])

        key_len = 0
        for i in parts:
            key_len += len(i)

        if key_len > len(self.ui.rez_encr.toPlainText()):
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Длина ключа должна быть меньше длины текста!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        for i in parts:
            for m in range(1, len(i) + 1):
                if m not in i:
                    QtWidgets.QMessageBox.critical(self, "Ошибка", "В записи ключа ошибка!", QtWidgets.QMessageBox.Ok)
                    return None

        self.ui.rez_decr.setPlainText(decodingRishel(self.ui.rez_encr.toPlainText(), key))

    def but_clear(self):
        self.ui.key.clear()
        self.ui.slova.clear()
        self.ui.rez_decr.clear()
        self.ui.rez_encr.clear()

class vigenerwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(vigenerwindow, self).__init__()
        self.ui = Ui_Dialog5()
        self.ui.setupUi(self)
        self.ui.but_encr.clicked.connect(self.but_encr)
        self.ui.but_decr.clicked.connect(self.but_decr)
        self.ui.but_clear.clicked.connect(self.but_clear)

    def but_encr(self):

        arr1_1 = "abcdefghijklmnopqrstuvwxyz"
        arr2_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        arr3_3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        arr4_4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0

        for i in self.ui.slova.toPlainText():
            if i in arr1_1:
                count1 += 1
            if i in arr2_2:
                count2 += 1
            if i in arr3_3:
                count3 += 1
            if i in arr4_4:
                count4 += 1
        if (count1 > 0 and count2 > 0) or (count1 > 0 and count3 > 0) or (count1 > 0 and count4 > 0) or (
                count2 > 0 and count3 > 0) or (count2 > 0 and count4 > 0) or (count3 > 0 and count4 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите текст, используя один алфавит!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        for i in range(0, len(self.ui.slova.toPlainText())):
            if ord((self.ui.slova.toPlainText())[i]) in range(14, 31) or ord((self.ui.slova.toPlainText())[i]) in range(
                    128, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите буквенный текст!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                #self.ui.key.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None

        count1_1 = 0
        count2_2 = 0
        count3_3 = 0
        count4_4 = 0

        for i in self.ui.key.text():
            if i in arr1_1:
                count1_1 += 1
            if i in arr2_2:
                count2_2 += 1
            if i in arr3_3:
                count3_3 += 1
            if i in arr4_4:
                count4_4 += 1
        if (count1_1 > 0 and count2_2 > 0) or (count1_1 > 0 and count3_3 > 0) or (count1_1 > 0 and count4_4 > 0) or (
                count2_2 > 0 and count3_3 > 0) or (count2_2 > 0 and count4_4 > 0) or (count3_3 > 0 and count4_4 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите ключ, используя один алфавит!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.key.text()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите ключ!", QtWidgets.QMessageBox.Ok)
            return None

        for i in range(0, len(self.ui.key.text())):
            if ord((self.ui.key.text())[i]) in range(0, 64) or ord((self.ui.key.text())[i]) in range(91, 96) or ord((self.ui.key.text())[i]) in range(123, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите буквенный ключ!", QtWidgets.QMessageBox.Ok)
                #self.ui.slova.clear()
                self.ui.key.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None

        if (count1 > 0 and count2_2 > 0) or (count1 > 0 and count3_3 > 0) or (count1 > 0 and count4_4 > 0) or (
                count2 > 0 and count1_1 > 0) or (count2 > 0 and count3_3 > 0) or (count2 > 0 and count4_4 > 0) or (count3 > 0 and count1_1 > 0) or (count3 > 0 and count2_2 > 0) or (count3 > 0 and count4_4 > 0) or (count4 > 0 and count1_1 > 0) or (count4 > 0 and count2_2 > 0) or (count4 > 0 and count3_3 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите текст и ключ, используя один алфавит!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        self.ui.rez_encr.setPlainText(codingVigener(self.ui.slova.toPlainText(), self.ui.key.text()))

    def but_decr(self):
        arr1_1 = "abcdefghijklmnopqrstuvwxyz"
        arr2_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        arr3_3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        arr4_4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0

        for i in self.ui.slova.toPlainText():
            if i in arr1_1:
                count1 += 1
            if i in arr2_2:
                count2 += 1
            if i in arr3_3:
                count3 += 1
            if i in arr4_4:
                count4 += 1

        if (self.ui.rez_encr.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Нечего расшифровывать!", QtWidgets.QMessageBox.Ok)
            return None

        count1_1 = 0
        count2_2 = 0
        count3_3 = 0
        count4_4 = 0

        for i in self.ui.key.text():
            if i in arr1_1:
                count1_1 += 1
            if i in arr2_2:
                count2_2 += 1
            if i in arr3_3:
                count3_3 += 1
            if i in arr4_4:
                count4_4 += 1

        if (count1_1 > 0 and count2_2 > 0) or (count1_1 > 0 and count3_3 > 0) or (count1_1 > 0 and count4_4 > 0) or (
                count2_2 > 0 and count3_3 > 0) or (count2_2 > 0 and count4_4 > 0) or (count3_3 > 0 and count4_4 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите ключ, используя один алфавит!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.key.text()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите ключ!", QtWidgets.QMessageBox.Ok)
            return None

        for i in range(0, len(self.ui.key.text())):
            if ord((self.ui.key.text())[i]) in range(14, 31) or ord((self.ui.key.text())[i]) in range(128, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите буквенный ключ!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                self.ui.key.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None

        if (count1 > 0 and count2_2 > 0) or (count1 > 0 and count3_3 > 0) or (count1 > 0 and count4_4 > 0) or (
                count2 > 0 and count1_1 > 0) or (count2 > 0 and count3_3 > 0) or (count2 > 0 and count4_4 > 0) or (count3 > 0 and count1_1 > 0) or (count3 > 0 and count2_2 > 0) or (count3 > 0 and count4_4 > 0) or (count4 > 0 and count1_1 > 0) or (count4 > 0 and count2_2 > 0) or (count4 > 0 and count3_3 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите текст и ключ, используя один алфавит!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        self.ui.rez_decr.setPlainText(decodingVigener(self.ui.rez_encr.toPlainText(), self.ui.key.text()))

    def but_clear(self):
        self.ui.key.clear()
        self.ui.slova.clear()
        self.ui.rez_decr.clear()
        self.ui.rez_encr.clear()

class gronsfwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(gronsfwindow, self).__init__()
        self.ui = Ui_Dialog6()
        self.ui.setupUi(self)
        self.ui.but_encr.clicked.connect(self.but_encr)
        self.ui.but_decr.clicked.connect(self.but_decr)
        self.ui.but_clear.clicked.connect(self.but_clear)

    def but_encr(self):
        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        for i in range(0, len(self.ui.slova.toPlainText())):
            if ord((self.ui.slova.toPlainText())[i]) in range(14, 31) or ord((self.ui.slova.toPlainText())[i]) in range(128, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите буквенный текст!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None

        number = self.ui.key.text()
        try:
            number = int(number)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите числовой ключ!", QtWidgets.QMessageBox.Ok)
            return None
        if int(number) < 1:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите числовой ключ больше 0!", QtWidgets.QMessageBox.Ok)
            return None

        self.ui.rez_encr.setPlainText(codingGronsf(self.ui.slova.toPlainText(), self.ui.key.text()))

    def but_decr(self):
        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        for i in range(0, len(self.ui.slova.toPlainText())):
            if ord((self.ui.slova.toPlainText())[i]) in range(14, 31) or ord((self.ui.slova.toPlainText())[i]) in range(
                    128, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите буквенный текст!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None

        number = self.ui.key.text()
        try:
            number = int(number)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if int(number) < 1:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число больше 0!", QtWidgets.QMessageBox.Ok)
            return None

        self.ui.rez_decr.setPlainText(decodingGronsf(self.ui.rez_encr.toPlainText(), self.ui.key.text()))

    def but_clear(self):
        self.ui.key.clear()
        self.ui.slova.clear()
        self.ui.rez_decr.clear()
        self.ui.rez_encr.clear()

"""class hillwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(hillwindow, self).__init__()
        self.ui = Ui_Dialog11()
        self.ui.setupUi(self)
        self.ui.but_encr.clicked.connect(self.but_encr)
        self.ui.but_decr.clicked.connect(self.but_decr)
        self.ui.but_clear.clicked.connect(self.but_clear)

    def but_encr(self):

        arr1 = "abcdefghijklmnopqrstuvwxyz_.?"
        arr2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.?"
        arr3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_.,-"
        arr4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя_.,-"

        arr1_1 = "abcdefghijklmnopqrstuvwxyz"
        arr2_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        arr3_3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        arr4_4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0

        for i in self.ui.slova.toPlainText():
            if i in arr1_1:
                count1 += 1
            if i in arr2_2:
                count2 += 1
            if i in arr3_3:
                count3 += 1
            if i in arr4_4:
                count4 += 1
        if (count1 > 0 and count2 > 0) or (count1 > 0 and count3 > 0) or (count1 > 0 and count4 > 0) or (
                count2 > 0 and count3 > 0) or (count2 > 0 and count4 > 0) or (count3 > 0 and count4 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите текст, используя один алфавит!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        for i in range(0, len(self.ui.slova.toPlainText())):
            if ord((self.ui.slova.toPlainText())[i]) in range(14, 31) or ord((self.ui.slova.toPlainText())[i]) in range(
                    128, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите буквенный текст!", QtWidgets.QMessageBox.Ok)
                #self.ui.slova.clear()
                #self.ui.key.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None

        count1_1 = 0
        count2_2 = 0
        count3_3 = 0
        count4_4 = 0

        for i in self.ui.key.text():
            if i in arr1_1:
                count1_1 += 1
            if i in arr2_2:
                count2_2 += 1
            if i in arr3_3:
                count3_3 += 1
            if i in arr4_4:
                count4_4 += 1
        if (count1_1 > 0 and count2_2 > 0) or (count1_1 > 0 and count3_3 > 0) or (count1_1 > 0 and count4_4 > 0) or (
                count2_2 > 0 and count3_3 > 0) or (count2_2 > 0 and count4_4 > 0) or (count3_3 > 0 and count4_4 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите ключ, используя один алфавит!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.key.text()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите ключ!", QtWidgets.QMessageBox.Ok)
            return None

        for i in range(0, len(self.ui.key.text())):
            if ord((self.ui.key.text())[i]) in range(0, 64) or ord((self.ui.key.text())[i]) in range(91, 96) or ord((self.ui.key.text())[i]) in range(123, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите буквенный ключ!", QtWidgets.QMessageBox.Ok)
                #self.ui.slova.clear()
                self.ui.key.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None

        if (count1 > 0 and count2_2 > 0) or (count1 > 0 and count3_3 > 0) or (count1 > 0 and count4_4 > 0) or (
                count2 > 0 and count1_1 > 0) or (count2 > 0 and count3_3 > 0) or (count2 > 0 and count4_4 > 0) or (count3 > 0 and count1_1 > 0) or (count3 > 0 and count2_2 > 0) or (count3 > 0 and count4_4 > 0) or (count4 > 0 and count1_1 > 0) or (count4 > 0 and count2_2 > 0) or (count4 > 0 and count3_3 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите текст и ключ, используя один алфавит!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        number = len(self.ui.key.text())
        number = sqrt(number)
        if (number - int(number) != 0) :
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Длина ключа должна быть квадратом целого числа!", QtWidgets.QMessageBox.Ok)
            return None


        if len(self.ui.slova.toPlainText()) % int(number) != 0:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Размер текста должен быть кратен корню длины ключа!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        self.ui.rez_encr.setPlainText(codingHill(self.ui.slova.toPlainText(), self.ui.key.text()))

    def but_decr(self):
        arr1_1 = "abcdefghijklmnopqrstuvwxyz"
        arr2_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        arr3_3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        arr4_4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0

        for i in self.ui.slova.toPlainText():
            if i in arr1_1:
                count1 += 1
            if i in arr2_2:
                count2 += 1
            if i in arr3_3:
                count3 += 1
            if i in arr4_4:
                count4 += 1

        if (self.ui.rez_encr.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Нечего расшифровывать!", QtWidgets.QMessageBox.Ok)
            return None

        count1_1 = 0
        count2_2 = 0
        count3_3 = 0
        count4_4 = 0

        for i in self.ui.key.text():
            if i in arr1_1:
                count1_1 += 1
            if i in arr2_2:
                count2_2 += 1
            if i in arr3_3:
                count3_3 += 1
            if i in arr4_4:
                count4_4 += 1

        if (count1_1 > 0 and count2_2 > 0) or (count1_1 > 0 and count3_3 > 0) or (count1_1 > 0 and count4_4 > 0) or (
                count2_2 > 0 and count3_3 > 0) or (count2_2 > 0 and count4_4 > 0) or (count3_3 > 0 and count4_4 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите ключ, используя один алфавит!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.key.text()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите ключ!", QtWidgets.QMessageBox.Ok)
            return None

        for i in range(0, len(self.ui.key.text())):
            if ord((self.ui.key.text())[i]) in range(14, 31) or ord((self.ui.key.text())[i]) in range(128, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите буквенный ключ!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                self.ui.key.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None

        if (count1 > 0 and count2_2 > 0) or (count1 > 0 and count3_3 > 0) or (count1 > 0 and count4_4 > 0) or (
                count2 > 0 and count1_1 > 0) or (count2 > 0 and count3_3 > 0) or (count2 > 0 and count4_4 > 0) or (count3 > 0 and count1_1 > 0) or (count3 > 0 and count2_2 > 0) or (count3 > 0 and count4_4 > 0) or (count4 > 0 and count1_1 > 0) or (count4 > 0 and count2_2 > 0) or (count4 > 0 and count3_3 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите текст и ключ, используя один алфавит!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        number = len(self.ui.key.text())
        number = sqrt(number)
        if (number - int(number) != 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Длина ключа должна быть квадратом целого числа!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        if len(self.ui.slova.toPlainText()) % int(number) != 0:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Размер текста должен быть кратен корню длины ключа!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        self.ui.rez_decr.setPlainText(decodingHill(self.ui.rez_encr.toPlainText(), self.ui.key.text()))

    def but_clear(self):
        self.ui.key.clear()
        self.ui.slova.clear()
        self.ui.rez_decr.clear()
        self.ui.rez_encr.clear()"""

class hillwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(hillwindow, self).__init__()
        self.ui = Ui_Dialog11()
        self.ui.setupUi(self)
        self.ui.but_encr.clicked.connect(self.but_encr)
        self.ui.but_decr.clicked.connect(self.but_decr)
        self.ui.but_clear.clicked.connect(self.but_clear)

    def but_encr(self):

        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        for i in range(0, len(self.ui.slova.toPlainText())):
            if ord((self.ui.slova.toPlainText())[i]) in range(14, 31) or ord((self.ui.slova.toPlainText())[i]) in range(
                    128, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите буквенный текст!", QtWidgets.QMessageBox.Ok)
                #self.ui.slova.clear()
                #self.ui.key.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None

        if (self.ui.key.text()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите ключ!", QtWidgets.QMessageBox.Ok)
            return None

        for i in range(0, len(self.ui.key.text())):
            if ord((self.ui.key.text())[i]) in range(14, 31) or ord((self.ui.key.text())[i]) in range(128, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите буквенный ключ!", QtWidgets.QMessageBox.Ok)
                #self.ui.slova.clear()
                self.ui.key.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None

        number = len(self.ui.key.text())
        number = sqrt(number)
        if (number - int(number) != 0) :
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Длина ключа должна быть квадратом целого числа!", QtWidgets.QMessageBox.Ok)
            return None

        if len(self.ui.slova.toPlainText()) % int(number) != 0:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Размер текста должен быть кратен корню длины ключа!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        self.ui.rez_encr.setPlainText(codingHill(self.ui.slova.toPlainText(), self.ui.key.text()))

    def but_decr(self):

        if (self.ui.rez_encr.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Нечего расшифровывать!", QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.key.text()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите ключ!", QtWidgets.QMessageBox.Ok)
            return None

        for i in range(0, len(self.ui.key.text())):
            if ord((self.ui.key.text())[i]) in range(14, 31) or ord((self.ui.key.text())[i]) in range(128, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите буквенный ключ!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                self.ui.key.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None

        number = len(self.ui.key.text())
        number = sqrt(number)
        if (number - int(number) != 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Длина ключа должна быть квадратом целого числа!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        if len(self.ui.slova.toPlainText()) % int(number) != 0:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Размер текста должен быть кратен корню длины ключа!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        self.ui.rez_decr.setPlainText(decodingHill(self.ui.rez_encr.toPlainText(), self.ui.key.text()))

    def but_clear(self):
        self.ui.key.clear()
        self.ui.slova.clear()
        self.ui.rez_decr.clear()
        self.ui.rez_encr.clear()

class pleifwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(pleifwindow, self).__init__()
        self.ui = Ui_Dialog7()
        self.ui.setupUi(self)
        self.ui.but_encr.clicked.connect(self.but_encr)
        self.ui.but_decr.clicked.connect(self.but_decr)
        self.ui.but_clear.clicked.connect(self.but_clear)

    def but_encr(self):
        """arr1_1 = "abcdefghiklmnopqrstuvwxyz"
        arr2_2 = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        arr3_3 = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        arr4_4 = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0

        for i in self.ui.slova.toPlainText():
            if i in arr1_1:
                count1 += 1
            if i in arr2_2:
                count2 += 1
            if i in arr3_3:
                count3 += 1
            if i in arr4_4:
                count4 += 1
        if (count1 > 0 and count2 > 0) or (count1 > 0 and count3 > 0) or (count1 > 0 and count4 > 0) or (
                count2 > 0 and count3 > 0) or (count2 > 0 and count4 > 0) or (count3 > 0 and count4 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите текст, используя один алфавит!",
                                           QtWidgets.QMessageBox.Ok)
            return None"""

        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        """for i in range(0, len(self.ui.slova.toPlainText())):
            if ord((self.ui.slova.toPlainText())[i]) in range(14, 31) or ord((self.ui.slova.toPlainText())[i]) in range(
                    128, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите буквенный текст!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None

        count1_1 = 0
        count2_2 = 0
        count3_3 = 0
        count4_4 = 0

        for i in self.ui.key.text():
            if i in arr1_1:
                count1_1 += 1
            if i in arr2_2:
                count2_2 += 1
            if i in arr3_3:
                count3_3 += 1
            if i in arr4_4:
                count4_4 += 1
        if (count1_1 > 0 and count2_2 > 0) or (count1_1 > 0 and count3_3 > 0) or (count1_1 > 0 and count4_4 > 0) or (
                count2_2 > 0 and count3_3 > 0) or (count2_2 > 0 and count4_4 > 0) or (count3_3 > 0 and count4_4 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите ключ, используя один алфавит!",
                                           QtWidgets.QMessageBox.Ok)
            return None"""

        if (self.ui.key.text()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите ключ!", QtWidgets.QMessageBox.Ok)
            return None

        """for i in range(0, len(self.ui.key.text())):
            if ord((self.ui.key.text())[i]) in range(0, 64) or ord((self.ui.key.text())[i]) in range(91, 96) or ord(
                    (self.ui.key.text())[i]) in range(123, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите буквенный ключ!", QtWidgets.QMessageBox.Ok)
                # self.ui.slova.clear()
                self.ui.key.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None

        if (count1 > 0 and count2_2 > 0) or (count1 > 0 and count3_3 > 0) or (count1 > 0 and count4_4 > 0) or (
                count2 > 0 and count1_1 > 0) or (count2 > 0 and count3_3 > 0) or (count2 > 0 and count4_4 > 0) or (
                count3 > 0 and count1_1 > 0) or (count3 > 0 and count2_2 > 0) or (count3 > 0 and count4_4 > 0) or (
                count4 > 0 and count1_1 > 0) or (count4 > 0 and count2_2 > 0) or (count4 > 0 and count3_3 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите текст и ключ, используя один алфавит!",
                                           QtWidgets.QMessageBox.Ok)
            return None"""

        self.ui.rez_encr.setPlainText(codingPleif(self.ui.slova.toPlainText(), self.ui.key.text()))

    def but_decr(self):

        """arr1_1 = "abcdefghiklmnopqrstuvwxyz"
        arr2_2 = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        arr3_3 = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        arr4_4 = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0

        for i in self.ui.slova.toPlainText():
            if i in arr1_1:
                count1 += 1
            if i in arr2_2:
                count2 += 1
            if i in arr3_3:
                count3 += 1
            if i in arr4_4:
                count4 += 1"""

        if (self.ui.rez_encr.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Нечего расшифровывать!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        """count1_1 = 0
        count2_2 = 0
        count3_3 = 0
        count4_4 = 0

        for i in self.ui.key.text():
            if i in arr1_1:
                count1_1 += 1
            if i in arr2_2:
                count2_2 += 1
            if i in arr3_3:
                count3_3 += 1
            if i in arr4_4:
                count4_4 += 1

        if (count1_1 > 0 and count2_2 > 0) or (count1_1 > 0 and count3_3 > 0) or (count1_1 > 0 and count4_4 > 0) or (
                count2_2 > 0 and count3_3 > 0) or (count2_2 > 0 and count4_4 > 0) or (count3_3 > 0 and count4_4 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите ключ, используя один алфавит!",
                                           QtWidgets.QMessageBox.Ok)
            return None"""

        if (self.ui.key.text()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите ключ!", QtWidgets.QMessageBox.Ok)
            return None

        """for i in range(0, len(self.ui.key.text())):
            if ord((self.ui.key.text())[i]) in range(14, 31) or ord((self.ui.key.text())[i]) in range(128, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите буквенный ключ!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                self.ui.key.clear()
                self.ui.rez_decr.clear()
                self.ui.rez_encr.clear()
                return None

        if (count1 > 0 and count2_2 > 0) or (count1 > 0 and count3_3 > 0) or (count1 > 0 and count4_4 > 0) or (
                count2 > 0 and count1_1 > 0) or (count2 > 0 and count3_3 > 0) or (count2 > 0 and count4_4 > 0) or (
                count3 > 0 and count1_1 > 0) or (count3 > 0 and count2_2 > 0) or (count3 > 0 and count4_4 > 0) or (
                count4 > 0 and count1_1 > 0) or (count4 > 0 and count2_2 > 0) or (count4 > 0 and count3_3 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите текст и ключ, используя один алфавит!",
                                           QtWidgets.QMessageBox.Ok)
            return None"""

        self.ui.rez_decr.setPlainText(decodingPleif(self.ui.rez_encr.toPlainText(), self.ui.key.text()))

    def but_clear(self):
        self.ui.key.clear()
        self.ui.slova.clear()
        self.ui.rez_decr.clear()
        self.ui.rez_encr.clear()

class vernamwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(vernamwindow, self).__init__()
        self.ui = Ui_Dialog12()
        self.ui.setupUi(self)
        self.ui.but_encr.clicked.connect(self.but_encr)
        self.ui.but_decr.clicked.connect(self.but_decr)
        self.ui.but_clear.clicked.connect(self.but_clear)
        self.ui.key_gen.clicked.connect(self.key_gen)

    def key_gen(self):
        #alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"№;%:?*()_-+/.,@#$%^&[]{}<> \n\x9d\x9e\x9f\xa0¡¢£¤¥¦§¨©ª«¬\xad®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüý\x00'
        alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !"#$%&\'()*+,-./0123456789:;<=>?@[\]^_`{|}~№«¬»±§©µ¶¦÷¡¿®×¢£¤¥\n\t\x9d\x9e\x9f\xad°²³·¸¹º¼½¾ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüý'
        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        key = u''

        for i in range(len(self.ui.slova.toPlainText())):
            o = randint(0, 255)
            key += alf[o]

        self.ui.key.setPlainText(key)

    def but_encr(self):
        alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !"#$%&\'()*+,-./0123456789:;<=>?@[\]^_`{|}~№«¬»±§©µ¶¦÷¡¿®×¢£¤¥\n\t\x9d\x9e\x9f\xad°²³·¸¹º¼½¾ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüý'
        for i in (self.ui.key.toPlainText()):
            if i not in alf:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ!", QtWidgets.QMessageBox.Ok)
                self.ui.key.clear()
                return None

        for i in (self.ui.slova.toPlainText()):
            if i not in alf:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                return None

        if len(self.ui.slova.toPlainText()) != len(self.ui.key.toPlainText()):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Длина текста должна быть равна длине ключа!", QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.key.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите ключ!", QtWidgets.QMessageBox.Ok)
            return None

        rez, vivod = codingVernam(self.ui.slova.toPlainText(), self.ui.key.toPlainText())

        self.ui.rez_encr.setPlainText(rez)
        self.ui.dop_inf.setPlainText(vivod)

    def but_decr(self):
        alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !"#$%&\'()*+,-./0123456789:;<=>?@[\]^_`{|}~№«¬»±§©µ¶¦÷¡¿®×¢£¤¥\n\t\x9d\x9e\x9f\xad°²³·¸¹º¼½¾ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüý'
        alf_key = '01'

        for i in (self.ui.key.toPlainText()):
            #if i not in alf_key:
            if i not in alf:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ!", QtWidgets.QMessageBox.Ok)
                self.ui.key.clear()
                return None

        for i in (self.ui.rez_encr.toPlainText()):
            if i not in alf:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                return None

        #if (8*len(self.ui.rez_encr.toPlainText())) != len(self.ui.key.toPlainText()):
        if len(self.ui.rez_encr.toPlainText()) != len(self.ui.key.toPlainText()):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Длина текста должна быть равна длине ключа!", QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.rez_encr.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Пустая строка! Нечего расшифровывать!", QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.key.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите ключ!", QtWidgets.QMessageBox.Ok)
            return None

        rez, vivod = codingVernam(self.ui.rez_encr.toPlainText(), self.ui.key.toPlainText())
        #rez, vivod = decodingVernam(self.ui.rez_encr.toPlainText(), self.ui.key.toPlainText())

        self.ui.rez_decr.setPlainText(rez)
        self.ui.dop_inf.setPlainText(vivod)

    def but_clear(self):
        self.ui.key.clear()
        self.ui.slova.clear()
        self.ui.rez_decr.clear()
        self.ui.rez_encr.clear()

"""class gammawindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(gammawindow, self).__init__()
        self.ui = Ui_Dialog13()
        self.ui.setupUi(self)
        self.ui.but_proc_file.clicked.connect(self.but_proc_file)
        self.ui.but_encr.clicked.connect(self.but_encr)
        self.ui.but_decr.clicked.connect(self.but_decr)
        self.ui.but_clear.clicked.connect(self.but_clear)
        self.ui.key_gen.clicked.connect(self.key_gen)
        self.ui.down_file.clicked.connect(self.down_file)
        self.ui.up_file.clicked.connect(self.up_file)
        self.ui.key_to_file.clicked.connect(self.key_to_file)
        self.ui.key_from_file.clicked.connect(self.key_from_file)

    def key_gen(self):
        chisl = '0123456789'
        for i in self.ui.key.toPlainText():
            if i not in chisl:
                QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите число для генерации!", QtWidgets.QMessageBox.Ok)
                return None
        if (self.ui.gen_a.text() == '') or (self.ui.gen_b.text() == '') or (self.ui.gen_m.text() == ''):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите число для генерации!", QtWidgets.QMessageBox.Ok)
            return None
        for i in self.ui.gen_a.text():
            if i not in chisl:
                QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите число для генерации!", QtWidgets.QMessageBox.Ok)
                return None
        for i in self.ui.gen_b.text():
            if i not in chisl:
                QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите число для генерации!", QtWidgets.QMessageBox.Ok)
                return None
        for i in self.ui.gen_m.text():
            if i not in chisl:
                QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите число для генерации!", QtWidgets.QMessageBox.Ok)
                return None

        if self.ui.key.toPlainText() == '':
            x_i = 0
        else:
            x_i = int(self.ui.key.toPlainText())

        a = int(self.ui.gen_a.text())
        b = int(self.ui.gen_b.text())
        m = int(self.ui.gen_m.text())

        if (x_i >= m) or (x_i < 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Начальное значение д/б <m!", QtWidgets.QMessageBox.Ok)
            return None

        if m < 2:
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Модуль д/б >=2!", QtWidgets.QMessageBox.Ok)
            return None
        if (a >= m) or (a < 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Множитель д/б 0<=a<m!", QtWidgets.QMessageBox.Ok)
            return None
        if (b >= m) or (b < 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Приращение д/б 0<=c<m!", QtWidgets.QMessageBox.Ok)
            return None
        key_ = (a * x_i + b) % m
        if key_ == 0:
            self.ui.key.setPlainText(str('0'))
            return None
        else:
            self.ui.key.setPlainText(str(key_))

    def key_to_file(self):
        alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !"#$%&\'()*+,-./0123456789:;<=>?@[\]^_`{|}~№«¬»±§©µ¶¦÷¡¿®×¢£¤¥\n\t\x9d\x9e\x9f\xad°²³·¸¹º¼½¾ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüý'
        alf_key = '0123456789'

        key = self.ui.key.toPlainText()
        if (self.ui.key.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Сгенерируйте ключ!", QtWidgets.QMessageBox.Ok)
            return None

        for i in (self.ui.key.toPlainText()):
            if i not in alf_key:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                return None

        fileName = QtWidgets.QFileDialog.getSaveFileName(self, 'Сохранить ключ в файл', './')
        if not fileName[0]:
            return None
        file = open(fileName[0], 'wb')
        bin_key = bytes([alf.index(_) for _ in key])
        file.write(bin_key)
        file.close()

    def key_from_file(self):
        alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !"#$%&\'()*+,-./0123456789:;<=>?@[\]^_`{|}~№«¬»±§©µ¶¦÷¡¿®×¢£¤¥\n\t\x9d\x9e\x9f\xad°²³·¸¹º¼½¾ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüý'
        alf_key = '0123456789'

        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Загрузить ключ из файла', './')
        if not fileName[0]:
            return None
        try:
            file = open(fileName[0], 'rb')
        except FileNotFoundError:
            show_messageBox("Такого файла не существует!", "Ошибка!", QtWidgets.QMessageBox.Critical,
                            QtWidgets.QMessageBox.Ok)
            return None

        key = file.read()
        file.close()
        if key:
            text_key = ''
            for i in key:
                if alf[i] not in alf_key:
                    QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ!", QtWidgets.QMessageBox.Ok)
                    return None

                else:
                    text_key += alf[i]
            self.ui.key.setPlainText(text_key)
        else:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Файл пуст!", QtWidgets.QMessageBox.Ok)
            return None

    def but_proc_file(self):
        alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !"#$%&\'()*+,-./0123456789:;<=>?@[\]^_`{|}~№«¬»±§©µ¶¦÷¡¿®×¢£¤¥\n\t\x9d\x9e\x9f\xad°²³·¸¹º¼½¾ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüý'
        alf_key = '0123456789'

        for i in (self.ui.key.toPlainText()):
            if i not in alf_key:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ!", QtWidgets.QMessageBox.Ok)
                self.ui.key.clear()
                return None

        key = self.ui.key.toPlainText()
        if key == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Сгенерируйте ключ!", QtWidgets.QMessageBox.Ok)
            return None

        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Обработать файл', './')
        if not fileName[0]:
            return None
        try:
            inp_file = open(fileName[0], 'rb')
        except FileNotFoundError:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Файла не существует!", QtWidgets.QMessageBox.Ok)
            return None

        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Сохранить файл', './')
        if not fileName[0]:
            return None
        opt_file = open(fileName[0], 'wb')

        inputText = inp_file.read()
        inputText2 = ''
        for i in range(len(inputText)):
            # print(inputText[i])
            inputText2 += alf[int(inputText[i])]
            # print(inputText2)

        if inputText2 != '':
            result, vivod = codingGamma_file(key, inputText2, opt_file=opt_file)
        else:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Файл пуст!", QtWidgets.QMessageBox.Ok)
            return None

        inp_file.close()
        opt_file.close()

        if result is None:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Во входных данных ошибка!", QtWidgets.QMessageBox.Ok)
            return None

        self.ui.dop_inf.setPlainText(vivod)

        #addData = "Ключ: длина {}\n{}\n\nОткрытый текст: длина {}\n{}\n\nШифртекст: длина {}\n{}".format(
            #len(result['bin_key']),
            #result['bin_key'], len(result['bin_input']), result['bin_input'], len(result['bin_output']),
            #result['bin_output'])

        #self.binaryDataTextEditGamma.setText(addData)

    def but_encr(self):
        alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !"#$%&\'()*+,-./0123456789:;<=>?@[\]^_`{|}~№«¬»±§©µ¶¦÷¡¿®×¢£¤¥\n\t\x9d\x9e\x9f\xad°²³·¸¹º¼½¾ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüý'

        for i in (self.ui.slova.toPlainText()):
            if i not in alf:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                return None

        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.key.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Сгенерируйте ключ!", QtWidgets.QMessageBox.Ok)
            return None

        rez, vivod = codingGamma(self.ui.slova.toPlainText(), self.ui.key.toPlainText())

        self.ui.rez_encr.setPlainText(rez)
        self.ui.dop_inf.setPlainText(vivod)

    def but_decr(self):
        alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !"#$%&\'()*+,-./0123456789:;<=>?@[\]^_`{|}~№«¬»±§©µ¶¦÷¡¿®×¢£¤¥\n\t\x9d\x9e\x9f\xad°²³·¸¹º¼½¾ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüý'
        alf_key = '0123456789'

        for i in (self.ui.key.toPlainText()):
            if i not in alf_key:
            #if i not in alf:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ!", QtWidgets.QMessageBox.Ok)
                self.ui.key.clear()
                return None

        for i in (self.ui.rez_encr.toPlainText()):
            if i not in alf:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ!", QtWidgets.QMessageBox.Ok)
                self.ui.slova.clear()
                return None

        if (self.ui.rez_encr.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Нечего расшифровывать!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.key.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Сгенерируйте ключ!", QtWidgets.QMessageBox.Ok)
            return None

        rez, vivod = codingGamma(self.ui.rez_encr.toPlainText(), self.ui.key.toPlainText())
        #rez, vivod = decodingGamma(self.ui.rez_encr.toPlainText(), self.ui.key.toPlainText())

        self.ui.rez_decr.setPlainText(rez)
        self.ui.dop_inf.setPlainText(vivod)

    def down_file(self):
        alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !"#$%&\'()*+,-./0123456789:;<=>?@[\]^_`{|}~№«¬»±§©µ¶¦÷¡¿®×¢£¤¥\n\t\x9d\x9e\x9f\xad°²³·¸¹º¼½¾ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüý'

        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Загрузить входные данные из файла', './')
        if not fileName[0]:
            return
        try:
            file = open(fileName[0], 'rb')
        except FileNotFoundError:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Файла не существует!", QtWidgets.QMessageBox.Ok)
            return None

        inputText = file.read()
        inputText2 = ''
        for i in range(len(inputText)):
            if i not in alf:
                
            print(inputText[i])
            inputText2 += alf[int(inputText[i])]
            print(inputText2)

        if inputText2 != '':
            self.ui.slova.setPlainText(inputText2)
        else:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Файл пуст!", QtWidgets.QMessageBox.Ok)
            return None

        file.close()

    def up_file(self):
        outputText = self.ui.rez_encr.toPlainText()
        if outputText == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустое поле, нечего загружать!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.key.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Сгенерируйте ключ!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        fileName = QtWidgets.QFileDialog.getSaveFileName(self, 'Выгрузить выходные данные в файл', './')
        if not fileName[0]:
            return

        file = open(fileName[0], 'wb')

        rez1, rez2 = codingGamma(self.ui.slova.toPlainText(), self.ui.key.toPlainText(), file=file)
        file.close()

    def but_clear(self):
        self.ui.key.clear()
        self.ui.slova.clear()
        self.ui.rez_decr.clear()
        self.ui.rez_encr.clear()
        self.ui.gen_a.clear()
        self.ui.gen_b.clear()
        self.ui.gen_m.clear()"""

class freqwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(freqwindow, self).__init__()
        self.ui = Ui_Dialog14()
        self.ui.setupUi(self)
        self.ui.but_decr.clicked.connect(self.but_decr)
        self.ui.but_clear.clicked.connect(self.but_clear)
        self.ui.down_file.clicked.connect(self.down_file)
        self.ui.btn_change.clicked.connect(self.btn_change)
        self.ui.btn_gist.clicked.connect(self.btn_gist)

    def but_decr(self):
        arr1 = "abcdefghijklmnopqrstuvwxyz"
        arr2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        arr3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        arr4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0

        for i in self.ui.slova.toPlainText():
            if i in arr1:
                count1 += 1
            if i in arr2:
                count2 += 1
            if i in arr3:
                count3 += 1
            if i in arr4:
                count4 += 1
        if (count1 > 0 and count2 > 0) or (count1 > 0 and count3 > 0) or (count1 > 0 and count4 > 0) or (
                count2 > 0 and count3 > 0) or (count2 > 0 and count4 > 0) or (count3 > 0 and count4 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите текст, используя один алфавит!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Нет данных для дешифрования!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        rez, vivod, podskazka = decodingFreq(self.ui.slova.toPlainText())

        strok_podsk = ''
        for i in podskazka:
            strok_podsk += i + ': '
            for j in range(len(podskazka[i])):
                strok_podsk += podskazka[i][j] + ' '
            strok_podsk += '\n'

        self.ui.rez_decr.setPlainText(rez)
        self.ui.dop_inf.setPlainText(vivod)
        self.ui.podskazka.setPlainText(strok_podsk)

    def btn_gist(self):
        arr1 = "abcdefghijklmnopqrstuvwxyz"
        arr2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        arr3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        arr4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

        freq_ru_h = {'О': 0.1097, 'Е': 0.0845, 'А': 0.0801, 'И': 0.0735, 'Н': 0.0670, 'Т': 0.0626, 'С': 0.0547,
                     'Р': 0.0473,
                     'В': 0.0454, 'Л': 0.0440, 'К': 0.0349, 'М': 0.0321, 'Д': 0.0298, 'П': 0.0281, 'У': 0.0262,
                     'Я': 0.0201,
                     'Ы': 0.0190, 'Ь': 0.0174, 'Г': 0.0170, 'З': 0.0165, 'Б': 0.0159, 'Ч': 0.0144, 'Й': 0.0121,
                     'Х': 0.0097,
                     'Ж': 0.0094, 'Ш': 0.0073, 'Ю': 0.0064, 'Ц': 0.0048, 'Щ': 0.0036, 'Э': 0.0032, 'Ф': 0.0026,
                     'Ъ': 0.0004,
                     'Ё': 0.0004}
        freq_ru_l = {'о': 0.1097, 'е': 0.0845, 'а': 0.0801, 'и': 0.0735, 'н': 0.0670, 'т': 0.0626, 'с': 0.0547,
                     'р': 0.0473, 'в': 0.0454, 'л': 0.0440, 'к': 0.0349, 'м': 0.0321, 'д': 0.0298, 'п': 0.0281,
                     'у': 0.0262, 'я': 0.0201, 'ы': 0.0190, 'ь': 0.0174, 'г': 0.0170, 'з': 0.0165, 'б': 0.0159,
                     'ч': 0.0144, 'й': 0.0121, 'х': 0.0097, 'ж': 0.0094, 'ш': 0.0073, 'ю': 0.0064, 'ц': 0.0048,
                     'щ': 0.0036, 'э': 0.0032, 'ф': 0.0026, 'ъ': 0.0004, 'ё': 0.0004}
        freq_en_h = {'E': 0.1270, 'T': 0.0906, 'A': 0.0817, 'O': 0.0751, 'I': 0.0697, 'N': 0.0675, 'S': 0.0633,
                     'H': 0.0609,
                     'R': 0.0599, 'D': 0.0425, 'L': 0.0403, 'C': 0.0278, 'U': 0.0276, 'M': 0.0241, 'W': 0.0236,
                     'F': 0.0223,
                     'G': 0.0202, 'Y': 0.0197, 'P': 0.0193, 'B': 0.0149, 'V': 0.0098, 'K': 0.0077, 'X': 0.0015,
                     'J': 0.0015,
                     'Q': 0.0010, 'Z': 0.0005}
        freq_en_l = {'e': 0.1270, 't': 0.0906, 'a': 0.0817, 'o': 0.0751, 'i': 0.0697, 'n': 0.0675, 's': 0.0633,
                     'h': 0.0609, 'r': 0.0599, 'd': 0.0425, 'l': 0.0403, 'c': 0.0278, 'u': 0.0276, 'm': 0.0241,
                     'w': 0.0236, 'f': 0.0223, 'g': 0.0202, 'y': 0.0197, 'p': 0.0193, 'b': 0.0149, 'v': 0.0098,
                     'k': 0.0077, 'x': 0.0015, 'j': 0.0015, 'q': 0.0010, 'z': 0.0005}

        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0

        alf = ''
        freq = None
        for i in self.ui.slova.toPlainText():
            if i in arr1:
                count1 += 1
                alf = arr1
                freq = freq_en_l
            if i in arr2:
                count2 += 1
                alf = arr2
                freq = freq_en_h
            if i in arr3:
                count3 += 1
                alf = arr3
                freq = freq_ru_h
            if i in arr4:
                count4 += 1
                alf = arr4
                freq = freq_ru_l
        if (count1 > 0 and count2 > 0) or (count1 > 0 and count3 > 0) or (count1 > 0 and count4 > 0) or (
                count2 > 0 and count3 > 0) or (count2 > 0 and count4 > 0) or (count3 > 0 and count4 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите текст, используя один алфавит!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Нечего обрабатывать!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        print_gist(self.ui.slova.toPlainText(), alf, freq)

    def btn_change(self):
        arr1 = "abcdefghijklmnopqrstuvwxyz"
        arr2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        arr3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        arr4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0

        alf = ''
        for i in self.ui.rez_decr.toPlainText():
            if i in arr1:
                count1 += 1
                alf = arr1
            if i in arr2:
                count2 += 1
                alf = arr2
            if i in arr3:
                count3 += 1
                alf = arr3
            if i in arr4:
                count4 += 1
                alf = arr4

        if (self.ui.rez_decr.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Нечего обрабатывать!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.symb1.text() not in alf) or (self.ui.symb2.text() not in alf):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите только один символ для замены и из одного алфавита!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.symb1.text() not in self.ui.rez_decr.toPlainText()):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Такого символа нет в тексте!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        new_slova = zamena(self.ui.rez_decr.toPlainText(), self.ui.symb1.text(), self.ui.symb2.text(), alf)
        #new_slova = self.ui.rez_decr.toPlainText().replace(self.ui.symb1.text(), self.ui.symb2.text())
        self.ui.rez_decr.setPlainText(new_slova)

    def down_file(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Загрузить входные данные из файла', './')
        if not fileName[0]:
            return
        try:
            file = open(fileName[0], 'r',encoding='utf-8')
        except FileNotFoundError:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Файла не существует!", QtWidgets.QMessageBox.Ok)
            return None

        inputText = file.read()
        file.close()
        self.ui.slova.clear()
        self.ui.slova.setPlainText(inputText)

    def but_clear(self):
        self.ui.slova.clear()
        self.ui.rez_decr.clear()
        self.ui.symb1.clear()
        self.ui.symb2.clear()
        self.ui.dop_inf.clear()

class pol_alfwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(pol_alfwindow, self).__init__()
        self.ui = Ui_Dialog15()
        self.ui.setupUi(self)
        self.ui.but_decr.clicked.connect(self.but_decr)
        self.ui.but_clear.clicked.connect(self.but_clear)
        self.ui.down_file.clicked.connect(self.down_file)
        self.ui.but_decr_index.clicked.connect(self.but_decr_index)
        self.ui.but_decr_autocor.clicked.connect(self.but_decr_autocor)
        self.ui.but_decr_kas.clicked.connect(self.but_decr_kas)
        self.ui.find_key_kas.clicked.connect(self.find_key_kas)

    def but_decr(self):
        arr1_1 = "abcdefghijklmnopqrstuvwxyz"
        arr2_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        arr3_3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        arr4_4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0

        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Нечего расшифровывать!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        for i in self.ui.slova.toPlainText():
            if i in arr1_1:
                count1 += 1
            if i in arr2_2:
                count2 += 1
            if i in arr3_3:
                count3 += 1
            if i in arr4_4:
                count4 += 1

        count1_1 = 0
        count2_2 = 0
        count3_3 = 0
        count4_4 = 0

        for i in self.ui.key.toPlainText():
            if i in arr1_1:
                count1_1 += 1
            if i in arr2_2:
                count2_2 += 1
            if i in arr3_3:
                count3_3 += 1
            if i in arr4_4:
                count4_4 += 1

        if (count1_1 > 0 and count2_2 > 0) or (count1_1 > 0 and count3_3 > 0) or (count1_1 > 0 and count4_4 > 0) or (
                count2_2 > 0 and count3_3 > 0) or (count2_2 > 0 and count4_4 > 0) or (count3_3 > 0 and count4_4 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите ключ, используя один алфавит!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        for i in range(0, len(self.ui.key.toPlainText())):
            if ord((self.ui.key.toPlainText())[i]) in range(0, 64) or ord((self.ui.key.toPlainText())[i]) in range(91, 96) or ord((self.ui.key.toPlainText())[i]) in range(123, 191):
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите буквенный ключ!", QtWidgets.QMessageBox.Ok)
                self.ui.key.clear()
                return None

        if (self.ui.key.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите ключ!", QtWidgets.QMessageBox.Ok)
            return None

        if (count1 > 0 and count2_2 > 0) or (count1 > 0 and count3_3 > 0) or (count1 > 0 and count4_4 > 0) or (
                count2 > 0 and count1_1 > 0) or (count2 > 0 and count3_3 > 0) or (count2 > 0 and count4_4 > 0) or (
                count3 > 0 and count1_1 > 0) or (count3 > 0 and count2_2 > 0) or (count3 > 0 and count4_4 > 0) or (
                count4 > 0 and count1_1 > 0) or (count4 > 0 and count2_2 > 0) or (count4 > 0 and count3_3 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите текст и ключ, используя один алфавит!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        print(self.ui.slova.toPlainText(), self.ui.key.toPlainText())
        self.ui.rez_decr.setPlainText(decodingVig(self.ui.slova.toPlainText(), self.ui.key.toPlainText()))

    def but_decr_index(self):
        """number = self.ui.key_index.toPlainText()
        try:
            number = int(number)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if int(number) < 1:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число больше 0!", QtWidgets.QMessageBox.Ok)
            return None"""

        arr1 = "abcdefghijklmnopqrstuvwxyz"
        arr2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        arr3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        arr4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0

        for i in self.ui.slova_index.toPlainText():
            if i in arr1:
                count1 += 1
            if i in arr2:
                count2 += 1
            if i in arr3:
                count3 += 1
            if i in arr4:
                count4 += 1
        if (count1 > 0 and count2 > 0) or (count1 > 0 and count3 > 0) or (count1 > 0 and count4 > 0) or (
                count2 > 0 and count3 > 0) or (count2 > 0 and count4 > 0) or (count3 > 0 and count4 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите текст, используя один алфавит!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.slova_index.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Нет данных для дешифрования!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        rez, key = index_similar(self.ui.slova_index.toPlainText())
        print(key)
        str_key = ''
        for i in key:
            str_key += str(i) + '\n'
        self.ui.key_index.setPlainText(str(rez))
        self.ui.rez_index.setPlainText(str_key)

    def but_decr_autocor(self):
        """number = self.ui.key_autocor.toPlainText()
        try:
            number = int(number)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if int(number) < 1:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число больше 0!", QtWidgets.QMessageBox.Ok)
            return None"""

        arr1 = "abcdefghijklmnopqrstuvwxyz"
        arr2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        arr3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        arr4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0

        for i in self.ui.slova_autocor.toPlainText():
            if i in arr1:
                count1 += 1
            if i in arr2:
                count2 += 1
            if i in arr3:
                count3 += 1
            if i in arr4:
                count4 += 1
        if (count1 > 0 and count2 > 0) or (count1 > 0 and count3 > 0) or (count1 > 0 and count4 > 0) or (
                count2 > 0 and count3 > 0) or (count2 > 0 and count4 > 0) or (count3 > 0 and count4 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите текст, используя один алфавит!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.slova_autocor.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Нет данных для дешифрования!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        rez, key = autocor(self.ui.slova_autocor.toPlainText())
        print(key)
        str_key = ''
        for i in key:
            str_key += str(i) + '\n'
        self.ui.key_autocor.setPlainText(str(rez))
        self.ui.rez_autocor.setPlainText(str_key)

    def but_decr_kas(self):
        number = self.ui.key_kas.toPlainText()
        try:
            number = int(number)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if int(number) < 2:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число больше 1!", QtWidgets.QMessageBox.Ok)
            return None

        arr1 = "abcdefghijklmnopqrstuvwxyz"
        arr2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        arr3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        arr4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0

        for i in self.ui.slova_kas.toPlainText():
            if i in arr1:
                count1 += 1
            if i in arr2:
                count2 += 1
            if i in arr3:
                count3 += 1
            if i in arr4:
                count4 += 1
        if (count1 > 0 and count2 > 0) or (count1 > 0 and count3 > 0) or (count1 > 0 and count4 > 0) or (
                count2 > 0 and count3 > 0) or (count2 > 0 and count4 > 0) or (count3 > 0 and count4 > 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введите текст, используя один алфавит!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.slova_kas.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Нет данных для дешифрования!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        deviders = kas(self.ui.slova_kas.toPlainText(), int(self.ui.key_kas.toPlainText()))
        str_deviders = ''
        for i in deviders:
            str_deviders += str(i) + ' '
        self.ui.all_key_kas.setPlainText(str_deviders)

    def find_key_kas(self):
        number = self.ui.long_key_kas.toPlainText()
        try:
            number = int(number)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if int(number) < 1:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число больше 0!", QtWidgets.QMessageBox.Ok)
            return None

        deviders = kas(self.ui.slova_kas.toPlainText(), int(self.ui.key_kas.toPlainText()))

        if number not in deviders:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число из списка возможных длин ключа!", QtWidgets.QMessageBox.Ok)
            return None

        alf, index, freq, text_only = prepare(self.ui.slova_kas.toPlainText())

        #rez = search_key_kas(alf, freq, text_only, number)
        rez = search_key_ind(alf, freq, text_only, number)
        str_rez = ''
        for i in rez:
            str_rez += str(i) + '\n'
        self.ui.rez_kas.setPlainText(str_rez)

    def down_file(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Загрузить входные данные из файла', './')
        if not fileName[0]:
            return None
        try:
            file = open(fileName[0], 'r', encoding='utf-8')
        except FileNotFoundError:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Файла не существует!", QtWidgets.QMessageBox.Ok)
            return None

        inputText = file.read()
        file.close()
        self.ui.slova.clear()
        self.ui.slova.setPlainText(inputText)

    def but_clear(self):
        self.ui.slova.clear()
        self.ui.key.clear()
        self.ui.rez_decr.clear()
        self.ui.slova_index.clear()
        self.ui.slova_autocor.clear()
        self.ui.slova_kas.clear()
        self.ui.key_index.clear()
        self.ui.key_autocor.clear()
        self.ui.key_kas.clear()

class gammawindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(gammawindow, self).__init__()
        self.ui = Ui_Dialog13()
        self.ui.setupUi(self)
        self.ui.but_proc_file.clicked.connect(self.but_proc_file)
        self.ui.but_encr.clicked.connect(self.but_encr)
        self.ui.but_decr.clicked.connect(self.but_decr)
        self.ui.but_clear.clicked.connect(self.but_clear)
        self.ui.key_gen.clicked.connect(self.key_gen)
        self.ui.down_file.clicked.connect(self.down_file)
        self.ui.up_file.clicked.connect(self.up_file)
        self.ui.key_to_file.clicked.connect(self.key_to_file)
        self.ui.key_from_file.clicked.connect(self.key_from_file)

    def key_gen(self):
        try:
            int(self.ui.key.toPlainText())
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None

        try:
            number = int(self.ui.gen_a.text())
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if int(number) < 1:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число больше 0!", QtWidgets.QMessageBox.Ok)
            return None

        try:
            number = int(self.ui.gen_b.text())
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if int(number) < 1:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число больше 0!", QtWidgets.QMessageBox.Ok)
            return None

        try:
            number = int(self.ui.gen_m.text())
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if int(number) < 1:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число больше 0!", QtWidgets.QMessageBox.Ok)
            return None

        x_i = int(self.ui.key.toPlainText())

        a = int(self.ui.gen_a.text())
        b = int(self.ui.gen_b.text())
        m = int(self.ui.gen_m.text())

        if (x_i >= m) or (x_i < 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Начальное значение д/б <m!", QtWidgets.QMessageBox.Ok)
            return None
        if m < 2:
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Модуль д/б >=2!", QtWidgets.QMessageBox.Ok)
            return None
        if (a >= m) or (a < 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Множитель д/б 0<=a<m!", QtWidgets.QMessageBox.Ok)
            return None
        if (b >= m) or (b < 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Приращение д/б 0<=c<m!", QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        key_rez = str(x_i)
        while len(key_rez) < len(self.ui.slova.toPlainText()):
            key_ = (a * x_i + b) % m
            print(key_)
            x_i = (a * x_i + b) % m
            key_rez += str(key_)
        self.ui.key.setPlainText(key_rez)

    def key_to_file(self):
        key = self.ui.key.toPlainText()
        try:
            number = int(key)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if int(number) < 1:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число больше 0!", QtWidgets.QMessageBox.Ok)
            return None

        fileName = QtWidgets.QFileDialog.getSaveFileName(self, 'Сохранить ключ в файл', './')
        if not fileName[0]:
            return None
        file = open(fileName[0], 'w')
        file.write(str(number))
        file.close()

    def key_from_file(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Загрузить ключ из файла', './')
        if not fileName[0]:
            return None
        try:
            file = open(fileName[0], 'rb')
        except FileNotFoundError:
            show_messageBox("Такого файла не существует!", "Ошибка!", QtWidgets.QMessageBox.Critical,
                            QtWidgets.QMessageBox.Ok)
            return None

        key = file.read()

        try:
            number = int(key)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if int(number) < 1:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число больше 0!", QtWidgets.QMessageBox.Ok)
            return None

        file.close()
        self.ui.key.setPlainText(str(number))

    def but_proc_file(self):
        try:
            int(self.ui.key.toPlainText())
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None

        try:
            number = int(self.ui.gen_a.text())
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if int(number) < 1:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число больше 0!", QtWidgets.QMessageBox.Ok)
            return None

        try:
            number = int(self.ui.gen_b.text())
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if int(number) < 1:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число больше 0!", QtWidgets.QMessageBox.Ok)
            return None

        try:
            number = int(self.ui.gen_m.text())
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if int(number) < 1:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число больше 0!", QtWidgets.QMessageBox.Ok)
            return None

        if self.ui.key.toPlainText() == '':
            x_i = 0
        else:
            x_i = int(self.ui.key.toPlainText())

        a = int(self.ui.gen_a.text())
        b = int(self.ui.gen_b.text())
        m = int(self.ui.gen_m.text())

        if (x_i >= m) or (x_i < 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Начальное значение д/б <m!", QtWidgets.QMessageBox.Ok)
            return None
        if m < 2:
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Модуль д/б >=2!", QtWidgets.QMessageBox.Ok)
            return None
        if (a >= m) or (a < 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Множитель д/б 0<=a<m!", QtWidgets.QMessageBox.Ok)
            return None
        if (b >= m) or (b < 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Приращение д/б 0<=c<m!", QtWidgets.QMessageBox.Ok)
            return None

        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Обработать файл', './')
        if not fileName[0]:
            return None
        try:
            inp_file = open(fileName[0], 'rb')
        except FileNotFoundError:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Файла не существует!", QtWidgets.QMessageBox.Ok)
            return None

        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Сохранить файл', './')
        if not fileName[0]:
            return None

        opt_file = open(fileName[0], 'wb')

        inputText = inp_file.read()

        key_rez = str(x_i)
        while len(key_rez) < len(inputText):
            key_ = (a * x_i + b) % m
            print(key_)
            x_i = (a * x_i + b) % m
            key_rez += str(key_)
        print(key_rez)

        if inputText != '':
            result = codingGammaFile(inputText, key_rez)
        else:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Файл пуст!", QtWidgets.QMessageBox.Ok)
            return None

        print(result)
        print('end')
        inp_file.close()

        if result is None:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Во входных данных ошибка!", QtWidgets.QMessageBox.Ok)
            return None

        opt_file.write(result)
        opt_file.close()

    def but_encr(self):

        if (self.ui.slova.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Пустая строка! Введите текст!", QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.key.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Сгенерируйте ключ!", QtWidgets.QMessageBox.Ok)
            return None

        rez, vivod = codingGamma(self.ui.slova.toPlainText(), self.ui.key.toPlainText())

        self.ui.rez_encr.setPlainText(rez)
        self.ui.dop_inf.setPlainText(vivod)

    def but_decr(self):
        key = self.ui.key.toPlainText()
        try:
            number = int(key)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if int(number) < 1:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число больше 0!", QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.rez_encr.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Нечего расшифровывать!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        rez, vivod = codingGamma(self.ui.rez_encr.toPlainText(), self.ui.key.toPlainText())

        self.ui.rez_decr.setPlainText(rez)
        self.ui.dop_inf.setPlainText(vivod)

    def down_file(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Загрузить входные данные из файла', './')
        if not fileName[0]:
            return
        try:
            file = open(fileName[0], 'rb')
        except FileNotFoundError:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Файла не существует!", QtWidgets.QMessageBox.Ok)
            return None

        inputText = file.read()

        inputText2 = ''
        for i in range(len(inputText)):
            inputText2 += (chr(int(inputText[i])))

        if inputText2 != '':
            self.ui.slova.setPlainText(inputText2)
        else:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Файл пуст!", QtWidgets.QMessageBox.Ok)
            return None

        file.close()

    def up_file(self):
        outputText = self.ui.rez_encr.toPlainText()
        if outputText == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустое поле, нечего загружать!", QtWidgets.QMessageBox.Ok)
            return None

        if self.ui.slova.toPlainText() == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустое поле, нечего загружать!", QtWidgets.QMessageBox.Ok)
            return None

        if self.ui.key.toPlainText() == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустое поле, нечего загружать!", QtWidgets.QMessageBox.Ok)
            return None

        fileName = QtWidgets.QFileDialog.getSaveFileName(self, 'Сохранить выходные данные в файл', './')
        if not fileName[0]:
            return None

        file = open(fileName[0], 'wb')

        result2 = bytearray('', 'utf-8')
        for char in self.ui.rez_encr.toPlainText():
            result2 += bytearray(char, 'utf-8')

        file.write(result2)
        file.close()

    def but_clear(self):
        self.ui.key.clear()
        self.ui.slova.clear()
        self.ui.rez_decr.clear()
        self.ui.rez_encr.clear()
        self.ui.gen_a.clear()
        self.ui.gen_b.clear()
        self.ui.gen_m.clear()
        self.ui.dop_inf.clear()

class deswindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(deswindow, self).__init__()
        self.ui = Ui_Dialog16()
        self.ui.setupUi(self)
        self.ui.but_encr.clicked.connect(self.but_encr)
        self.ui.but_decr.clicked.connect(self.but_decr)
        self.ui.but_clear.clicked.connect(self.but_clear)
        self.ui.key_gen.clicked.connect(self.key_gen)
        self.ui.down_file.clicked.connect(self.down_file)
        self.ui.up_file.clicked.connect(self.up_file)
        self.ui.key_to_file.clicked.connect(self.key_to_file)
        self.ui.key_from_file.clicked.connect(self.key_from_file)
        self.ui.vect_gen.clicked.connect(self.vect_gen)

        self.ui.ECBradioButton.toggled.connect(self.des_ECB)
        self.ui.CFBradioButton.toggled.connect(self.des_CFB)
        self.ui.CBCradioButton.toggled.connect(self.des_CBC)
        self.ui.OFBradioButton.toggled.connect(self.des_OFB)

    def des_ECB(self):
        self.ui.vect.setEnabled(False)
        self.ui.vect_gen.setEnabled(False)
    def des_CFB(self):
        self.ui.vect.setEnabled(True)
        self.ui.vect_gen.setEnabled(True)
    def des_CBC(self):
        self.ui.vect.setEnabled(True)
        self.ui.vect_gen.setEnabled(True)
    def des_OFB(self):
        self.ui.vect.setEnabled(True)
        self.ui.vect_gen.setEnabled(True)

    def key_gen(self):
        alf_passw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!";%:?*()_-+/.,@#$%^&[]{}\'<>`~|'

        password = u''
        for i in range(8):
            o = randint(0, len(alf_passw)-1)
            password += alf_passw[o]
        self.ui.key.setPlainText(password)

    def key_to_file(self):
        key = self.ui.key.toPlainText()
        if len(key) == 0:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Нечего загружать!", QtWidgets.QMessageBox.Ok)
            return None

        alf_passw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!";%:?*()_-+/.,@#$%^&[]{}\'<>`~|'
        for i in key:
            if i not in alf_passw:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ!", QtWidgets.QMessageBox.Ok)
                return None

        if len(key) != 8:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимая длина пароля!", QtWidgets.QMessageBox.Ok)
            return None

        fileName = QtWidgets.QFileDialog.getSaveFileName(self, 'Сохранить пароль в файл', './')
        if not fileName[0]:
            return None

        file = open(fileName[0], 'w')
        file.write(key)
        file.close()

    def key_from_file(self):
        alf_passw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!";%:?*()_-+/.,@#$%^&[]{}\'<>`~|'

        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Загрузить ключ из файла', './')
        if not fileName[0]:
            return None
        try:
            file = open(fileName[0], 'rb')
        except FileNotFoundError:
            show_messageBox("Такого файла не существует!", "Ошибка!", QtWidgets.QMessageBox.Critical,
                            QtWidgets.QMessageBox.Ok)
            return None

        key = file.read()
        key = key[:8]
        key_new = ''
        for i in key:
            if chr(i) not in alf_passw:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ!", QtWidgets.QMessageBox.Ok)
                return None
            else:
                key_new += chr(i)

        file.close()
        self.ui.key.setPlainText(key_new)

    def vect_gen(self):
        alf_passw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!";%:?*()_-+/.,@#$%^&[]{}\'<>`~|'
        vector = ''
        for i in range(8):
            o = randint(0, len(alf_passw)-1)
            vector += alf_passw[o]
        self.ui.vect.setPlainText(vector)

    def but_encr(self):
        alf_passw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!";%:?*()_-+/.,@#$%^&[]{}\'<>`~|'
        key = self.ui.key.toPlainText()
        if len(key) == 0:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите пароль!", QtWidgets.QMessageBox.Ok)
            return None
        if len(key) != 8:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимая длина пароля!", QtWidgets.QMessageBox.Ok)
            return None

        for i in key:
            if i not in alf_passw:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ!", QtWidgets.QMessageBox.Ok)
                return None

        inp_file = None
        out_file = None
        input_text = self.ui.slova.toPlainText()

        if input_text == '':
            fileName = self.ui.inp_file.toPlainText()
            if not fileName:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Не выбран входной файл!", QtWidgets.QMessageBox.Ok)
                return None
            try:
                inp_file = open(fileName, 'rb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Такого входного файла не существует!", QtWidgets.QMessageBox.Ok)
                return None

            fileName = self.ui.out_file.toPlainText()
            if not fileName:
                return None
            try:
                out_file = open(fileName, 'wb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None

        flag_ECB = None
        flag_CBC = None
        flag_CFB = None
        flag_OFB = None
        vector = None

        if self.ui.ECBradioButton.isChecked():
            flag_ECB = True
            flag_CBC = False
            flag_CFB = False
            flag_OFB = False

        if self.ui.CBCradioButton.isChecked():
            vector = self.ui.vect.toPlainText()
            alf_passw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!";%:?*()_-+/.,@#$%^&[]{}\'<>`~|'
            if len(vector) == 0:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите вектор!", QtWidgets.QMessageBox.Ok)
                return None
            if len(vector) != 8:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимая длина вектора!", QtWidgets.QMessageBox.Ok)
                return None
            for i in vector:
                if i not in alf_passw:
                    QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ в векторе!", QtWidgets.QMessageBox.Ok)
                    return None

            flag_ECB = False
            flag_CBC = True
            flag_CFB = False
            flag_OFB = False

        if self.ui.CFBradioButton.isChecked():
            vector = self.ui.vect.toPlainText()
            alf_passw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!";%:?*()_-+/.,@#$%^&[]{}\'<>`~|'
            if len(vector) == 0:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите вектор!", QtWidgets.QMessageBox.Ok)
                return None
            if len(vector) != 8:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимая длина вектора!", QtWidgets.QMessageBox.Ok)
                return None
            for i in vector:
                if i not in alf_passw:
                    QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ в векторе!",
                                                   QtWidgets.QMessageBox.Ok)
                    return None

            flag_ECB = False
            flag_CBC = False
            flag_CFB = True
            flag_OFB = False

        if self.ui.OFBradioButton.isChecked():
            vector = self.ui.vect.toPlainText()
            alf_passw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!";%:?*()_-+/.,@#$%^&[]{}\'<>`~|'
            if len(vector) == 0:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите вектор!", QtWidgets.QMessageBox.Ok)
                return None
            if len(vector) != 8:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимая длина вектора!", QtWidgets.QMessageBox.Ok)
                return None
            for i in vector:
                if i not in alf_passw:
                    QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ в векторе!",
                                                   QtWidgets.QMessageBox.Ok)
                    return None

            flag_ECB = False
            flag_CBC = False
            flag_CFB = False
            flag_OFB = True

        if (self.ui.inp_file.toPlainText() != '') and (self.ui.out_file.toPlainText() != ''):
            self.ui.slova.clear()
            self.ui.rez_encr.clear()
            self.ui.rez_decr.clear()
            fileName = self.ui.inp_file.toPlainText()
            if not fileName:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Не выбран входной файл!", QtWidgets.QMessageBox.Ok)
                return None
            try:
                inp_file = open(fileName, 'rb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Такого входного файла не существует!",
                                               QtWidgets.QMessageBox.Ok)
                return None

            fileName = self.ui.out_file.toPlainText()
            if not fileName:
                return None
            try:
                out_file = open(fileName, 'wb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None

        res = codingDES(self.ui.key.toPlainText(), self.ui.progressBar, inp_file, self.ui.slova.toPlainText(), out_file, vector, flag_ECB, flag_CBC, flag_CFB, flag_OFB)

        if out_file:
            out_file.close()
        if inp_file:
            inp_file.close()
        else:
            self.ui.rez_encr.setPlainText(res)

    def but_decr(self):
        flag_ECB = None
        flag_CBC = None
        flag_CFB = None
        flag_OFB = None
        vector = None

        inp_file = None
        out_file = None
        input_text = self.ui.rez_encr.toPlainText()

        alf_passw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!";%:?*()_-+/.,@#$%^&[]{}\'<>`~|'
        key = self.ui.key.toPlainText()
        if len(key) == 0:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите пароль!", QtWidgets.QMessageBox.Ok)
            return None
        if len(key) != 8:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимая длина пароля!", QtWidgets.QMessageBox.Ok)
            return None

        for i in key:
            if i not in alf_passw:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ!", QtWidgets.QMessageBox.Ok)
                return None

        if input_text == '':
            fileName = self.ui.inp_file.toPlainText()
            if not fileName:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Не выбран входной файл!", QtWidgets.QMessageBox.Ok)
                return None
            try:
                inp_file = open(fileName, 'rb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Такого входного файла не существует!",
                                               QtWidgets.QMessageBox.Ok)
                return None

            fileName = self.ui.out_file.toPlainText()
            if not fileName:
                return None
            try:
                out_file = open(fileName, 'wb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None

        if self.ui.ECBradioButton.isChecked():
            flag_ECB = True
            flag_CBC = False
            flag_CFB = False
            flag_OFB = False

        if self.ui.CBCradioButton.isChecked():
            vector = self.ui.vect.toPlainText()
            alf_passw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!";%:?*()_-+/.,@#$%^&[]{}\'<>`~|'
            if len(vector) == 0:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите вектор!", QtWidgets.QMessageBox.Ok)
                return None
            if len(vector) != 8:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимая длина вектора!", QtWidgets.QMessageBox.Ok)
                return None
            for i in vector:
                if i not in alf_passw:
                    QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ в векторе!",
                                                   QtWidgets.QMessageBox.Ok)
                    return None

            flag_ECB = False
            flag_CBC = True
            flag_CFB = False
            flag_OFB = False

        if self.ui.CFBradioButton.isChecked():
            vector = self.ui.vect.toPlainText()
            alf_passw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!";%:?*()_-+/.,@#$%^&[]{}\'<>`~|'
            if len(vector) == 0:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите вектор!", QtWidgets.QMessageBox.Ok)
                return None
            if len(vector) != 8:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимая длина вектора!", QtWidgets.QMessageBox.Ok)
                return None
            for i in vector:
                if i not in alf_passw:
                    QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ в векторе!",
                                                   QtWidgets.QMessageBox.Ok)
                    return None

            flag_ECB = False
            flag_CBC = False
            flag_CFB = True
            flag_OFB = False

        if self.ui.OFBradioButton.isChecked():
            vector = self.ui.vect.toPlainText()
            alf_passw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!";%:?*()_-+/.,@#$%^&[]{}\'<>`~|'
            if len(vector) == 0:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите вектор!", QtWidgets.QMessageBox.Ok)
                return None
            if len(vector) != 8:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимая длина вектора!", QtWidgets.QMessageBox.Ok)
                return None
            for i in vector:
                if i not in alf_passw:
                    QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ в векторе!",
                                                   QtWidgets.QMessageBox.Ok)
                    return None

            flag_ECB = False
            flag_CBC = False
            flag_CFB = False
            flag_OFB = True

        if (self.ui.inp_file.toPlainText() != '') and (self.ui.out_file.toPlainText() != ''):
            self.ui.slova.clear()
            self.ui.rez_encr.clear()
            self.ui.rez_decr.clear()
            fileName = self.ui.inp_file.toPlainText()
            if not fileName:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Не выбран входной файл!", QtWidgets.QMessageBox.Ok)
                return None
            try:
                inp_file = open(fileName, 'rb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Такого входного файла не существует!",
                                               QtWidgets.QMessageBox.Ok)
                return None

            fileName = self.ui.out_file.toPlainText()
            if not fileName:
                return None
            try:
                out_file = open(fileName, 'wb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None

        res = decodingDES(self.ui.key.toPlainText(), self.ui.progressBar, inp_file, self.ui.rez_encr.toPlainText(), out_file, vector, flag_ECB, flag_CBC, flag_CFB, flag_OFB)

        if out_file:
            out_file.close()
        if inp_file:
            inp_file.close()
        else:
            self.ui.rez_decr.setPlainText(res)

    def down_file(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбор входного файла', './')[0]
        if not fileName:
            return None
        self.ui.inp_file.setPlainText(fileName)

    def up_file(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбор выходного файла', './')[0]
        if not fileName:
            return None
        self.ui.out_file.setPlainText(fileName)

    def but_clear(self):
        self.ui.key.clear()
        self.ui.slova.clear()
        self.ui.rez_encr.clear()
        self.ui.rez_decr.clear()
        self.ui.out_file.clear()
        self.ui.inp_file.clear()
        self.ui.vect.clear()

class gostwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(gostwindow, self).__init__()
        self.ui = Ui_Dialog17()
        self.ui.setupUi(self)
        self.ui.but_encr.clicked.connect(self.but_encr)
        self.ui.but_decr.clicked.connect(self.but_decr)
        self.ui.but_clear.clicked.connect(self.but_clear)
        self.ui.key_gen.clicked.connect(self.key_gen)
        self.ui.down_file.clicked.connect(self.down_file)
        self.ui.up_file.clicked.connect(self.up_file)
        self.ui.key_to_file.clicked.connect(self.key_to_file)
        self.ui.key_from_file.clicked.connect(self.key_from_file)
        self.ui.vect_gen.clicked.connect(self.vect_gen)

        self.ui.ECBradioButton.toggled.connect(self.des_ECB)
        self.ui.CBCradioButton.toggled.connect(self.des_CBC)

    def des_ECB(self):
        self.ui.vect.setEnabled(False)
        self.ui.vect_gen.setEnabled(False)
    def des_CBC(self):
        self.ui.vect.setEnabled(True)
        self.ui.vect_gen.setEnabled(True)

    def key_gen(self):
        alf_passw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!";%:?*()_-+/.,@#$%^&[]{}\'<>`~|'
        password = ''
        for i in range(32):
            o = randint(0, len(alf_passw)-1)
            password += alf_passw[o]
        self.ui.key.setPlainText(password)

    def key_to_file(self):
        key = self.ui.key.toPlainText()
        if len(key) == 0:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Нечего загружать!", QtWidgets.QMessageBox.Ok)
            return None

        alf_passw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!";%:?*()_-+/.,@#$%^&[]{}\'<>`~|'
        for i in key:
            if i not in alf_passw:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ!", QtWidgets.QMessageBox.Ok)
                return None

        if len(key) != 32:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимая длина пароля!", QtWidgets.QMessageBox.Ok)
            return None

        fileName = QtWidgets.QFileDialog.getSaveFileName(self, 'Сохранить пароль в файл', './')
        if not fileName[0]:
            return None

        file = open(fileName[0], 'w')
        file.write(key)
        file.close()

    def key_from_file(self):
        alf_passw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!";%:?*()_-+/.,@#$%^&[]{}\'<>`~|'

        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Загрузить ключ из файла', './')
        if not fileName[0]:
            return None
        try:
            file = open(fileName[0], 'rb')
        except FileNotFoundError:
            show_messageBox("Такого файла не существует!", "Ошибка!", QtWidgets.QMessageBox.Critical,
                            QtWidgets.QMessageBox.Ok)
            return None

        key = file.read()
        key = key[:32]
        key_new = ''
        for i in key:
            if chr(i) not in alf_passw:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ!", QtWidgets.QMessageBox.Ok)
                return None
            else:
                key_new += chr(i)

        file.close()
        self.ui.key.setPlainText(key_new)

    def vect_gen(self):
        alf_passw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!";%:?*()_-+/.,@#$%^&[]{}\'<>`~|'
        vector = ''
        for i in range(8):
            o = randint(0, len(alf_passw)-1)
            vector += alf_passw[o]
        self.ui.vect.setPlainText(vector)

    def but_encr(self):
        alf_passw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!";%:?*()_-+/.,@#$%^&[]{}\'<>`~|'
        key = self.ui.key.toPlainText()
        if len(key) == 0:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите пароль!", QtWidgets.QMessageBox.Ok)
            return None
        if len(key) != 32:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимая длина пароля!", QtWidgets.QMessageBox.Ok)
            return None

        for i in key:
            if i not in alf_passw:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ!", QtWidgets.QMessageBox.Ok)
                return None

        inp_file = None
        out_file = None
        input_text = self.ui.slova.toPlainText()

        if input_text == '':
            fileName = self.ui.inp_file.toPlainText()
            if not fileName:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Не выбран входной файл!", QtWidgets.QMessageBox.Ok)
                return None
            try:
                inp_file = open(fileName, 'rb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Такого входного файла не существует!", QtWidgets.QMessageBox.Ok)
                return None

            fileName = self.ui.out_file.toPlainText()
            if not fileName:
                return None
            try:
                out_file = open(fileName, 'wb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None

        flag_CFB = None
        flag_ECB = None
        vector = None

        if self.ui.ECBradioButton.isChecked():
            flag_CFB = False
            flag_ECB = True

        if self.ui.CBCradioButton.isChecked():
            vector = self.ui.vect.toPlainText()
            alf_passw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!";%:?*()_-+/.,@#$%^&[]{}\'<>`~|'
            if len(vector) == 0:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите синхропосылку!", QtWidgets.QMessageBox.Ok)
                return None
            if len(vector) != 8:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимая длина синхропосылки!", QtWidgets.QMessageBox.Ok)
                return None
            for i in vector:
                if i not in alf_passw:
                    QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ в синхропосылке!", QtWidgets.QMessageBox.Ok)
                    return None
            flag_CFB = True
            flag_ECB = False

        if (self.ui.inp_file.toPlainText() != '') and (self.ui.out_file.toPlainText() != ''):
            self.ui.slova.clear()
            self.ui.rez_encr.clear()
            self.ui.rez_decr.clear()
            fileName = self.ui.inp_file.toPlainText()
            if not fileName:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Не выбран входной файл!", QtWidgets.QMessageBox.Ok)
                return None
            try:
                inp_file = open(fileName, 'rb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Такого входного файла не существует!",
                                               QtWidgets.QMessageBox.Ok)
                return None

            fileName = self.ui.out_file.toPlainText()
            if not fileName:
                return None
            try:
                out_file = open(fileName, 'wb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None

        res = codingGOST(self.ui.key.toPlainText(), self.ui.progressBar, inp_file, self.ui.slova.toPlainText(), out_file, vector, flag_ECB, flag_CFB)

        if out_file:
            out_file.close()
        if inp_file:
            inp_file.close()
        else:
            self.ui.rez_encr.setPlainText(res)

    def but_decr(self):
        flag_CFB = None
        flag_ECB = None
        vector = None

        inp_file = None
        out_file = None
        input_text = self.ui.rez_encr.toPlainText()

        alf_passw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!";%:?*()_-+/.,@#$%^&[]{}\'<>`~|'
        key = self.ui.key.toPlainText()
        if len(key) == 0:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите пароль!", QtWidgets.QMessageBox.Ok)
            return None
        if len(key) != 32:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимая длина пароля!", QtWidgets.QMessageBox.Ok)
            return None

        for i in key:
            if i not in alf_passw:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ!", QtWidgets.QMessageBox.Ok)
                return None

        if input_text == '':
            fileName = self.ui.inp_file.toPlainText()
            if not fileName:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Не выбран входной файл!", QtWidgets.QMessageBox.Ok)
                return None
            try:
                inp_file = open(fileName, 'rb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Такого входного файла не существует!",
                                               QtWidgets.QMessageBox.Ok)
                return None

            fileName = self.ui.out_file.toPlainText()
            if not fileName:
                return None
            try:
                out_file = open(fileName, 'wb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None

        #to_byte, res = codingDES(self.ui.key.toPlainText(), self.ui.progressBar, inp_file, self.ui.slova.toPlainText(), out_file)
        #to_byte2, res2 = decodingDES(to_byte, key, self.ui.progressBar)

        if self.ui.ECBradioButton.isChecked():
            flag_CFB = False
            flag_ECB = True

        if self.ui.CBCradioButton.isChecked():
            vector = self.ui.vect.toPlainText()
            alf_passw = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!";%:?*()_-+/.,@#$%^&[]{}\'<>`~|'

            if len(vector) == 0:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите синхропосылку!", QtWidgets.QMessageBox.Ok)
                return None
            if len(vector) != 8:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимая длина синхропосылки!", QtWidgets.QMessageBox.Ok)
                return None
            for i in vector:
                if i not in alf_passw:
                    QtWidgets.QMessageBox.critical(self, "Ошибка", "Недопустимый символ в синхропосылке!",
                                                   QtWidgets.QMessageBox.Ok)
                    return None
            flag_CFB = True
            flag_ECB = False

        if (self.ui.inp_file.toPlainText() != '') and (self.ui.out_file.toPlainText() != ''):
            self.ui.slova.clear()
            self.ui.rez_encr.clear()
            self.ui.rez_decr.clear()
            fileName = self.ui.inp_file.toPlainText()
            if not fileName:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Не выбран входной файл!", QtWidgets.QMessageBox.Ok)
                return None
            try:
                inp_file = open(fileName, 'rb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Такого входного файла не существует!",
                                               QtWidgets.QMessageBox.Ok)
                return None

            fileName = self.ui.out_file.toPlainText()
            if not fileName:
                return None
            try:
                out_file = open(fileName, 'wb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None

        res = decodingGOST(self.ui.key.toPlainText(), self.ui.progressBar, inp_file, self.ui.rez_encr.toPlainText(), out_file, vector, flag_ECB, flag_CFB)

        if out_file:
            out_file.close()
        if inp_file:
            inp_file.close()
        else:
            self.ui.rez_decr.setPlainText(res)

    def down_file(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбор входного файла', './')[0]
        if not fileName:
            return None
        self.ui.inp_file.setPlainText(fileName)

    def up_file(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбор выходного файла', './')[0]
        if not fileName:
            return None
        self.ui.out_file.setPlainText(fileName)

    def but_clear(self):
        self.ui.key.clear()
        self.ui.slova.clear()
        self.ui.rez_encr.clear()
        self.ui.rez_decr.clear()
        self.ui.out_file.clear()
        self.ui.inp_file.clear()
        self.ui.vect.clear()

class thofnumwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(thofnumwindow, self).__init__()
        self.ui = Ui_Dialog18()
        self.ui.setupUi(self)
        self.ui.but_degr.clicked.connect(self.but_degr)
        self.ui.but_nod.clicked.connect(self.but_nod)
        self.ui.but_inv.clicked.connect(self.but_inv)

    def but_degr(self):
        if (self.ui.degr_x.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.degr_p.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.degr_a.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None

        degr_x = self.ui.degr_x.toPlainText()
        try:
            degr_x = int(degr_x)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None

        degr_p = self.ui.degr_p.toPlainText()
        try:
            degr_p = int(degr_p)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if degr_p < 1:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Модуль д/б > 0!", QtWidgets.QMessageBox.Ok)
            return None

        degr_a = self.ui.degr_a.toPlainText()
        try:
            degr_a = int(degr_a)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None

        if degr_a > degr_p:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Число д/б < модуля", QtWidgets.QMessageBox.Ok)
            return None

        if degr_a < 0:
            degr_a = degr_a % degr_p
            print(degr_a)

        if degr_x < 0:
            if NOD(degr_a, degr_p)[0] != 1:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Инверсии не существует", QtWidgets.QMessageBox.Ok)
                return None
            else:
                degr_a = invers(degr_a, degr_p)
                degr_x = degr_x * (-1)

        self.ui.degr_rez.setPlainText(str(degree(degr_a, degr_x, degr_p)))

    def but_nod(self):
        if (self.ui.nod_a.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.nod_b.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None

        nod_a = self.ui.nod_a.toPlainText()
        try:
            nod_a = int(nod_a)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None

        nod_b = self.ui.nod_b.toPlainText()
        try:
            nod_b = int(nod_b)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (nod_a <= 0):
            nod_a = abs(nod_a)
        if (nod_b <= 0):
            nod_b = abs(nod_b)

        self.ui.nod_rez.setPlainText(str(NOD2(nod_a, nod_b)))
        #self.ui.nod_rez.setPlainText(str(NOD(nod_a, nod_b)[0]))

    def but_inv(self):
        if (self.ui.inv_x.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.inv_p.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None

        inv_x = self.ui.inv_x.toPlainText()
        try:
            inv_x = int(inv_x)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None

        inv_p = self.ui.inv_p.toPlainText()
        try:
            inv_p = int(inv_p)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None

        if inv_x > inv_p:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Число д/б < модуля", QtWidgets.QMessageBox.Ok)
            return None
        if (inv_x <= 0) or (inv_p <= 0):
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите положительное число!", QtWidgets.QMessageBox.Ok)
            return None

        if NOD(inv_x, inv_p)[0] != 1:
            self.ui.inv_rez.setPlainText('Инверсии не существует')

        else:
            x = invers2(inv_x, inv_p)
            self.ui.inv_rez.setPlainText(str(x))

class rsawindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(rsawindow, self).__init__()
        self.ui = Ui_Dialog19()
        self.ui.setupUi(self)
        self.ui.but_encr.clicked.connect(self.but_encr)
        self.ui.but_decr.clicked.connect(self.but_decr)
        self.ui.down_file.clicked.connect(self.down_file)
        self.ui.up_file.clicked.connect(self.up_file)
        self.ui.but_clear.clicked.connect(self.but_clear)
        self.ui.schet_all.clicked.connect(self.schet_all)
        self.ui.gen_pq.clicked.connect(self.gen_pq)

        self.ui.handradioButton.toggled.connect(self._hand)
        self.ui.genradioButton.toggled.connect(self._gen)

    def _hand(self):
        self.ui.p.setEnabled(True)
        self.ui.q.setEnabled(True)
        self.ui.gen_pq.setEnabled(False)

    def _gen(self):
        self.ui.p.setEnabled(False)
        self.ui.q.setEnabled(False)
        self.ui.gen_pq.setEnabled(True)

    def gen_pq(self):
        """prime_number = 82
        start_prime = 367
        tmp = start_prime
        pq = []
        for i in range(2):

            while len(str(tmp)) < prime_number:
                N = 4 * tmp + 2
                U = 0
                candidate = 0
                while True:
                    candidate = (N + U) * tmp + 1
                    if pow(2, int(candidate - 1), int(candidate)) == 1 and pow(2, int(N + U), int(candidate)) != 1:
                        tmp = candidate
                        break
                    else:
                        U = U - 2
            pq.append(tmp)
            start_prime = start_prime + 2
            while len(list(pyecm.factors(start_prime, False, True, 8, 1))) != 1:
                start_prime = start_prime + 2
            tmp = start_prime
        p = pq[0]
        q = pq[1]
        print("\np = {}, длина = {}".format(p, len(str(p))))
        print("\nq = {}, длина = {}".format(q, len(str(q))))

        self.ui.p.setPlainText(str(p))
        self.ui.q.setPlainText(str(q))"""

        p = gen_prime()
        self.ui.p.setPlainText(str(p))

        q = gen_prime()
        self.ui.q.setPlainText(str(q))

    def schet_all(self):
        if self.ui.handradioButton.isChecked():
            if (self.ui.p.toPlainText()) == '':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
                return None
            if (self.ui.q.toPlainText()) == '':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
                return None

            p = self.ui.p.toPlainText()
            try:
                p = int(p)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число p!", QtWidgets.QMessageBox.Ok)
                return None

            q = self.ui.q.toPlainText()
            try:
                q = int(q)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число q!", QtWidgets.QMessageBox.Ok)
                return None

            if (p < 3) or (q < 3):
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число больше 2!", QtWidgets.QMessageBox.Ok)
                return None

            #if IsPrime(p) == False:
            if PrimeFerma(p) == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число p не простое!", QtWidgets.QMessageBox.Ok)
                return None
            if PrimeFerma(q) == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число q не простое!", QtWidgets.QMessageBox.Ok)
                return None

        if self.ui.genradioButton.isChecked():
            if (self.ui.p.toPlainText()) == '':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
                return None
            if (self.ui.q.toPlainText()) == '':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
                return None

        p = int(self.ui.p.toPlainText())
        q = int(self.ui.q.toPlainText())

        N = p * q
        self.ui.N.setPlainText(str(N))

        f = (p - 1) * (q - 1)
        self.ui.f.setPlainText(str(f))

        e = 3
        for e in range(3, f):
            if NOD(e, f)[0] == 1:
                break
            #else:
                #e += 1
        self.ui.e.setPlainText(str(e))

        d = invers(e, f)
        self.ui.d.setPlainText(str(d))

    def but_encr(self):
        if (self.ui.N.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.e.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None

        inp_file = None
        out_file = None
        input_text = self.ui.message.toPlainText()

        if input_text == '':
            fileName = self.ui.inp_file.toPlainText()
            if not fileName:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Не выбран входной файл!", QtWidgets.QMessageBox.Ok)
                return None
            try:
                inp_file = open(fileName, 'rb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Такого входного файла не существует!",
                                               QtWidgets.QMessageBox.Ok)
                return None

            fileName = self.ui.out_file.toPlainText()
            if not fileName:
                return None
            try:
                out_file = open(fileName, 'w')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None

        e = self.ui.e.toPlainText()
        try:
            e = int(e)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число q!", QtWidgets.QMessageBox.Ok)
            return None

        N = int(self.ui.N.toPlainText())

        if (self.ui.inp_file.toPlainText() != '') and (self.ui.out_file.toPlainText() != ''):
            self.ui.message.clear()
            self.ui.rez_encr.clear()
            self.ui.rez_decr.clear()
            fileName = self.ui.inp_file.toPlainText()
            if not fileName:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Не выбран входной файл!", QtWidgets.QMessageBox.Ok)
                return None
            try:
                inp_file = open(fileName, 'rb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Такого входного файла не существует!",
                                               QtWidgets.QMessageBox.Ok)
                return None

            fileName = self.ui.out_file.toPlainText()
            if not fileName:
                return None
            try:
                out_file = open(fileName, 'w')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None

        res = codingRSA(N, e, self.ui.message.toPlainText(), inp_file, out_file)

        if out_file:
            out_file.close()
        if inp_file:
            inp_file.close()
        else:
            self.ui.rez_encr.setPlainText(res)

    def but_decr(self):
        if self.ui.rez_encr.toPlainText() == "Модуль N должен быть больше":
            self.ui.p.clear()
            self.ui.q.clear()
            self.ui.N.clear()
            self.ui.f.clear()
            self.ui.e.clear()
            self.ui.d.clear()
            self.ui.rez_encr.clear()
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите числа p и q больше!", QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.d.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.N.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None

        inp_file = None
        out_file = None
        input_text = self.ui.message.toPlainText()

        if input_text == '':
            fileName = self.ui.inp_file.toPlainText()
            if not fileName:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Не выбран входной файл!", QtWidgets.QMessageBox.Ok)
                return None
            try:
                inp_file = open(fileName, 'r')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Такого входного файла не существует!",
                                               QtWidgets.QMessageBox.Ok)
                return None

            fileName = self.ui.out_file.toPlainText()
            if not fileName:
                return None
            try:
                out_file = open(fileName, 'wb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None

        N = int(self.ui.N.toPlainText())
        d = int(self.ui.d.toPlainText())

        if (self.ui.inp_file.toPlainText() != '') and (self.ui.out_file.toPlainText() != ''):
            self.ui.message.clear()
            self.ui.rez_encr.clear()
            self.ui.rez_decr.clear()
            fileName = self.ui.inp_file.toPlainText()
            if not fileName:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Не выбран входной файл!", QtWidgets.QMessageBox.Ok)
                return None
            try:
                inp_file = open(fileName, 'r')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Такого входного файла не существует!",
                                               QtWidgets.QMessageBox.Ok)
                return None

            fileName = self.ui.out_file.toPlainText()
            if not fileName:
                return None
            try:
                out_file = open(fileName, 'wb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None

        res = decodingRSA(N, d, self.ui.rez_encr.toPlainText(), inp_file, out_file)

        if out_file:
            out_file.close()
        if inp_file:
            inp_file.close()
        else:
            self.ui.rez_decr.setPlainText(res)

    def down_file(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбор входного файла', './')[0]
        if not fileName:
            return None
        self.ui.inp_file.setPlainText(fileName)

    def up_file(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбор выходного файла', './')[0]
        if not fileName:
            return None
        self.ui.out_file.setPlainText(fileName)

    def but_clear(self):
        self.ui.p.clear()
        self.ui.q.clear()
        self.ui.N.clear()
        self.ui.f.clear()
        self.ui.e.clear()
        self.ui.d.clear()
        self.ui.message.clear()
        self.ui.rez_encr.clear()
        self.ui.rez_decr.clear()
        self.ui.inp_file.clear()
        self.ui.out_file.clear()

class diffiewindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(diffiewindow, self).__init__()
        self.ui = Ui_Dialog20()
        self.ui.setupUi(self)
        self.ui.schet_otkr.clicked.connect(self.schet_otkr)
        self.ui.schet_param.clicked.connect(self.schet_param)
        self.ui.schet_zakr.clicked.connect(self.schet_zakr)
        self.ui.but_clear.clicked.connect(self.but_clear)
        self.ui.gen_p.clicked.connect(self.gen_p)
        self.ui.gen_ab.clicked.connect(self.gen_ab)

        self.ui.handradioButton.toggled.connect(self._hand)
        self.ui.genradioButton.toggled.connect(self._gen)

    def _hand(self):
        self.ui.p.setEnabled(True)
        self.ui.gen_p.setEnabled(False)

    def _gen(self):
        self.ui.p.setEnabled(False)
        self.ui.gen_p.setEnabled(True)

    def gen_p(self):
        """a = 3
        q = generate_q(100, a)
        print(q)
        p = 2 * q + 1
        while (not IsPrime(p)):
            if len(list(pyecm.factors(a, False, True, 8, 1))) == 1:
                q = generate_q(100, a)
                p = 2 * q + 1
                a = a + 2
            else:
                a = a + 2
        if len(list(pyecm.factors(p, False, True, 8, 1))) == 1:
            print("\nq = {}, длина = {}".format(q, len(str(q))))
            print("\np = {}, длина = {}".format(p, len(str(p))))

            self.ui.p.setPlainText(str(p))
            self.ui.q.setPlainText(str(q))"""

        p = gen_prime()
        q = (p - 1) // 2
        while (PrimeFerma_big(q) != True):
            p = gen_prime()
            q = (p - 1) // 2
        self.ui.p.setPlainText(str(p))
        self.ui.q.setPlainText(str(q))

    def gen_ab(self):
        if (self.ui.p.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None

        p = int(self.ui.p.toPlainText())

        a = randint(1, p - 1)
        b = randint(1, p - 1)
        self.ui.a.setPlainText(str(a))
        self.ui.b.setPlainText(str(b))

    def schet_param(self):
        if self.ui.handradioButton.isChecked():
            if (self.ui.p.toPlainText()) == '':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
                return None

            p = self.ui.p.toPlainText()
            try:
                p = int(p)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число p!", QtWidgets.QMessageBox.Ok)
                return None

            if (p < 3):
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число больше 2!", QtWidgets.QMessageBox.Ok)
                return None

            #if IsPrime(p) == False:
            if PrimeFerma(p) == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число p не простое!", QtWidgets.QMessageBox.Ok)
                return None

            q = (p - 1)//2
            print(q)
            #if IsPrime(q) == False:
            if PrimeFerma(q) == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число q не простое!", QtWidgets.QMessageBox.Ok)
                return None

            self.ui.q.setPlainText(str(q))

            g = 2
            for i in range(p - 1):
                if degree(g, q, p) != 1:
                    break
                else:
                    g += 1
            print("g = ", g)
            self.ui.g.setPlainText(str(g))

        if self.ui.genradioButton.isChecked():
            if (self.ui.p.toPlainText()) == '':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
                return None

            p = int(self.ui.p.toPlainText())
            q = int(self.ui.q.toPlainText())

            g = 2
            for i in range(p - 1):
                if degree(g, q, p) != 1:
                    break
                else:
                    g += 1
            print("g = ", g)
            self.ui.g.setPlainText(str(g))

    def schet_otkr(self):
        if (self.ui.a.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.b.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.p.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None

        a = self.ui.a.toPlainText()
        try:
            a = int(a)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число q!", QtWidgets.QMessageBox.Ok)
            return None
        b = self.ui.b.toPlainText()
        try:
            b = int(b)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число q!", QtWidgets.QMessageBox.Ok)
            return None
        p = self.ui.p.toPlainText()
        try:
            p = int(p)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число q!", QtWidgets.QMessageBox.Ok)
            return None

        g = int(self.ui.g.toPlainText())
        A = degree(g, a, p)
        B = degree(g, b, p)

        self.ui.A.setPlainText(str(A))
        self.ui.B.setPlainText(str(B))

    def schet_zakr(self):
        if (self.ui.a.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.b.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.A.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.B.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.p.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None

        a = self.ui.a.toPlainText()
        try:
            a = int(a)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число q!", QtWidgets.QMessageBox.Ok)
            return None
        b = self.ui.b.toPlainText()
        try:
            b = int(b)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число q!", QtWidgets.QMessageBox.Ok)
            return None
        p = self.ui.p.toPlainText()
        try:
            p = int(p)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число q!", QtWidgets.QMessageBox.Ok)
            return None

        A = int(self.ui.A.toPlainText())
        B = int(self.ui.B.toPlainText())
        KA = degree(B, a, p)
        KB = degree(A, b, p)

        self.ui.ka.setPlainText(str(KA))
        self.ui.kb.setPlainText(str(KB))

    def but_clear(self):
        self.ui.p.clear()
        self.ui.q.clear()
        self.ui.g.clear()
        self.ui.a.clear()
        self.ui.b.clear()
        self.ui.A.clear()
        self.ui.B.clear()
        self.ui.ka.clear()
        self.ui.kb.clear()

class shamirwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(shamirwindow, self).__init__()
        self.ui = Ui_Dialog21()
        self.ui.setupUi(self)
        self.ui.A_gen.clicked.connect(self.A_gen)
        self.ui.B_gen.clicked.connect(self.B_gen)
        self.ui.but_clear.clicked.connect(self.but_clear)
        self.ui.down_file.clicked.connect(self.down_file)
        self.ui.up_file1.clicked.connect(self.up_file1)
        self.ui.up_file2.clicked.connect(self.up_file2)
        self.ui.up_file3.clicked.connect(self.up_file3)
        self.ui.up_file4.clicked.connect(self.up_file4)
        self.ui.but_encr.clicked.connect(self.but_encr)
        self.ui.gen_p.clicked.connect(self.gen_p)

        self.ui.handradioButton.toggled.connect(self._hand)
        self.ui.genradioButton.toggled.connect(self._gen)

    def _hand(self):
        self.ui.p.setEnabled(True)
        self.ui.gen_p.setEnabled(False)

    def _gen(self):
        self.ui.p.setEnabled(False)
        self.ui.gen_p.setEnabled(True)

    def gen_p(self):
        """prime_number = 82
        start_prime = 373
        tmp = start_prime
        p = 0
        while len(str(tmp)) < prime_number:
            N = 4 * tmp + 2
            U = 0
            candidate = 0
            while True:
                candidate = (N + U) * tmp + 1
                if pow(2, int(candidate - 1), int(candidate)) == 1 and pow(2, int(N + U), int(candidate)) != 1:
                    tmp = candidate
                    break
                else:
                    U = U - 2
        p = tmp
        print("\np = {}, длина = {}".format(p, len(str(p))))"""

        p = gen_prime()
        self.ui.p.setPlainText(str(p))

    def A_gen(self):
        if self.ui.handradioButton.isChecked():
            if (self.ui.p.toPlainText()) == '':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
                return None

            p = self.ui.p.toPlainText()
            try:
                p = int(p)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число p!", QtWidgets.QMessageBox.Ok)
                return None

            #if IsPrime(p) == False:
            if PrimeFerma(p) == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число p не простое!", QtWidgets.QMessageBox.Ok)
                return None

            if p < 3:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число p больше!", QtWidgets.QMessageBox.Ok)
                return None

        if self.ui.genradioButton.isChecked():
            if (self.ui.p.toPlainText()) == '':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
                return None
            p = self.ui.p.toPlainText()
            try:
                p = int(p)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число p!", QtWidgets.QMessageBox.Ok)
                return None

        p = int(self.ui.p.toPlainText())

        c_a = randint(1, p - 1)
        while (NOD(c_a, p - 1)[0] != 1):
            c_a = randint(1, p - 1)

        d_a = 0
        d_a = invers(c_a, p - 1)
        d_a = d_a % (p - 1)

        self.ui.c_A.setPlainText(str(c_a))
        self.ui.d_A.setPlainText(str(d_a))

    def B_gen(self):
        if self.ui.handradioButton.isChecked():
            if (self.ui.p.toPlainText()) == '':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!",
                                               QtWidgets.QMessageBox.Ok)
                return None

            p = self.ui.p.toPlainText()
            try:
                p = int(p)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число p!", QtWidgets.QMessageBox.Ok)
                return None

            #if IsPrime(p) == False:
            if PrimeFerma(p) == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число p не простое!", QtWidgets.QMessageBox.Ok)
                return None

            if p < 3:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число p больше!", QtWidgets.QMessageBox.Ok)
                return None

        if self.ui.genradioButton.isChecked():
            if (self.ui.p.toPlainText()) == '':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!",
                                               QtWidgets.QMessageBox.Ok)
                return None
            p = self.ui.p.toPlainText()
            try:
                p = int(p)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число p!", QtWidgets.QMessageBox.Ok)
                return None

        p = int(self.ui.p.toPlainText())

        c_b = randint(1, p - 1)
        while (NOD(c_b, p - 1)[0] != 1):
            c_b = randint(1, p - 1)

        d_b = 0
        d_b = invers(c_b, p - 1)
        d_b = d_b % (p - 1)

        self.ui.c_B.setPlainText(str(c_b))
        self.ui.d_B.setPlainText(str(d_b))

    def but_encr(self):
        if (self.ui.c_A.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.c_B.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.d_A.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.d_B.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None

        inp_file = None
        out_file1 = None
        out_file2 = None
        out_file3 = None
        out_file4 = None
        input_text = self.ui.message.toPlainText()

        if input_text == '':
            fileName = self.ui.inp_file.toPlainText()
            if not fileName:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Не выбран входной файл!", QtWidgets.QMessageBox.Ok)
                return None
            try:
                inp_file = open(fileName, 'rb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Такого входного файла не существует!",
                                               QtWidgets.QMessageBox.Ok)
                return None

            fileName = self.ui.out_file1.toPlainText()
            if not fileName:
                return None
            try:
                out_file1 = open(fileName, 'w')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None
            fileName = self.ui.out_file2.toPlainText()
            if not fileName:
                return None
            try:
                out_file2 = open(fileName, 'w')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None
            fileName = self.ui.out_file3.toPlainText()
            if not fileName:
                return None
            try:
                out_file3 = open(fileName, 'w')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None
            fileName = self.ui.out_file4.toPlainText()
            if not fileName:
                return None
            try:
                out_file4 = open(fileName, 'wb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None

        if (self.ui.inp_file.toPlainText() != '') and (self.ui.out_file1.toPlainText() != '') and (self.ui.out_file2.toPlainText() != '') and (self.ui.out_file3.toPlainText() != '') and (self.ui.out_file4.toPlainText() != ''):
            self.ui.message.clear()
            self.ui.x1.clear()
            self.ui.x2.clear()
            self.ui.x3.clear()
            self.ui.x4.clear()

            fileName = self.ui.inp_file.toPlainText()
            if not fileName:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Не выбран входной файл!", QtWidgets.QMessageBox.Ok)
                return None
            try:
                inp_file = open(fileName, 'rb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Такого входного файла не существует!",
                                               QtWidgets.QMessageBox.Ok)
                return None

            fileName = self.ui.out_file1.toPlainText()
            if not fileName:
                return None
            try:
                out_file1 = open(fileName, 'w')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None
            fileName = self.ui.out_file2.toPlainText()
            if not fileName:
                return None
            try:
                out_file2 = open(fileName, 'w')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None
            fileName = self.ui.out_file3.toPlainText()
            if not fileName:
                return None
            try:
                out_file3 = open(fileName, 'w')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None
            fileName = self.ui.out_file4.toPlainText()
            if not fileName:
                return None
            try:
                out_file4 = open(fileName, 'wb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None

        p = int(self.ui.p.toPlainText())
        c_a = int(self.ui.c_A.toPlainText())
        c_b = int(self.ui.c_B.toPlainText())
        d_a = int(self.ui.d_A.toPlainText())
        d_b = int(self.ui.d_B.toPlainText())

        res1, res2, res3, res4 = codingShamir(p, c_a, c_b, d_a, d_b, self.ui.message.toPlainText(), inp_file)
        print(res1, res2, res3, res4)
        if res1 == "p должно быть больше":
            QtWidgets.QMessageBox.critical(self, "Ошибка!", "Введите число p больше!",
                                           QtWidgets.QMessageBox.Ok)
            return None

        if (out_file1 and out_file2 and out_file3 and out_file4):
            out_file1.write(res1)
            out_file1.close()
            out_file2.write(res2)
            out_file2.close()
            out_file3.write(res3)
            out_file3.close()
            res4 = res4[:len(res4) - 1]
            for i in res4.split(' '):
                out_file4.write(bytes([int(i)]))
            out_file4.close()
        if inp_file:
            inp_file.close()
        else:
            new_res4 = ''
            self.ui.x1.setPlainText(res1)
            self.ui.x2.setPlainText(res2)
            self.ui.x3.setPlainText(res3)
            res4 = res4[:len(res4) - 1]
            for i in res4.split(' '):
                new_res4 += chr(int(i))
            self.ui.x4.setPlainText(new_res4)

    def down_file(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбор входного файла', './')[0]
        if not fileName:
            return None
        self.ui.inp_file.setPlainText(fileName)

    def up_file1(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбор выходного файла', './')[0]
        if not fileName:
            return None
        self.ui.out_file1.setPlainText(fileName)

    def up_file2(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбор выходного файла', './')[0]
        if not fileName:
            return None
        self.ui.out_file2.setPlainText(fileName)

    def up_file3(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбор выходного файла', './')[0]
        if not fileName:
            return None
        self.ui.out_file3.setPlainText(fileName)

    def up_file4(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбор выходного файла', './')[0]
        if not fileName:
            return None
        self.ui.out_file4.setPlainText(fileName)

    def but_clear(self):
        self.ui.p.clear()
        self.ui.message.clear()
        self.ui.c_A.clear()
        self.ui.c_B.clear()
        self.ui.d_A.clear()
        self.ui.d_B.clear()
        self.ui.x1.clear()
        self.ui.x2.clear()
        self.ui.x3.clear()
        self.ui.x4.clear()
        self.ui.inp_file.clear()
        self.ui.out_file1.clear()
        self.ui.out_file2.clear()
        self.ui.out_file3.clear()
        self.ui.out_file4.clear()

class gamalwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(gamalwindow, self).__init__()
        self.ui = Ui_Dialog22()
        self.ui.setupUi(self)
        self.ui.but_encr.clicked.connect(self.but_encr)
        self.ui.but_decr.clicked.connect(self.but_decr)
        self.ui.down_file.clicked.connect(self.down_file)
        self.ui.up_file.clicked.connect(self.up_file)
        self.ui.but_clear.clicked.connect(self.but_clear)
        self.ui.schet_keys.clicked.connect(self.schet_keys)
        self.ui.schet_g.clicked.connect(self.schet_g)
        self.ui.gen_p.clicked.connect(self.gen_p)

        self.ui.handradioButton.toggled.connect(self._hand)
        self.ui.genradioButton.toggled.connect(self._gen)

    def _hand(self):
        self.ui.p.setEnabled(True)
        self.ui.g.setEnabled(True)
        self.ui.gen_p.setEnabled(False)

    def _gen(self):
        self.ui.p.setEnabled(False)
        self.ui.g.setEnabled(False)
        self.ui.gen_p.setEnabled(True)

    def gen_p(self):
        """a = 3
        q = generate_q(100, a)
        print(q)
        p = 2 * q + 1
        while (not IsPrime(p)):
            if len(list(pyecm.factors(a, False, True, 8, 1))) == 1:
                q = generate_q(100, a)
                p = 2 * q + 1
                a = a + 2
            else:
                a = a + 2
        if len(list(pyecm.factors(p, False, True, 8, 1))) == 1:
            print("\nq = {}, длина = {}".format(q, len(str(q))))
            print("\np = {}, длина = {}".format(p, len(str(p))))"""
        p = gen_prime()
        q = (p - 1) // 2
        while (PrimeFerma_big(q) != True):
            p = gen_prime()
            print(p)
            q = (p - 1) // 2
        self.ui.p.setPlainText(str(p))

    def schet_g(self):
        if self.ui.handradioButton.isChecked():
            if (self.ui.p.toPlainText()) == '':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!",
                                               QtWidgets.QMessageBox.Ok)
                return None

            p = self.ui.p.toPlainText()
            try:
                p = int(p)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число p!", QtWidgets.QMessageBox.Ok)
                return None

            if (p < 3):
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число больше 2!", QtWidgets.QMessageBox.Ok)
                return None

            #if IsPrime(p) == False:
            if PrimeFerma(p) == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число p не простое!", QtWidgets.QMessageBox.Ok)
                return None

            q = (p - 1) // 2
            #if IsPrime(q) == False:
            if PrimeFerma(q) == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число q не простое!", QtWidgets.QMessageBox.Ok)
                return None

            g = 2
            for i in range(p - 1):
                if degree(g, q, p) != 1:
                    break
                else:
                    g += 1
            self.ui.g.setPlainText(str(g))

        if self.ui.genradioButton.isChecked():
            if (self.ui.p.toPlainText()) == '':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!",
                                               QtWidgets.QMessageBox.Ok)
                return None

            p = int(self.ui.p.toPlainText())
            q = (p - 1) // 2

            g = 2
            for i in range(p - 1):
                if degree(g, q, p) != 1:
                    break
                else:
                    g += 1
            self.ui.g.setPlainText(str(g))

    def schet_keys(self):
        if self.ui.handradioButton.isChecked():
            if (self.ui.p.toPlainText()) == '':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
                return None
            if (self.ui.g.toPlainText()) == '':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
                return None

            p = self.ui.p.toPlainText()
            try:
                p = int(p)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число p!", QtWidgets.QMessageBox.Ok)
                return None

            #if IsPrime(p) == False:
            if PrimeFerma(p) == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число p не простое!", QtWidgets.QMessageBox.Ok)
                return None

            g = int(self.ui.g.toPlainText())

            c = randint(1, p - 1)
            self.ui.c.setPlainText(str(c))
            #print("\nЗакрытый ключ x = ", x)

            d = degree(g, c, p)
            self.ui.d.setPlainText(str(d))
            #print("\nОткрытый ключ y = ", y)

            k = randint(1, p - 1)
            self.ui.k.setPlainText(str(k))
            # print("\nСессионный ключ k = ", k)

        if self.ui.genradioButton.isChecked():
            if (self.ui.p.toPlainText()) == '':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
                return None
            if (self.ui.g.toPlainText()) == '':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
                return None

            p = int(self.ui.p.toPlainText())
            g = int(self.ui.g.toPlainText())

            c = randint(1, p - 1)
            self.ui.c.setPlainText(str(c))
            # print("\nЗакрытый ключ x = ", x)

            d = degree(g, c, p)
            self.ui.d.setPlainText(str(d))
            # print("\nОткрытый ключ y = ", y)

            k = randint(1, p - 1)
            self.ui.k.setPlainText(str(k))
            #print("\nСессионный ключ k = ", k)

    def but_encr(self):
        if (self.ui.p.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.g.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.k.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.c.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.d.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None

        inp_file = None
        out_file = None
        input_text = self.ui.message.toPlainText()

        if input_text == '':
            fileName = self.ui.inp_file.toPlainText()
            if not fileName:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Не выбран входной файл!", QtWidgets.QMessageBox.Ok)
                return None
            try:
                inp_file = open(fileName, 'rb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Такого входного файла не существует!",
                                               QtWidgets.QMessageBox.Ok)
                return None

            fileName = self.ui.out_file.toPlainText()
            if not fileName:
                return None
            try:
                out_file = open(fileName, 'w')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None

        p = self.ui.p.toPlainText()
        try:
            p = int(p)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число p!", QtWidgets.QMessageBox.Ok)
            return None

        g = int(self.ui.g.toPlainText())
        p = int(self.ui.p.toPlainText())
        d = int(self.ui.d.toPlainText())
        k = int(self.ui.k.toPlainText())

        if (self.ui.inp_file.toPlainText() != '') and (self.ui.out_file.toPlainText() != ''):
            self.ui.message.clear()
            self.ui.rez_encr.clear()
            self.ui.rez_decr.clear()
            fileName = self.ui.inp_file.toPlainText()
            if not fileName:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Не выбран входной файл!", QtWidgets.QMessageBox.Ok)
                return None
            try:
                inp_file = open(fileName, 'rb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Такого входного файла не существует!",
                                               QtWidgets.QMessageBox.Ok)
                return None

            fileName = self.ui.out_file.toPlainText()
            if not fileName:
                return None
            try:
                out_file = open(fileName, 'w')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None

        res = codingGamal(p, g, d, k, self.ui.message.toPlainText(), inp_file, out_file)

        if out_file:
            out_file.close()
        if inp_file:
            inp_file.close()
        else:
            self.ui.rez_encr.setPlainText(res)

    def but_decr(self):
        if self.ui.rez_encr.toPlainText() == "p должно быть больше":
            self.ui.p.clear()
            self.ui.g.clear()
            self.ui.k.clear()
            self.ui.c.clear()
            self.ui.d.clear()
            self.ui.rez_encr.clear()
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число p больше!", QtWidgets.QMessageBox.Ok)
            return None

        if (self.ui.p.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.g.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.k.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.c.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if (self.ui.d.toPlainText()) == '':
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Пустая строка! Введите число!", QtWidgets.QMessageBox.Ok)
            return None

        inp_file = None
        out_file = None
        input_text = self.ui.message.toPlainText()

        if input_text == '':
            fileName = self.ui.inp_file.toPlainText()
            if not fileName:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Не выбран входной файл!", QtWidgets.QMessageBox.Ok)
                return None
            try:
                inp_file = open(fileName, 'r')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Такого входного файла не существует!",
                                               QtWidgets.QMessageBox.Ok)
                return None

            fileName = self.ui.out_file.toPlainText()
            if not fileName:
                return None
            try:
                out_file = open(fileName, 'wb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None

        g = int(self.ui.g.toPlainText())
        c = int(self.ui.c.toPlainText())
        p = int(self.ui.p.toPlainText())
        k = int(self.ui.k.toPlainText())

        if (self.ui.inp_file.toPlainText() != '') and (self.ui.out_file.toPlainText() != ''):
            self.ui.message.clear()
            self.ui.rez_encr.clear()
            self.ui.rez_decr.clear()
            fileName = self.ui.inp_file.toPlainText()
            if not fileName:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Не выбран входной файл!", QtWidgets.QMessageBox.Ok)
                return None
            try:
                inp_file = open(fileName, 'r')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Такого входного файла не существует!",
                                               QtWidgets.QMessageBox.Ok)
                return None

            fileName = self.ui.out_file.toPlainText()
            if not fileName:
                return None
            try:
                out_file = open(fileName, 'wb')
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Некорректный путь к файлу!",
                                               QtWidgets.QMessageBox.Ok)
                return None

        res = decodingGamal(p, g, c, k, self.ui.rez_encr.toPlainText(), inp_file, out_file)

        if out_file:
            out_file.close()
        if inp_file:
            inp_file.close()
        else:
            self.ui.rez_decr.setPlainText(res)

    def down_file(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбор входного файла', './')[0]
        if not fileName:
            return None
        self.ui.inp_file.setPlainText(fileName)

    def up_file(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбор выходного файла', './')[0]
        if not fileName:
            return None
        self.ui.out_file.setPlainText(fileName)

    def but_clear(self):
        self.ui.p.clear()
        self.ui.g.clear()
        self.ui.k.clear()
        self.ui.c.clear()
        self.ui.d.clear()
        self.ui.message.clear()
        self.ui.rez_encr.clear()
        self.ui.rez_decr.clear()
        self.ui.inp_file.clear()
        self.ui.out_file.clear()

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
