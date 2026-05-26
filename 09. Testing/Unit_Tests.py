""" Exercise 1: Function that veryfies if a number is even. """
def is_even(nr):
    if nr%2==0:
        return True
    else:
        return False

if __name__ == "__main__":
    nr = int(input("Number:"))
    print(is_even(nr))

# Testing the function
def test_positive_even():
    assert is_even(4) == True

def test_positive_odd():
    assert is_even(3) == False

def test_zero():
    assert is_even(0) == True

def test_negative_even():
    assert is_even(-42) == True

def test_negative_odd():
    assert is_even(-17) == False


