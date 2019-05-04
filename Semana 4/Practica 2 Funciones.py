#Crear una funcion que agrega contactos a la agenda

def agregar_contacto (Nombre, Telefono, Correo):

    agenda.update ({Nombre:
                        {"Telefono": Telefono,
                         "Correo": Correo}])

    agenda [Nombre] = {"telefono": Telefono,
                       "Correo",Correo}

    agregar_contacto (Nombre = "felipe",
                      Telefono=5555,
                      Correo="Felipe@gmail.com")




