# strict: planB counts 22,21,25 , amount exactly 7941 (no shift) reachable?
P=[5*i for i in range(1,25)]
R=lambda n:{n*p+b for p in P for b in (0,1,2)}
A,B,C=R(22),R(21),R(25)
print(sorted({a+b+c for a in A for b in B for c in C if 7900<=a+b+c<=7945}))
