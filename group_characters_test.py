import group_characters

def test_is_upper():
    code = "A"
    expected = True
    actual = group_characters.is_upper(code)
    assert (expected == actual)
    
def test_is_lower():
    code = "a"
    expected = True
    actual = group_characters.is_lower(code)
    assert (expected == actual)

def test_is_digit():
    character = "1"
    expected = True
    actual = group_characters.is_digit(character)
    assert (expected == actual)
    
def test_group_characters():
    complete_string = "123abcABC"
    expected = "123abcABC"
    actual = group_characters.group_characters(complete_string)
    assert (expected == actual)