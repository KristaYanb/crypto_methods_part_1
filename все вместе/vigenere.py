from PyQt5 import QtCore, QtGui, QtWidgets

def text_to_number(text,dictionary):   #заменяем символы текста/ключа на числа
    list_code = []
    
    for i in range(len(text)):
        for value in dictionary:
            if text[i] == dictionary[value]:
               list_code.append(value)
    return list_code

def codingVigener(stroka, key):
    arr1 = "abcdefghijklmnopqrstuvwxyz"
    arr2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    arr3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    arr4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

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
        if i in arr1:
            count1 += 1
        if i in arr2:
            count2 += 1
        if i in arr3:
            count3 += 1
        if i in arr4:
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

        p = 0
        while stroka != '':
            for j in range(len(key)):
                if stroka[0] in arr1:
                    new_index = (text_encoded[p] + key_encoded[j]) % len(arr1)
                    p += 1
                    stroka_new = stroka_new[1:]
                    result_shifr += arr1[new_index]
                else:
                    result_shifr += stroka[0]
                stroka = stroka[1:]
                if stroka == '':
                    break
            j = 0

    if count2 > 0:
        stroka_new = ''
        for k in stroka:
            if k in arr2:
                stroka_new += k
            else:
                stroka_new = stroka_new

        key_encoded = text_to_number(key, dictionary2)
        text_encoded = text_to_number(stroka_new, dictionary2)

        p = 0
        while stroka != '':
            for j in range(len(key)):
                if stroka[0] in arr2:
                    new_index = (text_encoded[p] + key_encoded[j]) % len(arr2)
                    p += 1
                    stroka_new = stroka_new[1:]
                    result_shifr += arr2[new_index]
                else:
                    result_shifr += stroka[0]
                stroka = stroka[1:]
                if stroka == '':
                    break
            j = 0

    if count3 > 0:
        stroka_new = ''
        for k in stroka:
            if k in arr3:
                stroka_new += k
            else:
                stroka_new = stroka_new

        key_encoded = text_to_number(key, dictionary3)
        text_encoded = text_to_number(stroka_new, dictionary3)

        p = 0
        while stroka != '':
            for j in range(len(key)):
                if stroka[0] in arr3:
                    new_index = (text_encoded[p] + key_encoded[j]) % len(arr3)
                    p += 1
                    stroka_new = stroka_new[1:]
                    result_shifr += arr3[new_index]
                else:
                    result_shifr += stroka[0]
                stroka = stroka[1:]
                if stroka == '':
                    break
            j = 0

    if count4 > 0:
        stroka_new = ''
        for k in stroka:
            if k in arr4:
                stroka_new += k
            else:
                stroka_new = stroka_new

        key_encoded = text_to_number(key, dictionary4)
        text_encoded = text_to_number(stroka_new, dictionary4)

        p = 0
        while stroka != '':
            for j in range(len(key)):
                if stroka[0] in arr4:
                    new_index = (text_encoded[p] + key_encoded[j]) % len(arr4)
                    p += 1
                    stroka_new = stroka_new[1:]
                    result_shifr += arr4[new_index]
                else:
                    result_shifr += stroka[0]
                stroka = stroka[1:]
                if stroka == '':
                    break
            j = 0

    return result_shifr

def decodingVigener(stroka, key):
    arr1 = "abcdefghijklmnopqrstuvwxyz"
    arr2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    arr3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    arr4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

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
        if i in arr1:
            count1 += 1
        if i in arr2:
            count2 += 1
        if i in arr3:
            count3 += 1
        if i in arr4:
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

        p = 0
        while stroka != '':
            for j in range(len(key)):
                if stroka[0] in arr1:
                    new_index = (text_encoded[p] - key_encoded[j]) % len(arr1)
                    p += 1
                    stroka_new = stroka_new[1:]
                    result_deshifr += arr1[new_index]
                    print(result_deshifr)
                else:
                    result_deshifr += stroka[0]
                stroka = stroka[1:]
                if stroka == '':
                    break
            j = 0

    if count2 > 0:
        stroka_new = ''
        for k in stroka:
            if k in arr2:
                stroka_new += k
            else:
                stroka_new = stroka_new

        key_encoded = text_to_number(key, dictionary2)
        text_encoded = text_to_number(stroka_new, dictionary2)

        p = 0
        while stroka != '':
            for j in range(len(key)):
                if stroka[0] in arr2:
                    new_index = (text_encoded[p] - key_encoded[j]) % len(arr2)
                    p += 1
                    stroka_new = stroka_new[1:]
                    result_deshifr += arr2[new_index]
                    print(result_deshifr)
                else:
                    result_deshifr += stroka[0]
                stroka = stroka[1:]
                if stroka == '':
                    break
            j = 0

    if count3 > 0:
        stroka_new = ''
        for k in stroka:
            if k in arr3:
                stroka_new += k
            else:
                stroka_new = stroka_new

        key_encoded = text_to_number(key, dictionary3)
        text_encoded = text_to_number(stroka_new, dictionary3)

        p = 0
        while stroka != '':
            for j in range(len(key)):
                if stroka[0] in arr3:
                    new_index = (text_encoded[p] - key_encoded[j]) % len(arr3)
                    p += 1
                    stroka_new = stroka_new[1:]
                    result_deshifr += arr3[new_index]
                    print(result_deshifr)
                else:
                    result_deshifr += stroka[0]
                stroka = stroka[1:]
                if stroka == '':
                    break
            j = 0

    if count4 > 0:
        stroka_new = ''
        for k in stroka:
            if k in arr4:
                stroka_new += k
            else:
                stroka_new = stroka_new

        key_encoded = text_to_number(key, dictionary4)
        text_encoded = text_to_number(stroka_new, dictionary4)

        p = 0
        while stroka != '':
            for j in range(len(key)):
                if stroka[0] in arr4:
                    new_index = (text_encoded[p] - key_encoded[j]) % len(arr4)
                    p += 1
                    stroka_new = stroka_new[1:]
                    result_deshifr += arr4[new_index]
                    print(result_deshifr)
                else:
                    result_deshifr += stroka[0]
                stroka = stroka[1:]
                if stroka == '':
                    break
            j = 0

    return result_deshifr
