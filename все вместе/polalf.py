from PyQt5 import QtCore, QtGui, QtWidgets
import re
import matplotlib
import matplotlib.pyplot as plt
matplotlib.matplotlib_fname()
matplotlib.get_configdir()
matplotlib.get_data_path()
'C:\\Users\\yanbe\\AppData\\Local\\Temp\\_MEI91762\\matplotlib\\mpl-data'

def text_to_number(text, dictionary):  # заменяем символы текста/ключа на числа
    list_code = []

    for i in range(len(text)):
        for value in dictionary:
            if text[i] == dictionary[value]:
                list_code.append(value)
    return list_code

def prepare(stroka): #подготовка алфавита, индекса, частот, текста без лишних символов
    arr1 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    arr2 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    arr3 = "abcdefghijklmnopqrstuvwxyz"
    arr4 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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

    index_ru = 0.0553
    index_en = 0.0644

    # выбор алфавита, частот, индекса
    alf = None
    index = None
    freq = None
    for i in stroka:
        if i in arr4:
            alf = arr4
            index = index_en
            freq = freq_en_h
        elif i in arr3:
            alf = arr3
            index = index_en
            freq = freq_en_l
        elif i in arr2:
            alf = arr2
            index = index_ru
            freq = freq_ru_h
        elif i in arr1:
            alf = arr1
            index = index_ru
            freq = freq_ru_l
        break

    # текст без лишних символов
    text_only = ''
    for i in stroka:
        if i in alf:
            text_only += i

    return alf, index, freq, text_only

def decodingVig(stroka, key): # для конечной расшифровки
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

        print(stroka_new)

        key_encoded = text_to_number(key, dictionary1)
        text_encoded = text_to_number(stroka_new, dictionary1)

        p = 0
        while stroka != '':
            for j in range(len(key)):
                print(stroka[0])
                if stroka[0] in arr1:
                    print(stroka[0])
                    new_index = (text_encoded[p] - key_encoded[p%len(key)]) % len(arr1)
                    p += 1
                    stroka_new = stroka_new[1:]
                    result_deshifr += arr1[new_index]
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
                    new_index = (text_encoded[p] - key_encoded[p%len(key)]) % len(arr2)
                    p += 1
                    stroka_new = stroka_new[1:]
                    result_deshifr += arr2[new_index]
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
                    new_index = (text_encoded[p] - key_encoded[p%len(key)]) % len(arr3)
                    p += 1
                    stroka_new = stroka_new[1:]
                    result_deshifr += arr3[new_index]
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
        print(key_encoded)

        p = 0
        while stroka != '':
            for j in range(len(key)):
                if stroka[0] in arr4:
                    new_index = (text_encoded[p] - key_encoded[p%len(key)]) % len(arr4)
                    p += 1
                    stroka_new = stroka_new[1:]
                    result_deshifr += arr4[new_index]
                else:
                    result_deshifr += stroka[0]
                stroka = stroka[1:]
                if stroka == '':
                    break
            j = 0

    return result_deshifr

"""def search_key_ind(alf, freq, text_only, len_key):
    key = []
    otd_str = []
    freq_list = list(freq)
    key_rez = ''
    max_len = len(text_only)
    now_index = 0.0
    MI = []

    # отдельные строки для анализа
    text_only2 = text_only
    for i in range(0, len_key):
        otd_str.append(text_only2[::len_key])
        text_only2 = text_only2[1:]

    for j in range(0, len_key):
        otd_str1 = otd_str[j]
        otd_str2 = otd_str[(j+1)%len_key]
        print(otd_str[j])
        print(otd_str[(j+1)%len_key])

        # подсчет частот
        count1 = {}
        for p in otd_str1:
            if p in count1:
                count1[p] = count1[p] + 1
            else:
                count1[p] = 1
        print(count1)

        # подсчет частот
        count2 = {}
        for l in otd_str2:
            if l in count2:
                count2[l] = count2[l] + 1
            else:
                count2[l] = 1
        print(count2)

        # подсчет индекса совпадений
        sovpad_index = 0.0
        for m in count1:
            print(m)
            if m in count2:
                print(count1[m], count2[m])
                sovpad_index += (count1[m] * count2[m]) / (len(otd_str1) * (len(otd_str2)))
            else:
                sovpad_index = sovpad_index
        print(sovpad_index)

        if sovpad_index > now_index:
            now_index = sovpad_index
            len_key = i
            if sovpad_index >= index:
                break

    for part in otd_str:
        # частоты символов
        otd_freq = {}
        for i in part:
            if i in otd_freq:
                otd_freq[i] = otd_freq[i] + 1
            else:
                otd_freq[i] = 1

        # поиск наиб частого символа
        big_symb = ('', 0)

        for i in otd_freq:
            if otd_freq[i] > big_symb[1]:
                big_symb = (i, otd_freq[i])

        key.append(alf[(alf.index(big_symb[0]) - alf.index(freq_list[0])) % len(alf)])

    for i in range(len(key)):
        key_rez += key[i]

    return key_rez"""

