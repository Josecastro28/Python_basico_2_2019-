# Escriba un código en python que determine cual grupo de personas contiene la mayor de todas las alturas de todas las personas


grupo_1 = [177,145,167,190,140,150,180,130]
suma = grupo_1[0] + grupo_1[1] + grupo_1[2] + grupo_1[3] + grupo_1[4] + grupo_1[5] + grupo_1[6] + grupo_1[7]
promedio_1 = suma / 8

grupo_2 = [165,176,145,189,170,189,159,190]
suma = grupo_2[0] + grupo_2[1] + grupo_2[2] + grupo_2[3] + grupo_2[4] + grupo_2[5] + grupo_2[6] + grupo_2[7]
promedio_2 = suma / 8

grupo_3 = [145,136,178,200,123,145,145,134]
suma = grupo_3[0] + grupo_3[1] + grupo_3[2] + grupo_3[3] + grupo_3[4] + grupo_3[5] + grupo_3[6] + grupo_3[7]
promedio_3 = suma / 8

grupo_4 = [201,110,187,175,156,165,156,135]
suma = grupo_4[0] + grupo_4[1] + grupo_4[2] + grupo_4[3] + grupo_4[4] + grupo_4[5] + grupo_4[6] + grupo_4[7]
promedio_4 = suma / 8


print('El promedio de altuta del grupo 1 es',promedio_1)
print('El promedio de altuta del grupo 2 es',promedio_2)
print('El promedio de altuta del grupo 3 es',promedio_3)
print('El promedio de altuta del grupo 4 es',promedio_4)

grupo_1 = promedio_1
grupo_2 = promedio_2
grupo_3 = promedio_3
grupo_4 = promedio_4

Lista_alturas_promedio = [grupo_1, grupo_2, grupo_3, grupo_4]
mayor = max(Lista_alturas_promedio)

if mayor ==grupo_1:
    print('El grupo con la mayor altura es el grupo 1 y la altura es', grupo_1)
if mayor ==grupo_2:
    print('El grupo con la mayor altura es el grupo 2 y la altura es', grupo_2)
if mayor ==grupo_3:
    print('El grupo con la mayor altura es el grupo 3 y la altura es', grupo_3)
if mayor ==grupo_4:
    print('El grupo con la mayor altura es el grupo 4 y la altura es', grupo_4)









