import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from . import encrypt
from . import utils

def aes_block(ciphertext, key):
    """Uses the AES algorithm in ECB mode to decrypt a 16-byte ciphertext
    block with a given key of the same length.

    Keyword arguments:
    ciphertext -- the byte string to be decrypted
    key        -- the byte string key
    """
    if len(ciphertext) != 16:
        raise ValueError("The ciphertext can only be one block (16 bytes).")
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()

def aes_cbc(ciphertext, key, init_vec):
    """Uses the AES algorithm in CBC mode to decrypt a ciphertext
    with a given key and initialization vector of the same length.

    Keyword arguments:
    ciphertext -- the byte string to be decrypted
    key        -- the byte string key
    init_vec   -- the initialization vector
    """
    block_size = 16
    plaintext = b''
    blocks = utils.list_blocks(ciphertext, block_size)
    prev_block = init_vec
    for block in blocks:
        plaintext += byte_key_xor(aes_block(block, key), prev_block)
        prev_block = block
    return plaintext

def aes_ecb(ciphertext, key):
    """Uses the AES algorithm in ECB mode to decrypt a ciphertext
    with a given key.

    Keyword arguments:
    ciphertext -- the byte string to be decrypted
    key        -- the byte string key
    """
    block_size = 16
    plaintext = b''
    for block in utils.list_blocks(ciphertext, block_size):
        plaintext += aes_block(block, key)
    return plaintext

def byte_key_xor(ciphertext, key):
    """Decrypts a byte string encrypted with XOR."""
    return encrypt.byte_key_xor(ciphertext, key)

def hex_key_xor(ciphertext, key):
    """Decrypts a hex string encrypted with XOR."""
    return encrypt.hex_key_xor(ciphertext, key)
