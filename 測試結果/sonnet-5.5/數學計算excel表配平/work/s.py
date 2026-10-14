import itertools
# data check
opt=[11799,7148,7148,2875,2641,4084]; print(sum(opt),sum(opt[:3])+2875-0, 35695-5695)
dr=[4084,7148,7148,7148,2520,110,2311,2520,480,3360]; print(sum(dr), 36829+171)
planC=[1258,1634,3324,2284,3360,4037,4084,3480,39801,2799,5126,4880,5417,1701,55,240,320,320,720,600,720,552,552,552,828,698,1225]
print(sum(planC), 90567+7433)
# planB tickets
orig=(22,21,25); T=8112
units=range(60,121,5)
best=[]
for dn in itertools.product(range(orig[0]-3,orig[0]+4),range(orig[1]-3,orig[1]+4),range(orig[2]-3,orig[2]+4)):
    cost=sum(abs(a-b) for a,b in zip(dn,orig))
    if cost>4: continue
    for us in itertools.product(units,repeat=3):
        base=sum(n*u for n,u in zip(dn,us))
        for bs in itertools.product((0,1,2),repeat=3):
            tot=base+sum(bs)
            if tot<=T:
                best.append((T-tot,cost,sum(dn),dn,us,bs))
best.sort(key=lambda x:(x[0],x[1]))
print("exact:",[b for b in best if b[0]==0][:15])
print("cost0 best:",[b for b in best if b[1]==0][:5])
print([b for b in best if b[0]==0 and b[1]<=2 and b[2]==68][:20])
