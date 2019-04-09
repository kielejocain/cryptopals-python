def list_blocks(itr, n):
    """A generator that breaks an iterable into a list of blocks.
    
    Keyword arguements:
    itr -- the incoming iterable to be chopped
    n   -- the size of each block (except possibly the last)
    """
    if n < 1:
        raise ValueError("Blocks must be of size at least 1")
    def blocks(itr, n):
        for i in range(0, len(itr), n):
            yield itr[i:i+n]
    return blocks(itr, n)

def pkcs7_padding(bstr, n):
    """Adds padding per PKCS#7 to the bytestring.

    Keyword arguments:
    bstr -- the byte string to be padded
    n    -- the assumed block size
    """
    if n < 2:
        raise ValueError("Blocks must be of size at least 2")
    blocks = list(list_blocks(bstr, n))
    if len(blocks) > 0:
        short = n - len(blocks[-1])
    else:
        short = n
    if short == 0:
        short = n
    for _ in range(short):
        bstr += bytes([short])
    return bstr
