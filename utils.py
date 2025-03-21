# utils.py

def to_bits(data: bytes) -> str:
    """Convert bytes to a binary string."""
    return ''.join(f'{byte:08b}' for byte in data)

def print_chunk(chunk: bytes):
    """Nicely print a 64-byte SHA block as 16 32-bit words."""
    if len(chunk) != 64:
        raise ValueError("Chunk must be exactly 64 bytes.")
    print("---- SHA Block (512 bits) ----")
    for i in range(0, 64, 4):
        word = chunk[i:i+4]
        print(f"Word {i//4:02}: {int.from_bytes(word, 'big'):08x}")
    print("-----------------------------")

def hex_dump(data: bytes):
    """Print a hex dump of the data."""
    for i in range(0, len(data), 16):
        line = ' '.join(f'{byte:02x}' for byte in data[i:i+16])
        print(f"{i:04x}: {line}")
