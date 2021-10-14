from PyQt5 import QtCore, QtGui, QtWidgets

def codingGronsf(stroka, key):
    arr1 = "abcdefghijklmnopqrstuvwxyz"
    arr2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    arr3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    arr4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    result_shifr = ''

    key *= len(stroka) // len(key) + 1
    p = -1
    for i in stroka:
        if i in arr1:
            for j, k in enumerate(arr1):
                if i == k:
                    p += 1
                    print(p)
                    print(key[p])
                    result_shifr += arr1[(j + int(key[p])) % len(arr1)]
        else:
            if i in arr2:
                for j, k in enumerate(arr2):
                    if i == k:
                        p += 1
                        print(p)
                        print(key[p])
                        result_shifr += arr2[(j + int(key[p])) % len(arr2)]
            else:
                if i in arr3:
                    for j, k in enumerate(arr3):
                        if i == k:
                            p += 1
                            print(p)
                            print(key[p])
                            result_shifr += arr3[(j + int(key[p])) % len(arr3)]
                else:
                    if i in arr4:
                        for j, k in enumerate(arr4):
                            if i == k:
                                p += 1
                                print(p)
                                print(key[p])
                                result_shifr += arr4[(j + int(key[p])) % len(arr4)]
                    else:
                        result_shifr += i
    return result_shifr

def decodingGronsf(stroka, key):
    arr1 = "abcdefghijklmnopqrstuvwxyz"
    arr2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    arr3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    arr4 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    result_deshifr = ''

    key *= len(stroka) // len(key) + 1
    p = -1
    for i in stroka:
        if i in arr1:
            for j, k in enumerate(arr1):
                if i == k:
                    p += 1
                    print(p)
                    print(key[p])
                    result_deshifr += arr1[(j - int(key[p])) % len(arr1)]
        else:
            if i in arr2:
                for j, k in enumerate(arr2):
                    if i == k:
                        p += 1
                        print(p)
                        print(key[p])
                        result_deshifr += arr2[(j - int(key[p])) % len(arr2)]
            else:
                if i in arr3:
                    for j, k in enumerate(arr3):
                        if i == k:
                            p += 1
                            print(p)
                            print(key[p])
                            result_deshifr += arr3[(j - int(key[p])) % len(arr3)]
                else:
                    if i in arr4:
                        for j, k in enumerate(arr4):
                            if i == k:
                                p += 1
                                print(p)
                                print(key[p])
                                result_deshifr += arr4[(j - int(key[p])) % len(arr4)]
                    else:
                        result_deshifr += i

    return result_deshifr
