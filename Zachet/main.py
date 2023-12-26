# bilet 8

#zadanie pervoe

def rasschet():
    Znachenie = int(input("Vvedi x dlya resheniya formuli: "))
    print(2 * Znachenie ** 2 + 15)
#
rasschet()

# zadanie vtoroe

def proverka():
    Chislo = int(input("Vvedi chislo dlya proverki: "))
    if Chislo % 6 == 0:
        print("chislo kratno 6")
    else:
        print("chislo ne kratno 6")

proverka()

# zadanie tretie

def diapozonchik():
    pe = int(input("Vvedi pervoe chislo contsa diapozona: "))
    ve = int(input("Vvedi vtoroe chislo nachala diapozona: "))
    for i in range(ve, pe + 1):
        print(i)

diapozonchik()