
def solve(H) :
    s,i,m = [],0,0
    while i < len(H):
        if not s or H[i] > H[s[-1]]:
            s.append(i)
            i += 1
        else:
            t = s.pop()
            a = H[t] * ((i - s[-1] - 1) if s else i)
            if a > m:
                m = a
    while s:
        t = s.pop()
        a = H[t] * ((i - s[-1] - 1) if s else i)
        if a>m:
            m = a
    return m
N = int(input())
H = list(int(_) for _ in input().split())

print(solve(H))
