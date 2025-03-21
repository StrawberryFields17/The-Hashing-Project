# benchmarks.py

import time
import hashlib
from usha1 import USHA1

def benchmark(func, name, input_data, loops=5):
    durations = []
    for _ in range(loops):
        start = time.time()
        func(input_data)
        durations.append(time.time() - start)
    avg_time = sum(durations) / loops
    print(f"{name:>15}: {avg_time:.6f} sec (avg over {loops} runs)")

def main():
    input_text = "The quick brown fox jumps over the lazy dog" * 10000

    benchmark(lambda d: USHA1(d).hexdigest(), "USHA-1", input_text)
    benchmark(lambda d: hashlib.sha256(d.encode()).hexdigest(), "hashlib", input_text)

if __name__ == "__main__":
    main()
