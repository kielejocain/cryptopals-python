import itertools
import os
import random

from . import utils

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


AES_BLOCK_SIZE = 16

def aes_block(plaintext, key):
    """Uses the AES algorithm in ECB mode to encrypt a plaintext
    with a given key of the same length.

    Keyword arguments:
    plaintext -- the byte string to be encrypted
    key        -- the byte string key
    """
    if len(plaintext) != AES_BLOCK_SIZE:
        raise ValueError(f"The plaintext can only be one block ({AES_BLOCK_SIZE} bytes).")
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    return encryptor.update(plaintext) + encryptor.finalize()

def aes_cbc(plaintext, key, init_vec):
    """Uses the AES algorithm in CBC mode to encrypt a ciphertext
    with a given key and initialization vector of the same length.

    Keyword arguments:
    plaintext -- the byte string to be encrypted
    key       -- the byte string key
    init_vec  -- the initialization vector
    """
    if len(init_vec) != AES_BLOCK_SIZE:
        raise ValueError("The initialization vector can only be one block (16 bytes).")
    ciphertext = b''
    blocks = utils.list_blocks(plaintext, AES_BLOCK_SIZE)
    prev_cblock = init_vec
    for block in blocks:
        cblock = byte_key_xor(aes_block(block, prev_cblock), key)
        ciphertext += cblock
        prev_cblock = cblock
    return ciphertext

def aes_ecb(plaintext, key):
    """Uses the AES algorithm in ECB mode to encrypt a ciphertext
    with a given key.

    Keyword arguments:
    plaintext -- the byte string to be encrypted
    key       -- the byte string key
    """
    blocks = utils.list_blocks(plaintext, AES_BLOCK_SIZE)
    ciphertext = b''
    for block in blocks:
        ciphertext += aes_block(block, key)
    return ciphertext

def aes_rando(plaintext):
    """"""
    # Pad the plaintext randomly
    prefix = os.urandom(random.randint(5,10))
    suffix = os.urandom(random.randint(5,10))
    padded_text = prefix + plaintext + suffix
    padded_text = utils.pkcs7_padding(padded_text, AES_BLOCK_SIZE)

    # Generate a key
    key = os.urandom(AES_BLOCK_SIZE)

    # Encrypt using random mode
    if random.randint(1,2) == 1:
        init_vec = os.urandom(AES_BLOCK_SIZE)
        return aes_cbc(padded_text, key, init_vec)
    else:
        return aes_ecb(padded_text, key)

def byte_key_xor(plaintext, key):
    """Encrypt a byte string with a byte string key.

    Keywork arguments:
    plaintext -- the byte string to be encrypted
    key       -- the encryption key
    """

    output = b''

    #convert chars to binary, XOR (^), and append to output
    for pc, kc in zip(plaintext, itertools.cycle(key)):
        output += bytes([pc ^ kc])

    return output

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
