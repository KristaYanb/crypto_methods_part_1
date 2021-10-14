from PyQt5 import QtCore, QtGui, QtWidgets

def codingPolibii(text): #Шифрование

    arr1_1 = "abcdefghijklmnopqrstuvwxyz"
    arr2_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    arr3_3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    arr4_4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    arr1 = [['a', 'b', 'c', 'd', 'e'],
            ['f', 'g', 'h', 'i', 'j'],
            ['k', 'l', 'm', 'n', 'o'],
            ['p', 'q', 'r', 's', 't'],
            ['u', 'v', 'w', 'x', 'y'],
            ['z', '_', '_', '_', '_']]

    arr2 = [['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O'],
            ['P', 'Q', 'R', 'S', 'T'],
            ['U', 'V', 'W', 'X', 'Y'],
            ['Z', '_', '_', '_', '_']]

    arr3 = [['А', 'Б', 'В', 'Г', 'Д', 'Е'],
            ['Ё', 'Ж', 'З', 'И', 'Й', 'К'],
            ['Л', 'М', 'Н', 'О', 'П', 'Р'],
            ['С', 'Т', 'У', 'Ф', 'Х', 'Ц'],
            ['Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь'],
            ['Э', 'Ю', 'Я', '_', '_', '_']]

    arr4 = [['а', 'б', 'в', 'г', 'д', 'е'],
            ['ё', 'ж', 'з', 'и', 'й', 'к'],
            ['л', 'м', 'н', 'о', 'п', 'р'],
            ['с', 'т', 'у', 'ф', 'х', 'ц'],
            ['ч', 'ш', 'щ', 'ъ', 'ы', 'ь'],
            ['э', 'ю', 'я', '_', '_', '_']]

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

    result_shifr = ''
    if count1 > 0:
        for k in text:
            if k in arr1_1:
                arr_height = 6
                arr_weidth = 5
                for i in range(0, arr_height):
                    for j in range(0, arr_weidth):
                        if ((k == 'v' and j==1) or (k == 'w' and j==2) or (k == 'x' and j==3) or (k == 'y' and j==4)) and (i == 4):
                            result_shifr += arr1[0][j]
                            continue
                        if k == arr1[i][j]:
                            result_shifr += arr1[(i + 1) % arr_height][j]
            else:
                result_shifr += k

    if count2 > 0:
        for k in text:
            if k in arr2_2:
                arr_height = 6
                arr_weidth = 5
                for i in range(0, arr_height):
                    for j in range(0, arr_weidth):
                        if ((k == 'V' and j==1) or (k == 'W' and j==2) or (k == 'X' and j==3) or (k == 'Y' and j==4)) and (i == 4):
                            result_shifr += arr2[0][j]
                            continue
                        if k == arr2[i][j]:
                            result_shifr += arr2[(i + 1) % arr_height][j]
            else:
                result_shifr += k

    if count3 > 0:
        for k in text:
            if k in arr3_3:
                arr_height = 6
                arr_weidth = 6
                for i in range(0, arr_height):
                    for j in range(0, arr_weidth):
                        if ((k == 'Ъ' and j==3) or (k == 'Ы' and j==4) or (k == 'Ь' and j==5)) and (i == 4):
                            result_shifr += arr3[0][j]
                            continue
                        if k == arr3[i][j]:
                            result_shifr += arr3[(i + 1) % arr_height][j]
            else:
                result_shifr += k

    if count4 > 0:
        for k in text:
            if k in arr4_4:
                arr_height = 6
                arr_weidth = 6
                for i in range(0, arr_height):
                    for j in range(0, arr_weidth):
                        if ((k == 'ъ' and j==3) or (k == 'ы' and j==4) or (k == 'ь' and j==5)) and (i == 4):
                            result_shifr += arr4[0][j]
                            continue
                        if k == arr4[i][j]:
                            result_shifr += arr4[(i + 1) % arr_height][j]
            else:
                result_shifr += k

    return result_shifr

