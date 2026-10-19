print("--- TUOTEHALLINTA ---")
lista=[]
listahinta=[]
numero=1
maara=0
kokohinta=0
while True:
    print("1. Listaa tuotteet")
    print("2. Lisaa tuote")
    print("3. Poista tuote")
    print("4. Nayta varaston kokonaisarvo")
    print("0. Lopeta")
    luku=input("Valitse toiminto: ")
    if luku=="1":
        for i in lista:
            print(i)
    if luku=="2":
        tuote=str(input("Tuotteen nimi: "))
        hinta=float(input("Tuotteen hinta: "))
        kokohinta+=hinta
        listahinta.append(hinta)
        kokotuote=tuote+" "+str(hinta)
        lista.append(kokotuote)
        maara+=1
    if luku=="3":
        for i in lista:
            print(numero,i)
            numero+=1
        poisto=int(input("Poista tuote numeron avulla: "))
        lista.pop(poisto-1)
        maara-=1
        kokohinta-=listahinta[poisto-1]
        listahinta.pop(poisto-1)
        numero=1
    if luku=="4":
        print("Tuotteiden maara:",maara)
        print("Kokonaishinta",kokohinta)
    if luku=="0":
        break
