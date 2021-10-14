from PyQt5 import QtCore, QtGui, QtWidgets

def xor(a, b):
    res = ""
    for i in range(0,len(a)):
        if a[i] == '1':
            if b[i] == '1':
                res += '0'
            else:
                res += '1'
        if a[i] == '0':
            if b[i] == '1':
                res += '1'
            else:
                res += '0'
    return res

def codingGammaFile(stroka, key):

    """stroch = []
    for i in range(len(stroka)):
        am = (ord(stroka[i]))
        print(am)
        stroch.append(am)

    key_new = []
    for i in range(len(key)):
        ak = (ord(key[i]))
        key_new.append(ak)

    key_new *= len(stroka) // len(key) + 1

    rez = []
    for i in range(len(stroka)):
        al = stroch[i] ^ key_new[i]
        rez.append(al)

    result_shifr = ''
    for i in range(len(stroka)):
        result_shifr += chr(rez[i])

    return result_shifr"""

    key_bin = []
    for i in range(0, len(key)):
        key_bin.append((bin(int(key[i]))[2:]).zfill(30))

    stroka_bin = []
    for i in range(0, len(stroka)):
        stroka_bin.append((bin(stroka[i])[2:]).zfill(30))

    res = bytearray(b"")
    for i in range(0, len(stroka_bin)):
        temp = xor(stroka_bin[i], key_bin[i])
        res.append(int(temp, 2) % 256)

    return res

def codingGamma(stroka, key):
    result_shifr = ''
    bin_str = ''
    bin_key = ''
    rez = ''

    for i in range(len(stroka)):
        am = str((bin(ord(stroka[i]))[2::]))
        if len(am) < 64:
            for j in range(0, 64 - len(am)):
                am = '0' + am
        if len(am) > 64:
            break
        bin_str += am
    len_str = len(bin_str)

    for i in range(len(key)):
        ak = str((bin(ord(key[i]))[2::]))
        if len(ak) < 64:
            for j in range(0, 64 - len(ak)):
                ak = '0' + ak
        bin_key += ak

    bin_key *= len_str // len(bin_key) + 1

    for i in range(len_str):
        ak = str(int(bin_str[i]) ^ int(bin_key[i]))
        rez += ak
    print('end')

    rez2 = rez
    for i in range(len_str//64):
        result_shifr += str(chr(int(rez[:64], 2)))
        rez = rez[64:]
    print('end')

    vivod = 'Открытый текст: длина = ' + str(len_str) + '\n' + bin_str + '\n\nКлюч: длина = ' + str(
        len_str) + '\n' + bin_key[:len_str] + '\n\nРезультат: длина = ' + str(len(rez2)) + '\n' + rez2

    return result_shifr, vivod