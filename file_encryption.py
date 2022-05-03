from substitution_cipher import *
if __name__ == "__main__":
    h = open("plain.txt", "rt")
    content = h.read()
    h.close
    encbook, decbook = make_codebook()
    content = encrypt(content, encbook)
    h = open("encryption.txt", "wt+")
    h.write(content)
    h.close()