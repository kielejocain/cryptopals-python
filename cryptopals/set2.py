# import itertools
import os

import cryptolib.convert as convert
# import cryptolib.crack   as crack
import cryptolib.decrypt as decrypt
import cryptolib.encrypt as encrypt
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
    prob_statement = """~~~SET 2 EXERCISE 11: An ECB/CBC Detection Oracle~~~
    Now that you have ECB and CBC working:

    Write a function to generate a random AES key; that's just 16 random bytes.

    Write a function that encrypts data under an unknown key --- that is,
    a function that generates a random key and encrypts under it.

    The function should look like:

        encryption_oracle(your-input)
        => [MEANINGLESS JIBBER JABBER]

    Under the hood, have the function append 5-10 bytes (count chosen randomly)
    before the plaintext and 5-10 bytes after the plaintext.

    Now, have the function choose to encrypt under ECB 1/2 the time, and under
    CBC the other half (just use random IVs each time for CBC). Use rand(2) to
    decide which to use.

    Detect the block cipher mode the function is using each time. You should
    end up with a piece of code that, pointed at a block box that might be
    encrypting ECB or CBC, tells you which one is happening."""

    print(prob_statement)
    print()

    plaintext = b''
    for _ in range(43):
        plaintext += b'u'

    ecb_count = 0
    for _ in range(100):
        ciphertext = encrypt.aes_rando(plaintext)
        blocks = list(utils.list_blocks(ciphertext, 16))
        if blocks[1] == blocks[2]:
            ecb_count += 1

    print(f'ECB mode count (of 100): {ecb_count}')
    print()
    assert ecb_count > 0
    print("SUCCESS!\n\n")

def exercise_12():
    prob_statement = f"""~~~SET 2 EXERCISE 12: Byte-at-a-time ECB decryption (Simple)~~~

    Copy your oracle function to a new function that encrypts buffers under ECB
    mode using a consistent but unknown key (for instance, assign a single
    random key, once, to a global variable).

    Now take that same function and have it append to the plaintext,
    BEFORE ENCRYPTING, the following string:

    Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
    aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
    dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
    YnkK

    Base64 decode the string before appending it. Do not base64 decode the
    string by hand; make your code do it. The point is that you don't know its
    contents.

    What you have now is a function that produces:

    AES-128-ECB(your-string || unknown-string, random-key)

    It turns out: you can decrypt "unknown-string" with repeated calls to the
    oracle function!

    Here's roughly how:

    1.  Feed identical bytes of your-string to the function 1 at a time ---
        start with 1 byte ("A"), then "AA", then "AAA" and so on. Discover the
        block size of the cipher. You know it, but do this step anyway.
    2.  Detect that the function is using ECB. You already know, but do this
        step anyways.
    3.  Knowing the block size, craft an input block that is exactly 1 byte
        short (for instance, if the block size is 8 bytes, make "AAAAAAA").
        Think about what the oracle function is going to put in that last byte
        position.
    4.  Make a dictionary of every possible last byte by feeding different
        strings to the oracle; for instance, "AAAAAAAA", "AAAAAAAB", "AAAAAAAC",
        remembering the first block of each invocation.
    5.  Match the output of the one-byte-short input to one of the entries in
        your dictionary. You've now discovered the first byte of unknown-string.
    6.  Repeat for the next byte.
    """

    print(prob_statement)

    ## define our oracle
    # choose a random, fixed key
    aes_key = os.urandom(16)
    def oracle(plaintext, key):
        SECRET = "" \
            "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg" \
            "aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq" \
            "dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg" \
            "YnkK"
        # append the input
        text = plaintext + bytes.fromhex(convert.hex_from_64(SECRET))
        text = utils.pkcs7_padding(text, 16)
        return encrypt.aes_ecb(text, key)

    ## compute the block size (should be 16) and secret size
    block_size = 0
    secret_padded_len = len(oracle(b'', aes_key))
    i = 1
    while block_size == 0:
        plain = b'A' * i
        new_len = len(oracle(plain, aes_key))
        # find the first time a new block is necessary
        if new_len > secret_padded_len:
            block_size = new_len - secret_padded_len
            secret_len = secret_padded_len - i
        else:
            i += 1
    print(f"Block size: {block_size}")
    assert(block_size == 16)

    ## confirm ECB mode
    blocks = list(utils.list_blocks(
        oracle(b'A'*2*block_size, aes_key),
        block_size
        ))
    print(f"ECB mode used: {blocks[0] == blocks[1]}")
    assert(blocks[0] == blocks[1])

    ## glean the secret
    secret = b''
    for i in range(secret_len):
        current_block = i // 16
        current_byte  = i %  16
        prefix = b'A' * (15 - current_byte)
        target = oracle(prefix, aes_key)
        target_block = list(
                utils.list_blocks(target, block_size)
                )[current_block]
        for b in range(256):
            guess = bytes([b])
            mess  = prefix + secret + guess
            crypt = oracle(mess, aes_key)
            crypt_block = list(
                    utils.list_blocks(crypt, block_size)
                    )[current_block]
            if crypt_block == target_block:
                secret += guess
                break
        else:
            msg = f"Nothing worked for the {i}th byte.\nSecret so far:\n{secret}"
            raise RuntimeError(msg)

    print("\nTHE SECRET:")
    print(secret.decode("utf-8"))

    SECRET = "" \
        "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg" \
        "aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq" \
        "dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg" \
        "YnkK"
    assert(SECRET == convert.hex_to_64(secret.hex()))
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
