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

def matrix_minor(arr, i, j, mod):
    tmp = delete(delete(arr,i,axis=0), j, axis=1)
    detTmp = round(linalg.det(tmp)) % mod
    return (pow(-1, (i+1)+(j+1)) * detTmp) % mod

def codingHill(stroka, key):
    #arr = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"№;%:?*()_-+\\/.,@#$^&[]{}\'<>`~|\t\n '

    arr1 = "abcdefghijklmnopqrstuvwxyz_.?"
    arr2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.?"
    arr3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_.,-"
    arr4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя_.,-"

    arr1_1 = "abcdefghijklmnopqrstuvwxyz"
    arr2_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    arr3_3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    arr4_4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    dictionary1 = {}
    j = 0
    for i in arr1:
        dictionary1[j] = i
        j = j + 1

    dictionary2 = {}
    j = 0
    for i in arr2:
        dictionary2[j] = i
        j = j + 1

    dictionary3 = {}
    j = 0
    for i in arr3:
        dictionary3[j] = i
        j = j + 1

    dictionary4 = {}
    j = 0
    for i in arr4:
        dictionary4[j] = i
        j = j + 1

    """dictionary5 = {}
    j = 0
    for i in arr5:
        dictionary5[j] = i
        j = j + 1"""

    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0

    for i in stroka:
        if i in arr1_1:
            count1 += 1
        if i in arr2_2:
            count2 += 1
        if i in arr3_3:
            count3 += 1
        if i in arr4_4:
            count4 += 1

    result_shifr = ''

    if count1 > 0:
        stroka_new = ''
        for k in stroka:
            if k in arr1:
                stroka_new += k
            else:
                stroka_new = stroka_new

        key_encoded = text_to_number(key, dictionary1)
        text_encoded = text_to_number(stroka_new, dictionary1)

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
        print("umnoz ", umnoz)

        print("len = ", len(arr1))
        for i in range(len(umnoz)):
            for j in range(len(umnoz[i])):
                umnoz[i][j] = umnoz[i][j]%(len(arr1))
        print("umnoz ", umnoz)

        for i in range(len(umnoz)):
            for j in range(len(umnoz[i])):
                result_shifr += arr1[umnoz[i][j]]
        print("result_shifr ", result_shifr)

    if count2 > 0:
        stroka_new = ''
        for k in stroka:
            if k in arr2:
                stroka_new += k
            else:
                stroka_new = stroka_new

        key_encoded = text_to_number(key, dictionary2)
        text_encoded = text_to_number(stroka_new, dictionary2)

        size = int(sqrt(len(key_encoded)))
        arr_key = []
        for i in range(size):
            matr = []
            for j in range(size):
                matr.append(key_encoded[0])
                key_encoded = key_encoded[1:]
            arr_key.append(matr)
        arr_key = array(arr_key)
        #print(arr_key)

        arr_str = []
        for i in range(len(text_encoded) // size):
            matr = []
            for j in range(size):
                matr.append(text_encoded[0])
                text_encoded = text_encoded[1:]
            arr_str.append(matr)
        arr_str = array(arr_str)
        #print(arr_str)

        umnoz = []
        for i in range(len(arr_str)):
            umnoz.append(dot(arr_key, arr_str[i]))
            #umnoz.append(dot(arr_str[i], arr_key))
        umnoz = array(umnoz)
        print("umnoz ", umnoz)

        print("len = ", len(arr2))
        for i in range(len(umnoz)):
            for j in range(len(umnoz[i])):
                umnoz[i][j] = umnoz[i][j] % (len(arr2))
        print("umnoz ", umnoz)

        for i in range(len(umnoz)):
            for j in range(len(umnoz[i])):
                result_shifr += arr2[umnoz[i][j]]
        print("result_shifr ", result_shifr)

    if count3 > 0:
        stroka_new = ''
        for k in stroka:
            if k in arr3:
                stroka_new += k
            else:
                stroka_new = stroka_new

        key_encoded = text_to_number(key, dictionary3)
        text_encoded = text_to_number(stroka_new, dictionary3)

        size = int(sqrt(len(key_encoded)))
        arr_key = []
        for i in range(size):
            matr = []
            for j in range(size):
                matr.append(key_encoded[0])
                key_encoded = key_encoded[1:]
            arr_key.append(matr)
        arr_key = array(arr_key)
        # print(arr_key)

        arr_str = []
        for i in range(len(text_encoded) // size):
            matr = []
            for j in range(size):
                matr.append(text_encoded[0])
                text_encoded = text_encoded[1:]
            arr_str.append(matr)
        arr_str = array(arr_str)
        # print(arr_str)

        umnoz = []
        for i in range(len(arr_str)):
            #umnoz.append(dot(arr_str[i],arr_key))
            umnoz.append(dot(arr_key, arr_str[i]))
        umnoz = array(umnoz)
        print("umnoz ", umnoz)

        print("len = ", len(arr3))
        for i in range(len(umnoz)):
            for j in range(len(umnoz[i])):
                umnoz[i][j] = umnoz[i][j] % (len(arr3))
        print("umnoz ", umnoz)

        for i in range(len(umnoz)):
            for j in range(len(umnoz[i])):
                result_shifr += arr3[umnoz[i][j]]
        print("result_shifr ", result_shifr)

    if count4 > 0:
        stroka_new = ''
        for k in stroka:
            if k in arr4:
                stroka_new += k
            else:
                stroka_new = stroka_new

        key_encoded = text_to_number(key, dictionary4)
        text_encoded = text_to_number(stroka_new, dictionary4)

        size = int(sqrt(len(key_encoded)))
        arr_key = []
        for i in range(size):
            matr = []
            for j in range(size):
                matr.append(key_encoded[0])
                key_encoded = key_encoded[1:]
            arr_key.append(matr)
        arr_key = array(arr_key)
        # print(arr_key)

        arr_str = []
        for i in range(len(text_encoded) // size):
            matr = []
            for j in range(size):
                matr.append(text_encoded[0])
                text_encoded = text_encoded[1:]
            arr_str.append(matr)
        arr_str = array(arr_str)
        # print(arr_str)

        umnoz = []
        for i in range(len(arr_str)):
            umnoz.append(dot(arr_key, arr_str[i]))
            #umnoz.append(dot(arr_str[i], arr_key))
        umnoz = array(umnoz)
        print("umnoz ", umnoz)

        print("len = ", len(arr4))
        for i in range(len(umnoz)):
            for j in range(len(umnoz[i])):
                umnoz[i][j] = umnoz[i][j] % (len(arr4))
        print("umnoz ", umnoz)

        for i in range(len(umnoz)):
            for j in range(len(umnoz[i])):
                result_shifr += arr4[umnoz[i][j]]
        print("result_shifr ", result_shifr)

    return result_shifr

def decodingHill(stroka, key):
    arr1 = "abcdefghijklmnopqrstuvwxyz_.?"
    arr2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.?"
    arr3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_.,-"
    arr4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя_.,-"

    arr1_1 = "abcdefghijklmnopqrstuvwxyz"
    arr2_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    arr3_3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    arr4_4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    dictionary1 = {}
    j = 0
    for i in arr1:
        dictionary1[j] = i
        j = j + 1

    dictionary2 = {}
    j = 0
    for i in arr2:
        dictionary2[j] = i
        j = j + 1

    dictionary3 = {}
    j = 0
    for i in arr3:
        dictionary3[j] = i
        j = j + 1

    dictionary4 = {}
    j = 0
    for i in arr4:
        dictionary4[j] = i
        j = j + 1

    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0

    for i in stroka:
        if i in arr1_1:
            count1 += 1
        if i in arr2_2:
            count2 += 1
        if i in arr3_3:
            count3 += 1
        if i in arr4_4:
            count4 += 1

    result_deshifr = ''

    if count1 > 0:
        stroka_new = ''
        for k in stroka:
            if k in arr1:
                stroka_new += k
            else:
                stroka_new = stroka_new

        key_encoded = text_to_number(key, dictionary1)
        text_encoded = text_to_number(stroka_new, dictionary1)

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
                Matr_minor[i][j] = matrix_minor(arr_key, i, j, len(arr1))
        print("minors ", Matr_minor)

        Matr_minor = Matr_minor.transpose()
        print("minors_transp ", Matr_minor)

        det_K = int(linalg.det(arr_key)) % len(arr1)
        print('det ', det_K)
        if (det_K == 0):
            result_deshifr = 'Определитель матрицы равен нулю! Декодирование невозможно!'
            return result_deshifr

        obr_det_K = exgcd(det_K, len(arr1)) % len(arr1)
        print("obr_det_K ", obr_det_K)

        for i in range(len(Matr_minor)):
            for j in range(len(Matr_minor[i])):
                K_obr[i][j] = (obr_det_K * Matr_minor[i][j]) % len(arr1)
        print("K_obr ", K_obr)

        umnoz = []
        for i in range(len(arr_str)):
            umnoz.append(dot(K_obr, arr_str[i]))
        umnoz = array(umnoz)
        print(umnoz)

        for i in range(len(umnoz)):
            for j in range(len(umnoz[i])):
                umnoz[i][j] = umnoz[i][j] % (len(arr1))
        print(umnoz)

        for i in range(len(umnoz)):
            for j in range(len(umnoz[i])):
                result_deshifr += arr1[umnoz[i][j]]
        print(result_deshifr)

    if count2 > 0:
        stroka_new = ''
        for k in stroka:
            if k in arr2:
                stroka_new += k
            else:
                stroka_new = stroka_new

        key_encoded = text_to_number(key, dictionary2)
        text_encoded = text_to_number(stroka_new, dictionary2)

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
                Matr_minor[i][j] = matrix_minor(arr_key, i, j, len(arr2))
        print("minors ", Matr_minor)

        Matr_minor = Matr_minor.transpose()
        print("minors_transp ", Matr_minor)

        det_K = int(linalg.det(arr_key)) % len(arr2)
        print('det ', det_K)
        if (det_K == 0):
            result_deshifr = 'Определитель матрицы равен нулю! Декодирование невозможно!'
            return result_deshifr

        obr_det_K = exgcd(det_K, len(arr2)) % len(arr2)
        print("obr_det_K ", obr_det_K)

        for i in range(len(Matr_minor)):
            for j in range(len(Matr_minor[i])):
                K_obr[i][j] = (obr_det_K * Matr_minor[i][j]) % len(arr2)
        print("K_obr ", K_obr)

        umnoz = []
        for i in range(len(arr_str)):
            umnoz.append(dot(K_obr, arr_str[i]))
        umnoz = array(umnoz)
        print(umnoz)

        for i in range(len(umnoz)):
            for j in range(len(umnoz[i])):
                umnoz[i][j] = umnoz[i][j] % (len(arr2))
        print(umnoz)

        for i in range(len(umnoz)):
            for j in range(len(umnoz[i])):
                result_deshifr += arr2[umnoz[i][j]]
        print(result_deshifr)


    if count3 > 0:
        stroka_new = ''
        for k in stroka:
            if k in arr3:
                stroka_new += k
            else:
                stroka_new = stroka_new

        key_encoded = text_to_number(key, dictionary3)
        text_encoded = text_to_number(stroka_new, dictionary3)

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
                Matr_minor[i][j] = matrix_minor(arr_key, i, j, len(arr3))
        print("minors ", Matr_minor)

        Matr_minor = Matr_minor.transpose()
        print("minors_transp ", Matr_minor)

        det_K = int(linalg.det(arr_key)) % len(arr3)
        print('det ', det_K)
        if (det_K == 0):
            result_deshifr = 'Определитель матрицы равен нулю! Расшифрование невозможно!'
            return result_deshifr

        obr_det_K = exgcd(det_K, len(arr3)) % len(arr3)
        print("obr_det_K ", obr_det_K)

        for i in range(len(Matr_minor)):
            for j in range(len(Matr_minor[i])):
                K_obr[i][j] = (obr_det_K * Matr_minor[i][j]) % len(arr3)
        print("K_obr ", K_obr)

        umnoz = []
        for i in range(len(arr_str)):
            umnoz.append(dot(K_obr, arr_str[i]))
            #umnoz.append(dot(arr_str[i],K_obr))
        umnoz = array(umnoz)
        print(umnoz)

        for i in range(len(umnoz)):
            for j in range(len(umnoz[i])):
                umnoz[i][j] = umnoz[i][j] % (len(arr3))
        print(umnoz)

        for i in range(len(umnoz)):
            for j in range(len(umnoz[i])):
                result_deshifr += arr3[umnoz[i][j]]
        print(result_deshifr)


    if count4 > 0:
        stroka_new = ''
        for k in stroka:
            if k in arr4:
                stroka_new += k
            else:
                stroka_new = stroka_new

        key_encoded = text_to_number(key, dictionary4)
        text_encoded = text_to_number(stroka_new, dictionary4)

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
                Matr_minor[i][j] = matrix_minor(arr_key, i, j, len(arr4))
        print("minors ", Matr_minor)

        Matr_minor = Matr_minor.transpose()
        print("minors_transp ", Matr_minor)

        det_K = int(linalg.det(arr_key)) % len(arr4)
        print('det ', det_K)
        if (det_K == 0):
            result_deshifr = 'Определитель матрицы равен нулю! Декодирование невозможно!'
            return result_deshifr

        obr_det_K = exgcd(det_K, len(arr4)) % len(arr4)
        print("obr_det_K ", obr_det_K)

        for i in range(len(Matr_minor)):
            for j in range(len(Matr_minor[i])):
                K_obr[i][j] = (obr_det_K * Matr_minor[i][j]) % len(arr4)
        print("K_obr ", K_obr)

        umnoz = []
        for i in range(len(arr_str)):
            umnoz.append(dot(K_obr, arr_str[i]))
            #umnoz.append(dot(arr_str[i], K_obr))
        umnoz = array(umnoz)
        print(umnoz)

        for i in range(len(umnoz)):
            for j in range(len(umnoz[i])):
                umnoz[i][j] = umnoz[i][j] % (len(arr4))
        print(umnoz)

        for i in range(len(umnoz)):
            for j in range(len(umnoz[i])):
                result_deshifr += arr4[umnoz[i][j]]
        print(result_deshifr)


    return result_deshifr
