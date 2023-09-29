import practice

def test_absolute_difference():
    a = 7
    b = 8
    expected = 1
    actual = int(practice.absolute_difference(a, b))
    assert actual == expected

def test_absolute_difference2():
    x = 9
    y = 5
    expected = 4
    actual = int(practice.absolute_difference(x, y))
    assert actual == expected

def test_absolute_difference3():
    c = 1
    d = 9
    expected = 8
    actual = int(practice.absolute_difference(c, d))
    assert actual == expected

if __name__ == "__main__":
    test_absolute_difference()