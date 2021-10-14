from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from numpy import array,delete,reshape,shape
from random import randint

def do_matr(key):   #заменяем символы текста/ключа на числа
    size = int(key)
    arr1 = []

    k = 1
    for i in range(size):
        matr = []
        for j in range(size):
            matr.append(str(k))
            k += 1
        arr1.append(matr)

    arr3 = np.rot90(arr1)
    arr4 = np.rot90(arr3)
    arr2 = np.rot90(arr4)

    arr1 = array(arr1, dtype="U25")
    arr2 = array(arr2, dtype="U25")
    arr3 = array(arr3, dtype="U25")
    arr4 = array(arr4, dtype="U25")

    # генерация матрицы
    for k in range(1, size * size + 1):
        number_matr = randint(1, 4)
        if number_matr == 1:
            for i in range(len(arr1)):
                for j in range(len(arr1)):
                    if arr1[i][j] == str(k):
                        arr1[i][j] += 'X'

        if number_matr == 2:
            for i in range(len(arr2)):
                for j in range(len(arr2)):
                    if arr2[i][j] == str(k):
                        arr2[i][j] += 'X'

        if number_matr == 3:
            for i in range(len(arr3)):
                for j in range(len(arr3)):
                    if arr3[i][j] == str(k):
                        arr3[i][j] += 'X'

        if number_matr == 4:
            for i in range(len(arr4)):
                for j in range(len(arr4)):
                    if arr4[i][j] == str(k):
                        arr4[i][j] += 'X'

    arr11 = np.hstack((arr1, arr2))  # вправо
    arr12 = np.hstack((arr3, arr4))  # вправо
    arr = np.vstack((arr11, arr12))  # вниз

    return arr

def resh_to_matr(reshetka, size):

    lines = []
    lines = reshetka.split(' \n')

    out = []
    for i in lines:
        if i == '':
            break
        arr_el = i.split(' ')
        min_arr = []
        for j in range(size*2):
            min_arr.append(arr_el[j])
        min_arr = np.array(min_arr)
        out.append(min_arr)
    out = array(out, dtype="U25")
    print("out_res ", out)
    return out

def codingCardano(stroka, key, reshetka):
    size = int(key)

    arr = resh_to_matr(reshetka,size)
    #print("arr_coding ", arr)

    while len(stroka) % (4 * size * size) != 0:
        o = randint(65,126)
        stroka += chr(o)
        #stroka += "*"

    # заполнение результирующей матрицы
    restext = ""
    for r in range(len(stroka) // (size * size * 4)):
        # результирующая пока пустая матрица
        res = []
        for i in range(size * 2):
            res_min = []
            for j in range(size * 2):
                res_min.append("")
            res.append(res_min)

        for p in range(4):
            for k in range(1, size * size + 1):
                i, j = np.where(arr == str(k) + "X")
                res[int(i)][int(j)] = stroka[k - 1]
            arr = np.rot90(arr)
            stroka = stroka[size * size:]

        for i in range(len(res)):
            for k in range(len(res[i])):
                restext += res[i][k]
        #print(restext, " restext")

    #print(restext, " restext")
    return restext

def decodingCardano(stroka_encr, key, reshetka):
    size = int(key)

    arr = resh_to_matr(reshetka, size)
    #print("arr_decoding ", arr)

    stroka_res = ''
    for j in range(len(stroka_encr)):
        stroka_res += stroka_encr[j]

    outputText = ''
    # процесс
    for r in range(len(stroka_res) // (size * size * 4)):
        # матрица с исходным текстом
        res_matr = []
        for i in range(size * 2):
            res_min = []
            for j in range(size * 2):
                res_min.append(stroka_res[0])
                stroka_res = stroka_res[1:]
            res_matr.append(res_min)

        for p in range(4):
            for k in range(1, size * size + 1):
                i, j = np.where(arr == str(k) + "X")
                outputText += res_matr[int(i)][int(j)]
            arr = np.rot90(arr)
    #outputText = outputText.replace('*', '')
    #print(outputText)
    return outputText
