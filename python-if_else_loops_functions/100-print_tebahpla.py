#!/usr/bin/python3
for i in range(26):
    if i % 2 == 0:
        print(chr(ord('z') - i), end="")
    else:
        print(chr(ord('Y') - (i - 1)), end="")
