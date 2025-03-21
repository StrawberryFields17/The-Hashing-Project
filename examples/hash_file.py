from usha1 import USHA1
import sys

def hash_file(path):
    with open(path, 'rb') as f:
        data = f.read()
    print("USHA-1 hash:", USHA1(data).hexdigest())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hash_file.py <filename>")
    else:
        hash_file(sys.argv[1])
