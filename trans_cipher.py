ENC = 0
DEC = 1

def parse_key(key):
    tmp = []
    key = key.upper()
    for i, k in enumerate(key): # 문자의 인덱스와 문자를 가져온다
        tmp.append((i, k)) # tmp 리스트에 튜플 형태로 저장한다.
    tmp = sorted(tmp, key=lambda x:x[1]) # key는 키워드 매개변수로, 함수를 인자로 받는다. (해당 함수로 처리된 데이터로 정렬한다. 이 경우 lambda의 리턴값이 문자에 해당하는 부분이므로 문자의 상대적인 순서에 따라 배치된다)
    enc_table = {}
    dec_table = {}
    for i, r in enumerate(tmp): # 알파벳간의 상대적인 우선순위로 정렬된 tmp
        enc_table[r[0]] = i
        dec_table[i] = r[0]
    return enc_table, dec_table

def transposition(msg, key, mode):
    msgsize = len(msg)
    keysize = len(key)
    ret = ''
    filler = ''
    if msgsize%keysize != 0:
        filler = '0'*(keysize-msgsize%keysize)
    msg = msg.upper()
    msg += filler
    enc_table, dec_table = parse_key(key)
    if mode == ENC:
        table = enc_table
    if mode == DEC:
        table = dec_table
    if mode == ENC:
        buf = ['']*keysize
        for i, c in enumerate(msg):
            col = i %keysize
            index = table[col]
            buf[index] += c
        for text in buf:
            ret += text
    else:
        blocksize = int(msgsize/keysize)
        buf = ['']*keysize
        pos = 0
        for i in range(keysize):
            text = msg[pos:pos+blocksize]
            index = table[i]
            buf[index] += text
            pos += blocksize
        for i in range(blocksize):
            for j in range(keysize):
                if buf[j][i] != '0':
                    ret += buf[j][i]
    return ret

def main():
    key = "BRAIN"
    msg = "TREASUREBOXISBURRIEDATTWOHUNDREADFEETTONORTHEASTAWAYFROMYOURHOME"
    print("Original :\t%s" %msg.upper())
    cryptogram = transposition(msg, key, ENC)
    print("Ciphered :\t%s" %cryptogram)
    deciphertext = transposition(cryptogram, key, DEC)
    print("Deciphered :\t%s" %deciphertext)

if __name__ == "__main__":
    main()