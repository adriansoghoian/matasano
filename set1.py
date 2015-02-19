

def hex_to_base64(string):
    return string.decode('hex').encode('base64').rstrip()


def fixed_xor(string1, string2):    
    output = ""
    for char1, char2 in zip(string1.decode('hex'), string2.decode('hex')):
        output += chr(ord(char1) ^ ord(char2))

    return output


def char_frequency(string1, is_hex=True):
    """
    Returns most frequent character in a hex encoded string.
    """
    if is_hex: string1 = string1.decode('hex')
    chars = list(string1)
    freq = []

    for char in set(chars):
        freq.append((char, chars.count(char)))

    return sorted(freq, key=lambda char: char[1], reverse=True)[0]


def single_char_xor(string, char, is_hex=True):
    """
    XORs a single character against a hex-encoded string.
    """
    result = ""
    if is_hex: string = string.decode('hex')

    for letter in string:
        result += chr(ord(letter) ^ ord(char))

    return result


def problem_4(file_path):
    strings = []
    freqs = []
    with open(file_path, 'rb') as f:
        for line in f:
            strings.append(line.rstrip())

    for each in strings:
        freq_char = char_frequency(each, is_hex=False) # Tuple of: (most common char, char count)
        freqs.append((each, freq_char[0], freq_char[1])) # Triple of: (string, most common char, char count)

    candidate = sorted(freqs, key=lambda triple: triple[2], reverse=True)[0]
    return single_char_xor(candidate[0], candidate[1])


def repeating_xor(plaintext, xor_keys):
    """
    Repeating key xor with a single character.
    """
    pass




if __name__ == "__main__":
    ### Problem 1
    input_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    output_str = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    print hex_to_base64(input_str) == output_str
    print "*"*25

    ### Problem 2
    input_str1 = "1c0111001f010100061a024b53535009181c"
    input_str2 = "686974207468652062756c6c277320657965"
    output_str = "746865206b696420646f6e277420706c6179"
    print fixed_xor(input_str1, input_str2)
    print "*"*25

    ## Problem 3
    input_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    freq_char = char_frequency(input_str)[0]
    print single_char_xor(input_str, freq_char)
    print "*"*25

    ## Problem 4
    print problem_4("text/set1_problem4.txt")

    ## Problem 5
    ptxt = "Burning 'em, if you ain't quick and nimble \nI go crazy when I hear a cymbal"
    desired_ctxt = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"





