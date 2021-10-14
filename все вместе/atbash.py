from PyQt5 import QtCore, QtGui, QtWidgets

def codingAtbash(text):
    arr1 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    arr2 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    arr3 = "abcdefghijklmnopqrstuvwxyz"
    arr4 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    crypt = ""
    for i in text:
        if i in arr1:
            for j, k in enumerate(arr1):
                if i == k:
                    crypt += arr1[32 - j]
        else:
            if i in arr2:
                for j, k in enumerate(arr2):
                    if i == k:
                        crypt += arr2[32 - j]
            else:
                if i in arr3:
                    for j, k in enumerate(arr3):
                        if i == k:
                            crypt += arr3[25 - j]
                else:
                    if i in arr4:
                        for j, k in enumerate(arr4):
                            if i == k:
                                crypt += arr4[25 - j]
                    else:
                        crypt += i
    return crypt
