# setup.py

from setuptools import setup

setup(
    name="usha1",
    version="0.1",
    description="Pure Python SHA-256 clone for educational use",
    author="Elementary-Penguin",
    py_modules=["usha1", "utils"],
    packages=["examples"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Security :: Cryptography",
        "License :: OSI Approved :: MIT License",
    ],
)
