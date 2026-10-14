P=[5*i for i in range(1,25)]
def reach(n):
    d={}
    for p in P[::-1]:
        for b in (0,1,2): d.setdefault(n*p+b,(p,b))
    return d
R={n:reach(n) for n in range(1,40)}; R[0]={0:(0,0)}
print("rest 2476/21:")
for o in range(0,22):
    for ao,(po,bo) in R[o].items():
        if ao<=1030 and 2476-ao in R[21-o]: print(o,po,bo,ao,21-o,R[21-o][2476-ao],2476-ao)
print("planB 7941 combos:")
for a,(pa,ba) in R[22].items():
  for b,(pb,bb) in R[21].items():
    c=7941-a-b
    if c in R[25]: print((22,pa,ba,a),(21,pb,bb,b),(25,)+R[25][c]+(c,))
print("planB 8061 combos:")
for a,(pa,ba) in R[22].items():
  for b,(pb,bb) in R[21].items():
    c=8061-a-b
    if c in R[25]: print((22,pa,ba,a),(21,pb,bb,b),(25,)+R[25][c]+(c,))
print("rest 2521/24:")
for o in range(0,25):
    for ao,(po,bo) in R[o].items():
        if ao<=1030 and 2521-ao in R[24-o]: print(o,po,bo,ao,24-o,R[24-o][2521-ao],2521-ao)
