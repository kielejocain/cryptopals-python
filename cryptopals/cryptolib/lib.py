def hex_to_64(hexstr):
    """Take in a hex string, convert to base64 string"""
    binary_to_64(hex_to_binary(hexstr))


def hex_to_binary(hexstr):
    """Take in a hex string, validate, and convert to binary"""
    LEGAL = "0123456789abcdef"
    if not all([c in LEGAL for c in hexstr]):
        raise ValueError("At least one character in hexstr is invalid hex.")
    else:
        output = [hex_char_to_binary(c) for c in hexstr]
        return "".join(output)

def hex_char_to_binary(char):
    """converts a single hex character to a binary string"""
    HEX_DICT = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
                'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}
    return HEX_DICT[char]

def binary_to_64(binstr):
    """Take in a binary string, validate, and convert to base64"""
    bin_chars = binary_chunks(binstr)
    return "".join(map(binary_to_64_char, bin_chars))

def binary_chunks(binstr):
    """Break a binary string into length-6 chunks with padding"""
    if len(binstr) == 6:
        return [binstr]
    else:
        return [binstr[0:6]] + binary_chunks(binstr[6:])

def binary_to_64_char(binstr):
    """convers a binary string of length 6 to a hex character"""
    TREE_64 = [[[[[['A', 'B'], ['C', 'D']], [['E', 'F'], ['G', 'H']]],
                [[['I', 'J'], ['K', 'L']], [['M', 'N'], ['O', 'P']]]],
                [[[['Q', 'R'], ['S', 'T']], [['U', 'V'], ['W', 'X']]],
                [[['Y', 'Z'], ['a', 'b']], [['c', 'd'], ['e', 'f']]]]],
                [[[[['g', 'h'], ['i', 'j']], [['k', 'l'], ['m', 'n']]],
                [[['o', 'p'], ['q', 'r']], [['s', 't'], ['u', 'v']]]],
                [[[['w', 'x'], ['y', 'z']] ,[['0', '1'], ['2', '3']]],
                [[['4', '5'], ['6', '7']], [['8', '9'], ['+', '/']]]]]]
    ind = [int(i) for i in binstr]
    return TREE_64[ind[0]][ind[1]][ind[2]][ind[3]][ind[4]][ind[5]]

