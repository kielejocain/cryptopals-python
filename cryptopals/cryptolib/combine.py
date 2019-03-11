def hex_xor(hex1, hex2):
    """XOR two hex strings together.

    Keyword arguments:
    hex1 -- the first hex string
    hex2 -- the second hex string
    """
    if len(hex1) != len(hex2):
        raise ValueError("The two strings are not the same length.")

    HEXCHARS = '0123456789abcdef'
    output = ''

    # take next two characters, convert to binary, XOR them together,
    # and lookup the associated hex value in HEXCHARS
    for c1, c2 in zip(hex1, hex2):
        dec1 = int(c1, 16)
        dec2 = int(c2, 16)
        output += HEXCHARS[dec1 ^ dec2]

    return output
