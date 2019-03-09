def hex_to_64(hexstr):
    """Take in a hex string, convert to base64 string"""
    B64CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    ## internals
    # bits contains the bits read off so far that don't make enough for a char
    bits = 0
    # bits_left tracks how many bits are left until a char is ready to convert
    bits_left = 6
    # output holds the accrued base64 string thus far
    output = ''

    # Read each hex char as four bits.  Every time 6 are accrued,
    # convert them to base64 and continue.
    for h in hexstr:
        hbits = int(h, 16)

        if bits_left == 6:
            # h's bits aren't enough.  Hold 'em and keep going.
            bits = hbits
            bits_left = 2

        elif bits_left == 4:
            # h's bits are just enough.  Add 'em to the bits bin and convert.
            bits = (bits << 4) | hbits
            output += B64CHARS[bits]
            bits = 0
            bits_left = 6

        else:
            # h's top two bits finish a set of 6.  Convert the set
            # and save the last two of h's bits.
            bits = (bits << 2) | (hbits >> 2)
            output += B64CHARS[bits]
            bits = hbits & 3
            bits_left = 4

    # After reading hexstr, we may need some zeroes for padding.
    # We should also add '=' chars for each pair of padding bits.
    if bits_left < 6:
        output += B64CHARS[bits << bits_left]
        output += '=' * (bits_left // 2)

    return output
