from PyQt5 import QtCore, QtGui, QtWidgets

def codingScitala(text, n): #Шифрование
    k = len(text)
    m = abs((k-1)//n) + 1
    #print(m, n)

    result_shifr = ''
    for i in range(0,k+10):
        result_shifr += '*'

    for i in range(0,k):
        new_ind = abs(m*(i % n))+abs(i // n)
        result_shifr = result_shifr[:new_ind]+text[i]+result_shifr[(new_ind+1):]
        #print(result_shifr)

    return result_shifr

#def decodingScitala(text, m, len2): #Дешифрование
def decodingScitala(text, m):
    k = len(text)
    n = abs((k - 1) // m) + 1
    #print(m, n)
    result_deshifr = ''
    for i in range(0, k+1):
        result_deshifr += ' '

    for i in range(0,k):
        new_ind1 = abs(m*(i % n))+abs(i // n)
        result_deshifr = result_deshifr[:new_ind1]+text[i]+result_deshifr[(new_ind1+1):]
        #print(result_deshifr)

    #result_deshifr = result_deshifr[:len2]
    #result_deshifr = result_deshifr.replace("*", "")
    return result_deshifr
