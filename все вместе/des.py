def encrypt(block, key): #ф-ия шифрования
    EXPANSION = [32, 1, 2, 3, 4, 5,
                 4, 5, 6, 7, 8, 9,
                 8, 9, 10, 11, 12, 13,
                 12, 13, 14, 15, 16, 17,
                 16, 17, 18, 19, 20, 21,
                 20, 21, 22, 23, 24, 25,
                 24, 25, 26, 27, 28, 29,
                 28, 29, 30, 31, 32, 1]

    REVERSE_COMPRESSION = [16, 7, 20, 21, 29, 12, 28, 17,
                           1, 15, 23, 26, 5, 18, 31, 10,
                           2, 8, 24, 14, 32, 27, 3, 9,
                           19, 13, 30, 6, 22, 11, 4, 25]

    #расширение блока до 48 бит
    block_expansion = ''
    for i in EXPANSION:
        block_expansion += block[i - 1]

    block_xor = xor(block_expansion, key) #xor правого блока и ключа
    block_8 = div_8_blocks(block_xor) #результат из 48 бит делим на 8 блоков по 6 бит по правилу

    #еще одна перестановка
    block_new = ''
    for i in REVERSE_COMPRESSION:
        block_new += block_8[i - 1]

    return block_new

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

def div_8_blocks(data): #8 блоков по 6 бит по правилу
    ZAMENA = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
               [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
               [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
               [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13], ],

              [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
               [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
               [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
               [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9], ],

              [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
               [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
               [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
               [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12], ],

              [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
               [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
               [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
               [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14], ],

              [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
               [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
               [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
               [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3], ],

              [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
               [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
               [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
               [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13], ],

              [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
               [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
               [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
               [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12], ],

              [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
               [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
               [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
               [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11], ]]

    res = ''
    #делим на блоки по 6 бит
    vect = []
    data2 = data
    for i in range(0, 8):
        vect.append(data2[:6])
        data2 = data2[6:]

    #по правилу
    num_box = 0
    for vector in vect:
        row = int(vector[0] + vector[len(vector) - 1], 2) #строка
        column = int(vector[1:len(vector) - 1], 2) #столбец

        res += bin(ZAMENA[num_box][row][column])[2:].zfill(4) #опред эл-т
        num_box += 1

    return res

def prepare_text(new_text):
    # делим исходный текст на блоки по 8 байт
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

    # проверка если пусто
    new_text_in_block = []
    for i in text_in_block:
        if i != b'':
            new_text_in_block.append(i)
    #print('текст на блоки ', new_text_in_block)

    return new_text_in_block

def prepare_key(password):
    KEY_REPLACE = [57, 49, 41, 33, 25, 17, 9,
                   1, 58, 50, 42, 34, 26, 18,
                   10, 2, 59, 51, 43, 35, 27,
                   19, 11, 3, 60, 52, 44, 36,
                   63, 55, 47, 39, 31, 23, 15,
                   7, 62, 54, 46, 38, 30, 22,
                   14, 6, 61, 53, 45, 37, 29,
                   21, 13, 5, 28, 20, 12, 4]

    KEY_SDVIG = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    KEY_COMPRESS = [14, 17, 11, 24, 1, 5, 3, 28,
                    15, 6, 21, 10, 23, 19, 12, 4,
                    26, 8, 16, 7, 27, 20, 13, 2,
                    41, 52, 31, 37, 47, 55, 30, 40,
                    51, 45, 33, 48, 44, 49, 39, 56,
                    34, 53, 46, 42, 50, 36, 29, 32]

    # подготовка пароля - переводим в 64 бит
    password_in_byte = ''
    for char in password:
        password_in_byte += (bin(ord(char))[0] + bin(ord(char))[2:]).zfill(8)
    #print('Пароль в 64 бит: ', password_in_byte)

    # перестановка в пароле (56 бит) (первонач подг ключа)
    password_replace = ''
    for i in KEY_REPLACE:
        password_replace += password_in_byte[i - 1]
    #print('Первоначальная перестановка в пароле: ', password_replace)

    # делим на 2 блока по 28 бит
    C_0 = password_replace[:28]
    D_0 = password_replace[28:]
    #print('Пароль 2 блока по 28 бит: ', C_0, D_0)

    # сжатие пароля до 48 бит
    keys_for_cycle = []
    new_keys_for_cycle = []
    for shift in KEY_SDVIG:
        C_0 = C_0[shift:] + C_0[:shift]
        D_0 = D_0[shift:] + D_0[:shift]
        not_compress_key = C_0 + D_0

        compress_key = ''  # двоичный вид
        for i in KEY_COMPRESS:
            compress_key += not_compress_key[i - 1]

        #дополнительно
        compress_key_bin = b''  # байты
        compress_key2 = compress_key
        for byte in range(0, 6):
            compress_key_bin += bytes([int(compress_key2[:8], 2)])
            compress_key2 = compress_key2[8:]

        keys_for_cycle.append(compress_key)
        new_keys_for_cycle.append(compress_key_bin)

    #print('Пароли сжатые (двоичный вид): ', keys_for_cycle)
    #print('Пароли сжатые (байты): ', new_keys_for_cycle)

    return keys_for_cycle

def begin_replace(text_in_block_pad):
    ONE_REPLACE = [58, 50, 42, 34, 26, 18, 10, 2,
                 60, 52, 44, 36, 28, 20, 12, 4,
                 62, 54, 46, 38, 30, 22, 14, 6,
                 64, 56, 48, 40, 32, 24, 16, 8,
                 57, 49, 41, 33, 25, 17, 9, 1,
                 59, 51, 43, 35, 27, 19, 11, 3,
                 61, 53, 45, 37, 29, 21, 13, 5,
                 63, 55, 47, 39, 31, 23, 15, 7]

    # все блоки переводим в 64 бит
    text_in_block_in_byte = []
    for one_block in text_in_block_pad:
        one_block_in_byte = ''
        for char in one_block:
            one_block_in_byte += bin(char)[2:].zfill(8)
        text_in_block_in_byte.append(one_block_in_byte)
    #print('все блоки в 64 бит: ', text_in_block_in_byte)

    # начальная перестановка
    text_in_block_replace = []
    for one_block in text_in_block_in_byte:
        one_block_replace = ''
        for i in ONE_REPLACE:
            one_block_replace += one_block[i - 1]
        text_in_block_replace.append(one_block_replace)
    #print('нач перестановка: ', text_in_block_replace)

    return text_in_block_replace

"""def end_replace(result_blocks):
    END_REPLACE = [40, 8, 48, 16, 56, 24, 64, 32,
                   39, 7, 47, 15, 55, 23, 63, 31,
                   38, 6, 46, 14, 54, 22, 62, 30,
                   37, 5, 45, 13, 53, 21, 61, 29,
                   36, 4, 44, 12, 52, 20, 60, 28,
                   35, 3, 43, 11, 51, 19, 59, 27,
                   34, 2, 42, 10, 50, 18, 58, 26,
                   33, 1, 41, 9, 49, 17, 57, 25]

    # конечная перестановка
    text_replace_end = []
    for one_block in result_blocks:
        one_block_replace_end = ''
        for i in END_REPLACE:
            one_block_replace_end += one_block[i - 1]
        text_replace_end.append(one_block_replace_end)
    #print('конечная: ', text_replace_end)

    return text_replace_end"""

def end_replace1(result_blocks):
    END_REPLACE = [40, 8, 48, 16, 56, 24, 64, 32,
                   39, 7, 47, 15, 55, 23, 63, 31,
                   38, 6, 46, 14, 54, 22, 62, 30,
                   37, 5, 45, 13, 53, 21, 61, 29,
                   36, 4, 44, 12, 52, 20, 60, 28,
                   35, 3, 43, 11, 51, 19, 59, 27,
                   34, 2, 42, 10, 50, 18, 58, 26,
                   33, 1, 41, 9, 49, 17, 57, 25]

    # конечная перестановка
    one_block_replace_end = ''
    for i in END_REPLACE:
        one_block_replace_end += result_blocks[i - 1]
    #print('конечная: ', text_replace_end)

    return one_block_replace_end

def cycling_for_encr(block, keys_for_cycle):
    for i in range(16):
        # разбиение на 2 части
        left_part = block[:32]
        right_part = block[32:]

        # отдельная обработка лев и прав частей
        enc_right = encrypt(right_part, keys_for_cycle[i])
        left_part = xor(left_part, enc_right)

        # объединение
        if i == (16 - 1):
            block = left_part + right_part
        else:
            block = right_part + left_part

    return block

def cycling_for_decr(block, keys_for_cycle):
    for i in range(16):
        # разбиение на 2 части
        left_part = block[:32]
        right_part = block[32:]
        # отдельная обработка лев и прав частей
        enc_right = encrypt(right_part, keys_for_cycle[(16 - 1) - i])
        left_part = xor(left_part, enc_right)

        # объединение
        if i == (16 - 1):
            block = left_part + right_part
        else:
            block = right_part + left_part

    return block

"""def func_res(text_replace_end):
    result = b''
    for block in text_replace_end:
        text2 = block
        for i in range(0, 8):
            result += bytes([int(text2[:8], 2)])
            text2 = text2[8:]
    #print('Результат: ', result) #!надо

    return result"""

def func_res1(text_replace_end):
    result = b''
    text2 = text_replace_end
    for i in range(0, 8):
        result += bytes([int(text2[:8], 2)])
        text2 = text2[8:]
    #print('Результат: ', result) #!надо

    return result

def codingDES(password, progress_bar, input_file=None, text=None, output_file=None, a_vector_block=None, flag_ECB=None, flag_CBC=None, flag_CFB=None, flag_OFB=None): #шифрование
    keys_for_cycle = prepare_key(password)
    res = b''
    vector_block = ''
    if flag_CBC or flag_CFB or flag_OFB:
        for char in a_vector_block:
            vector_block += (bin(ord(char))[0] + bin(ord(char))[2:]).zfill(8)

        #print('Вектор в 64 бит: ', vector_block)

    new_text = None
    if input_file:
        new_text = input_file.read()
    elif text:
        new_text = text.encode()
        print('input_data ', new_text)    #!надо

    new_text_in_block = prepare_text(new_text)

    #паддинг
    text_in_block_pad = []
    if len(new_text_in_block) == 1:
        if len(new_text_in_block[0]) < 8:
            new_one_block = new_text_in_block[0] + b'\x00' * (8 - (len(new_text_in_block[0]) + 1)) + bytes([8 - len(new_text_in_block[0])])
            text_in_block_pad.append(new_one_block)
        else:
            text_in_block_pad.append(new_text_in_block[0])

    else:
        text_in_block_pad = new_text_in_block[:len(new_text_in_block) - 1]
        analyze = new_text_in_block[len(new_text_in_block)-1]
        if len(analyze) < 8:
            analyze = analyze + b'\x00' * (8 - (len(analyze) + 1)) + bytes([8 - len(analyze)])
            text_in_block_pad.append(analyze)

    #print('pad ', text_in_block_pad) #!надо

    text_in_block_replace = begin_replace(text_in_block_pad)

    bar_state = 0.0
    bar_step = 100 / len(text_in_block_pad)  # для процентов

    result_blocks = []
    if flag_ECB or flag_CBC:
        #циклы шифрования
        for one_block in text_in_block_replace:
            if flag_CBC:
                one_block = xor(one_block, vector_block)

            one_block = cycling_for_encr(one_block, keys_for_cycle)

            if flag_CBC:
                vector_block = one_block

            one_block = end_replace1(one_block)
            one_block = func_res1(one_block)
            #result_blocks.append(one_block)
            res += one_block

            bar_state += bar_step
            print(bar_state)
            progress_bar.setValue(bar_state)

    if flag_CFB:
        # отработка первого шага с вектором
        vector_block = cycling_for_encr(vector_block, keys_for_cycle)
        vector_block = xor(text_in_block_replace[0], vector_block)
        c1 = end_replace1(vector_block)
        c1 = func_res1(c1)
        #result_blocks.append(vector_block)
        res += c1

        # отработка остального
        for p in range(1, len(text_in_block_replace)):
            vector_block = cycling_for_encr(vector_block, keys_for_cycle)
            vector_block = xor(text_in_block_replace[p], vector_block)

            c1 = end_replace1(vector_block)
            c1 = func_res1(c1)
            #result_blocks.append(vector_block)
            res += c1

            bar_state += bar_step
            print(bar_state)
            progress_bar.setValue(bar_state)

    if flag_OFB:
        # отработка первого шага с вектором
        vector_block = cycling_for_encr(vector_block, keys_for_cycle)
        c1 = xor(text_in_block_replace[0], vector_block)
        c1 = end_replace1(c1)
        c1 = func_res1(c1)
        res += c1

        # отработка остального
        for p in range(1, len(text_in_block_replace)):
            vector_block = cycling_for_encr(vector_block, keys_for_cycle)
            c1 = xor(text_in_block_replace[p], vector_block)
            c1 = end_replace1(c1)
            c1 = func_res1(c1)
            #result_blocks.append(c1)
            res += c1

            bar_state += bar_step
            print(bar_state)
            progress_bar.setValue(bar_state)

    #print('result: ', result_blocks)

    #text_replace_end = end_replace(result_blocks)

    #result = func_res(text_replace_end)

    progress_bar.setValue(0)

    if output_file:
        output_file.write(res)
        #output_file.write(result_blocks)

    else:
        print('res ', res)
        #print('res ', result_blocks)
        resultat = ''
        #result_blocks.decode('utf-8')
        #for i in result:
        for i in res:
            resultat += chr(i)
        print('Результат в символах: ', resultat)

        return resultat

def decodingDES(password, progress_bar, input_file=None, text=None, output_file=None, a_vector_block=None, flag_ECB=None, flag_CBC=None, flag_CFB=None, flag_OFB=None): #расшифрование
    keys_for_cycle = prepare_key(password)
    res = b''
    vector_block = ''
    if flag_CBC or flag_CFB or flag_OFB:
        for char in a_vector_block:
            vector_block += (bin(ord(char))[0] + bin(ord(char))[2:]).zfill(8)
        next_vector_block = None
        #print('Вектор в 64 бит: ', vector_block)

    new_text = None
    if input_file:
        new_text = input_file.read()
    elif text:
        new_text = b''
        for i in text:
            new_text += bytes([ord(i)])
        print('input_data ', new_text) #!надо

    text_in_block_pad = prepare_text(new_text)

    text_in_block_replace = begin_replace(text_in_block_pad)

    bar_state = 0.0
    bar_step = 100 / len(text_in_block_pad)  # для процентов

    #циклы шифрования
    result_blocks = []
    if flag_ECB or flag_CBC:
        for one_block in text_in_block_replace:
            if flag_CBC:
                next_vector_block = one_block

            one_block = cycling_for_decr(one_block, keys_for_cycle)

            if flag_CBC:
                one_block = xor(one_block, vector_block)
                vector_block = next_vector_block

            one_block = end_replace1(one_block)
            one_block = func_res1(one_block)
            # result_blocks.append(one_block)
            res += one_block
            #result_blocks.append(one_block)

            bar_state += bar_step
            print(bar_state)
            progress_bar.setValue(bar_state)

    if flag_CFB:
        # отработка первого шага с вектором
        vector_block = cycling_for_encr(vector_block, keys_for_cycle)
        vector_block = xor(text_in_block_replace[0], vector_block)
        one_block = end_replace1(vector_block)
        one_block = func_res1(one_block)
        # result_blocks.append(one_block)
        res += one_block
        #result_blocks.append(vector_block)

        # отработка остального
        for p in range(1, len(text_in_block_replace)):
            vector_block = text_in_block_replace[p-1]
            vector_block = cycling_for_encr(vector_block, keys_for_cycle)
            vector_block = xor(text_in_block_replace[p], vector_block)
            one_block = end_replace1(vector_block)
            one_block = func_res1(one_block)
            res += one_block
            #result_blocks.append(vector_block)

            bar_state += bar_step
            print(bar_state)
            progress_bar.setValue(bar_state)

    if flag_OFB:
        # отработка первого шага с вектором
        vector_block = cycling_for_encr(vector_block, keys_for_cycle)
        c1 = xor(text_in_block_replace[0], vector_block)
        one_block = end_replace1(c1)
        one_block = func_res1(one_block)
        res += one_block
        #result_blocks.append(c1)

        # отработка остального
        for p in range(1, len(text_in_block_replace)):
            vector_block = cycling_for_encr(vector_block, keys_for_cycle)
            c1 = xor(text_in_block_replace[p], vector_block)
            one_block = end_replace1(c1)
            one_block = func_res1(one_block)
            res += one_block
            #result_blocks.append(c1)

            bar_state += bar_step
            print(bar_state)
            progress_bar.setValue(bar_state)

    #print('result: ', result_blocks)

    #text_replace_end = end_replace(result_blocks)

    #result = func_res(text_replace_end)

    # удаляем паддинг
    """res = result[:len(result) - 8]
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
            res += analyze"""

    result = res[:len(res) - 8]
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

    #print('del pad ', res) #!надо

    progress_bar.setValue(0)

    if output_file:
        output_file.write(result)

    else:
        print('res ', res)
        print('del pad ', result)

        resultat = ''
        for i in result:
            resultat += chr(i)
        print('Результат в символах: ', resultat)

        return resultat