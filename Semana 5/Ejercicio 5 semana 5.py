class Animal:

    def __init__(self, e,a):
        self.especie = e
        self.edad = a

    def correr (self):
        print("soy un {}."
              "Estory corriendo".format(self.especie))

    def crecer (self, edad = 0):
        if (self.edad + edad) > 14:
            self.vivo = False
        else:
            self.edad += edad
            self.vivo = True

perro = Animal ("perro",3)
print( "Hola soy un {}"
       "tengo {} años".format(perro.especie,
                              perro.edad))
perro.crecer(10)

print( "Hola soy un {}"
       "tengo {} años".format(perro.especie,
                              perro.edad))

perro.crecer(2)

if perro.vivo:
    print("Hola soy un {}"
          "tengo {} años".format(perro.especie,
                                 perro.edad))
else:
    print("ME MORI....RIP")

perro.crecer(-10)

if perro.vivo:
    print("Hola soy un {}"
          "tengo {} años".format(perro.especie,
                                 perro.edad))
else:
    print("ME MORI....RIP")



