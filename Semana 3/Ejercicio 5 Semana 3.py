# Utilizando 1,2,4 eliminar verduras


verduras = ["tomate", "papas", "cebollas", "ajos"]
frutas = ["piña", "naraja", "sandia"]
carnes = ["mortadel", "pollo", "costilla de cerdo"]
limpieza = ["javon", "cloro", "shampoo"]

lista_de_compras = []
lista_de_compras.append (verduras)
lista_de_compras.append (frutas)
lista_de_compras.append (carnes)
lista_de_compras.append (limpieza)

verduras.append("chile")
frutas.append("mango")

#verduras.clear() , "Elimina el contenido de la variable"

#del verduras, "Elimina variable verduras"

#verduras = [], "Este no funciona"

del verduras [:], "Elimina el contenido de la variable"

print(lista_de_compras)

pass