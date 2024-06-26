N = 5
Lista = ['a', 'z', 'w', 'y', 'n']
i = 0

while i < N:
    Menor = i
    j = i + 1
    while j < N:
        if Lista[j] < Lista[Menor]:
            Menor = j
        j += 1

    Lista[i], Lista[Menor] = Lista[Menor], Lista[i]
    i += 1

print("Lista ordenada:", Lista)

