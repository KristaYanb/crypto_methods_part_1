def xor(block, key): #xor правого блока и ключа
    res = ''
    for i in range(len(block)):
        if block[i] == '1':
            if key[i] == '1':
                res += '0'
            else:
                res += '1'
        if block[i] == '0':
            if key[i] == '1':
                res += '1'
            else:
                res += '0'
    return res

def div_8_blocks(data): #8 блоков по 4 бит по правилу
    ZAMENA = [[4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3],
            [14, 11, 4, 12, 6, 13, 15, 10, 2, 3, 8, 1, 0, 7, 5, 9],
            [5, 8, 1, 13, 10, 3, 4, 2, 14, 15, 12, 7, 6, 0, 9, 11],
            [7, 13, 10, 1, 0, 8, 9, 15, 14, 4, 6, 12, 11, 2, 5, 3],
            [6, 12, 7, 1, 5, 15, 13, 8, 4, 10, 9, 14, 0, 3, 11, 2],
            [4, 11, 10, 0, 7, 2, 1, 13, 3, 6, 8, 5, 9, 12, 15, 14],
            [13, 11, 4, 1, 3, 15, 5, 9, 0, 10, 14, 7, 6, 8, 2, 12],
            [1, 15, 13, 0, 5, 7, 10, 4, 9, 2, 3, 14, 6, 11, 8, 12]]

    #делим на блоки по 4 бит
    vect = []
    data2 = data
    for i in range(0, 8):
        vect.append(data2[:4])
        data2 = data2[4:]

    res = ''
    #по правилу
    for i in range(len(vect)):
        res += bin(ZAMENA[i][int(vect[i], 2)])[2:].zfill(4)

    return res

def prepare_keys(password, flag):
    keys_for_cycle = []
    password2 = password
    # делим по 4 символа
    for i in range(0, 8):
        keys_for_cycle.append(password2[:4])
        password2 = password2[4:]

    # делаем подключи
    subkey = []
    if flag == 0:
        for i in range(3):
            for sub in keys_for_cycle:
                subkey.append(sub)
        keys_for_cycle.reverse()
        for sub in keys_for_cycle:
            subkey.append(sub)

    if flag == 1:
        for sub in keys_for_cycle:
            subkey.append(sub)
        keys_for_cycle.reverse()
        for i in range(3):
            for sub in keys_for_cycle:
                subkey.append(sub)

    #print('подключи ', subkey)

    subkey_bytes = []
    new_keys_for_cycle = []
    for sub in subkey:
        subkey_bin = b'' # байты
        subkey_bin_bin = ''

        for char in sub:
            subkey_bin += bytes([ord(char), 2])
            subkey_bin_bin += (bin(ord(char))[0] + bin(ord(char))[2:]).zfill(8)
        subkey_bytes.append(subkey_bin)
        new_keys_for_cycle.append(subkey_bin_bin)

    #print('Пароли (байты): ', subkey_bytes)
    #print('Пароли (двоичный вид): ', new_keys_for_cycle)

    return new_keys_for_cycle

