import itertools

import cryptolib.convert as convert
import cryptolib.encrypt as encrypt
import cryptolib.measure as measure

def exercise_1():
    INPUT = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    CHECK = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    prob_statement = """~~~SET 1 EXERCISE 1: Convert hex to base64~~~

    The string
    {input}

    should produce
    {output}
    """.format(input=INPUT, output=CHECK)

    print(prob_statement)

    # run the exercise and allow the user to visually inspect
    output = convert.hex_to_64(INPUT)
    print("Here is the output, written above the desired output.")
    print(output)
    print(CHECK)

    # confirm the assertion
    assert output == CHECK
    print("SUCCESS!\n\n")

def exercise_2():
    INPUT1 = "1c0111001f010100061a024b53535009181c"
    INPUT2 = "686974207468652062756c6c277320657965"
    CHECK  = "746865206b696420646f6e277420706c6179"

    prob_statement = """~~~SET 1 EXERCISE 2: Fixed XOR~~~

    Write a function that takes two equal-length buffers and produces their XOR combination.

    If your function works properly, then when you feed it the string:
    {input1}

    ... after hex decoding, and when XOR'd against:
    {input2}

    ... should produce:
    {check}
    """.format(input1=INPUT1, input2=INPUT2, check=CHECK)

    print(prob_statement)

    # run the exercise and allow the user to visually inspect
    print("Here is the output, written above the desired output.")
    output = encrypt.hex_key_xor(INPUT1, INPUT2)
    print(output)
    print(CHECK)

    # confirm the assertion
    assert output == CHECK
    print("SUCCESS!\n\n")

def exercise_3():
    INPUT = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    CHECK = "Cooking MC's like a pound of bacon"

    prob_statement = """~~~SET 1 EXERCISE 3: Single-byte XOR cipher~~~

    The hex encoded string:
    {input}

    ... has been XOR'd against a single character.  Find the key, decrypt the message.
    """.format(input=INPUT)

    print(prob_statement)

    possibles = []
    for c1, c2 in itertools.product('0123456789abcdef', repeat = 2):
        key = chr((int(c1, 16) << 4) | int(c2, 16))
        out = convert.hex_to_ascii(encrypt.hex_key_xor(INPUT, c1+c2))
        score = measure.english_frequency_score(out)
        possibles.append((key, score, out))

    possibles.sort(key=lambda x: x[1], reverse = True)

    print("key: {}".format(possibles[0][0]))
    print("msg: {}".format(possibles[0][2]))

    assert possibles[0][2] == CHECK
    print("SUCCESS!\n\n")



if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
