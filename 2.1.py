# juku

nimi = input("Sisesta eesnimi: ")

if nimi.lower() == "juku":
    print("Lähme Jukuga kinno!")
    if nimi.isupper():
        print("Ära karju, Juku!")

    vanus_str = input("Sisesta Juku vanus: ")
    if vanus_str.isdigit():
        vanus = int(vanus_str)
        if vanus < 0 or vanus > 100:
            print("Viga andmetes!")
        elif vanus < 6:
            print("Tasuta pilet")
        elif vanus <= 14:
            print("Lastepilet")
        elif vanus <= 65:
            print("Täispilet")
        else:
            print("Sooduspilet")
    else:
        print("Vanus peab olema täisarv!")
else:
    print("Täna kinno ei minda.")


#Pinginaabrid

nimi1 = input("Sisesta esimene nimi: ")
nimi2 = input("Sisesta teine nimi: ")

if not nimi1.isalpha() or not nimi2.isalpha():
    print("Viga: nimed peavad koosnema ainult tähtedest!")
else:
    if nimi1.capitalize()[0] == nimi2.capitalize()[0]:
        print(f"{nimi1.capitalize()} ja {nimi2.capitalize()} on täna pinginaabrid!")
    else:
        print(f"{nimi1.capitalize()} ja {nimi2.capitalize()} ei ole täna pinginaabrid.")

# remont
pikkus = float(input("Sisesta toa pikkus (m): "))
laius = float(input("Sisesta toa laius (m): "))

pindala = pikkus * laius
print(f"Põranda pindala {round(pindala, 2)}")

remont = input("Kas soovid remonti teha? (jah/ei): ").lower()

if remont == "jah":
    hind = float(input("Sisesta ruutmeetri hind (€): "))
    koguhind = pindala * hind
    print(f"Remondi hind: {round(koguhind, 2)} €")

    ise = input("Kas teed remondi ise? (jah/ei): ").lower()
    if ise == "ei":
        toohind = float(input("Sisesta töö hind ruutmeetri kohta (€): "))
        kokku = pindala * (hind + toohind)
        print(f"Remondi koguhind koos tööga: {round(kokku, 2)} €")
    else:
        print("Head õnnestust!")
else:
    print("Remondist loobutud.")


# allahindlus

alghind = float(input("Sisesta toote alghind (€): "))

if alghind > 700:
    loplik_hind = alghind * 0.70
    print(f"Lõplik hind: {round(lopik_hind, 2)} €")
else:
    print(f"Lõplik hind: {round(alghind, 2)} €")   


# temperatuur

try:
    temp = float(input("Sisesta toatemperatuur (°C): "))
    if temp > 18:
        print(f"Temperatuur on {temp} °C — üle soovitatava!")
    else:
        print(f"Temperatuur on {temp} °C — toasoojus on korras.")
except ValueError:
    print("Viga: sisesta arv!")

# pikkus

# Piirid:
# lühike:  < 160 cm
# keskmine: 160–180 cm
# pikk:    > 180 cm

pikkus = float(input("Sisesta pikkus (cm): "))

if pikkus < 160:
    print(f"Pikkus {pikkus} cm — lühike")
elif pikkus <= 180:
    print(f"Pikkus {pikkus} cm — keskmine")
else:
    print(f"Pikkus {pikkus} cm — pikk")   

# pikkus ja sugu

# Piirid:
# Naised: lühike < 155, keskmine 155–170, pikk > 170
# Mehed:  lühike < 165, keskmine 165–185, pikk > 185

sugu = input("Sisesta sugu (mehes/naine): ").lower()
pikkus = float(input("Sisesta pikkus (cm): "))

if sugu == "m" or sugu == "mehes":
    print("Sugu: mees")
    if pikkus < 165:
        print(f"Pikkus {pikkus} cm — lühike")
    elif pikkus <= 185:
        print(f"Pikkus {pikkus} cm — keskmine")
    else:
        print(f"Pikkus {pikkus} cm — pikk")
elif sugu == "n" or sugu == "naine":
    print("Sugu: naine")
    if pikkus < 155:
        print(f"Pikkus {pikkus} cm — lühike")
    elif pikkus <= 170:
        print(f"Pikkus {pikkus} cm — keskmine")
    else:
        print(f"Pikkus {pikkus} cm — pikk")
else:
    print("Viga: sisesta sugu kui 'mehes' või 'naine'!") 


# poes

import random

tooted = [
    ("Piim", round(random.uniform(0.5, 3), 2)),
    ("Sai", round(random.uniform(0.5, 3), 2)),
    ("Leib", round(random.uniform(0.5, 3), 2)),
    ("Muna", round(random.uniform(0.5, 3), 2)),
    ("Juust", round(random.uniform(0.5, 3), 2)),
]

ostud = []

for nimi, hind in tooted:
    print(f"\n{nimi} — {hind} €")
    ostab = input(f"Kas soovid {nimi.lower()}t osta? (jah/ei): ").lower()
    if ostab == "jah":
        kogus_str = input("Kogus: ")
        if kogus_str.isdigit():
            kogus = int(kogus_str)
            if kogus > 0:
                summa = round(hind * kogus, 2)
                ostud.append((nimi, hind, kogus, summa))
            else:
                print("Kogus peab olema positiivne!")
        else:
            print("Kogus peab olema täisarv!")

print("\n" + "=" * 30)
print(f"{'TSEKK':^30}")
print("=" * 30)

kogusumma = 0
for nimi, hind, kogus, summa in ostud:
    print(f"{nimi:<10} {kogus} x {hind:.2f} € = {summa:.2f} €")
    kogusumma += summa

print("-" * 30)
print(f"{"KOGUSUMMA":<19} {kogusumma:.2f} €")
print("=" * 30)

if not ostud:
    print("Ostu ei tehtud.")   