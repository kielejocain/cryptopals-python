from nose.tools import assert_raises

import cryptopals.cryptolib.convert as convert

def test_hex_to_64():
    assert convert.hex_to_64('') == ''
    assert convert.hex_to_64('4') == 'Q='
    assert convert.hex_to_64('49') == 'SQ=='
    assert convert.hex_to_64('492') == 'SS'
    assert convert.hex_to_64('4927') == 'SSc='
    assert convert.hex_to_64('49276') == 'SSdg=='
    assert convert.hex_to_64('49276d') == 'SSdt'
    assert_raises(ValueError, convert.hex_to_64, 'best')

