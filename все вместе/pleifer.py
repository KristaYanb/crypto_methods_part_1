from PyQt5 import QtCore, QtGui, QtWidgets
from math import sqrt

def codingPleif(stroka, key):
    arr = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"№;%:?*()-+@#$^&_=\n\t <>/\\\'|'
    #arr1 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"№;%:?*()_-+\\\n '
    new_arr = ''

    stroka = stroka.replace('Ё', 'Е')

    for i in key:
        if i not in new_arr:
            new_arr += i
    for i in arr:
        if i not in new_arr:
            new_arr += i
    print(new_arr)

    result_shifr = ''

    size = int(sqrt(len(arr)))
    arr_matr = []
    for i in range(13):
        matr = []
        for j in range(12):
            matr.append(new_arr[0])
            new_arr = new_arr[1:]
        arr_matr.append(matr)
    #arr_matr = array(arr_matr)
    for i in range(13):
        print(arr_matr[i])

    bigrams = []
    i = 0
    while i < len(stroka):
        two_symb = ''
        if i + 1 == len(stroka):
            two_symb += stroka[i]
            two_symb += "Ё"
            i += 1
            bigrams.append(two_symb)
            break
        if stroka[i] == stroka[i + 1]:
            two_symb += stroka[i]
            two_symb += "Ё"
            i += 1
        else:
            two_symb += stroka[i]
            two_symb += stroka[i + 1]
            i += 2
        bigrams.append(two_symb)
    print("bigrams", bigrams)

    """bigrams = []
    i = 0
    while i < len(stroka):
        two_symb = ''
        if i + 1 == len(stroka):
            two_symb += stroka[i]
            two_symb += ""
            i += 1
            bigrams.append(two_symb)
            break
        if stroka[i] == stroka[i + 1]:
            two_symb += stroka[i]
            two_symb += ""
            i += 1
        else:
            two_symb += stroka[i]
            two_symb += stroka[i + 1]
            i += 2
        bigrams.append(two_symb)
    print("bigrams", bigrams)"""

    for part in bigrams:
        coord1_1 = 0
        coord1_2 = 0
        coord2_1 = 0
        coord2_2 = 0

        """if len(part) == 1:
            for i in range(len(arr_matr)):
                if part[0] in arr_matr[i]:
                    coord1_1 = i
                    coord1_2 = arr_matr[i].index(part[0])
                    break
            print(coord1_1, coord1_2)
            coord2_1 = 7
            coord2_2 = 8

            if coord1_1 == coord2_1:
                result_shifr += arr_matr[coord1_1][(coord1_2 + 1) % 12]
                #result_shifr += arr_matr[coord2_1][(coord2_2 + 1) % 12]

            if coord1_2 == coord2_2:
                result_shifr += arr_matr[(coord1_1 + 1) % len(arr_matr)][coord1_2]
                #result_shifr += arr_matr[(coord2_1 + 1) % len(arr_matr)][coord2_2]

            if (coord1_1 != coord2_1) and (coord1_2 != coord2_2):
                result_shifr += arr_matr[coord1_1][coord2_2]
                #result_shifr += arr_matr[coord2_1][coord1_2]

        else:"""
        for i in range(len(arr_matr)):
            if part[0] in arr_matr[i]:
                coord1_1 = i
                coord1_2 = arr_matr[i].index(part[0])
                break
        for i in range(len(arr_matr)):
            if part[1] in arr_matr[i]:
                coord2_1 = i
                coord2_2 = arr_matr[i].index(part[1])
                break
        print(coord1_1, coord1_2, coord2_1, coord2_2)

        if coord1_1 == coord2_1:
            result_shifr += arr_matr[coord1_1][(coord1_2 + 1) % 12]
            result_shifr += arr_matr[coord2_1][(coord2_2 + 1) % 12]

        if coord1_2 == coord2_2:
            result_shifr += arr_matr[(coord1_1 + 1) % len(arr_matr)][coord1_2]
            result_shifr += arr_matr[(coord2_1 + 1) % len(arr_matr)][coord2_2]

        if (coord1_1 != coord2_1) and (coord1_2 != coord2_2):
            result_shifr += arr_matr[coord1_1][coord2_2]
            result_shifr += arr_matr[coord2_1][coord1_2]

    return result_shifr

