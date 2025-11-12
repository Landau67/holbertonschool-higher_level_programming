#!/usr/bin/python3
for i in range(26):
    if i % 2 == 0:
        a=chr(ord('z') - i)
    else:
        a=chr(ord('Y') - (i - 1))
    print(a,end="")
