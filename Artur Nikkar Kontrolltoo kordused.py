# 1
n = int(input("Sisesta arv (1-9): "))

for i in range(n):
    print("  ^")
    print(" / /")
    print(" \\ \\")
    print("  / /")
    print("  __")
    print()

# 2
t = int(input("Mitu sõpra tuli restorani: "))
sisse = 0

for i in range(t):
    vanus = int(input("Sisesta vanus: "))
    if vanus > 16:
        sisse = sisse + 1

print("Õhtusöögile pääseb", sisse, "sõpra")

# 3
x = int(input("Mitu sportlast saabus: "))

poisid = 0
tydrukud = 0

for i in range(x):
    sugu = input("Sisesta sugu (p - poiss, t - tüdruk): ")
    if sugu == "p":
        poisid = poisid + 1
    elif sugu == "t":
        tydrukud = tydrukud + 1

kokku = poisid + tydrukud

toad = kokku // 2
if kokku % 2 != 0:
    toad = toad + 1

print("Poisse:", poisid)
print("Tüdrukuid:", tydrukud)
print("Tube on vaja:", toad)

#4
kaal = float(input("Sisesta kaal (kg): "))
pikkus = float(input("Sisesta pikkus (m): "))
vanus = int(input("Sisesta vanus: "))

bmi = kaal / (pikkus * pikkus)

print("Sinu BMI on:", bmi)

if bmi < 18.5:
    print("Alakaal")
elif bmi < 25:
    print("Normaalkaal")
elif bmi < 30:
    print("Ülekaal")
else:
    print("Rasvumine")

# 5
n = int(input("Mitu isikukoodi sisestatakse: "))

mehed = 0
naised = 0

for i in range(n):
    isikukood = input("Sisesta isikukood: ")

    if len(isikukood) == 11:
        if isikukood[0] == "1" or isikukood[0] == "3" or isikukood[0] == "5":
            mehed = mehed + 1
        elif isikukood[0] == "2" or isikukood[0] == "4" or isikukood[0] == "6":
            naised = naised + 1
    else:
        print("Vigane isikukood")

print("Mehi:", mehed)
print("Naisi:", naised)
