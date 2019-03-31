import cryptopals.cryptolib.measure as measure

def test_english_frequency_score():
    assert measure.english_frequency_score(' ') == 18.288
    assert measure.english_frequency_score('b') == 1.259
    assert measure.english_frequency_score(chr(0)) == 0
    assert measure.english_frequency_score(' b' + chr(5)) == 19.547
