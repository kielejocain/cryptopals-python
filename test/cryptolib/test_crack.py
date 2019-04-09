import os 

import cryptopals.cryptolib.convert as convert
import cryptopals.cryptolib.crack   as crack

def test_single_byte_xor():
    bytes1 = bytes.fromhex('1b37373331363f78151b7f2b783431333d78')
    assert crack.single_byte_xor(bytes1)[0] == b"X"
    assert crack.single_byte_xor(bytes1)[1] == b"Cooking MC's like "
    bytes2 = bytes.fromhex('397828372d363c78373e783a393b3736')
    assert crack.single_byte_xor(bytes2)[0] == b"X"
    assert crack.single_byte_xor(bytes2)[1] == b"a pound of bacon"

def test_repeating_key_xor():
    file_dir = os.path.dirname(os.path.realpath(__file__))
    input_file = file_dir + "/../../cryptopals/data/6.txt"
    with open(input_file, 'r') as f:
        data = ''.join([l.strip() for l in f.readlines()])
    data = bytes.fromhex(convert.hex_from_64(data))
    key, _ = crack.repeating_key_xor(data)
    assert key == b"Terminator X: Bring the noise"
