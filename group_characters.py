def is_upper(character):
    code = ord(character)
    return code >= 65 and code <= 90

def is_lower(character):
   code = ord(character)
   return code >= 97 and code <= 122
    
def is_digit(character):
    return '0' <= character <= '9' 

def group_characters(string):
    upper = ""
    lower = ""
    digit = ""
    for each_char in string:
        if is_digit(each_char):
            digit += each_char
        elif is_lower(each_char):
            lower += each_char
        elif is_upper(each_char):
            upper += each_char
    complete_string = digit + lower + upper
    return complete_string

def main():
    while True:
        x = input("enter a string consisting of only letters and digits: ")
        if x == "":
            break
        complete_string = group_characters(x)
        print(complete_string)
if __name__ == "__main__":
    main()