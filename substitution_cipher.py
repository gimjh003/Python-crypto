# decbook = cryptogram letter : plain_text letter (for decode)
# encbook = plain_text letter : cryptogram letter (for encode)
def make_codebook():
    decbook = {'5':'a','2':'b','#':'d','8':'e','1':'f','3':'g','4':'h','6':'i','0':'l','9':'m'\
              ,'*':'n','%':'o','=':'p','(':'r',')':'s',';':'t','?':'u','@':'v',':':'y','7':' '}
    encbook = {}
    for k in decbook:
        val = decbook[k]
        encbook[val] = k
    return encbook, decbook
# encrypt : plain_text -> cryptogram (encbook(plain_text letter : cryptogram letter))
def encrypt(msg, encbook): # msg : plain_text
    for c in msg:
        if c in encbook:
            msg = msg.replace(c, encbook[c]) # replace character
    return msg # msg : cryptogram
# for c in msg : cryptogram -> plain_text (decbook(cryptogram letter : plain_text letter))
def decrypt(msg, decbook): # msg : cryptogram
    for c in msg:
        if c in decbook:
            msg = msg.replace(c, decbook[c]) # replace character
    return msg # msg : plain_text
# showcase
if __name__ == "__main__":
    encbook, decbook = make_codebook()
    cryptogram = encrypt("hello world", encbook)
    print(cryptogram)
    plain_text = decrypt(cryptogram, decbook)
    print(plain_text)