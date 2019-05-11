# Crear una clase "bebe"

# declarar cuatro acciones respirar comer llorar dormir
#Simular un dia normal de un bebe

class Bebe:

    def __init__(self, nombre,edad=0):
        self.bebe_nombre = nombre
        self.bebe_edad = edad

    def respirar (self):
        print("El Bebe respira")

    def comer (self):
        print("El bebe come")

    def llora(self):
        print("El bebe llora")

    def dormir(self):
        print("El bebe duerme")

    def crecer(self, edad=1):
        self.bebe_edad += edad
        print("Hola soy {}"
              " y tengo {} años ".format(self.bebe_nombre,
                                        self.bebe_edad))


pepe= Bebe("Pepe")
pepe.llora()
pepe.respirar()
pepe.llora()
pepe.comer()
pepe.llora()
pepe.llora()
pepe.dormir()

pepe.crecer(10)

