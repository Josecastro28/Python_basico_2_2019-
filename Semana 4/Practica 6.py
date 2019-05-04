#Agregar un nuevo contacto

agenda ={
    "Carlos Rojas" : {"telefono" : 87001030,
                      "correo" : "Crojas@hotmail.com"},
    "Juan Perez" : {"telefono" : 83013040,
                    "correo" : "jperez@gmail.com"},
    "ana Marin" : {"telefono" : 88978729,
                   "correo" : "Amarin@gmail.com"}
}

agenda ["Juan Perez"] ["telefono"] = ["66575647", "67457834"]

sofia = {"telefono": 33333333,
         "correo": "sofia@gmail.com"}

agenda ["sofia castro"] = sofia

# Opcion dos

agenda.update({"sofia alfaro": sofia})

for persona in agenda.keys():
    print("nombre:", persona,
          "telefono:", agenda [persona] ["telefono"],
          "correo:", agenda [persona] ["correo"])