import itertools
import os

import cryptolib.convert as convert
import cryptolib.crack   as crack
import cryptolib.decrypt as decrypt
import cryptolib.encrypt as encrypt
import cryptolib.measure as measure
import cryptolib.utils   as utils

def exercise_1():
    INPUT = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    CHECK = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    prob_statement = f"""~~~SET 1 EXERCISE 1: Convert hex to base64~~~

    The string
    {INPUT}

    should produce
    {CHECK}
    """

    print(prob_statement)

    # run the exercise and allow the user to visually inspect
    output = convert.hex_to_64(INPUT)
    print(f"OUTPUT: {output}")
    print(f"ANSWER: {CHECK}")

    # confirm the assertion
    assert output == CHECK
    print("SUCCESS!\n\n")

def exercise_2():
    INPUT1 = "1c0111001f010100061a024b53535009181c"
    INPUT2 = "686974207468652062756c6c277320657965"
    CHECK  = "746865206b696420646f6e277420706c6179"

    prob_statement = f"""~~~SET 1 EXERCISE 2: Fixed XOR~~~

    Write a function that takes two equal-length buffers and produces their XOR combination.

    If your function works properly, then when you feed it the string:
    {INPUT1}

    ... after hex decoding, and when XOR'd against:
    {INPUT2}

    ... should produce:
    {CHECK}
    """

    print(prob_statement)

    # run the exercise and allow the user to visually inspect
    output = encrypt.hex_key_xor(INPUT1, INPUT2)
    print(f"OUTPUT: {output}")
    print(f"ANSWER: {CHECK}")

    # confirm the assertion
    assert output == CHECK
    print("SUCCESS!\n\n")

def exercise_3():
    INPUT = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    CHECK = "Cooking MC's like a pound of bacon"

    prob_statement = f"""~~~SET 1 EXERCISE 3: Single-byte XOR cipher~~~

    The hex encoded string:
    {INPUT}

    ... has been XOR'd against a single character.  Find the key, decrypt the message.
    """

    print(prob_statement)

    bytestr = bytes.fromhex(INPUT)
    key, plainbytes = crack.single_byte_xor(bytestr)
    key = key.decode('utf-8')
    plaintext = plainbytes.decode('utf-8')

    print(f"KEY:    {key}")
    print(f"OUTPUT: {plaintext}")
    assert plaintext == CHECK
    print("SUCCESS!\n\n")

def exercise_4():
    # get the directory of the current file to compute
    # the path to the data file
    file_dir = os.path.dirname(os.path.realpath(__file__))
    input_file = file_dir + "/data/1.4.txt"
    CHECK = "Now that the party is jumping\n"

    prob_statement = """~~~SET 1 EXERCISE 4: Detect single-character XOR~~~

    One of the 60-character strings in ./data/1.4.txt has been encrypted by
    single-character XOR.

    Find it.
    """

    print(prob_statement)

    print("Reading data file")
    with open(input_file, 'r') as f:
        data = [l.strip() for l in f.readlines()]

    print("Computing most likely plaintext for each line")
    possibles = []
    for line in data:
        bytestr = bytes.fromhex(line)
        possibles.append(crack.single_byte_xor(bytestr)[1])

    print("Picking a winner from the winners of each line")
    possibles = [(p, measure.english_frequency_score(p)) for p in possibles]
    possibles.sort(key=lambda x: x[1], reverse = True)

    winner = possibles[0][0].decode('utf-8')
    print(f"OUTPUT: {winner}")
    assert winner == CHECK
    print("SUCCESS!\n\n")

