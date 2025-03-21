from usha1 import USHA1

text = input("Enter text to hash: ")
print("USHA-1 hash:", USHA1(text).hexdigest())
