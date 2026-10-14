P=[5*i for i in range(1,25)]
def reach(n):
    d={}
    for p in P:
        for b in (0,1,2): d.setdefault(n*p+b,(p,b))
    return d
R={n:reach(n) for n in range(1,80)}
# planB 3 tickets with counts (n1,n2,n3), which totals <=8112 near reachable
for n1,n2,n3 in [(22,21,25),(23,21,25),(22,22,25),(22,21,26),(24,21,25),(23,22,25),(22,21,27),(25,21,25)]:
    best=set()
    for a in R[n1]:
        for b in R[n2]:
            for c in R[n3]:
                s=a+b+c
                if 8100<=s<=8112: best.add(s)
    print((n1,n2,n3),sorted(best))
