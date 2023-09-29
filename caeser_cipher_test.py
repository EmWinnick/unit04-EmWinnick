import caesar_cipher

def test_ceasar_cipher():
    plaintext = "A"
    shifted = 3
    expected = "D"
    actual = caesar_cipher.encrypt_letter(plaintext, shifted)
    assert (expected == actual)

#I am not sure why A and D are not reporting as an undefined variable.
#I will have to fiddle with this more
#Oh I think I fixed it by adding quotes around the parameters

def test_is_alphabetic():
    letter = "a"
    expected = "true"
    actual = caesar_cipher.is_alphabetic(letter)
    assert (expected == actual)

def test_encrypt_letter_less_than_A():
    plaintext = "@"
    shift = None
    expected = ""
    actual = caesar_cipher.encrypt_letter(plaintext, shift)
    assert (expected == actual)

#run tests for each function - check slides to see how many times

def test_encrypt_letter_A_no_shift():
    