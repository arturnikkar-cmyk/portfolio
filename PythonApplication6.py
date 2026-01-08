import os

def loe_failist(failinimi: str) -> list:
    """loeb faili ja tagastab selle sisu listina"""

    if not failinimi.endswith(".txt"):
        failinimi += ".txt"
    print("Python töökaust:", os.getcwd())
    print("Otsitav fail:", failinimi)

    loend = []
    try:
        with open(failinimi, "r", encoding="utf-8") as f:
            for rida in f:
                loend.append(rida.strip())
    except FileNotFoundError:
        print("❌ Faili ei leitud selles kaustas!")
    return loend


def kirjuta_faili(failinimi: str, loend: list):
    """kirjutab listi sisu faili"""

    if not failinimi.endswith(".txt"):
        failinimi += ".txt"

    reziim = input("kas soovid üle kirjutada -w- või lisada -a- ")
    with open(failinimi, reziim, encoding="utf-8") as f:
        for rida in loend:
            f.write(rida + "\n")


failinimi = input("sisesta failinimi ilma laiendita: ")
päevad = loe_failist(failinimi)

print("\nFaili sisu read on:")
for rida in päevad:
    print(rida)

print("\nFaili sisu listina:")
print(päevad)

nimekiri = []
for i in range(5):
    nimi = input(f"sisesta {i+1}. nimi: ")
    nimekiri.append(nimi)

failinimi = input("sisesta faili nimi ilma laiendita, kuhu nimed salvestada: ")
kirjuta_faili(failinimi, nimekiri)
