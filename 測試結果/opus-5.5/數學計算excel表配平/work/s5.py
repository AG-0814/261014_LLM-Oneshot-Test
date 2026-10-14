P=[5*i for i in range(1,25)]
def reach(n):
    d={}
    if n<=0: return {0:(0,0)} if n==0 else {}
    for p in P:
        for b in (0,1,2): d.setdefault(n*p+b,(p,b))
    return d
R={n:reach(n) for n in range(0,80)}
own=(22,21,25); TOT=10582
def restok(nb,rest):
    outs=[]
    for o in range(0,nb+1):
        q=nb-o
        for ao,(po,bo) in R[o].items():
            if ao>1030: continue
            aq=rest-ao
            if aq in R[q]: outs.append((o,ao,po,bo,q,aq)+R[q][aq])
    return outs
res=[]
for n1 in range(15,30):
 for n2 in range(15,30):
  for n3 in range(15,32):
   k=n1+n2+n3-68
   if k!=0: continue
   ch=sum(max(0,o-n) for o,n in zip(own,(n1,n2,n3)))
   if ch>15: continue
   sols=[]
   for a,(pa,ba) in R[n1].items():
     for b,(pb,bb) in R[n2].items():
       c=8112-a-b
       if c in R[n3]: sols.append(((n1,pa,ba,a),(n2,pb,bb,b),(n3,)+R[n3][c]+(c,)))
   if not sols: continue
   r=restok(24-k,TOT-8112)
   if r: res.append((ch,k,(n1,n2,n3),len(sols),sols[:4],r[:3],len(r)))
res.sort(key=lambda t:(t[0],t[1]))
for x in res[:15]: print(x,"\n")
