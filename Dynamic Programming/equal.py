//here i don't know why we take only upto min-5
t= int(input())
for ti in range(t):
    to = int(input())
    n = input().split(' ')
    n = [int(i) for i in n]
    li = []
    mi = min(n)
    for j in range(mi-4,mi+1):
        total = 0;
        for i in range(to):
            x = n[i] - j
            total += x//5 +(x%5)//2 + (x%5)%2 
        li.append(total)
    print(min(li))
    
