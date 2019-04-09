from nose.tools import assert_raises

import cryptopals.cryptolib.utils as utils

def test_list_blocks():
    blocks = utils.list_blocks("Hello, world!", 4)
    answer = ["Hell", "o, w",  "orld", "!"]
    for i, b in enumerate(blocks):
        assert b == answer[i]

    blocks = utils.list_blocks([1, 2, 3, 4], 3)
    answer = [[1, 2, 3], [4]]
    for i, b in enumerate(blocks):
        assert b == answer[i]

    blocks = utils.list_blocks(b'\x00\x01\x02\x03abcd\n\t\r\n', 4)
    answer = [b'\x00\x01\x02\x03', b'abcd', b'\n\t\r\n']
    for i, b in enumerate(blocks):
        assert b == answer[i]

    assert list(utils.list_blocks(b'', 4)) == []
    assert_raises(ValueError, utils.list_blocks, 'Q==', 0)

def test_pkcs7_padding():
    assert utils.pkcs7_padding(b'a', 4) == b'a\x03\x03\x03'
    assert utils.pkcs7_padding(b'ab', 4) == b'ab\x02\x02'
    assert utils.pkcs7_padding(b'abc', 4) == b'abc\x01'
    assert utils.pkcs7_padding(b'', 8) == b'\x08\x08\x08\x08\x08\x08\x08\x08'
    assert utils.pkcs7_padding(b'abcde', 2) == b'abcde\x01'
    assert utils.pkcs7_padding(b'abcde', 3) == b'abcde\x01'
    assert utils.pkcs7_padding(b'abcd', 2) == b'abcd\x02\x02'

    assert_raises(ValueError, utils.pkcs7_padding, b'abcd', 1)
