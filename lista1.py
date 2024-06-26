lista = [['z', -1], ['a', 3], ['w', 0], ['d', 4], ['r', 2]]
t = 1

print("Elementos de la lista:")
ap = t
while ap != -1:
    rec = lista[ap]
    print(rec[0])
    ap = rec[1]

c = input("Ingrese un elemento: ")
ap = t
while ap != -1:
    rec = lista[ap]
    if rec[0] < c:
        print("Menor ", end="")
    elif rec[0] == c:
        print("Igual ", end="")
    else:
        print("Mayor ", end="")
    print(rec[0])

    if c < rec[0]:
        nuevo_nodo = [c, ap]
        if ap == t:
            p = len(lista)
        else:
            lista[ap_ant][1] = len(lista)
        lista.append(nuevo_nodo)
        break
    ap_ant = ap
    ap = rec[1]
    
print("Lista actualizada:")
ap = p
while ap != -1:
    rec = lista[ap]
    print(rec[0])
    ap = rec[1]
print(lista)

