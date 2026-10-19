teksti=str(input("Anna teksti: "))
a=0
b=0
c=0
pituus=0
sanamaara=0
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
    yleisin_s=yleisin_s[b+1:]
    if sana in yleisin_s:
        sanamaara+=1

while c!=-1:
    c=pisin_s.find(" ")
    pisinsana=pisin_s[:c]
    if len(pisinsana)>pituus:
        pituus=len(pisinsana)
    pisin_s=pisin_s[c+1:]


print("Sanojen maara:",maara)
print("Rivien maara:",maara-1)
print("Yleisin sana",sanamaara)
print("Pisin sana",pituus)