def prepare_text(new_text):
    # делим исходный текст на блоки по 8 символов
    text_in_block = []
    text2 = new_text
    if len(text2) > 8:
        for i in range(0, len(new_text) // 8 + 2):
            if len(text2) < 8:
                text_in_block.append(text2[:len(text2)])
                text2 = text2[len(text2):]
            else:
                text_in_block.append(text2[:8])
                text2 = text2[8:]
    else:
        text_in_block.append(text2)
    #print('текст на блоки ', text_in_block)

    new_text_in_block = []
    for i in text_in_block:
        if i != b'':
            new_text_in_block.append(i)
    #print('текст на блоки ', new_text_in_block)

    return new_text_in_block

def prepare_bits(text_in_block_pad):
    #все блоки переводим в 64 бит
    text_in_block_in_byte = []
    for one_block in text_in_block_pad:
        one_block_in_byte = ''
        for char in one_block:
            one_block_in_byte += bin(char)[2:].zfill(8)
        text_in_block_in_byte.append(one_block_in_byte)
    #print('все блоки в 64 бит: ', text_in_block_in_byte)

    return text_in_block_in_byte

def func_res(result_blocks):
    result = b''
    for block in result_blocks:
        text2 = block
        for i in range(0, 8):
            result += bytes([int(text2[:8], 2)])
            text2 = text2[8:]
    #print('Результат: ', result)

    return result

def func_res1(result_blocks):
    result = b''
    text2 = result_blocks
    for i in range(0, 8):
        result += bytes([int(text2[:8], 2)])
        text2 = text2[8:]
    #print('Результат: ', result)

    return result

def cycling(one_block, new_keys_for_cycle):
    for i in range(len(new_keys_for_cycle)):
        # делим на 2 блока
        left = one_block[:32]
        right = one_block[32:]
        # ф-ция f
        # слож по мод 2^32
        new_right = (int(right, 2) + int(new_keys_for_cycle[i], 2)) % 4294967296
        new_right = bin(new_right)[2:].zfill(32)

        new_right = div_8_blocks(new_right)  # делим на 8 4-битовых подпосл-тей
        new_right = new_right[11:] + new_right[:11]  # циклический сдвиг влево на 11
        new_right = xor(left, new_right)

        if i != len(new_keys_for_cycle) - 1:
            one_block = right + new_right
        else:
            one_block = new_right + right

    return one_block

def codingGOST(password, progress_bar, input_file=None, text=None, output_file=None, a_vector_block=None, flag_ECB=None, flag_CFB=None): #шифрование
    flag = 0
    res = b''
    new_keys_for_cycle = prepare_keys(password, flag)

    vector_block = ''
    if flag_CFB:
        for char in a_vector_block:
            vector_block += (bin(ord(char))[0] + bin(ord(char))[2:]).zfill(8)

    new_text = None
    if input_file:
        new_text = input_file.read()
    elif text:
        new_text = text.encode()
        print('input_data ', new_text)

    new_text_in_block = prepare_text(new_text)

    # паддинг
    text_in_block_pad = []
    if len(new_text_in_block) == 1:
        if len(new_text_in_block[0]) < 8:
            new_one_block = new_text_in_block[0] + b'\x00' * (8 - (len(new_text_in_block[0]) + 1)) + bytes(
                [8 - len(new_text_in_block[0])])
            text_in_block_pad.append(new_one_block)
        else:
            text_in_block_pad.append(new_text_in_block[0])

    else:
        text_in_block_pad = new_text_in_block[:len(new_text_in_block) - 1]
        analyze = new_text_in_block[len(new_text_in_block) - 1]
        if len(analyze) < 8:
            analyze = analyze + b'\x00' * (8 - (len(analyze) + 1)) + bytes([8 - len(analyze)])
            text_in_block_pad.append(analyze)

    #print('pad ', text_in_block_pad)

    text_in_block_in_byte = prepare_bits(text_in_block_pad)

    bar_state = 0.0
    bar_step = 100 / len(text_in_block_pad)  # для процентов

    #циклы шифрования
    result_blocks = []
    if flag_ECB:
        for one_block in text_in_block_in_byte:
            one_block = cycling(one_block, new_keys_for_cycle)
            one_block = func_res1(one_block)
            res += one_block
            #result_blocks.append(one_block)

            bar_state += bar_step
            print(bar_state)
            progress_bar.setValue(bar_state)

    if flag_CFB:
        # отработка первого шага с синхропосылкой
        vector_block = cycling(vector_block, new_keys_for_cycle)
        vector_block = xor(text_in_block_in_byte[0], vector_block)

        one_block = func_res1(vector_block)
        res += one_block
        #result_blocks.append(vector_block)

        # отработка остального
        for p in range(1, len(text_in_block_in_byte)):
            #vector_block = text_in_block_in_byte[p-1]
            vector_block = cycling(vector_block, new_keys_for_cycle)
            vector_block = xor(text_in_block_in_byte[p], vector_block)
            one_block = func_res1(vector_block)
            res += one_block
            #result_blocks.append(vector_block)

            bar_state += bar_step
            print(bar_state)
            progress_bar.setValue(bar_state)

    #print('result: ', result_blocks)

    #result = func_res(result_blocks)

    progress_bar.setValue(0)

    if output_file:
        #output_file.write(result)
        output_file.write(res)

    else:
        #print('res ', result)
        print('res ', res)

        resultat = ''
        #for i in result:
        for i in res:
            resultat += chr(i)
        print('Результат в символах: ', resultat)

        return resultat

def decodingGOST(password, progress_bar, input_file=None, text=None, output_file=None, a_vector_block=None, flag_ECB=None, flag_CFB=None): #расшифрование
    flag = 1
    res = b''
    if flag_CFB:
        flag = 0
    new_keys_for_cycle = prepare_keys(password, flag)

    vector_block = ''
    if flag_CFB:
        for char in a_vector_block:
            vector_block += (bin(ord(char))[0] + bin(ord(char))[2:]).zfill(8)

    new_text = None
    if input_file:
        new_text = input_file.read()
    elif text:
        new_text = b''
        for i in text:
            new_text += bytes([ord(i)])
        print('input_data ', new_text)

    new_text_in_block = prepare_text(new_text)

    text_in_block_in_byte = prepare_bits(new_text_in_block)

    bar_state = 0.0
    bar_step = 100 / len(text_in_block_in_byte)  # для процентов

    #циклы шифрования
    result_blocks = []
    if flag_ECB:
        for one_block in text_in_block_in_byte:
            one_block = cycling(one_block, new_keys_for_cycle)
            one_block = func_res1(one_block)
            res += one_block
            #result_blocks.append(one_block)

            bar_state += bar_step
            print(bar_state)
            progress_bar.setValue(bar_state)

    if flag_CFB:
        # отработка первого шага с вектором
        vector_block = cycling(vector_block, new_keys_for_cycle)
        vector_block = xor(text_in_block_in_byte[0], vector_block)
        one_block = func_res1(vector_block)
        res += one_block
        #result_blocks.append(vector_block)

        # отработка остального
        for p in range(1, len(text_in_block_in_byte)):
            vector_block = text_in_block_in_byte[p - 1]
            vector_block = cycling(vector_block, new_keys_for_cycle)
            vector_block = xor(text_in_block_in_byte[p], vector_block)
            one_block = func_res1(vector_block)
            res += one_block
            #result_blocks.append(vector_block)

            bar_state += bar_step
            print(bar_state)
            progress_bar.setValue(bar_state)

    #print('result: ', result_blocks)

    #result = func_res(result_blocks)

    """res = result[:len(result) - 8]
    # удаляем паддинг
    count = 0
    seq_flag = False
    analyze = result[len(result) - 8:]
    for i in range(len(analyze)):
        if analyze[i] == 0:
            if not seq_flag:
                seq_flag = True
            count += 1
        elif (analyze[i] - 1 <= count) and (i == len(analyze) - 1):
            res += analyze[:len(analyze) - (analyze[i])]
            break
        elif seq_flag:
            seq_flag = False
            count = 0
        elif (i == 8 - 1) and (count == 0):
            res += analyze
    #print('del pad ', res)"""

    result = res[:len(res) - 8]
    # удаляем паддинг
    count = 0
    seq_flag = False
    analyze = res[len(res) - 8:]
    for i in range(len(analyze)):
        if analyze[i] == 0:
            if not seq_flag:
                seq_flag = True
            count += 1
        elif (analyze[i] - 1 <= count) and (i == len(analyze) - 1):
            result += analyze[:len(analyze) - (analyze[i])]
            break
        elif seq_flag:
            seq_flag = False
            count = 0
        elif (i == 8 - 1) and (count == 0):
            result += analyze
    # print('del pad ', res)

    progress_bar.setValue(0)
    if output_file:
        #output_file.write(res)
        output_file.write(result)

    else:
        print('res ', res)
        print('del pad ', result)

        resultat = ''
        for i in result:
            resultat += chr(i)
        print('Результат в символах: ', resultat)

        return resultat