# test_usha1.py

from usha1 import USHA1
import hashlib

def test_vector(msg):
    expected = hashlib.sha256(msg.encode()).hexdigest()
    actual = USHA1(msg).hexdigest()
    assert expected == actual, f"Mismatch for message: {msg}"

def run_tests():
    test_vector("")
    test_vector("a")
    test_vector("abc")
    test_vector("hello world")
    test_vector("The quick brown fox jumps over the lazy dog")
    print("✅ All tests passed!")

if __name__ == "__main__":
    run_tests()
