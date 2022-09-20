# alphabet = 'abcdefghijklmnopqrstuvwxyz'

# xyz
# x = 23, y = 24, z = 25
# x:23 + 2 = 25; z
# y:24 + 2 = 26 % 26 = 0 a
# z: 25 + 2 = 27 % 26 = 1 b


# abc
# a=0, b=1, c=2
# c, d, f


def caesarCipherEncryptor(string, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    codex = ""

    for char in string:
        chr_idx = alphabet.index(char) 
        new_chr_idx = (chr_idx + key ) % 26
        new_chr = alphabet[new_chr_idx] 
        codex += new_chr
    return ','.join(codex)
