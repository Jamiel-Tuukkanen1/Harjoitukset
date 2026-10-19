print("--- KULUSEURANTA ---")
lista=[]
hintalista=[]
summa=0
while True:
    print("1. Lisaa kulu")
    print("2. Nayta kulut")
    print("3. Nayta tilasto")
    print("4. Lopeta sovellus")
    luku=input()
    if luku=="1":
        nimi=str(input("Nimi: "))
        hinta=float(input("Hinta: "))
        hintalista.append(hinta)
        summa+=hinta
        sana=nimi+" "+str(hinta)
        lista.append(sana)
    if luku=="2":
        for i in lista:
            print(i)
    if luku=="3":
        hintalista.sort()
        print("Kokonaiskulu",summa)
        print("Pienin kulu", hintalista[0])
        print("Suurin kulu", hintalista[-1])
    if luku=="4":
        break
