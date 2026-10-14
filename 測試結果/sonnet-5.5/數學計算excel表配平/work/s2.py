import itertools
orig=(22,21,25); T=8112
for lo in (100,80,60,5):
  units=range(lo,121,5); res=[]
  for dn in itertools.product(range(15,35),range(15,35),range(15,35)):
    cost=sum(abs(a-b) for a,b in zip(dn,orig))
    if cost>3: continue
    for us in itertools.product(units,repeat=3):
        base=sum(n*u for n,u in zip(dn,us))
        r=T-base
        if 0<=r<=6:
            for bs in itertools.product((0,1,2),repeat=3):
                if sum(bs)==r: res.append((cost,sum(dn),dn,us,bs))
  res.sort(); print(lo,len(res),res[:8])
