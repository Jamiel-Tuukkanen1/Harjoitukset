lista=["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
lista1=[1,2,3,4,5,6,7,8,9,0]
lista2=["!","@","#","£","¤","$","%","&","/","=","?","+","€",";",",",":",".","_","-"]
vahvuus=0
salasana=input("Laita salasana: ")

if len(salasana)>=8:
    vahvuus+=1
for i in lista1:
    numero=salasana.find(str(i))
    if numero!=-1:
        vahvuus+=1
        break
for i in lista:
    a=salasana.find(i)
    if a!=-1:
        vahvuus+=1
        break
for i in lista2:
    merkki=salasana.find(i)
    if merkki!=-1:
        vahvuus+=1
        break
if vahvuus==4:
    print("Erinomainen")
elif vahvuus==3:
    print("Hyva")
elif vahvuus==2:
    print("Kohtalainen")
else:
    print("Heikko")
