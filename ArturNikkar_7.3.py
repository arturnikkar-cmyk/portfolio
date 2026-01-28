import random
import os

# 1. failide nimed
k_fail = "kusimused_vastused.txt"
o_fail = "oiged.txt"
v_fail = "valed.txt"
k_fail_k = "koik.txt"
t_fail = "testitud.txt"

# 2. kusimuste lugemine
def loe_kusimused():
    kus = []
    vas = []
    try:
        with open(k_fail, 'r', encoding='utf-8') as f:
            for rida in f:
                rida = rida.strip()
                if ':' in rida:
                    osad = rida.split(':', 1)
                    kus.append(osad[0].strip())
                    vas.append(osad[1].strip())
    except:
        kus = ["Mis on Python?", "Mis värvi on lumi?"]
        vas = ["programmeerimiskeel", "valge"]
        with open(k_fail, 'w', encoding='utf-8') as f:
            for k, v in zip(kus, vas):
                f.write(f"{k}:{v}\n")
    return kus, vas

# 3. testitud inimeste lugemine
def loe_testitud():
    testitud = set()
    try:
        with open(t_fail, 'r', encoding='utf-8') as f:
            for rida in f:
                testitud.add(rida.strip().lower())
    except:
        pass
    return testitud

# 4. email genereerimine
def teema_email(nimi):
    osad = nimi.split()
    if len(osad) >= 2:
        return f"{osad[0].lower()}.{osad[-1].lower()}@example.com"
    else:
        return f"{nimi.lower().replace(' ', '')}@example.com"

# 5. kusimuste lisamine
def lisa_kusimus(kus, vas):
    print("\nUue küsimuse lisamine")
    uus_k = input("Uus küsimus: ").strip()
    uus_v = input("Õige vastus: ").strip()
    if uus_k and uus_v:
        with open(k_fail, 'a', encoding='utf-8') as f:
            f.write(f"\n{uus_k}:{uus_v}")
        kus.append(uus_k)
        vas.append(uus_v)
        print("Küsimus lisatud")
    return kus, vas

# 6. uks kusitlus
def tee_test(kus, vas, testitud, tulemused):
    nimi = input("Sisesta nimi: ").strip()
    if not nimi:
        return False
    
    if nimi.lower() in testitud:
        print("Juba testitud")
        return False
    
    email = teema_email(nimi)
    print(f"Email: {email}")
    
    # mitu kusimust
    kogus = len(kus)
    if kogus < 2:
        print("Liiga vähe küsimusi")
        return False
    
    N = random.randint(2, min(4, kogus))
    
    # vali kusimused
    valitud_idx = random.sample(range(kogus), N)
    
    oiged = 0
    print(f"\nTere, {nimi}! {N} küsimust:")
    
    for i, idx in enumerate(valitud_idx, 1):
        print(f"\n{i}. {kus[idx]}")
        vastus = input("Vastus: ").strip().lower()
        if vastus == vas[idx].lower():
            oiged += 1
    
    edukas = oiged > N / 2
    print(f"\nTulemus: {oiged}/{N}")
    print("Õnnestus" if edukas else "Ei õnnestunud")
    
    # lisa tulemused
    tulemused.append((nimi, oiged, email, edukas))
    
    # salvesta koik.txt
    with open(k_fail_k, 'a', encoding='utf-8') as f:
        f.write(f"{nimi},{oiged},{email},{edukas}\n")
    
    # lisa testituks
    testitud.add(nimi.lower())
    
    # emaili teade (simuleerime)
    print(f"Email saadetud: {email}")
    
    return True

# 7. tulemuste salvestamine
def salvesta_tulemused(tulemused):
    # oiged.txt
    edukad = [r for r in tulemused if r[3]]
    edukad.sort(key=lambda x: x[1], reverse=True)
    with open(o_fail, 'w', encoding='utf-8') as f:
        for n, o, e, _ in edukad:
            f.write(f"{n} - {o} õigesti\n")
    
    # valed.txt
    eba = [r for r in tulemused if not r[3]]
    eba.sort(key=lambda x: x[0])
    with open(v_fail, 'w', encoding='utf-8') as f:
        for n, o, e, _ in eba:
            f.write(f"{n} - {o} õigesti\n")

# 8. tooandja aruanne
def saada_aruanne(tulemused):
    if not tulemused:
        return
    
    # sort
    sorted_t = sorted(tulemused, key=lambda x: x[1], reverse=True)
    
    # tee sisu
    sisu = "Tere!\n\nTulemused:\n\n"
    for i, (n, o, e, ed) in enumerate(sorted_t, 1):
        olek = "SOBIS" if ed else "EI SOBI"
        sisu += f"{i}. {n} - {o} - {e} - {olek}\n"
    
    # parim
    if sorted_t:
        parim_n, parim_o, _, _ = sorted_t[0]
        sisu += f"\nParim: {parim_n} ({parim_o})\n"
    
    # saada (simuleerime)
    print("\nSaadetud aruanne tööandjale")
    print(sisu)

# 9. peamine programm
def main():
    kus, vas = loe_kusimused()
    testitud = loe_testitud()
    tulemused = []
    
    # kustuta vana koik.txt
    if os.path.exists(k_fail_k):
        os.remove(k_fail_k)
    
    print("Küsimustiku programm")
    print(f"Küsimusi: {len(kus)}")
    
    while True:
        print("\nValikud:")
        print("1. Alusta küsimustikku")
        print("2. Lisa küsimus")
        print("3. Välju")
        
        valik = input("Vali: ")
        
        if valik == "1":
            # testime 3 inimest
            for i in range(3):
                print(f"\nInimene {i+1}/3")
                while not tee_test(kus, vas, testitud, tulemused):
                    pass
            
            # salvesta tulemused
            if tulemused:
                salvesta_tulemused(tulemused)
                saada_aruanne(tulemused)
            
            # kuva tulemused ekraanil
            print("\nTulemused:")
            edukad = [r for r in tulemused if r[3]]
            for n, o, _, _ in sorted(edukad, key=lambda x: x[1], reverse=True):
                print(f"  {n} - {o}")
            
            print("Emailid saadetud")
            
            # salvesta testitud
            with open(t_fail, 'w', encoding='utf-8') as f:
                for n in testitud:
                    f.write(f"{n}\n")
            
            # reset sessiooniks
            tulemused = []
        
        elif valik == "2":
            kus, vas = lisa_kusimus(kus, vas)
        
        elif valik == "3":
            print("Väljun")
            break
        
        else:
            print("Vale valik")

if __name__ == "__main__":
    main()