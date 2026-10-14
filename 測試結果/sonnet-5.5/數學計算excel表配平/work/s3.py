import itertools
orig=(22,21,25); T=8112
units=range(90,121,5); res=[]
for dn in itertools.product(range(15,35),range(15,35),range(15,35)):
    cost=sum(abs(a-b) for a,b in zip(dn,orig))
    if cost>6: continue
    for us in itertools.product(units,repeat=3):
        r=T-sum(n*u for n,u in zip(dn,us))
        if 0<=r<=6:
            for bs in itertools.product((0,1,2),repeat=3):
                if sum(bs)==r: res.append((cost,abs(sum(dn)-68),dn,us,bs))
res.sort()
seen=set()
for x in res:
    k=(x[0],x[2],x[3])
    if k in seen: continue
    seen.add(k); print(x)
    if len(seen)>25: break