def search_key_ind(alf, freq, text_only, len_key): # поиск ключа методом взаимных индексов
    otd_str = []

    # отдельные строки для анализа (их кол-во - длина ключа)
    text_only2 = text_only
    for i in range(0, len_key):
        otd_str.append(text_only2[::len_key])
        text_only2 = text_only2[1:]

    sdvigi = []
    for j in range(0, len_key-1):
        otd_str1 = otd_str[0] # относительно первой строки ищем индексы
        otd_str2 = otd_str[j+1]
        print(otd_str1)
        print(otd_str2)

        sovpad = [] # все индексы по строкам
        for y in range(0, len(alf)):
            # заменяем последовательно символы 2-й строки на след по алфавиту
            new_otd_str2 = ''
            for x in otd_str2:
                for z in range(0, len(alf)):
                    if (x == alf[z]):
                        new_otd_str2 += alf[(z + y) % len(alf)]

            # подсче частот в каждой из строк
            count1 = {}
            for p in otd_str1:
                if p in count1:
                    count1[p] = count1[p] + 1
                else:
                    count1[p] = 1

            count2 = {}
            for p in new_otd_str2:
                if p in count2:
                    count2[p] = count2[p] + 1
                else:
                    count2[p] = 1

            # подсчет индекса совпадений
            sovpad_index = 0.0
            for m in count1:
                if m in count2:
                    sovpad_index += (count1[m] * count2[m]) / (len(otd_str1) * (len(new_otd_str2)))
                else:
                    sovpad_index = sovpad_index
            sovpad.append(sovpad_index)
        print(sovpad)

        # поиск наиб сдвига
        vz_index = 0.0
        sdvig_one = 0
        for i in range(len(sovpad)):
            if sovpad[i] > vz_index:
                vz_index = sovpad[i]
                sdvig_one = i
        sdvigi.append(sdvig_one)
        print(sdvigi)

    # ищем все слова по найденным сдвигам
    slova = []
    for i in range(len(alf)):
        slovo = '' + alf[i]
        for j in range(len(sdvigi)):
            slovo += alf[(i - sdvigi[j]) % len(alf)]
        slova.append(slovo)
    print(slova)

    return slova

"""def search_key_autocor(alf, freq, text_only, len_key):
    key = []
    otd_str = []
    freq_list = list(freq)
    key_rez = ''

    # отдельные строки для анализа
    text_only2 = text_only
    for i in range(0, len_key):
        otd_str.append(text_only2[::len_key])
        text_only2 = text_only2[1:]

    for part in otd_str:
        # частоты символов
        otd_freq = {}
        for i in part:
            if i in otd_freq:
                otd_freq[i] = otd_freq[i] + 1
            else:
                otd_freq[i] = 1

        # поиск наиб частого символа
        big_symb = ('', 0)

        for i in otd_freq:
            if otd_freq[i] > big_symb[1]:
                big_symb = (i, otd_freq[i])

        key.append(alf[(alf.index(big_symb[0]) - alf.index(freq_list[0])) % len(alf)])

    for i in range(len(key)):
        key_rez += key[i]

    return key_rez"""

