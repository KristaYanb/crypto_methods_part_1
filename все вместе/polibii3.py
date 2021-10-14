from PyQt5 import QtCore, QtGui, QtWidgets

def codingPolibii3(text): #Шифрование

    arr1_1 = "abcdefghijklmnopqrstuvwxyz"
    arr2_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    arr3_3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    arr4_4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    arr1 = [['a', 'b', 'c', 'd', 'e'],
            ['f', 'g', 'h', 'i', 'k'],
            ['l', 'm', 'n', 'o', 'p'],
            ['q', 'r', 's', 't', 'u'],
            ['v', 'w', 'x', 'y', 'z']]

    arr2 = [['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'K'],
            ['L', 'M', 'N', 'O', 'P'],
            ['Q', 'R', 'S', 'T', 'U'],
            ['V', 'W', 'X', 'Y', 'Z']]

    arr3 = [['А', 'Б', 'В', 'Г', 'Д'],
            ['Е', 'Ж', 'З', 'И', 'К'],
            ['Л', 'М', 'Н', 'О', 'П'],
            ['Р', 'С', 'Т', 'У', 'Ф'],
            ['Х', 'Ц', 'Ч', 'Ш', 'Щ'],
            ['Ы', 'Ь', 'Э', 'Ю', 'Я']]

    arr4 = [['а', 'б', 'в', 'г', 'д'],
            ['е', 'ж', 'з', 'и', 'к'],
            ['л', 'м', 'н', 'о', 'п'],
            ['р', 'с', 'т', 'у', 'ф'],
            ['х', 'ц', 'ч', 'ш', 'щ'],
            ['ы', 'ь', 'э', 'ю', 'я']]

    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0

    for i in text:
        if i in arr1_1:
            count1 += 1
        if i in arr2_2:
            count2 += 1
        if i in arr3_3:
            count3 += 1
        if i in arr4_4:
            count4 += 1

    text = text.replace('Ё', 'Е')
    text = text.replace('Ъ', 'Ь')
    text = text.replace('Й', 'И')
    text = text.replace('j', 'i')
    text = text.replace('J', 'I')
    text = text.replace('ё', 'е')
    text = text.replace('ъ', 'ь')
    text = text.replace('й', 'и')

    result_shifr = ''
    result_shifr2 = ''
    for i in (range(0, len(text))):
        result_shifr += '*'
        result_shifr2 += '*'

    for i in (range (0,len(text))):
        if (text[i] not in arr1_1) and (text[i] not in arr2_2) and (text[i] not in arr3_3) and (text[i] not in arr4_4):
            result_shifr = result_shifr[:i] + text[i] + result_shifr[(i + 1):]
            result_shifr2 = result_shifr2[:i] + text[i] + result_shifr2[(i + 1):]

    str1 = ''
    str2 = ''
    str_cod = ''
    str_cod_use = ''

    if count1 > 0:
        for k in text:
            if k in arr1_1:
                arr_height = 5
                arr_weidth = 5
                for i in range(0, arr_height):
                    for j in range(0, arr_weidth):
                        if k == arr1[i][j]:
                            str1 += str(j)
                            str2 += str(i)
        #str_cod = str1 + str2   #для 2 метода
        str_cod = str1[1:] + str2 + str1[:1]   #для 3 метода
        while (len(str_cod) > 0):
            str_cod_use = str_cod[:2]
            str_cod = str_cod[2:]
            a = str_cod_use[0]
            b = str_cod_use[1]
            for l in range (0,len(result_shifr)):
                if result_shifr[l] == '*':
                    result_shifr = result_shifr[:l] + arr1[int(b)][int(a)] + result_shifr[(l + 1):]
                    result_shifr2 = result_shifr
                    break

    if count2 > 0:
        count = 0
        for k in text:
            if k in arr2_2:
                arr_height = 5
                arr_weidth = 5
                for i in range(0, arr_height):
                    for j in range(0, arr_weidth):
                        if k == arr2[i][j]:
                            str1 += str(j)
                            str2 += str(i)
        str_cod = str1 + str2   #для 2 метода
        #str_cod = str1[1:] + str2 + str1[:1]   #для 3 метода

        while (len(str_cod) > 0):
            str_cod_use = str_cod[:2]
            str_cod = str_cod[2:]
            a = str_cod_use[0]
            b = str_cod_use[1]
            for l in range (0,len(result_shifr)):
                if result_shifr[l] == '*':
                    result_shifr = result_shifr[:l] + arr2[int(b)][int(a)] + result_shifr[(l + 1):]
                    result_shifr2 = result_shifr
                    break

    if count3 > 0:
        for k in text:
            if k in arr3_3:
                arr_height2 = 6
                arr_weidth2 = 5
                for i in range(0, arr_height2):
                    for j in range(0, arr_weidth2):
                        if k == arr3[i][j]:
                            str1 += str(j)
                            str2 += str(i)
        str_cod = str1 + str2   #для 2 метода
        #str_cod = str1[1:] + str2 + str1[:1]   #для 3 метода

        result_shifr = str_cod
        while (len(str_cod) > 0):
            str_cod_use = str_cod[:2]
            str_cod = str_cod[2:]
            a = str_cod_use[0]
            b = str_cod_use[1]
            a2 = (int(a) % 5)
            b2 = int(b)
            for l in range (0,len(result_shifr2)):
                if result_shifr2[l] == '*':
                    #result_shifr = result_shifr[:l] + arr3[int(b)][int(a)] + result_shifr[(l + 1):]
                    result_shifr2 = result_shifr2[:l] + arr3[int(b2)][int(a2)] + result_shifr2[(l + 1):]
                    break

    if count4 > 0:
        count = 0
        for k in text:
            if k in arr4_4:
                arr_height2 = 6
                arr_weidth2 = 5
                for i in range(0, arr_height2):
                    for j in range(0, arr_weidth2):
                        if k == arr4[i][j]:
                            str1 += str(j)
                            str2 += str(i)
        str_cod = str1 + str2   #для 2 метода
        #str_cod = str1[1:] + str2 + str1[:1]   #для 3 метода

        result_shifr = str_cod
        while (len(str_cod) > 0):
            str_cod_use = str_cod[:2]
            str_cod = str_cod[2:]
            a = str_cod_use[0]
            b = str_cod_use[1]
            a2 = (int(a) % 5)
            b2 = int(b)
            for l in range (0,len(result_shifr2)):
                if result_shifr2[l] == '*':
                    #result_shifr = result_shifr[:l] + arr4[int(b)][int(a)] + result_shifr[(l + 1):]
                    result_shifr2 = result_shifr2[:l] + arr4[int(b2)][int(a2)] + result_shifr2[(l + 1):]
                    break


    return result_shifr, result_shifr2

def decodingPolibii3(text, text_print, count1,count2,count3,count4): #Дешифрование

    arr1_1 = "abcdefghiklmnopqrstuvwxyz"
    arr2_2 = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    arr3_3 = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ"
    arr4_4 = "абвгдежзиклмнопрстуфхцчшщыьэюя"

    arr1 = [['a', 'b', 'c', 'd', 'e'],
            ['f', 'g', 'h', 'i', 'k'],
            ['l', 'm', 'n', 'o', 'p'],
            ['q', 'r', 's', 't', 'u'],
            ['v', 'w', 'x', 'y', 'z']]

    arr2 = [['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'K'],
            ['L', 'M', 'N', 'O', 'P'],
            ['Q', 'R', 'S', 'T', 'U'],
            ['V', 'W', 'X', 'Y', 'Z']]

    arr3 = [['А', 'Б', 'В', 'Г', 'Д'],
            ['Е', 'Ж', 'З', 'И', 'К'],
            ['Л', 'М', 'Н', 'О', 'П'],
            ['Р', 'С', 'Т', 'У', 'Ф'],
            ['Х', 'Ц', 'Ч', 'Ш', 'Щ'],
            ['Ы', 'Ь', 'Э', 'Ю', 'Я']]

    arr4 = [['а', 'б', 'в', 'г', 'д'],
            ['е', 'ж', 'з', 'и', 'к'],
            ['л', 'м', 'н', 'о', 'п'],
            ['р', 'с', 'т', 'у', 'ф'],
            ['х', 'ц', 'ч', 'ш', 'щ'],
            ['ы', 'ь', 'э', 'ю', 'я']]

    """count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0

    for i in text:
        if i in arr1_1:
            count1 += 1
        if i in arr2_2:
            count2 += 1
        if i in arr3_3:
            count3 += 1
        if i in arr4_4:
            count4 += 1"""

    result_deshifr = ''
    """len_result_deshifr = len(text)
    if count3 > 0 or count4 > 0:
        len_text = len_result_deshifr // 2
    for i in (range(0, len_result_deshifr)):
        result_deshifr += '*'"""

    for i in (range(0, len(text_print))):
        result_deshifr += '*'

    for i in (range(0, len(text_print))):
        if (text_print[i] not in arr1_1) and (text_print[i] not in arr2_2) and (text_print[i] not in arr3_3) and (text_print[i] not in arr4_4):
            result_deshifr = result_deshifr[:i] + text_print[i] + result_deshifr[(i + 1):]

    str1 = ''
    str2 = ''
    str_cod = ''
    str_cod_use1 = ''
    str_cod_use2 = ''

    if count1>0:
        count = 0
        for k in text:
            if k in arr1_1:
                arr_height = 5
                arr_weidth = 5
                for i in range(0, arr_height):
                    for j in range(0, arr_weidth):
                        if k == arr1[i][j]:
                            str_cod += str(j)
                            str_cod += str(i)
        str_cod = str_cod[-1] + str_cod[:len(str_cod)]     # +строчка для 3 метода
        str1 = str_cod[:(len(str_cod)//2)]
        str2 = str_cod[(len(str_cod)//2):]

        while (len(str1) > 0):
            str_cod_use1 = str1[:1]
            print(str_cod_use1)
            str1 = str1[1:]
            str_cod_use2 = str2[:1]
            str2 = str2[1:]
            print(str1,str2)
            a = str_cod_use1
            b = str_cod_use2
            for l in range (0,len(result_deshifr)):
                if result_deshifr[l] == '*':
                    result_deshifr = result_deshifr[:l] + arr1[int(b)][int(a)] + result_deshifr[(l + 1):]
                    print(result_deshifr)
                    break

    if count2 > 0:
        count = 0
        for k in text:
            if k in arr2_2:
                arr_height = 5
                arr_weidth = 5
                for i in range(0, arr_height):
                    for j in range(0, arr_weidth):
                        if k == arr2[i][j]:
                            str_cod += str(j)
                            str_cod += str(i)
        #str_cod = str_cod[-1] + str_cod[:len(str_cod)]  # +строчка для 3 метода
        str1 = str_cod[:(len(str_cod) // 2)]
        str2 = str_cod[(len(str_cod) // 2):]

        while (len(str1) > 0):
            str_cod_use1 = str1[:1]
            print(str_cod_use1)
            str1 = str1[1:]
            str_cod_use2 = str2[:1]
            str2 = str2[1:]
            print(str1, str2)
            a = str_cod_use1
            b = str_cod_use2
            for l in range (0,len(result_deshifr)):
                if result_deshifr[l] == '*':
                    result_deshifr = result_deshifr[:l] + arr2[int(b)][int(a)] + result_deshifr[(l + 1):]
                    print(result_deshifr)
                    break

    if count3>0:
        arr_height = 6
        arr_weidth = 5
        """for k in text:
            if k in arr3_3:
                
                for i in range(0, arr_height):
                    for j in range(0, arr_weidth):
                        if k == arr3[i][j]:
                            str_cod += str(j)
                            str_cod += str(i)"""

        str_cod = text
        #str_cod = str_cod[-1] + str_cod[:len(str_cod)]  # +строчка для 3 метода

        str1 = str_cod[:(len(str_cod) // 2)]
        str2 = str_cod[(len(str_cod) // 2):]

        while (len(str1) > 0):
            str_cod_use1 = str1[0]
            str1 = str1[1:]
            str_cod_use2 = str2[0]
            str2 = str2[1:]
            a = str_cod_use1
            b = str_cod_use2

            for l in range (0,len(result_deshifr)):
                if result_deshifr[l] == '*':
                    result_deshifr = result_deshifr[:l] + arr3[int(b)][int(a)] + result_deshifr[(l + 1):]
                    break

    if count4>0:
        arr_height = 6
        arr_weidth = 5
        """for k in text:
            if k in arr4_4:
                arr_height = 6
                arr_weidth = 5
                for i in range(0, arr_height):
                    for j in range(0, arr_weidth):
                        if k == arr4[i][j]:
                            str_cod += str(j)
                            str_cod += str(i)"""
        str_cod = text
        #str_cod = str_cod[-1] + str_cod[:len(str_cod)]  # +строчка для 3 метода

        str1 = str_cod[:(len(str_cod) // 2)]
        str2 = str_cod[(len(str_cod) // 2):]

        while (len(str1) > 0):
            str_cod_use1 = str1[0]
            str1 = str1[1:]
            str_cod_use2 = str2[0]
            str2 = str2[1:]
            a = str_cod_use1
            b = str_cod_use2

            for l in range (0,len(result_deshifr)):
                if result_deshifr[l] == '*':
                    result_deshifr = result_deshifr[:l] + arr4[int(b)][int(a)] + result_deshifr[(l + 1):]
                    break

    return result_deshifr
