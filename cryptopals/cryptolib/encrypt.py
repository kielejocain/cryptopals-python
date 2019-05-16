import itertools

def aes_block(plaintext, key):
    """Uses the AES algorithm in ECB mode to encrypt a plaintext
    with a given key of the same length.

    Keyword arguments:
    plaintext -- the byte string to be encrypted
    key        -- the byte string key
    """
    if len(plaintext) != 16:
        raise ValueError("The plaintext can only be one block (16 bytes).")
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
    block_size = 16
    ciphertext = b''
    blocks = utils.list_blocks(plaintext, block_size)
    prev_cblock = init_vec
    for block in blocks:
        cblock = byte_key_xor(aes_block(block, prev_cblock), key)
        ciphertext += cblock
        prev_cblock = cblock
    return plaintext

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
