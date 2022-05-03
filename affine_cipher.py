ENC = 0
DEC = 1

def make_disk(k1, k2):
    enc_disk = {}
    dec_disk = {}
    for i in range(26):
        enc_i = (k1*i+k2)%26
        enc_ascii = enc_i + 65
        enc_disk[chr(i+65)] = chr(enc_ascii)
        dec_disk[chr(enc_ascii)] = chr(i+65)
    return enc_disk, dec_disk

def affine(msg, key1, key2, mode):
    ret = ""
    msg = msg.upper()
    enc_disk, dec_disk = make_disk(key1, key2)
    if mode is ENC: disk = enc_disk
    if mode is DEC: disk = dec_disk
    for c in msg:
        if c in disk: ret += disk[c]
        else: ret += c
    return ret

def main():
    k1, k2 = 3, 5 # k1은 26과 서로 소인 25 이하의 양의 정수, 그렇지 않다면 대응되는 문자가 중복되면서 해독이 불가능해진다.
    msg = "abcdefghijklmnopqrstuvwxyz"
    print("Original :\t%s" %msg.upper())
    msg = affine(msg, k1, k2, ENC)
    print("Affine cipher :\t%s" %msg)
    msg = affine(msg, k1, k2, DEC)
    print("Deciphered :\t%s" %msg)

if __name__ == "__main__":
    main()