def exercise_5():
    INPUT = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    CHECK = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272" + \
            "a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

    prob_statement = """~~~SET 1 EXERCISE 5: Implement repeating-key XOR~~~

    Here is the opening stanza of an important work of the English language:

    Burning 'em, if you ain't quick and nimble
    I go crazy when I hear a cymbal

    Encrypt it, under the key "ICE", using repeating-key XOR.

    In repeating-key XOR, you'll sequentially apply each byte of the key;
    the first byte of plaintext will be XOR'd against I, the next C,
    the next E, then I again for the 4th byte, and so on.

    It should come out to:

    0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
    a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f

    Encrypt a bunch of stuff using your repeating-key XOR function.
    Encrypt your mail.  Encrypt your password file.  Your .sig file.
    Get a feel for it.  I promise, we aren't wasting your time with this.
    """

    print(prob_statement)

    bytestr = bytes([ord(c) for c in INPUT])
    ciphertext = encrypt.byte_key_xor(bytestr, b'ICE').hex()

    print(f"OUTPUT: {ciphertext[:75]}")
    print(f"        {ciphertext[75:]}")
    print(f"ANSWER: {CHECK[:75]}")
    print(f"        {CHECK[75:]}")
    assert ciphertext == CHECK
    print("SUCCESS!\n\n")

def exercise_6():
    file_dir = os.path.dirname(os.path.realpath(__file__))
    input_file = file_dir + "/data/1.6.txt"

    prob_statement = """~~~SET 1 EXERCISE 6: Break repeating-key XOR~~~
    There is a file at ./data/1.6.txt.  It's been base64'd after being encrypted
    with repeating-key XOR.

    Decrypt it.
    """

    print(prob_statement)

    print("Reading data file")

    with open(input_file, 'r') as f:
        data = ''.join([l.strip() for l in f.readlines()])
    data = bytes.fromhex(convert.hex_from_64(data))
    key, plaintext = crack.repeating_key_xor(data)
    key = key.decode('utf-8')
    plaintext = plaintext.decode('utf-8')

    print(f"KEY: {key}")
    print(f"PLAINTEXT:\n{plaintext}")
    assert key == "Terminator X: Bring the noise"
    print("SUCCESS!\n\n")

def exercise_7():
    file_dir = os.path.dirname(os.path.realpath(__file__))
    input_file = file_dir + "/data/1.7.txt"

    prob_statement = """~~~SET 1 EXERCISE 7: AES in ECB mode~~~
    The base64-encoded content in ./data/1.7.txt has been encrypted via
    AES-128 in ECB mode under the key

    "YELLOW SUBMARINE".

    Decrypt it.  You know the  key, after all.
    """

    print(prob_statement)

    print("Reading data file")

    with open(input_file, 'r') as f:
        data = ''.join([l.strip() for l in f.readlines()])
    data = bytes.fromhex(convert.hex_from_64(data))
    key = b'YELLOW SUBMARINE'
    plaintext = decrypt.aes_ecb(data, key).decode('utf-8')

    print(f"PLAINTEXT:\n{plaintext}")
    assert plaintext.split('\n')[0] == "I'm back and I'm ringin' the bell "
    print("SUCCESS!\n\n")

def exercise_8():
    file_dir = os.path.dirname(os.path.realpath(__file__))
    input_file = file_dir + "/data/1.8.txt"

    prob_statement = """~~~SET 1 EXERCISE 8: Detect AES in ECB mode~~~
    In ./data/1.8.txt are a bunch of hex-encoded ciphertexts.

    One of them has been encrypted with ECB.

    Detect it.

    Remember that the problem with ECB is that it is stateless and deterministic;
    the same 16 byte plaintext block will always produce the same 16 byte
    ciphertext.
    """

    print(prob_statement)

    print("Reading data file")

    with open(input_file, 'r') as f:
        inputs = [l.strip() for l in f.readlines()]
    repeats = []
    for i, data in enumerate(inputs):
        ct = bytes.fromhex(data)
        cb = list(utils.list_blocks(ct, 16))
        cs = set(cb)
        repeats.append((i, cb, len(cb) - len(cs)))
    repeats.sort(key=lambda x: x[2], reverse=True)
    print("MOST REPETITIVE LINE:\n{}".format(
        '\n'.join([bytes.hex(b) for b in repeats[0][1]])
        ))
    assert repeats[0][0] == 132
    print("SUCCESS!\n\n")


if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7()
    exercise_8()
