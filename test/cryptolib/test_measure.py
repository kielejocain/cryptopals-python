import cryptopals.cryptolib.measure as measure

def test_english_frequency_score():
    assert measure.english_frequency_score(b'\x00') == -1
    assert measure.english_frequency_score(b'\r') == 0
    assert measure.english_frequency_score(b'\t') == 0
    assert measure.english_frequency_score(b'\n') == 0
    assert measure.english_frequency_score(b'\x1f') == -1
    assert measure.english_frequency_score(b' ') == 18.288
    assert measure.english_frequency_score(b'b') == 1.259
    assert measure.english_frequency_score(b' b') == 19.547
    assert measure.english_frequency_score(b' b\x05') == -1

def test_hamming_distance():
    assert measure.hamming_distance(b'b', b'b') == 0
    assert measure.hamming_distance(b'a', b'b') == 2
    assert measure.hamming_distance(b'\x00', b'\xff') == 8
    assert measure.hamming_distance(b'\x00\x01\x02', b'\xff\xfe\xfd') == 24
    assert measure.hamming_distance(b'this is a test', b'wokka wokka!!!') == 37
