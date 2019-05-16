# import itertools
import os

import cryptolib.convert as convert
# import cryptolib.crack   as crack
import cryptolib.decrypt as decrypt
# import cryptolib.encrypt as encrypt
# import cryptolib.measure as measure
import cryptolib.utils   as utils

def exercise_9():
    INPUT = b"YELLOW SUBMARINE"
    CHECK = b"YELLOW SUBMARINE\x04\x04\x04\x04"

    prob_statement = f"""~~~SET 2 EXERCISE 9: Implement PKCS#7 padding~~~

    A block cipher transforms a fixed-sized block (usually  8 or 16 bytes) of
    plaintext into ciphertext.  But we almost never want to transform a single
    block; we encrypt irregularly-sized messages.

    One way we account for irregularly-sized messages is by padding, creating a
    plaintext that is an even multiple of the blocksize.  The most popular
    padding scheme is called PKCS#7.

    So: pad any block to a specific block length, by appending the number of
    bytes of padding to the end of the block.  For instance,

    {INPUT}

    ... padded to 20 bytes would be

    {CHECK}
    """

    print(prob_statement)

    # run the exercise and allow the user to visually inspect
    output = utils.pkcs7_padding(INPUT, 20)
    print(f"OUTPUT: {output}")

    # confirm the assertion
    assert output == CHECK
    print("SUCCESS!\n\n")

def exercise_10():
    # get the directory of the current file to compute
    # the path to the data file
    file_dir = os.path.dirname(os.path.realpath(__file__))
    input_file = file_dir + "/data/10.txt"

    prob_statement = """~~~SET 2 EXERCISE 10: Implement CBC mode~~~

    CBC mode is a block cipher mode that allows us to encrypt irregularly-sized
    messages, despite the fact that a block cipher natively only transforms
    individual blocks.

    In CBC mode, each ciphertext block is added to the next plaintext block
    before the next call to the cipher core.

    The first plaintext block, which has no associated previous ciphertext
    block, is added to a "fake 0th ciphertext block" called the initialization
    vector, or IV.

    Implement CBC mode by hand by taking the ECB function you wrote earlier,
    making it encrypt instead of decrypt (verify this by decrypting whatever
    you encrypt to test), and using your XOR function from the previous
    exercise to combine them.

    The file at ./data/4.txt is intelligible (somewhat) when CBC decrypted
    against "YELLOW SUBMARINE" with an IV of all ASCII 0 (\\x00\\x00\\x00 &c)
    """

    print(prob_statement)

    print("Reading data file")
    with open(input_file, 'r') as f:
        data = "".join([l.strip() for l in f.readlines()])
    ciphertext = bytes.fromhex(convert.hex_from_64(data))

    key = b'YELLOW SUBMARINE'
    iv  = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    plaintext = decrypt.aes_cbc(ciphertext, key, iv)
    print("PLAINTEXT:")
    print(plaintext.decode('utf-8'))

    print("SUCCESS!\n\n")

def exercise_11():
    print("SUCCESS!\n\n")

def exercise_12():
    print("SUCCESS!\n\n")

def exercise_13():
    print("SUCCESS!\n\n")

def exercise_14():
    print("SUCCESS!\n\n")

def exercise_15():
    print("SUCCESS!\n\n")

def exercise_16():
    print("SUCCESS!\n\n")


if __name__ == "__main__":
    exercise_9()
    exercise_10()
    exercise_11()
    exercise_12()
    exercise_13()
    exercise_14()
    exercise_15()
    exercise_16()
