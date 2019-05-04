#Suponga que juan Perez Cambio de Telefono y ahora tiene 2 nuevos

agenda ={
    "Carlos Rojas" : {"telefono" : 87001030,
                      "correo" : "Crojas@hotmail.com"},
    "Juan Perez" : {"telefono" : 83013040,
                    "correo" : "jperez@gmail.com"},
    "ana Marin" : {"telefono" : 88978729,
                   "correo" : "Amarin@gmail.com"}
}

agenda ["Juan Perez"] ["telefono"] = ["66575647", "67457834"]

for persona in agenda.keys():
    print("nombre:", persona,
          "telefono:", agenda [persona] ["telefono"],
          "correo:", agenda [persona] ["correo"])