"""def search_key_kas(alf, freq, text_only, len_key):
    key = []
    otd_str = []
    freq_list = list(freq)
    key_rez = ''

    # отдельные строки для анализа
    text_only2 = text_only
    for i in range(0, len_key):
        otd_str.append(text_only2[::len_key])
        text_only2 = text_only2[1:]

    for part in otd_str:
        # частоты символов
        otd_freq = {}
        for i in part:
            if i in otd_freq:
                otd_freq[i] = otd_freq[i] + 1
            else:
                otd_freq[i] = 1

        # поиск наиб частого символа
        big_symb = ('', 0)

        for i in otd_freq:
            if otd_freq[i] > big_symb[1]:
                big_symb = (i, otd_freq[i])

        key.append(alf[(alf.index(big_symb[0]) - alf.index(freq_list[0])) % len(alf)])

    for i in range(len(key)):
        key_rez += key[i]

    return key_rez"""

def index_similar(stroka):
    alf, index, freq, text_only = prepare(stroka)
    len_key = 0
    max_len = len(text_only)

    for p in range(2, max_len):
        # отдельные строки для анализа (поочредно из кол-во увеличивается)
        text_only2 = text_only
        otd_str = []
        for i in range(0, p):
            otd_str.append(text_only2[::p])
            text_only2 = text_only2[1:]
        print(otd_str) #все подстроки

        sovpad = []
        for l in range(0, len(otd_str)):
            # подсчет частот в каждой строке
            new_str = otd_str[l]
            count = {}
            for k in new_str:
                if k in count:
                    count[k] = count[k] + 1
                else:
                    count[k] = 1

            print(count)

            # подсчет индекса совпадений
            sovpad_index = 0.0
            for j in count:
                sovpad_index += (count[j] * (count[j] - 1)) / (len(new_str) * (len(new_str) - 1))
            print(sovpad_index)

            #if sovpad_index > now_index:
                #now_index = sovpad_index
                #len_key = l
            #print(len_key, now_index)

            sovpad.append(sovpad_index)

        # поиск первого индекса, что больше индекса для алфавита
        for t in range(0, len(otd_str)):
            print(sovpad[t], index)
            if sovpad[t] >= index:
                len_key = len(otd_str)
                break

        if len_key > 0:
            break

    print(len_key)

    key = search_key_ind(alf, freq, text_only, len_key) # поиск ключа

    return len_key, key

def plot_autocor(gamma, x):
    fig = plt.plot(x, gamma)
    plt.show()

def autocor(stroka):
    alf, index, freq, text_only = prepare(stroka)
    len_key = 0
    max_len = len(text_only)
    now_index = 0.0
    arr_gamma = []
    x = []
    razn_ind = []

    for i in range(1, max_len):
        # кол-во совпадений при каждом сдвиге текста
        sravn_str = text_only[i:] + text_only[:i]
        count_sovpad = 0
        for j in range(len(text_only)):
            if text_only[j] == sravn_str[j]:
                count_sovpad += 1

        gamma = count_sovpad / (len(text_only))
        #arr_gamma.append(gamma)
        #x.append(i)

        #if gamma > now_index:
            #now_index = gamma
            #len_key = i

            #if new_count_sovpad >= index:
                #break
            #if abs((index - new_count_sovpad)/index)*100 < 10:
                #break
        if ((gamma > index) or ((((gamma - index) / index) * 100 < 0) and (((gamma - index) / index) * 100 > -10))):
            razn_ind.append(i)
        if (len(razn_ind) > 200) or (i == max_len):
            break
    print('razn_ind ', razn_ind)

    all_razn = []
    for i in range(len(razn_ind) - 1):
        all_razn.append(razn_ind[i + 1] - razn_ind[i])
    print('all_razn ', all_razn)

    # частоты значений разности
    freq_razn = {}
    for i in all_razn:
        if i in freq_razn:
            freq_razn[i] = freq_razn[i] + 1
        else:
            freq_razn[i] = 1
    print(freq_razn)

    # в список и сортируем
    freq_razn = list(freq_razn.items())
    freq_razn.sort(key=lambda chastota: chastota[1], reverse=True)
    print(freq_razn)

    # длина ключа - первый в списке
    len_key = freq_razn[0][0]

    #plot_autocor(arr_gamma,x) # вывод диаграммы

    key = search_key_ind(alf, freq, text_only, len_key) # поиск ключа

    return len_key, key

