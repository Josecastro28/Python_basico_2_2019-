# Hacer un codigo que me diga cuantos elementos voy a comprar

verduras = ["tomate", "papas", "cebollas", "ajos"]
frutas = ["piña", "naraja", "sandia"]
carnes = ["mortadel", "pollo", "costilla de cerdo"]
limpieza = ["javon", "cloro", "shampoo"]

lista_de_compras = []
lista_de_compras.append (verduras)
lista_de_compras.append (frutas)
lista_de_compras.append (carnes)
lista_de_compras.append (limpieza)


for categoria in lista_de_compras:
    print(categoria, type(categoria))

mi_lista= []

for categoria in lista_de_compras:
    mi_lista.extend(categoria)

print(len(mi_lista))

pass

