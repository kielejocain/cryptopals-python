import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

import cryptopals.cryptolib.decrypt as decrypt

def test_aes_ecb():
    backend = default_backend()
    key = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    plaintext = b"This is my plaintext, ain't it!!"
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    output = decrypt.aes_ecb(ciphertext, key)
    assert plaintext == output
