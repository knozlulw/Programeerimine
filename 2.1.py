# juku


# nimi = input("sisesta eesnimi: ")

# if nimi.lower() == "juku":
#     print("lähme jukuga kinno!")
#     if nimi.isupper():
#         print("ära karju, juku!")

#     vanus_str = input("sisesta juku vanus: ")
#     if vanus_str.isdigit():
#         vanus = int(vanus_str)
#         if vanus < 0 or vanus > 100:
#             print("viga andmetes!")
#         elif vanus < 6:
#             print("tasuta pilet")
#         elif vanus <= 14:
#             print("lastepilet")
#         elif vanus <= 65:
#             print("täispilet")
#         else:
#             print("sooduspilet")
#     else:
#         print("vanus peab olema täisarv!")
# else:
#     print("täna kinno ei minda.")


# #Pinginaabrid

# nimi1 = input("Sisesta esimene nimi: ")
# nimi2 = input("Sisesta teine nimi: ")

# if not nimi1.isalpha() or not nimi2.isalpha():
#     print("Viga: nimed peavad koosnema ainult tähtedest!")
# else:
#     if nimi1.capitalize()[0] == nimi2.capitalize()[0]:
#         print(f"{nimi1.capitalize()} ja {nimi2.capitalize()} on täna pinginaabrid!")
#     else:
#         print(f"{nimi1.capitalize()} ja {nimi2.capitalize()} ei ole täna pinginaabrid.")

# # remont
# pikkus = float(input("Sisesta toa pikkus (m): "))
# laius = float(input("Sisesta toa laius (m): "))

# pindala = pikkus * laius
# print(f"Põranda pindala {round(pindala, 2)}")

# remont = input("Kas soovid remonti teha? (jah/ei): ").lower()

# if remont == "jah":
#     hind = float(input("Sisesta ruutmeetri hind (€): "))
#     koguhind = pindala * hind
#     print(f"Remondi hind: {round(koguhind, 2)} €")

#     ise = input("Kas teed remondi ise? (jah/ei): ").lower()
#     if ise == "ei":
#         toohind = float(input("Sisesta töö hind ruutmeetri kohta (€): "))
#         kokku = pindala * (hind + toohind)
#         print(f"Remondi koguhind koos tööga: {round(kokku, 2)} €")
#     else:
#         print("Head õnnestust!")
# else:
#     print("Remondist loobutud.")


# # allahindlus

# alghind = float(input("Sisesta toote alghind (€): "))

# if alghind > 700:
#     loplik_hind = alghind * 0.70
#     print(f"Lõplik hind: {round(lopik_hind, 2)} €")
# else:
#     print(f"Lõplik hind: {round(alghind, 2)} €")   


# # temperatuur

# try:
#     temp = float(input("Sisesta toatemperatuur (C): "))
#     if temp > 18:
#         print(f"Temperatuur on {temp} C: üle soovitatava!")
#     else:
#         print(f"Temperatuur on {temp} C: toasoojus on korras.")
# except ValueError:
#     print("Viga: sisesta arv!")

# # pikkus

# # Piirid:
# # lühike:  < 160 cm
# # keskmine: 160–180 cm
# # pikk:    > 180 cm


# try:
#     pikkus = float(input("Sisesta pikkus (cm): "))

#     if pikkus < 160:
#         print(f"Pikkus lühike")
#     elif pikkus <= 180:
#         print(f"Pikkus keskmine")
#     else:
#         print(f"Pikkus pikk")   
# except ValueError:
#     print("sisesta number")





# Piirid:
# Naised: lühike < 155, keskmine 155–170, pikk > 170
# Mehed:  lühike < 165, keskmine 165–185, pikk > 185

# import random


# sugu = input("Sisesta sugu (mees/naine): ").lower()
# pikkus = float(input("Sisesta pikkus (cm): "))

# if sugu == "mees":
#     print("Sugu: mees")
#     if pikkus < 165:
#         print(f"Pikkus lühike")
#     elif pikkus <= 185:
#         print(f"Pikkus keskmine")
#     else:
#         print(f"Pikkus pikk")
# elif sugu == "naine":
#     print("Sugu: naine")
#     if pikkus < 155:
#         print(f"Pikkus lühike")
#     elif pikkus <= 170:
#         print(f"Pikkus keskmine")
#     else:
#         print(f"Pikkus pikk")
# else:
#     print("sisesta sugu kui mees või naine!")



#pood
import random

piim = random.randint(1, 4)
sai = random.randint(1, 4)
leib = random.randint(1, 4)

table = {"piim", "sai", "leib"}
#print(table)


valik = input(f'Sisesta toode mis tahad osta (piim "{piim}$", sai "{sai}$", leib "{leib}$")')

if valik == "piim" or valik == "sai" or valik == "leib":
    kogus = input(f'Valisid: "{valik}", Vali kogus: ')

    if kogus.isdigit():
        kogus = int(kogus)
        hind = locals()[valik]
        print(f'Ostsid "{valik}" koguses "{kogus}", läks maksma "{hind * kogus}$"')
        table.remove(valik)
        #print(table)

    veel = input(f'Kas soovid veel midagi osta ("{table}", ei)?')

    if veel == "ei":
        print("ei soovi")

    if veel in table:
        #print("on")

        kogus = input(f'Valisid: "{veel}", Vali kogus: ')

        if kogus.isdigit():
            kogus = int(kogus)
            hind = locals()[valik]
            print(f'Ostsid "{valik}" koguses "{kogus}", läks maksma "{hind * kogus}$"')
            table.remove(veel)
            #print(table)


    veel = input(f'Kas soovid veel midagi osta ("{table}", ei)?')

    if veel == "ei":
        print("ei soovi")

    if veel in table:
        print("on")

        kogus = input(f'Valisid: "{veel}", Vali kogus: ')

        if kogus.isdigit():
            kogus = int(kogus)
            hind = locals()[valik]
            print(f'Ostsid "{valik}" koguses "{kogus}", läks maksma "{hind * kogus}$"')
            table.remove(veel)
            #print(table)

           





    #if veel == "jah":
