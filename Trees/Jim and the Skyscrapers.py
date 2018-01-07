N = int(input())
h = [int(i) for i in input().split()]
count = 0

s = [] #stack
for i in range(0,N):
    while len(s) > 0 and s[-1][0] < h[i]:
        s.pop()
    if len(s) > 0 and s[-1][0] == h[i]:
        count += s[-1][1]
        s[-1][1] += 1
    else:
        s.append([h[i],1])
print(2*count)

#
# Take Out ----
# 
# when you have increasing and decreasing elements use stack
# 
