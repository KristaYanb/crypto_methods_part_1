from PyQt5 import QtCore, QtGui, QtWidgets

import urllib

def text_to_number(text, dictionary):  # заменяем символы текста/ключа на числа
    list_code = []

    for i in range(len(text)):
        for value in dictionary:
            if text[i] == dictionary[value]:
                list_code.append(value)
    return list_code

def codingGamma(stroka, key, file = None):
    alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !"#$%&\'()*+,-./0123456789:;<=>?@[\]^_`{|}~№«¬»±§©µ¶¦÷¡¿®×¢£¤¥\n\t\x9d\x9e\x9f\xad°²³·¸¹º¼½¾ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüý'

    result_shifr = ''
    bin_str = ''
    rez = ''

    dictionary = {}
    j = 0
    for i in alf:
        dictionary[j] = i
        j = j + 1

    text_encoded = text_to_number(stroka, dictionary)

    for i in range(len(stroka)):
        am = str(bin(text_encoded[i])[2::])
        if len(am) < 8:
            for j in range(0, 8 - len(am)):
                am = '0' + am
        bin_str += am
    len_str = len(bin_str)

    key_encoded1 = bin(int(key))[2::]
    key_encoded1 *= len_str // len(key_encoded1) + 1

    for i in range(len_str):
        ak = str(int(bin_str[i]) ^ int(key_encoded1[i]))
        rez += ak

    rez2 = rez
    out_bytes = []
    for i in range(len_str//8):
        result_shifr += alf[int(rez2[:8], 2)]
        out_bytes.append(int(rez2[:8], 2))
        rez2 = rez2[8:]

    vivod = 'Открытый текст: длина = ' + str(len_str) + '\n' +  bin_str +  '\n\nКлюч: длина = ' + str(len_str) + '\n' + key_encoded1[:len_str] + '\n\nРезультат: длина = ' + str(len(rez)) + '\n' + rez

    if file:
        output_data = bytes(out_bytes)
        file.write(output_data)
        return result_shifr, vivod
    else:
        return result_shifr, vivod

def decodingGamma(stroka, key):
    alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !"#$%&\'()*+,-./0123456789:;<=>?@[\]^_`{|}~№«¬»±§©µ¶¦÷¡¿®×¢£¤¥\n\t\x9d\x9e\x9f\xad°²³·¸¹º¼½¾ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüý'

    result_deshifr = ''
    bin_str = ''
    rez = ''

    dictionary = {}
    j = 0
    for i in alf:
        dictionary[j] = i
        j = j + 1

    text_encoded = text_to_number(stroka, dictionary)

    for i in range(len(stroka)):
        am = str(bin(text_encoded[i])[2::])
        if len(am) < 8:
            for j in range(0, 8 - len(am)):
                am = '0' + am
        bin_str += am
    len_str = len(bin_str)

    key_encoded1 = key

    for i in range(len_str):
        ak = str(int(bin_str[i]) ^ int(key_encoded1[i]))
        rez += ak

    rez2 = rez
    for i in range(len_str // 8):
        result_deshifr += alf[int(rez2[:8], 2)]
        rez2 = rez2[8:]

    vivod = 'Открытый текст: длина = ' + str(len_str) + '\n' + bin_str + '\n\nКлюч: длина = ' + str(
        len_str) + '\n' + key_encoded1[:len_str] + '\n\nРезультат: длина = ' + str(len(rez)) + '\n' + rez

    return result_deshifr, vivod

def codingGamma_file(key, stroka, opt_file=None):
    alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !"#$%&\'()*+,-./0123456789:;<=>?@[\]^_`{|}~№«¬»±§©µ¶¦÷¡¿®×¢£¤¥\n\t\x9d\x9e\x9f\xad°²³·¸¹º¼½¾ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüý'

    result_shifr = ''
    bin_str = ''
    rez = ''

    dictionary = {}
    j = 0
    for i in alf:
        dictionary[j] = i
        j = j + 1

    text_encoded = text_to_number(stroka, dictionary)

    for i in range(len(stroka)):
        am = str(bin(text_encoded[i])[2::])
        if len(am) < 8:
            for j in range(0, 8 - len(am)):
                am = '0' + am
        bin_str += am
    len_str = len(bin_str)

    key_encoded1 = bin(int(key))[2::]
    key_encoded1 *= len_str // len(key_encoded1) + 1

    for i in range(len_str):
        ak = str(int(bin_str[i]) ^ int(key_encoded1[i]))
        rez += ak

    rez2 = rez
    out_bytes = []
    for i in range(len_str//8):
        result_shifr += alf[int(rez2[:8], 2)]
        out_bytes.append(int(rez2[:8], 2))
        rez2 = rez2[8:]

    vivod = 'Открытый текст: длина = ' + str(len_str) + '\n' +  bin_str +  '\n\nКлюч: длина = ' + str(len_str) + '\n' + key_encoded1[:len_str] + '\n\nРезультат: длина = ' + str(len(rez)) + '\n' + rez

    if opt_file:
        output_data = bytes(out_bytes)
        opt_file.write(output_data)
        return result_shifr, vivod
    else:
        return result_shifr, vivod

"""def codingGamma(stroka, key):

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