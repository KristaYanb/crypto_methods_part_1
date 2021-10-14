from PyQt5 import QtCore, QtGui, QtWidgets

import urllib

def text_to_number(text, dictionary):  # заменяем символы текста/ключа на числа
    list_code = []

    for i in range(len(text)):
        for value in dictionary:
            if text[i] == dictionary[value]:
                list_code.append(value)
    return list_code

def codingVernam(stroka, key):
    alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !"#$%&\'()*+,-./0123456789:;<=>?@[\]^_`{|}~№«¬»±§©µ¶¦÷¡¿®×¢£¤¥\n\t\x9d\x9e\x9f\xad°²³·¸¹º¼½¾ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüý'

    dictionary = {}
    j = 0
    for i in alf:
        dictionary[j] = i
        j = j + 1

    key_encoded = text_to_number(key, dictionary)
    text_encoded = text_to_number(stroka, dictionary)

    result_shifr = ''
    bin_key = ''
    bin_str = ''
    rez = ''

    for i in range(len(stroka)):
        #print(type(txt[i]),key2[i], txt[i] ^ key2[i])
        #print(bytes([txt[i] ^ key2[i]]).decode('cp1251'))
        result_shifr += alf[text_encoded[i] ^ key_encoded[i]]
        #print(result_shifr)

        ak = str(bin(text_encoded[i] ^ key_encoded[i]))[2::]
        al = str(bin(key_encoded[i])[2::])
        am = str(bin(text_encoded[i])[2::])
        #print(ak, al, am)
        if len(ak) < 8:
            for j in range(0, 8 - len(ak)):
                ak = '0' + ak
        if len(al) < 8:
            for j in range(0, 8 - len(al)):
                al = '0' + al
        if len(am) < 8:
            for j in range(0, 8 - len(am)):
                am = '0' + am
        #print(ak,al,am)
        rez += ak
        bin_key += al
        bin_str += am
    len_rez = len(rez)
    len_str = len(bin_str)
    len_key = len(bin_key)

    vivod = 'Открытый текст: длина = ' + str(len_str) + '\n' +  bin_str +  '\n\nКлюч: длина = ' + str(len_key) + '\n' + bin_key + '\n\nРезультат: длина = ' + str(len_rez) + '\n' + rez

    return result_shifr, vivod

def decodingVernam(stroka, key):
    alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !"#$%&\'()*+,-./0123456789:;<=>?@[\]^_`{|}~№«¬»±§©µ¶¦÷¡¿®×¢£¤¥\n\t\x9d\x9e\x9f\xad°²³·¸¹º¼½¾ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüý'

    dictionary = {}
    j = 0
    for i in alf:
        dictionary[j] = i
        j = j + 1

    text_encoded = text_to_number(stroka, dictionary)

    result_deshifr = ''
    bin_str = ''
    rez = ''

    key2 = key
    for i in range(len(stroka)):
        k_part = int(key[:8], 2)
        #print(k_part)
        key = key[8:]
        #print(key)
        # print(type(txt[i]),key2[i], txt[i] ^ key2[i])
        # print(bytes([txt[i] ^ key2[i]]).decode('cp1251'))
        result_deshifr += alf[text_encoded[i] ^ k_part]
        #print(result_deshifr)

        ak = str(bin(text_encoded[i] ^ k_part))[2::]
        am = str(bin(text_encoded[i])[2::])
        # print(ak, am)
        if len(ak) < 8:
            for j in range(0, 8 - len(ak)):
                ak = '0' + ak
        if len(am) < 8:
            for j in range(0, 8 - len(am)):
                am = '0' + am
        # print(ak, am)
        rez += ak
        bin_str += am
    len_rez = len(rez)
    len_str = len(bin_str)

    vivod = 'Открытый текст: длина = ' + str(len_str) + '\n' + bin_str + '\n\nКлюч: длина = ' + str(len(key2)) + '\n' + key2 + '\n\nРезультат: длина = ' + str(len_rez) + '\n' + rez

    return result_deshifr, vivod

"""def codingVernam(stroka, key):

    result_shifr = u''
    bin_key = ''
    bin_str = ''
    rez = ''

    txt = stroka.encode('cp1251')
    #print(txt)

    key2 = key.encode('cp1251')
    #print(key2)

    for i in range(len(txt)):
        #print(type(txt[i]),key2[i], txt[i] ^ key2[i])
        #print(bytes([txt[i] ^ key2[i]]).decode('cp1251'))
        result_shifr += (bytes([txt[i] ^ key2[i]]).decode('cp1251'))
        #print(result_shifr)

        ak = str(bin(txt[i] ^ key2[i]))[2::]
        al = str(bin(key2[i])[2::])
        am = str(bin(txt[i])[2::])
        #print(ak, al, am)
        if len(ak) < 8:
            for j in range(0, 8 - len(ak)):
                ak = '0' + ak
        if len(al) < 8:
            for j in range(0, 8 - len(al)):
                al = '0' + al
        if len(am) < 8:
            for j in range(0, 8 - len(am)):
                am = '0' + am
        #print(ak,al,am)
        rez += ak
        bin_key += al
        bin_str += am
    len_rez = len(rez)
    len_str = len(bin_str)
    len_key = len(bin_key)

    vivod = 'Открытый текст: длина = ' + str(len_str) + '\n' +  bin_str +  '\n\nКлюч: длина = ' + str(len_key) + '\n' + bin_key + '\n\nРезультат: длина = ' + str(len_rez) + '\n' + rez

    return result_shifr, vivod"""