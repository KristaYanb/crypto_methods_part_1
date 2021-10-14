from PyQt5 import QtCore, QtGui, QtWidgets

def text_to_number(text, dictionary):   #заменяем символы текста/ключа на числа
    list_code = []
    
    for i in range(len(text)):
        for value in dictionary:
            if text[i] == dictionary[value]:
               list_code.append(value)
    return list_code

def codingAlberti(stroka, key, key2):

    #arr = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"№;%:?*()_-+\\/.,@#$^&[]{}\'<>`~|\t\n '
    arr = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    #arr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_arr = ''

    for i in key:
        if i not in new_arr:
            new_arr += i

    for i in arr:
        if i not in new_arr:
            new_arr += i
    #print(new_arr)

    dictionary = {}
    j = 0
    for i in arr:
        dictionary[j] = i
        j = j + 1

    result_shifr = ''

    key2 *= len(stroka) // len(key2) + 1
    #print(key2)
    key_encoded = text_to_number(key2, dictionary)
    #print(key_encoded)
    p = -1
    for i in stroka:
        if i in arr:        #только буквы
            for j, k in enumerate(arr):
                if i == k:
                    p += 1
                    #print(p)
                    #print(j, key_encoded[p])
                    result_shifr += new_arr[(j - key_encoded[p]) % len(new_arr)]
        else:               #только буквы
            result_shifr += i   #только буквы

    return result_shifr

def decodingAlberti(stroka, key, key2):
    #arr = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"№;%:?*()_-+\\/.,@#$^&[]{}\'<>`~|\t\n '
    arr = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    #arr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_arr = ''

    for i in key:
        if i not in new_arr:
            new_arr += i

    for i in arr:
        if i not in new_arr:
            new_arr += i

    dictionary = {}
    j = 0
    for i in arr:
        dictionary[j] = i
        j = j + 1

    result_deshifr = ''

    key2 *= len(stroka) // len(key2) + 1
    key_encoded = text_to_number(key2, dictionary)
    p = -1
    for i in stroka:
        if i in arr:            #только буквы
            for j, k in enumerate(new_arr):
                if i == k:
                    p += 1
                    result_deshifr += arr[(j + key_encoded[p]) % len(arr)]
        else:                   #только буквы
            result_deshifr += i #только буквы

    return result_deshifr
