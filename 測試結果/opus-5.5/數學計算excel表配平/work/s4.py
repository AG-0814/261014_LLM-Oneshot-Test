P=[5*i for i in range(1,25)]
def reach(n):
    d={}
    if n<=0: return {0:(0,0)} if n==0 else {}
    for p in P:
        for b in (0,1,2): d.setdefault(n*p+b,(p,b))
    return d
R={n:reach(n) for n in range(0,80)}
best={}
for n1 in range(10,40):
 for n2 in range(10,40):
  for n3 in range(10,40):
   M=n1+n2+n3
   if not (68<=M<=71): continue
   for a in R[n1]:
     for b in R[n2]:
       c0=8106-a-b
       for c in range(c0+1,8113-a-b):
         if c in R[n3]:
           s=a+b+c; best.setdefault(s,[]).append((n1,n2,n3,M))
for s in sorted(best): print(s, best[s][:6], len(best[s]))
