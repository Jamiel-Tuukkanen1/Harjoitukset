print("--- KULUSEURANTA ---")
lista=[1,5,3,9,6,2,1,5,0]
lista.sort
print(lista)
summa=0
while True:
    print("1. Lisaa kulu")
    print("2. Nayta kulut")
    print("3. Nayta tilasto")
    print("4. Lopeta sovellus")
    luku=input()
    if luku==1:
        nimi=str(input("Nimi"))
        hinta=float(input("Hinta"))
        summa=+hinta
        sana=nimi+str(hinta)
        lista.append(sana)
    if luku==2:
        for i in lista:
            print(i)
    if luku==3:
        print("Kokonaiskulu",summa)
        print("Pienin kulu", )
        print("Suurin kulu",)