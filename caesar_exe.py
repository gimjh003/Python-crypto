# 카이사르 문자변환식 : Enc(i) = (i+k) mod 26
ENC = 0
DEC = 1

def make_disk(key):
    enc_disk = {}; dec_disk = {}
    for i in range(26):
        enc_i = chr((i+key)%26 + 65)
        i = chr(i+65)
        enc_disk[i] = enc_i
        dec_disk[enc_i] = i
    return enc_disk, dec_disk

def caesar(msg, key, mode):
    enc_disk, dec_disk = make_disk(key)
    ret = ''
    msg = msg.upper()
    if mode is ENC : disk = enc_disk
    elif mode is DEC : disk = dec_disk
    for c in msg:
        ret += disk[c]
    return ret

msg = input("type plain_test : ")
key = int(input("type key : "))
cryptogram = caesar(msg, key, ENC)
plain_text = caesar(cryptogram, key, DEC)
print(f"caesar ciphered : {cryptogram}")
print(f"deciphered : {plain_text}")