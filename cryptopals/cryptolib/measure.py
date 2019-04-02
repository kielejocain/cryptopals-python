def english_frequency_score(text):
    """Scores a byte string on how likely it is to be in English.

    Keyword arguments:
    text -- the byte string to be scored
    """
    # source: http://www.macfreek.nl/memory/Letter_Distribution
    FREQUENCY = {' ': 18.288, 'e': 10.267, 't': 7.517, 'a': 6.532, 'o': 6.160,
                'n': 5.712, 'i': 5.668, 's': 5.317, 'r': 4.988, 'h': 4.979,
                'l': 3.318, 'd': 3.283, 'u': 2.276, 'c': 2.234, 'm': 2.027,
                'f': 1.983, 'w': 1.704, 'g': 1.625, 'p': 1.504, 'y': 1.428,
                'b': 1.259, 'v': 0.796, 'k': 0.561, 'x': 0.141, 'j': 0.098,
                'q': 0.084, 'z': 0.051
                }

    score = 0
    for c in text:
        # tabs and linefeeds/carriage returns
        if c in [9, 10, 13]:
            continue
        # if c isn't an English character or punctuation,
        # the string isn't English.
        elif c < 32 or c > 126:
            return -1
        else:
            score += FREQUENCY.get(chr(c).lower(), 0)

    return score

def hamming_distance(str1, str2):
    """Computes the hamming distance (i.e. the number of
    differing bits) between two byte strings.

    Keyword arguments:
    str1 -- the first byte string
    str2 -- the second byte string
    """
    distance = 0
    for b1, b2 in zip(str1, str2):
        # xor in each place is 1 if the bits differ, 0 otherwise
        bdiff = b1 ^ b2
        while bdiff > 0:
            # if the last bit is 1, count it
            if bdiff % 2 == 1:
                distance += 1
            # drop the last bit
            bdiff = bdiff >> 1
    return distance
