def list_blocks(itr, n):
    """A generator that breaks an iterable into a list of blocks"""
    if n < 1:
        raise ValueError("Blocks must be of size at least 1")
    def blocks(itr, n):
        for i in range(0, len(itr), n):
            yield itr[i:i+n]
    return blocks(itr, n)
