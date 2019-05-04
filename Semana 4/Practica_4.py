#Inprima la informacion de cada contacto

agenda ={
    "Carlos Rojas" : {"telefono" : 87001030,
                      "correo" : "Crojas@hotmail.com"},
    "Juan Perez" : {"telefono" : 83013040,
                    "correo" : "jperez@gmail.com"},
    "ana Marin" : {"telefono" : 88978729,
                   "correo" : "Amarin@gmail.com"}
}

for persona in agenda.keys():
    print("nombre:", persona,
          "telefono:", agenda [persona] ["telefono"],
          "correo:", agenda [persona] ["correo"])

#Items

for persona, info in agenda.items():
    print("nombre:", persona,
          "telefono:", info ["telefono"],
          "correo:", info ["correo"])

    pass


