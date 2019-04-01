import cryptopals.cryptolib.measure as measure

def test_english_frequency_score():
    assert measure.english_frequency_score(b' ') == 18.288
    assert measure.english_frequency_score(b'b') == 1.259
    assert measure.english_frequency_score(b'\x00') == 0
    assert measure.english_frequency_score(b' b\x05') == 19.547