def decodingPolibii(text): #Дешифрование

    arr1_1 = "abcdefghijklmnopqrstuvwxyz"
    arr2_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    arr3_3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    arr4_4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    arr1 = [['a', 'b', 'c', 'd', 'e'],
            ['f', 'g', 'h', 'i', 'j'],
            ['k', 'l', 'm', 'n', 'o'],
            ['p', 'q', 'r', 's', 't'],
            ['u', 'v', 'w', 'x', 'y'],
            ['z', '_', '_', '_', '_']]

    arr2 = [['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O'],
            ['P', 'Q', 'R', 'S', 'T'],
            ['U', 'V', 'W', 'X', 'Y'],
            ['Z', '_', '_', '_', '_']]

    arr3 = [['А', 'Б', 'В', 'Г', 'Д', 'Е'],
            ['Ё', 'Ж', 'З', 'И', 'Й', 'К'],
            ['Л', 'М', 'Н', 'О', 'П', 'Р'],
            ['С', 'Т', 'У', 'Ф', 'Х', 'Ц'],
            ['Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь'],
            ['Э', 'Ю', 'Я', '_', '_', '_']]

    arr4 = [['а', 'б', 'в', 'г', 'д', 'е'],
            ['ё', 'ж', 'з', 'и', 'й', 'к'],
            ['л', 'м', 'н', 'о', 'п', 'р'],
            ['с', 'т', 'у', 'ф', 'х', 'ц'],
            ['ч', 'ш', 'щ', 'ъ', 'ы', 'ь'],
            ['э', 'ю', 'я', '_', '_', '_']]

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

    print(len(text))
    result_deshifr = ''
    if count1>0:
        for k in text:
            if k in arr1_1:
                arr_height = 6
                arr_weidth = 5
                for i in range(0, arr_height):
                    for j in range(0, arr_weidth):
                        if ((k == 'b' and j==1) or (k == 'c' and j==2) or (k == 'd' and j==3) or (k == 'e' and j==4)) and (i == 0):
                            result_deshifr += arr1[4][j]
                            continue
                        if k == arr1[i][j]:
                            result_deshifr += arr1[(i-1) % arr_height][j]
            else:
                result_deshifr += k

    if count2 > 0:
        for k in text:
            if k in arr2_2:
                arr_height = 6
                arr_weidth = 5
                for i in range(0, arr_height):
                    for j in range(0, arr_weidth):
                        if ((k == 'B' and j==1) or (k == 'C' and j==2) or (k == 'D' and j==3) or (k == 'E' and j==4)) and (i == 0):
                            result_deshifr += arr2[4][j]
                            continue
                        if k == arr2[i][j]:
                            result_deshifr += arr2[(i-1) % arr_height][j]
            else:
                result_deshifr += k

    if count3>0:
        for k in text:
            if k in arr3_3:
                arr_height = 6
                arr_weidth = 6
                for i in range(0, arr_height):
                    for j in range(0, arr_weidth):
                        if ((k == 'Г' and j==3) or (k == 'Д' and j==4) or (k == 'Е' and j==5)) and (i == 0):
                            result_deshifr += arr3[4][j]
                            continue
                        if k == arr3[i][j]:
                            result_deshifr += arr3[(i-1) % arr_height][j]
            else:
                result_deshifr += k

    if count4>0:
        for k in text:
            if k in arr4_4:
                arr_height = 6
                arr_weidth = 6
                for i in range(0, arr_height):
                    for j in range(0, arr_weidth):
                        if ((k == 'г' and j==3) or (k == 'д' and j==4) or (k == 'е' and j==5)) and (i == 0):
                            result_deshifr += arr4[4][j]
                            continue
                        if k == arr4[i][j]:
                            result_deshifr += arr4[(i-1) % arr_height][j]
            else:
                result_deshifr += k

    return result_deshifr