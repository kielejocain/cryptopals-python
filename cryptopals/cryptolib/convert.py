def hex_to_64(hexstr):
    """Convert a hex string to a base64 string.
    
    Keyword arguments:
    hexstr -- the hex string we wish to convert
    """
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

def hex_from_64(b64str):
    """Convert a base64 string to a hex string.

    Keyword arguments:
    b64str -- the base64 string we wish to convert
    """
    if b64str == '':
        return ''

    B64CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    HEXCHARS = '0123456789abcdef'

    ## internals
    # bits contains the bits read off so far that don't make enough for a char
    bits = 0
    # bits_left tracks how many bits are left until a char is ready to convert
    bits_left = 4
    # output hods the accrued hex string thus far
    output = ''

    # compute expected padding to validate at the end
    padding = 0
    unpadded_str = b64str
    while unpadded_str[-1] == '=':
        padding += 2
        unpadded_str = unpadded_str[:-1]

    for b in unpadded_str:
        charbits = B64CHARS.find(b)
        if charbits == -1:
            err_msg = 'The given string was not base64-encoded: {}\nDue to char: {}'
            raise ValueError(err_msg.format(b64str, b))
        # if no bits carried over
        if bits_left == 4:
            # append the first four bits as a hex char
            output += HEXCHARS[charbits >> 2]
            # save the last two bits
            bits = charbits & 3
            bits_left = 2
        else:
            # two bits are carried over; prepend them
            charbits = (bits << 6) | charbits
            output += HEXCHARS[charbits >> 4] + HEXCHARS[charbits & 15]
            # clear the bit carring mechanism
            bits = 0
            bits_left = 4

    # validate and trim if necessary
    if padding == 4:
        # there should be no bits carried,
        # and the last char should be an unnecessary '0' from padding
        if (bits_left == 2) or (output[-1] != '0'):
            err_msg = 'The given string was not base64-encoded: {}\nPadding error'
            raise ValueError(err_msg.format(b64str))
        else:
            output = output[:-1]
    elif padding == 2:
        # there should be two padding bits carried that are zeroes
        if (bits_left == 4) or (bits > 0):
            err_msg = 'The given string was not base64-encoded: {}\nPadding error'
            raise ValueError(err_msg.format(b64str))
    else:
        # there should be no carried bits
        if bits_left == 2:
            err_msg = 'The given string was not base64-encoded: {}\nPadding error'
            raise ValueError(err_msg.format(b64str))
    
    return output
