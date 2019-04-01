import itertools

def hex_key_xor(plaintext, key):
    """Encrypt a hex string with a hex key.

    Keyword arguments:
    plaintext -- the hex string to be encrypted
    key       -- the encryption key
    """
    HEXCHARS = '0123456789abcdef'

    output = ''

    # convert chars to binary, XOR (^), and append to output
    for pc, kc in zip(plaintext, itertools.cycle(key)):
        output += HEXCHARS[int(pc, 16) ^ int(kc, 16)]

    return output

def byte_key_xor(plaintext, key):
    """Encrypt an byte string with a byte string key.

    Keywork arguments:
    plaintext -- the byte string to be encrypted
    key       -- the encryption key
    """

    output = b''

    #convert chars to binary, XOR (^), and append to output
    for pc, kc in zip(plaintext, itertools.cycle(key)):
        output += bytes([pc ^ kc])

    return output
