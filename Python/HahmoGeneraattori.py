import random

a=0
x=0
strength=0
dexterity=0
constitution=0
intelligence=0
wisdom=0
charisma=0
ominaisuus=[strength, dexterity, constitution, intelligence, wisdom, charisma]
rotu=["Human", "Elf", "Dwarf"]
hahmo=["Warrior", "Wizard","Priest","Rogue"]
while x<6:
    for i in range(3):
        a=random.randint(1,6)
        ominaisuus[x]+=a
    x+=1
    b=random.choice(hahmo)
    c=random.choice(rotu)
print("hahmo:",b)
print("rotu:",c)
print("Strength:",ominaisuus[0])
print("Dexterity:",ominaisuus[1])
print("Constitution:",ominaisuus[2])
print("Intelligence:",ominaisuus[3])
print("Wisdom:",ominaisuus[4])
print("Charisma:",ominaisuus[5])
