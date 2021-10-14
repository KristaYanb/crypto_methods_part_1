from PyQt5 import QtCore, QtGui, QtWidgets
from math import sqrt
from numpy import array, dot, linalg, transpose, delete,round

def text_to_number(text, dictionary):  # заменяем символы текста/ключа на числа
    list_code = []

    for i in range(len(text)):
        for value in dictionary:
            if text[i] == dictionary[value]:
                list_code.append(value)
    return list_code

def exgcd(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return x

def minor_matr(arr, i, j, len1):
    temp_mal_matr = delete(delete(arr, i, axis = 0), j, axis = 1)
    determ = round(linalg.det(temp_mal_matr)) % len1
    rez = (pow(-1, (i + 1) + (j + 1)) * determ) % len1
    return rez

def codingHill(stroka, key):
    arr = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"№;%:?*()_-+\\/.,@#$^&[]{}\'<>`~|\t\n '

    print(len(arr))

    dictionary = {}
    j = 0
    for i in arr:
        dictionary[j] = i
        j = j + 1

    result_shifr = ''

    stroka_new = ''
    for k in stroka:
        if k in arr:
            stroka_new += k
        else:
            stroka_new = stroka_new

    key_encoded = text_to_number(key, dictionary)
    text_encoded = text_to_number(stroka_new, dictionary)

    size = int(sqrt(len(key_encoded)))
    arr_key = []
    for i in range(size):
        matr = []
        for j in range(size):
            matr.append(key_encoded[0])
            key_encoded = key_encoded[1:]
        arr_key.append(matr)
    arr_key = array(arr_key)
    print("arr_key ", arr_key)

    arr_str = []
    for i in range(len(text_encoded) // size):
        matr = []
        for j in range(size):
            matr.append(text_encoded[0])
            text_encoded = text_encoded[1:]
        arr_str.append(matr)
    arr_str = array(arr_str)
    print("arr_str ", arr_str)

    umnoz = []
    for i in range(len(arr_str)):
        umnoz.append(dot(arr_key, arr_str[i]))
        #umnoz.append(dot(arr_str[i], arr_key))
    umnoz = array(umnoz)

    for i in range(len(umnoz)):
        for j in range(len(umnoz[i])):
            umnoz[i][j] = umnoz[i][j]%(len(arr))
    print("umnoz ", umnoz)

    for i in range(len(umnoz)):
        for j in range(len(umnoz[i])):
            result_shifr += arr[umnoz[i][j]]
    print("result_shifr ", result_shifr)

    return result_shifr

def decodingHill(stroka, key):
    arr = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"№;%:?*()_-+\\/.,@#$^&[]{}\'<>`~|\t\n '

    dictionary = {}
    j = 0
    for i in arr:
        dictionary[j] = i
        j = j + 1

    result_deshifr = ''

    stroka_new = ''
    for k in stroka:
        if k in arr:
            stroka_new += k
        else:
            stroka_new = stroka_new

    key_encoded = text_to_number(key, dictionary)
    text_encoded = text_to_number(stroka_new, dictionary)

    size = int(sqrt(len(key_encoded)))
    arr_key = []
    K_obr = []
    Matr_minor = []
    for i in range(size):
        matr = []
        k_obr = []
        matr_minor = []
        for j in range(size):
            matr.append(key_encoded[0])
            key_encoded = key_encoded[1:]
            k_obr.append(0)
            matr_minor.append(0)
        arr_key.append(matr)
        K_obr.append(k_obr)
        Matr_minor.append(matr_minor)
    arr_key = array(arr_key)
    print("arr_key ", arr_key)
    K_obr = array(K_obr)
    print("K_obr ", K_obr)
    Matr_minor = array(Matr_minor)
    print("Matr_minor ", Matr_minor)

    arr_str = []
    for i in range(len(text_encoded) // size):
        matr = []
        for j in range(size):
            matr.append(text_encoded[0])
            text_encoded = text_encoded[1:]
        arr_str.append(matr)
    arr_str = array(arr_str)
    print("arr_str ", arr_str)

    for i in range(size):
        for j in range(size):
            Matr_minor[i][j] = minor_matr(arr_key, i, j, len(arr))
    print("minors ", Matr_minor)

    Matr_minor = Matr_minor.transpose()
    print("minors_transp ", Matr_minor)

    #det_K = int(linalg.det(arr_key)) % len(arr)
    det_K = round(linalg.det(arr_key)) % len(arr)
    print('det ', det_K)
    if (det_K == 0):
        result_deshifr = 'Определитель матрицы равен нулю! Расшифрование невозможно!'
        return result_deshifr

    obr_det_K = exgcd(det_K, len(arr)) % len(arr)
    print("obr_det_K ", obr_det_K)

    for i in range(len(Matr_minor)):
        for j in range(len(Matr_minor[i])):
            K_obr[i][j] = (obr_det_K * Matr_minor[i][j]) % len(arr)
    print("K_obr ", K_obr)

    umnoz = []
    for i in range(len(arr_str)):
        umnoz.append(dot(K_obr, arr_str[i]))
    umnoz = array(umnoz)

    for i in range(len(umnoz)):
        for j in range(len(umnoz[i])):
            umnoz[i][j] = umnoz[i][j] % (len(arr))
    print(umnoz)

    for i in range(len(umnoz)):
        for j in range(len(umnoz[i])):
            result_deshifr += arr[umnoz[i][j]]
    print(result_deshifr)

    return result_deshifr
