#!/bin/python3

import sys

n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]
t1 = 0;
t2 = 0;
t3 = 0;
for i in range(1,max(n1,n2,n3)+1):
    if i < n1+1:
        t1 += h1[-i]
        h1[-i] = t1
    if i < n2+1:
        t2 += h2[-i]
        h2[-i] = t2
    if i < n3+1:
        t3 += h3[-i]
        h3[-i] = t3
op = 0
mi = min(n1,n2,n3)
for i in range(mi):
    if(mi == n1 and h1[i] in h2 and h1[i] in h3):                
        op = h1[i]
        break;
    if(mi == n2 and h2[i] in h1 and h2[i] in h3):
        op = h2[i]
        break;
    if(mi == n3 and h3[i] in h2 and h3[i] in h1):
        op = h3[i]
        break;
    
print(op)
--------------------------------------------------------------------------------------------



#!/bin/python3

import sys

sz = [int(i) for i in input().strip().split(' ')]
n1 = [int(A_temp) for A_temp in input().strip().split(' ')]
n2 = [int(A_temp) for A_temp in input().strip().split(' ')]
n3 = [int(A_temp) for A_temp in input().strip().split(' ')]

n = [n1, n2, n3]
h = [sum(i) for i in n]
while h[0] != h[1] or h[1] != h[2]:
    i = h.index(max(h))
    h[i] -= n[i].pop(0)
print(h[0])


