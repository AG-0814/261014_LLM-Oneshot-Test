P=[5*i for i in range(1,25)]
def reach(n):
    d={}
    if n==0: return {0:(0,0)}
    for p in P:
        for b in (0,1,2): d.setdefault(n*p+b,(p,b))
    return d
R={n:reach(n) for n in range(0,80)}
TOT=10582
out=[]
for x in range(0,12):
 for y in range(0,12-x):
  for z in range(0,12-x-y):
   k=x+y+z
   if k>24: continue
   A,B,C=R[22+x],R[21+y],R[25+z]
   Ds={}
   for a in A:
     for b in B:
       for c in C:
         s=a+b+c
         if 8050<=s<=8112 and s not in Ds: Ds[s]=(a,b,c)
   nb=24-k
   for D in sorted(Ds,reverse=True):
     rest=TOT-D
     found=None
     for o in range(0,nb+1):
       q=nb-o
       for ao,(po,bo) in R[o].items():
         if ao>1030: continue
         aq=rest-ao
         if aq in R[q]:
           found=(o,ao,(po,bo),q,aq,R[q][aq]); break
       if found: break
     if found:
       out.append((8112-D,k,(x,y,z),Ds[D],found)); break
out.sort()
for r in out[:25]: print(r)
