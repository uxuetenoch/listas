def gap(lista, indice, gap):
    for indice_actual in range(indice + gap, len(lista), gap):
        valor = lista[indice_actual]
        posicion = indice_actual
        
        while posicion >= gap and lista[posicion - gap] > valor:
            lista[posicion] = lista[posicion - gap]
            posicion -= gap
        lista[posicion] = valor

def shell(lista): 
    sublistas = len(lista) // 2
    while sublistas > 0:
        for indice in range(sublistas):
            gap(lista, indice, sublistas)
        sublistas //= 2

lista = [5, 3, 2, 9, 8, 7, 1]
shell(lista)
print(lista)  
