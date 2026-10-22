import math # PARANDATUD: "import * from math" asemel on korrektne "import math"

print("Ruudu karakteristikud")
a = float(input('Sisesta ruudu külje pikkus => ')) # PARANDATUD: input() tekst arvuks float(), et saaks arvutada
S = a**2
print("Ruudu pindala", S)
P = 4 * a
print("Ruudu ümbermõõt", P) # PARANDATUD: vigased jutumärgid '' korrektsega "
di = a * math.sqrt(2) # PARANDATUD: math.sqr(2) asemel on funktsioon math.sqrt(2)
print("Ruudu diagonaal", round(di, 2))
print()

print("Ristküliku karakteristikud") # PARANDATUD: reo lõpust eemaldatud üks liigne sulg ))
b = float(input("Sisesta ristküliku 1. külje pikkus => ")) # PARANDATUD: lisatud float() tüübiteisendus
c = float(input("Sisesta ristküliku 2. külje pikkus => ")) # PARANDATUD: lisatud float() tüübiteisendus
S = b * c
print('Ristküliku pindala', S) # PARANDATUD: puuduv algusjutumärk lisatud teksti 'Ristküliku pindala' ette
P = 2 * (b + c) # PARANDATUD: lisatud puuduv korrutusmärk * sulgude ette
print("Ristküliku ümbermõõt", P)
di = math.sqrt(b**2 + c**2) # PARANDATUD: b*2 ja c*2 (mis on korrutamine) asendatud b**2 ja c**2
print("Ristküliku diagonaal", round(di, 2)) # PARANDATUD: lisatud rea lõpust puuduv sulg ) ning ümardamise täpsus
print()

print("Ringi karakteristikud")
r = float(input('Sisesta ringi raadiusi pikkus => ')) # PARANDATUD: eemaldatud vigased topeltjutumärgid '' ja liigsed sulud )) ning lisatud float()
d = 2 * r # PARANDATUD: lisatud puuduv korrutusmärk * muutuja r ette
print("Ringi läbimõõt", d) # PARANDATUD: lisatud puuduv koma teksti ja muutuja d vahele
S = math.pi * r**2 # PARANDATUD: pi() asendatud math.pi-ga ning r*2 (korrutamine) asendatud raadiuse ruutu võtmisega r**2
print("Ringi pindala", round(S, 2)) # PARANDATUD: lisatud rea lõpust puuduv sulg )
C = 2 * math.pi * r # PARANDATUD: 2pi() asendatud korrektse matemaatilise tehtega 2 * math.pi
print("Ringjoone pikkus", round(C, 2)) # PARANDATUD: lisatud rea lõpust puuduv sulg )
