sample=['esp1', 'esp2', 'esp1', 'esp3', 'esp1', 'esp1', 'esp3', 'esp2', 'esp2', 'esp1', 'esp3']
abondance=[]
R=7 #ratio Vtot/Vobs
V=100 #volume de l'échantillon en mL

n=len(sample)
for i in range (n):
    a=True
    for j in range (len(abondance)):
        if sample[i]==abondance[j][0]:
            abondance[j][1]+=1
            a=False
    if a :
        abondance.append([sample[i],1])
abondance.append(['total',n])

for i in range (len(abondance)):
        abondance[i][1]*=(R/V)

print (abondance)


## dimensions manquantes
#entrer les dimensions moyennes présentes dans l'annexe
dim1=2
dim2=5
dim3=3

#entrer les dimensions mesurées, entrer False si pas de valeurs
d1=False
d2=10
d3=False

dimensions_moyennes=[dim1, dim2,dim3]
dimensions_mesurees=[d1, d2, d3]


dim=[]
if not dimensions_mesurees[0]:
    if not dimensions_mesurees[1]:
        r=dimensions_mesurees[2]/dimensions_moyennes[2]
    elif not dimensions_mesurees[2]:
        r=dimensions_mesurees[1]/dimensions_moyennes[1]
    else :
        r=(dimensions_mesurees[2]/dimensions_moyennes[2]+dimensions_mesurees[1]/dimensions_moyennes[1])/2
elif not dimensions_mesurees[1]:
    if not dimensions_mesurees[2]:
        r=dimensions_mesurees[0]/dimensions_moyennes[0]
    else :
        r=(dimensions_mesurees[2]/dimensions_moyennes[2]+dimensions_mesurees[0]/dimensions_moyennes[0])/2
else :
    r=(dimensions_mesurees[0]/dimensions_moyennes[0]+dimensions_mesurees[1]/dimensions_moyennes[1])/2
for i in range (3):
    if not dimensions_mesurees[i]:
        dim.append(r*dimensions_moyennes[i])
    else :
        dim.append(dimensions_mesurees[i])

print (dim)



