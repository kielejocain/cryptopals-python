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

def test_hex_from_64():
    assert convert.hex_from_64('') == ''
    assert convert.hex_from_64('Q=') == '4'
    assert convert.hex_from_64('SQ==') == '49'
    assert convert.hex_from_64('SS') == '492'
    assert convert.hex_from_64('SSc=') == '4927'
    assert convert.hex_from_64('SSdg==') == '49276'
    assert convert.hex_from_64('SSdt') == '49276d'
    assert_raises(ValueError, convert.hex_from_64, 'Hello, world!')
    assert_raises(ValueError, convert.hex_from_64, 'Q')
    assert_raises(ValueError, convert.hex_from_64, 'SS=')
    assert_raises(ValueError, convert.hex_from_64, 'Q==')
