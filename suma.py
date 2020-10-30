suma = 0
lista = []

print('\nPodaj liczby - wpisz "q" aby zakonczyc:')
while True:
    wartosc1 = input()
    if wartosc1 == 'q':
        break
    else:
        wartosc1 = int(wartosc1)
        suma += wartosc1
        lista.append(suma)

for suma in lista:
    print(suma)