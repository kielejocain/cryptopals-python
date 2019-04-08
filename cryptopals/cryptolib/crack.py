from . import encrypt
from . import measure
from . import utils

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
        possibles.append((key, out, score))

    possibles.sort(key=lambda x: x[2], reverse = True)

    return (possibles[0][0], possibles[0][1])

def repeating_key_xor(ciphertext):
    """Decrypt a byte string XOR encrypted with a byte string key.

    Keyword arguments:
    plaintext -- the byte string to be decrypted
    """

    def transpose(byte_list):
        """Transposes a list of byte strings so that the first list
        of the output contains all the first elements of the input
        lists, the second contains all the second elements, etc."""
        output = []
        for _ in byte_list[0]:
            output.append(b'')
        for byte_str in byte_list:
            for i in range(len(byte_str)):
                output[i] += byte_str[i:i+1]
        return output

    # Attempt to deduce the key length
    length_scores = []
    for l in range(2, 41):
        cipher_blocks = list(utils.list_blocks(ciphertext, l))
        score = 0
        for s1, s2 in zip(cipher_blocks, cipher_blocks[1:]):
            score += measure.hamming_distance(s1, s2)
        score = score / (l * (len(cipher_blocks) - 1))
        length_scores.append((l, cipher_blocks, score))
    length_scores.sort(key=lambda x: x[2])
    key_length, cipher_blocks, _ = length_scores[0]
    del length_scores

    # Transpose the blocks into lists of bytes XOR'd with the same key byte
    sub_ciphers = transpose(cipher_blocks)

    # Crack each set of characters XOR'd to the same key byte
    key = b''
    sub_texts = []
    for cipher in sub_ciphers:
        keybyte, sub_text = single_byte_xor(cipher)
        key += keybyte
        sub_texts.append(sub_text)

    # Transpose again to get the characters back in order
    plain_blocks = transpose(sub_texts)
    plaintext = b''
    for block in plain_blocks:
        plaintext += block
    return (key, plaintext)
