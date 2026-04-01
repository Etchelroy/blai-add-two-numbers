import sys
from main import add_numbers

def test_add_positive_numbers():
    assert add_numbers(2, 3) == 5
    print("✓ test_add_positive_numbers passed")

def test_add_negative_numbers():
    assert add_numbers(-5, -3) == -8
    print("✓ test_add_negative_numbers passed")

def test_add_floats():
    assert add_numbers(1.5, 2.3) == 3.8
    print("✓ test_add_floats passed")

if __name__ == "__main__":
    test_add_positive_numbers()
    test_add_negative_numbers()
    test_add_floats()
    print("\nAll tests passed!")