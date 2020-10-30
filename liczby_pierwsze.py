def liczba_pierwsza(liczba):
    if liczba == 0 or liczba == 1:
        print('nie')
        liczba += 1
        return
    for i in range(liczba):
        if i == 0 or i == 1:
            continue
        elif liczba % i == 0:
            return print('nie')
    print('tak')

for warotsc in range(1,5):
    liczba_pierwsza(warotsc)