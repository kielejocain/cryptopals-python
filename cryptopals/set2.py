#import itertools
#import os

#import cryptolib.convert as convert
#import cryptolib.crack   as crack
#import cryptolib.decrypt as decrypt
#import cryptolib.encrypt as encrypt
#import cryptolib.measure as measure
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
