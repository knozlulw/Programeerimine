# if lause
try:
    x = int(input("Sisesta arv: "))
    if x > 0:
        print("Positiivne arv")
        print("See rida on ka if-i sees")
    print("See rida täidetakse alati")
except ValueError:
    print("Palun sisesta kehtiv täisarv.")

# if..else lause

try:
    x = int(input("Sisesta arv: "))
    if x == 1:
        print("Õige")
    else:
        print("Vale")
except ValueError:
    print("Palun sisesta kehtiv täisarv.")

#tingimised
vastus = input("Kas soovid jätkata? (jah/ei) ")
if vastus.lower() == "jah":
    print("Jätkame!")
else:
    print("Head aega!")