def decodingPleif(stroka, key):
    arr = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"№;%:?*()-+@#$^&_=\n\t <>/\\\'|'
    #arr1 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"№;%:?*()_-+\\/\xa0'
    new_arr = ''

    #stroka = stroka.replace('Ё', 'Е')

    for i in key:
        if i not in new_arr:
            new_arr += i
    for i in arr:
        if i not in new_arr:
            new_arr += i
    print(new_arr)

    result_deshifr = ''

    size = int(sqrt(len(arr)))
    arr_matr = []
    for i in range(13):
        matr = []
        for j in range(12):
            matr.append(new_arr[0])
            new_arr = new_arr[1:]
        arr_matr.append(matr)
    for i in range(13):
        print(arr_matr[i])

    bigrams = []
    i = 0
    while i < len(stroka):
        two_symb = ''
        if i + 1 == len(stroka):
            two_symb += stroka[i]
            two_symb += "Ё"
            i += 1
            bigrams.append(two_symb)
            break
        if stroka[i] == stroka[i + 1]:
            two_symb += stroka[i]
            two_symb += "Ё"
            i += 1
        else:
            two_symb += stroka[i]
            two_symb += stroka[i + 1]
            i += 2
        bigrams.append(two_symb)
    print("bigrams", bigrams)

    """bigrams = []
    i = 0
    while i < len(stroka):
        two_symb = ''
        if i + 1 == len(stroka):
            two_symb += stroka[i]
            two_symb += ""
            i += 1
            bigrams.append(two_symb)
            break
        if stroka[i] == stroka[i + 1]:
            two_symb += stroka[i]
            two_symb += ""
            i += 1
        else:
            two_symb += stroka[i]
            two_symb += stroka[i + 1]
            i += 2
        bigrams.append(two_symb)
    print("bigrams", bigrams)"""

    for part in bigrams:
        coord1_1 = 0
        coord1_2 = 0
        coord2_1 = 0
        coord2_2 = 0

        """if len(part) == 1:
            for i in range(len(arr_matr)):
                if part[0] in arr_matr[i]:
                    coord1_1 = i
                    coord1_2 = arr_matr[i].index(part[0])
                    break
            print(coord1_1, coord1_2)
            coord2_1 = 7
            coord2_2 = 8

            if coord1_1 == coord2_1:
                result_deshifr += arr_matr[coord1_1][(coord1_2 - 1) % 12]
                #result_shifr += arr_matr[coord2_1][(coord2_2 + 1) % 12]

            if coord1_2 == coord2_2:
                result_deshifr += arr_matr[(coord1_1 - 1) % len(arr_matr)][coord1_2]
                #result_shifr += arr_matr[(coord2_1 + 1) % len(arr_matr)][coord2_2]

            if (coord1_1 != coord2_1) and (coord1_2 != coord2_2):
                result_deshifr += arr_matr[coord1_1][coord2_2]
                #result_shifr += arr_matr[coord2_1][coord1_2]

        else:"""

        for i in range(len(arr_matr)):
            if part[0] in arr_matr[i]:
                coord1_1 = i
                coord1_2 = arr_matr[i].index(part[0])
                break
        for i in range(len(arr_matr)):
            if part[1] in arr_matr[i]:
                coord2_1 = i
                coord2_2 = arr_matr[i].index(part[1])
                break
        if coord1_1 == coord2_1:
            result_deshifr += arr_matr[coord1_1][(coord1_2 - 1) % 12]
            result_deshifr += arr_matr[coord2_1][(coord2_2 - 1) % 12]

        if coord1_2 == coord2_2:
            result_deshifr += arr_matr[(coord1_1 - 1) % len(arr_matr)][coord1_2]
            result_deshifr += arr_matr[(coord2_1 - 1) % len(arr_matr)][coord2_2]

        if (coord1_1 != coord2_1) and (coord1_2 != coord2_2):
            result_deshifr += arr_matr[coord1_1][coord2_2]
            result_deshifr += arr_matr[coord2_1][coord1_2]

    print(result_deshifr)
    result_deshifr = result_deshifr.replace("Ё","")

    return result_deshifr
