# Makefile

test:
	python test_usha1.py

run:
	python examples/hash_text.py

bench:
	python benchmarks.py

hashfile:
	python examples/hash_file.py example.txt
