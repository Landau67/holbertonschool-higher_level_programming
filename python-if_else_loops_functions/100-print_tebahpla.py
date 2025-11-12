#!/usr/bin/python3
print("".join(chr(ord('z') - i) if i % 2 == 0 else chr(ord('Y') - (i - 1)) for i in range(26)), end="")
