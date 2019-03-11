from nose.tools import assert_raises

import cryptopals.cryptolib.combine as combine

def test_hex_xor():
    assert combine.hex_xor('1', '2') == '3'
    assert combine.hex_xor('5', 'f') == 'a'
    assert combine.hex_xor('1c0', '686') == '746'
    assert_raises(ValueError, combine.hex_xor, "1", "12")
