import random

def create_ascii_range_string(start, stop):
    result = ""
    for n in range(start, stop, 1):
        result += chr(n)
    return result

def create_uppercase_letters_string():
    return create_ascii_range_string(65, 91)

def create_lowercase_letters_string():
    return create_ascii_range_string(97, 123)

def create_digits_string():
    return create_ascii_range_string(48, 58)

def create_symbols_string():
    all_symbols = [(33, 48), (58, 65), (91, 97), (123, 127)]
    symbols = ""
    for start, stop in all_symbols:
        symbols += create_ascii_range_string(start, stop)
    return symbols

def get_random_char_from_string(single_string):
    if not single_string:
        return None
    random1 = random.random()
    int_and_length = int(random1 * len(single_string))
    random_char = single_string[int_and_length]
    return random_char 

def generate_random_password(upper, lower, digits, symbols):
    upper = create_uppercase_letters_string()
    lower = create_lowercase_letters_string()
    digits = create_digits_string()
    symbols = create_symbols_string()

    password = ""

    password += get_random_char_from_string(upper)
    password += get_random_char_from_string(lower)
    password += get_random_char_from_string(digits)
    password += get_random_char_from_string(symbols)

    return password

def main():
    prompt = input("Enter numbers for: [upper] [lower] [digits] [symbols] amounts: ")
    while True:
        if not prompt:
            print("Invalid")
            break
        prompt_length = prompt.split()
        if len(prompt_length) != 4:
            print("error message, try again") 
            break
        else:
            if prompt = (upper, lower, digits, symbols)
            new_password = generate_random_password(upper, lower, digits, symbols)
        print(new_password)
    print(create_ascii_range_string(97, 100))
    print(create_uppercase_letters_string())
    print(create_lowercase_letters_string())
    print(create_digits_string())
    print(create_symbols_string())
    print(get_random_char_from_string('abc'))
    print(generate_random_password('ABC', 'abc', '123', '!@#'))
if __name__ == "__main__":
    main()

