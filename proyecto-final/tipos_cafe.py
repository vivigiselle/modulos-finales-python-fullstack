#Tipos de cafe disponibles y sus precios asociados
cafes = {
    "espresso": 4500,
    "americano": 4800,
    "latte": 5500,
    "capuccino": 5800,
    "matcha": 5800,
    "mocaccino": 6400,
    "macchiato": 6800,
    
}

#Bienvenida a la cafeteria
def inicio():
    print("BIEVENIDO A LA CAFETERIA 404")
    for cafe, precio in cafes.items(): #for para buscar cada item y obtener su  numero + precio
        print(f"{cafe.title()} - ${precio}")

def valor_precio(nombre):
    return cafes.get(nombre.lower())