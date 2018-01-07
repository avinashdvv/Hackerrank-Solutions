"""
    Intial soltuion below,
    it pretty much easy but only qualifies only 6 TestCases
"""
t = int(input())
for _ in range(t):
    n = int(input())
    points = input().split(" ")
    people = input().split(" ")
    points = [int(i) for i in points]
    people = [int(i) for i in people]
    op = 0
    for i in range(n-1):
        for j in range(i+1,n):
            data = max(people[i],people[j]) * abs(points[i] - points[j]) 
            op += data
    print(op % 1000000007)

"""
    
    Test case 1:
    1
    3
    1 3 6
    10 20 30

"""


class Fenwick_tree: #Binary Indexed Tree
    def __init__(self, n):
        sz = 1
        while n >= sz:
            sz *= 2
        self.size = sz
        self.data = [0]*sz
 
    def sum(self, i):
        if i <= 0: return 0
        s = 0
        while i >= 0:
            s += self.data[i]
            i = (i & (i+1)) - 1
        return s

    def sumrange(self,lo,hi):
        return self.sum(hi-1) - self.sum(lo-1) 
 
    def add(self, i, x):
        assert i > 0
        while i < self.size:
            self.data[i] += x
            i |= i + 1

def get_lookup(arr):
    value_to_idx,idx_to_value = {},{}
    arr.sort()
    idx = 1
    for i in arr:
        if i not in value_to_idx:
            value_to_idx[i] = idx
            idx_to_value[idx] = i
            idx += 1
    return (value_to_idx,idx_to_value)
            
mod = 10**9+7
for case in range(int(input())):
    N = int(input())
    C = list(map(int,input().split())) #x-coord
    P = list(map(int,input().split())) #population
    arr = list(sorted((c,p) for p,c in zip(P,C)))
    # [(1, 10), (3, 20), (6, 30)]
    cvi,civ = get_lookup(C)
    # {1: 1, 3: 2, 6: 3} {1: 1, 2: 3, 3: 6}
    pvi,piv = get_lookup(P)
    # {10: 1, 20: 2, 30: 3} {1: 10, 2: 20, 3: 30}
    tpd,tpn = Fenwick_tree(N+1),Fenwick_tree(N+1)
    tpdp,tpp = Fenwick_tree(N+1),Fenwick_tree(N+1)
    #[0, 0, 0, 0, 0, 0, 0, 0] [0, 0, 0, 0, 0, 0, 0, 0]
    #[0, 0, 0, 0, 0, 0, 0, 0] [0, 0, 0, 0, 0, 0, 0, 0]

    ans = 0
    for c,p in arr:
        ci,pi = cvi[c],pvi[p]
        #1 1
        #
        
        #get number of cities with fewer or equal people
        num_cit = tpn.sum(pi)
        #0
        
        #get sum distances with fewer or equal people
        sum_cit = tpd.sum(pi)
        #0 
        
        ans = (ans + (num_cit*c-sum_cit) * p) % mod
        #0 
        
        #get sum distances*population with more people
        sumprod_cit = tpdp.sumrange(pi+1,N+1)
        #0 
        
        #get sum population with more people
        sum_pop = tpp.sumrange(pi+1,N+1)
        #0
        ans = (ans + sum_pop*c - sumprod_cit) % mod
        #0 
        
        tpn.add(pi,1)
        #[0, 1, 0, 1, 0, 0, 0, 1]
        tpd.add(pi,c)
        #[0, 1, 0, 1, 0, 0, 0, 1]
        tpdp.add(pi,c*p)
        #[0, 10, 0, 10, 0, 0, 0, 10]
        tpp.add(pi,p)
        #[0, 10, 0, 10, 0, 0, 0, 10]
        
    print(ans)