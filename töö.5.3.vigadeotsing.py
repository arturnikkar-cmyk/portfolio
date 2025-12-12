from random import randint

def vahetus(a, b):
    # исправлено: раньше значения не менялись местами
    abi = a
    a = b
    b = abi
    return a, b


def generaator(n, loend, a, b):
    # исправлено: range(n) — раньше не было скобок
    for i in range(n):
        loend.append(randint(a, b))


def jagamine(loend, p, n, nol):
    # исправлено: "elif::" был неправильный синтаксис
    for el in loend:
        if el > 0:
            p.append(el)
        elif el < 0:
            n.append(el)
        else:
            nol.append(el)


def keskmine(loend):
    # исправлено: защита от пустого списка
    if len(loend) == 0:
        return 0

    summa = 0
    for i in loend:
        summa += i

    return round(summa / len(loend), 2)


def lisamine(loend, el):
    loend.append(el)
    loend.sort()  # исправлено: sort() был использован неверно


def arvud_loendis():
    print("Andmed:")

    #iga sisendi jaoks oma try-except
    while True:
        try:
            n = abs(int(input("Mitu täisarvu genereerime loendisse? => ")))
            break
        except:
            print("Ошибка: sisesta täisarv!")  

    while True:
        try:
            mini = int(input("Sisesta vahemiku minimaalne arv => "))
            break
        except:
            print("Ошибка: sisesta täisarv!")

    while True:
        try:
            maxi = int(input("Sisesta vahemiku maksimaalne arv => "))
            break
        except:
            print("Ошибка: sisesta täisarv!")

    #исправлено: если минимум >= максимум меняем местами
    if mini >= maxi:
        mini, maxi = vahetus(mini, maxi)

    s = []
    generaator(n, s, mini, maxi)

    print("\nTulemused:")
    print(f"Saadud loend vahemikus {mini} kuni {maxi} :", s)

    s.sort()
    print("Sorteeritud loend:", s)

    pos = []
    neg = []
    nol = []

    jagamine(s, pos, neg, nol)

    print("Positiivsed arvud:", pos)
    print("Negatiivsed arvud:", neg)
    print("Nullid:", nol)

    kesk_pos = keskmine(pos)
    lisamine(s, kesk_pos)
    print("Positiivsete keskmine:", kesk_pos)

    kesk_neg = keskmine(neg)
    lisamine(s, kesk_neg)
    print("Negatiivsete keskmine:", kesk_neg)

    print("\nLisame keskmised algsesse massiivi ja sorteerime:")
    print(s)




