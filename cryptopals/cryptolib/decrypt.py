import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from . import encrypt

def aes_ecb(ciphertext, key):
    """Uses the AES algorithm in ECB mode to decrypt a ciphertext
    with a given key.

    Keyword arguments:
    ciphertext -- the byte string to be decrypted
    key        -- the byte string key
    """
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()

def byte_key_xor(ciphertext, key):
    """Decrypts a byte string encrypted with XOR."""
    return encrypt.byte_key_xor(ciphertext, key)

def hex_key_xor(ciphertext, key):
    """Decrypts a hex string encrypted with XOR."""
    return encrypt.hex_key_xor(ciphertext, key)
