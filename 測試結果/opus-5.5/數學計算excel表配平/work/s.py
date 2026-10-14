from itertools import product
P=[5*i for i in range(1,25)]
def reach(n):  # amounts n*p+b, b in 0..2 -> dict amount->(p,b)
    d={}
    if n==0: return {0:(0,0)}
    for p in P:
        for b in (0,1,2):
            d.setdefault(n*p+b,(p,b))
    return d
R={n:reach(n) for n in range(0,60)}
# Scenario S1: planA 24 boxes split: x,y,z to planB 11/14/18 tickets, o stays planA, rest q to 計畫C
res=[]
for x in range(0,4):
 for y in range(0,4-x):
  for z in range(0,4-x-y):
   k=x+y+z
   A,B,C=R[22+x],R[21+y],R[25+z]
   # planB sum 8112
   sols=[]
   for a in A:
     for b in B:
       c=8112-a-b
       if c in C: sols.append((a,b,c))
   if not sols: continue
   rest=10582-8112; nb=24-k
   # option: o boxes stay planA (amount<=1030), q=nb-o to 計畫C
   for o in range(0,nb+1):
     q=nb-o
     for ao in R[o]:
       if ao>1030: continue
       aq=rest-ao
       if aq in R[q] and (o>0 or ao==0) and (q>0 or aq==0):
         res.append((k,x,y,z,o,ao,R[o][ao],q,aq,R[q][aq],sols[0],len(sols)))
res.sort()
for r in res[:40]: print(r)
print(len(res))
