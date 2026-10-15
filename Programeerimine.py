print("ma õpin", 1, "kursusel")
print("Aasta on", 2026)

kursus = 1
aasta = 2026

print("ma õpin", kursus, "kursusel")
print("aasta on", aasta)

print("aastal", aasta+1, "olen juba", kursus+1, "kursus")
print("2026", "10", "1", sep="/")
print("Sama ", end="")
print("rida")



nimi=input("Sisesta oma nimi: ")
print("Tere",nimi,"!")



a = int(input("essa arv: "))
b = int(input("teine arv: "))
print(a, "+", b, "=", a + b)
print(a, "-", b, "=", a - b)
print(a, "*", b, "=", a * b)



hind = 19.9
kogus = 3
print(f"Kokku: {hind + kogus:.2f} eurot")



import math

print("Pii väärtus:", math.pi)
print("√16 =", math.sqrt(16))
print("sin(π/2) =", math.sin(math.pi / 2))
print("sin(30°) =", round(math.sin(math.radians(30)), 2))
print("5! =", math.factorial(5))