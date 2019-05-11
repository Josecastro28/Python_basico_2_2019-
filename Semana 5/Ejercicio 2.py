# El numero mas grande sin max  [1,2,7,1,9,2]

lista1 = [1,2,7,1,9,2]

def mayor_lista_1(lista1):
    mayor = lista[0]
    for valor in lista1:
        if valor > mayor:
            mayor = valor
    return mayor

print mayor_lista_1(lista1)
