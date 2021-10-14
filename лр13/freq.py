from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib
import matplotlib.pyplot as plt

matplotlib.matplotlib_fname()
matplotlib.get_configdir()
matplotlib.get_data_path()
'C:\\Users\\yanbe\\AppData\\Local\\Temp\\_MEI91762\\matplotlib\\mpl-data'
import numpy as np


def make_prompt(pattern):
    prompt = {}

    for key in pattern:
        tmp = []
        prompt[key] = tmp

        for key_ in pattern:
            if (abs((pattern[key] - pattern[key_])) / pattern[key_]) * 100 <= 10:
                prompt[key].append(key_)

    return prompt


def print_gist(stroka, alf, freq_alf):
    text_only = ''
    for i in stroka:
        if i in alf:
            text_only += i

    freq = {}
    for i in text_only:
        if i in freq:
            freq[i] = freq[i] + 1
        else:
            freq[i] = 1

    freq = list(freq.items())
    freq.sort(key=lambda chastota: chastota[1], reverse=True)

    freq_new = []
    for i in range(len(freq)):
        freq_new1 = []
        freq_new1.append(freq[i][0])
        freq_new1.append(round(int(freq[i][1]) / len(text_only), 4))
        freq_new.append(freq_new1)

    freq_alf_new = list(freq_alf.items())

    x = []
    y = []
    for i in range(len(freq_new)):
        x.append(freq_new[i][0])
        y.append(freq_new[i][1])
    fig, ax = plt.subplots()
    ax.bar(x, y)
    plt.show()


def zamena(stroka, symb1, symb2, alf):
    new_stroka = ''
    for i in range(0, len(stroka)):
        if stroka[i] == symb1:
            new_stroka += str(symb2)
        else:
            if stroka[i] == symb2:
                new_stroka += str(symb1)
            else:
                if (stroka[i] != symb2) and (stroka[i] != symb1):
                    new_stroka += stroka[i]

    return new_stroka


