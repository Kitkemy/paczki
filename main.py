import sys
liczba_elementow = int(sys.argv[1])

numer_paczki = 1
waga_paczki = 0
waga_elementu = 0
wyslane_kg = 0
puste_kg = 0
max_puste_kg = 0
nr_paczki_puste_kg = 0

for element in range(liczba_elementow):
    waga_elementu = int(input("podaj wage elementu: "))
    if waga_elementu == 0:
        break
    elif waga_elementu < 0 or waga_elementu > 10:
        print("nieprawidłowa waga elementu!")
        break
    else:
        if waga_paczki + waga_elementu <= 20:
           waga_paczki += waga_elementu
           wyslane_kg += waga_elementu           
        else:
            numer_paczki += 1
            if 20 - wyslane_kg >= max_puste_kg:
                max_puste_kg = 20 - wyslane_kg                            
            wyslane_kg += waga_elementu
            waga_paczki = waga_elementu
    
nr_paczki_puste_kg = numer_paczki
puste_kg = numer_paczki * 20 - wyslane_kg
      
print("******************************************")
print(f"liczba wysłanych paczek: {numer_paczki}")        
print(f"liczba wysłanych kg: {wyslane_kg}")
print(f"suma pustych kg: {puste_kg}")
print(f"najwięcej pustych kg miała paczka: {nr_paczki_puste_kg}")        