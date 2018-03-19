q = int(input())
s1 = []
s2 = []
for _ in range(q):
    query = [int(i) for i in input().split(" ")]
    if query[0] == 1:
        s1.append(query[1])
    elif query[0] == 2:
        if len(s2) > 0:
            s2.pop()
        else:
            for i in range(len(s1)):
                ele = s1.pop()
                s2.append(ele)
            s2.pop()
    elif query[0] == 3:
        if len(s2) > 0:
            print(s2[-1])
        else:
            print(s1[0])