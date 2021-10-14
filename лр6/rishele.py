from PyQt5 import QtCore, QtGui, QtWidgets

def codingRishel(stroka, key):
    result_shifr = ''
    print(key)

    parts = []
    for i in key:
        parts.append([int(j) for j in i.split(',')])
    #print(parts)

    for part in parts:
        len_part = len(part)
        stroka_part = stroka[:(len_part)]
        stroka = stroka[len_part:]
        for i in range(0, len_part):
            result_shifr += stroka_part[int(part[i]) - 1]

    """for part in key:
        part = part.replace(",", "")
        len_part = len(part)
        stroka_part = stroka[:(len_part)]
        stroka = stroka[len_part:]
        for i in range(0,len_part):
            result_shifr += stroka_part[int(part[i])-1]"""

    result_shifr += stroka
    return result_shifr

def decodingRishel(stroka, key):
    result_deshifr = ''

    parts = []
    for i in key:
        parts.append([int(j) for j in i.split(',')])
    #print(parts)

    for part in parts:
        len_part = len(part)
        stroka_part = stroka[:(len_part)]
        stroka = stroka[len_part:]
        for i in range(1, len_part+1):
            for j in range(0, len_part):
                #print(i, int(part[j]))
                if i == int(part[j]):
                    result_deshifr += stroka_part[j]

    result_deshifr += stroka
    return result_deshifr
