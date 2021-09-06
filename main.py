import sys
liczba_elementow = int(sys.argv[1])

numer_paczki = 1
waga_paczki = 0
waga_elementu = 0
puste_kg = 0

for element in range(liczba_elementow):
    waga_elementu = int(input("podaj wage elementu: "))
    if waga_elementu == 0:
        break
    elif waga_elementu < 0 and waga_elementu > 10:
        print("nieprawidłowa waga elementu!")
    else:
        if waga_paczki + waga_elementu <= 20:
           waga_paczki += waga_elementu
        else:
            numer_paczki += 1

            waga_paczki = waga_elementu

print(numer_paczki, waga_paczki)
        