def nod(one, two):
    if two > one:
        t = one
        one = two
        two = t
    if one % two == 0:
        return two
    else:
        return nod(one % two, two)

def find_deviders(num):
    return [i for i in range(2, num + 1) if num % i == 0]

def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

def kas(stroka, len_podstr):
    alf, index, freq, text_only = prepare(stroka)
    all_podstr = {}

    # определение мест вхождений
    text_only2 = text_only
    while len(text_only2) >= len_podstr:
        podstr_str = text_only2[:len_podstr]

        if podstr_str not in all_podstr:
            all_podstr[podstr_str] = []
            for i in re.finditer(podstr_str, text_only):
                all_podstr[podstr_str].append(i.span()[0])
        text_only2 = text_only2[1:]
    print(all_podstr)

    # определение мест вхождений без тех, что 1 раз
    new_all_podstr = {}
    for podstr_str in all_podstr:
        if (len(all_podstr[podstr_str]) > 2):
        #if (len(all_podstr[podstr_str]) != 1):
            new_all_podstr[podstr_str] = []
            for i in range(len(all_podstr[podstr_str])):
                new_all_podstr[podstr_str].append(all_podstr[podstr_str][i])
    print(new_all_podstr)

    # расстояния между вхождениями для каждых подстрок
    all_razn = {}
    for podstr_str in new_all_podstr:
        all_razn[podstr_str] = []
        for i in range(len(new_all_podstr[podstr_str])-1):
            all_razn[podstr_str].append(new_all_podstr[podstr_str][i+1] - new_all_podstr[podstr_str][i])
    print(all_razn)

    if len(all_razn) == 0:
        deviders = 'Невозможно найти длину ключа!'
        return deviders

    # ноды для каждой подстроки
    nods = {}
    obz_nod = []
    for podstr_str in new_all_podstr:
        nod_one = all_razn[podstr_str][0]
        nods[podstr_str] = []
        rez_nod = all_razn[podstr_str][0]
        if (len(all_razn[podstr_str]) > 1) or (all_razn[podstr_str] != []):
            for i in range(1, len(all_razn[podstr_str])):
                nod_two = all_razn[podstr_str][i]
                rez_nod = nod(nod_one, nod_two)
                nod_one = rez_nod
            nods[podstr_str].append(rez_nod)
            obz_nod.append(rez_nod)
        if (len(all_razn[podstr_str]) == 1):
            nods[podstr_str].append(rez_nod)
            obz_nod.append(rez_nod)

    print(obz_nod)
    print(nods)

    # ноды без 0 и повторений
    new_nods = []
    for i in obz_nod:
        if (i != 0) and (i not in new_nods):
            new_nods.append(i)
    print(new_nods)

    # если нет нодов > 0
    count = 0
    for i in new_nods:
        if i == 0:
            count += 1
    if count != 0:
        deviders = 'Невозможно найти длину ключа!'
        return deviders

    # самый последний нод
    rez_nod = 0
    if len(new_nods) != 1:
        nod_one = new_nods[0]
        rez_nod = 0
        for i in range(1, len(new_nods)):
            nod_two = new_nods[i]
            rez_nod = nod(nod_one, nod_two)
            nod_one = rez_nod
    else:
        for i in new_nods:
            rez_nod = i
    print(rez_nod)

    # если нод = 1
    if rez_nod == 1:
        deviders = 'Невозможно найти длину ключа!'
        return deviders

    print(rez_nod)

    # проверка на простоту нода
    if IsPrime(rez_nod) == False:
        deviders = find_deviders(rez_nod)
        print(deviders)
    else:
        deviders = [rez_nod]

    return deviders