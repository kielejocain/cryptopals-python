import cryptopals.cryptolib.decrypt as decrypt

def test_single_byte_xor():
    bytes1 = bytes.fromhex('1b37373331363f78151b7f2b783431333d78')
    assert decrypt.single_byte_xor(bytes1).decode('utf-8') == "Cooking MC's like "
    bytes2 = bytes.fromhex('397828372d363c78373e783a393b3736')
    assert decrypt.single_byte_xor(bytes2).decode('utf-8') == "a pound of bacon"
