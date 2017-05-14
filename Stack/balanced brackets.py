#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    s = input().strip()
    dict = {
        '}' : '{',
        ']' : '[',
        ')' : '(',
    }
    stack = []
    for i in s:
        if stack and dict.get(i) == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')

    
