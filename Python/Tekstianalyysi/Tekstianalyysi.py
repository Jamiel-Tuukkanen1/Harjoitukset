teksti=str(input("Anna teksti: "))
a=0
b=0
c=0
x=0
o=0
sanamaara1=0
loop=0
lista=[]
pituus=0
sanamaara=1
sana=""
rivien_m=0
maara=0
sanojen_m=teksti
yleisin_s=teksti
pisin_s=teksti

while a!=-1:
    a=sanojen_m.find(" ")
    maara+=1
    sanojen_m=sanojen_m[a+1:]
rivien_m=maara-1

while b!=-1:
    b=yleisin_s.find(" ")
    sana=yleisin_s[:b]
    if "." in sana:
        sana=sana[:-1]
    if "," in sana:
        sana=sana[:-1]
    if b==-1:
        sana=sana+teksti[-1]
    yleisin_s=yleisin_s[b+1:]
    lista.append(sana)

lista2=lista
while loop<len(lista):
    o=0
    lista=lista2
    sana2=lista[x]
    for i in lista:
        if i==sana2:
            sanamaara+=1
    if sanamaara>sanamaara1:
        sanamaara1=sanamaara
        sanamaara=1
        sana3=sana2
    else:
        sanamaara=1
    x+=1
    loop+=1

while c!=-1:
    c=pisin_s.find(" ")
    pisinsana=pisin_s[:c]
    if "." in pisinsana:
        pisinsana=pisinsana[:-1]
    if "," in pisinsana:
        pisinsana=pisinsana[:-1]
    if c==-1:
        pisinsana=pisinsana+teksti[-1]
    if len(pisinsana)>pituus:
        pituus1=pisinsana
        pituus=len(pisinsana)
    pisin_s=pisin_s[c+1:]


print("Sanojen maara:",maara)
print("Rivien maara:",maara-1)
print("Yleisin sana:",sana3)
print("Pisin sana:",pituus1)