def decodingFreq(stroka):
    arr1 = "abcdefghijklmnopqrstuvwxyz"
    arr2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    arr3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    arr4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    freq_ru_h = {'О': 0.1097, 'Е': 0.0845, 'А': 0.0801, 'И': 0.0735, 'Н': 0.0670, 'Т': 0.0626, 'С': 0.0547, 'Р': 0.0473,
                 'В': 0.0454, 'Л': 0.0440, 'К': 0.0349, 'М': 0.0321, 'Д': 0.0298, 'П': 0.0281, 'У': 0.0262, 'Я': 0.0201,
                 'Ы': 0.0190, 'Ь': 0.0174, 'Г': 0.0170, 'З': 0.0165, 'Б': 0.0159, 'Ч': 0.0144, 'Й': 0.0121, 'Х': 0.0097,
                 'Ж': 0.0094, 'Ш': 0.0073, 'Ю': 0.0064, 'Ц': 0.0048, 'Щ': 0.0036, 'Э': 0.0032, 'Ф': 0.0026, 'Ъ': 0.0004,
                 'Ё': 0.0004}
    arr_ru_h = 'ОЕАИНТСРВЛКМДПУЯЫЬГЗБЧЙХЖШЮЦЩЭФЪЁ'
    freq_ru_l = {'о': 0.1097, 'е': 0.0845, 'а': 0.0801, 'и': 0.0735, 'н': 0.0670, 'т': 0.0626, 'с': 0.0547,
                 'р': 0.0473, 'в': 0.0454, 'л': 0.0440, 'к': 0.0349, 'м': 0.0321, 'д': 0.0298, 'п': 0.0281,
                 'у': 0.0262, 'я': 0.0201, 'ы': 0.0190, 'ь': 0.0174, 'г': 0.0170, 'з': 0.0165, 'б': 0.0159,
                 'ч': 0.0144, 'й': 0.0121, 'х': 0.0097, 'ж': 0.0094, 'ш': 0.0073, 'ю': 0.0064, 'ц': 0.0048,
                 'щ': 0.0036, 'э': 0.0032, 'ф': 0.0026, 'ъ': 0.0004, 'ё': 0.0004}
    arr_ru_l = 'оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъё'
    freq_en_h = {'E': 0.1270, 'T': 0.0906, 'A': 0.0817, 'O': 0.0751, 'I': 0.0697, 'N': 0.0675, 'S': 0.0633, 'H': 0.0609,
                 'R': 0.0599, 'D': 0.0425, 'L': 0.0403, 'C': 0.0278, 'U': 0.0276, 'M': 0.0241, 'W': 0.0236, 'F': 0.0223,
                 'G': 0.0202, 'Y': 0.0197, 'P': 0.0193, 'B': 0.0149, 'V': 0.0098, 'K': 0.0077, 'X': 0.0015, 'J': 0.0015,
                 'Q': 0.0010, 'Z': 0.0005}
    arr_en_h = 'ETAOINSHRDLCUMWFGYPBVKXJQZ'
    freq_en_l = {'e': 0.1270, 't': 0.0906, 'a': 0.0817, 'o': 0.0751, 'i': 0.0697, 'n': 0.0675, 's': 0.0633,
                 'h': 0.0609, 'r': 0.0599, 'd': 0.0425, 'l': 0.0403, 'c': 0.0278, 'u': 0.0276, 'm': 0.0241,
                 'w': 0.0236, 'f': 0.0223, 'g': 0.0202, 'y': 0.0197, 'p': 0.0193, 'b': 0.0149, 'v': 0.0098,
                 'k': 0.0077, 'x': 0.0015, 'j': 0.0015, 'q': 0.0010, 'z': 0.0005}
    arr_en_l = 'etaoinshrdlcumwfgypbvkxjqz'

    alf = None
    arr = ''
    arr_norm = ''
    for i in stroka:
        if i in freq_en_h:
            alf = freq_en_h
            arr = arr_en_h
            arr_norm = arr2
        elif i in freq_en_l:
            alf = freq_en_l
            arr = arr_en_l
            arr_norm = arr1
        elif i in freq_ru_h:
            alf = freq_ru_h
            arr = arr_ru_h
            arr_norm = arr3
        elif i in freq_ru_l:
            alf = freq_ru_l
            arr = arr_ru_l
            arr_norm = arr4
        break

    text_only = ''
    for i in stroka:
        if i in alf:
            text_only += i

    freq = {}
    for i in text_only:
        if i in freq:
            freq[i] = freq[i] + 1
        else:
            freq[i] = 1

    podskazka = make_prompt(freq)
    # print(str(podskazka))

    freq = list(freq.items())
    freq.sort(key=lambda chastota: chastota[1], reverse=True)
    print(freq)

    for q in range(len(arr_norm)):
        for i in range(len(freq) - 1):
            j = i + 1
            zam1 = 0
            zam2 = 0
            if freq[i][1] == freq[j][1]:
                for k in range(len(arr_norm)):
                    if freq[i][0] == arr_norm[k]:
                        zam1 = k
                    if freq[j][0] == arr_norm[k]:
                        zam2 = k
                if (zam1 > zam2):
                    freq[i], freq[j] = freq[j], freq[i]
    # print(freq)

    freq_new = []
    for i in range(len(freq)):
        freq_new1 = []
        freq_new1.append(freq[i][0])
        freq_new1.append(round(int(freq[i][1]) / len(text_only), 4))
        freq_new.append(freq_new1)
    print(freq_new)

    vivod = 'Замены:\n'

    for i in range(len(freq_new)):
        vivod += (freq_new[i][0] + ' ' + arr[i] + '\n')

    new_stroka = ''
    for i in range(len(stroka)):
        if stroka[i] in arr:
            for j in range(len(freq_new)):
                if stroka[i] == freq_new[j][0]:
                    new_stroka = new_stroka + arr[j]
        else:
            new_stroka += stroka[i]

    return new_stroka, vivod, podskazka
