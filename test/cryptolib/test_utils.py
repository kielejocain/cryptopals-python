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
