from . import encrypt
from . import measure

def single_byte_xor(ciphertext):
    """Decrypt a byte string XOR encrypted with a single byte key.

    Keyword arguments:
    plaintext -- the byte string to be decrypted
    """

    possibles = []
    for b in range(256):
        key = bytes([b])
        out = encrypt.byte_key_xor(ciphertext, key)
        score = measure.english_frequency_score(out)
        possibles.append((out, score))

    possibles.sort(key=lambda x: x[1], reverse = True)

    return possibles[0][0]
