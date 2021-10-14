from PyQt5 import QtCore, QtGui, QtWidgets

def codingCezar(text, n): #Шифрование
    arr1 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    arr2 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    arr3 = "abcdefghijklmnopqrstuvwxyz"
    arr4 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #n = int(input("Введите ключ: "))
    result_shifr = ''

    for i in text:
        if i in arr1:
            for j,k in enumerate(arr1):
                 if i == k:
                    result_shifr += arr1[(j+n)% len(arr1)]
        else:
            if i in arr2:
                for j,k in enumerate(arr2):
                     if i == k:
                        result_shifr += arr2[(j+n)% len(arr2)]
            else:
                if i in arr3:
                    for j,k in enumerate(arr3):
                        if i == k:
                            result_shifr += arr3[(j+n)% len(arr3)]
                else:
                    if i in arr4:
                        for j,k in enumerate(arr4):
                            if i == k:
                                result_shifr += arr4[(j+n)% len(arr4)]
                    else:
                        result_shifr += i
    return result_shifr

def decodingCezar(text, n): #Дешифрование
    arr1 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    arr2 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    arr3 = "abcdefghijklmnopqrstuvwxyz"
    arr4 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result_deshifr = ''

    for i in text:
        if i in arr1:
            for j,k in enumerate(arr1):
                 if i == k:
                    result_deshifr += arr1[(j-n)% len(arr1)]
        else:
            if i in arr2:
                for j,k in enumerate(arr2):
                     if i == k:
                        result_deshifr += arr2[(j-n)% len(arr2)]
            else:
                if i in arr3:
                    for j,k in enumerate(arr3):
                        if i == k:
                            result_deshifr += arr3[(j-n)% len(arr3)]
                else:
                    if i in arr4:
                        for j,k in enumerate(arr4):
                            if i == k:
                                result_deshifr += arr4[(j-n)% len(arr4)]
                    else:
                        result_deshifr += i
    return result_deshifr
