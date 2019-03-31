from nose.tools import assert_raises

import cryptopals.cryptolib.encrypt as encrypt

def test_hex_key_xor():
    assert encrypt.hex_key_xor('0', '0') == '0'
    assert encrypt.hex_key_xor('f', 'f') == '0'
    assert encrypt.hex_key_xor('1', '2') == '3'
    assert encrypt.hex_key_xor('5', 'f') == 'a'
    assert encrypt.hex_key_xor('7', '0') == '7'
    assert encrypt.hex_key_xor('7', '1') == '6'
    assert encrypt.hex_key_xor('7', '2') == '5'
    assert encrypt.hex_key_xor('7', '3') == '4'
    assert encrypt.hex_key_xor('7', '4') == '3'
    assert encrypt.hex_key_xor('7', '5') == '2'
    assert encrypt.hex_key_xor('7', '6') == '1'
    assert encrypt.hex_key_xor('7', '7') == '0'
    assert encrypt.hex_key_xor('7', '8') == 'f'
    assert encrypt.hex_key_xor('7', '9') == 'e'
    assert encrypt.hex_key_xor('7', 'a') == 'd'
    assert encrypt.hex_key_xor('7', 'b') == 'c'
    assert encrypt.hex_key_xor('7', 'c') == 'b'
    assert encrypt.hex_key_xor('7', 'd') == 'a'
    assert encrypt.hex_key_xor('7', 'e') == '9'
    assert encrypt.hex_key_xor('7', 'f') == '8'
    assert encrypt.hex_key_xor('1c0', '686') == '746'
    assert encrypt.hex_key_xor('111111', '2') == '333333'
    assert encrypt.hex_key_xor('5a2', 'f1') == 'abd'
