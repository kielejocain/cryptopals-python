from cryptolib.convert import hex_to_64

def exercise_1():
    INPUT = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    CHECK = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    prob_statement = """SET 1 EXERCISE 1: CONVERT HEX TO BASE64

    The string
    {input}

    should produce
    {output}.
    """.format(input=INPUT, output=CHECK)

    print(prob_statement)

    assert hex_to_64(INPUT) == CHECK

    print("The assertion held.")


if __name__ == "__main__":
    exercise_1()
