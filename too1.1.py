
# Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
# Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.

# Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:

# “Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”

from random import Random


print("Tere, maailm!")

nimi=input("Sisesta oma nimi: ")
print("Tere, maailm! Tervitan sind", nimi)
vanus=input("Sisesta oma vanus: ")
print("Tere, maailm! Tervitan sind", nimi, "! Sa oled", vanus, "aastat vana.")



#Mis tüüpi on järgnevad muutujad:

#a) vanus = 18 - int
#b) eesnimi = "Jaak" - str
#c) pikkus = 16.5 - float
#d) kas_käib_koolis = True - bool
#Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
#Kirjuta kood tüüpide kontrollimiseks.

vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True 

print(f"Muutuja: {vanus}, tüüp {type(vanus)}")
print(f"Muutuja: {eesnimi}, tüüp {type(eesnimi)}")
print(f"Muutuja: {pikkus}, tüüp {type(pikkus)}")
print(f"Muutuja: {kas_käib_koolis}, tüüp {type(kas_käib_koolis)}")


#Kirjuta enda koodis laual olevate kommide arv muutujasse(kommide arv on juhuslik). 
#Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
#Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta. 
#Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile, kui palju komme laual nüüd on.
from random import randint
kommid = randint(10, 50)
print(f"Mitu kommi tahad võtta, laual on {kommid} kommi")
soov = int(input("Mitu kommi võtad? => "))
kommid -= soov
print(f"Laual on nüüd {kommid} kommi.")