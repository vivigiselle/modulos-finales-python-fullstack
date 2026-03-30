import tipos_cafe

def pedir_cafe(): # Muestra el menú, valida si el café existe.
    tipos_cafe.inicio()
    nombre = input("Escriba el nombre del café: ").lower()
    precio = tipos_cafe.valor_precio(nombre)
    
    if precio is None:
        print("El cafe no se encuentra en el menú. Vuelva a intentarlo")
        return None
    
    cantidad = pedir_cantidad() #calcula el total a pagar.
    total = precio * cantidad
    return nombre, cantidad, total

def pedir_cantidad(): #funcion para validar la cantidad ingresada por el usuario. Con while, break, continue
    while True:
        cantidad = input("Ingrese la cantidad de cafés deseados: ")

        if not cantidad.isdigit(): #isdigit solo para numeros
            print("Solo se permiten números mayor a 0")
            continue

        cantidad = int(cantidad)
        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0")
            continue
        break
    return cantidad

def menu_cafeteria(): #menu principal con opciones de pedir de una lista, almacenar informacion y salir
    pedidos = []
    while True:
        print("1. Pedir café")
        print("2. Ver pedidos")
        print("3. Salir")
        opcion = input("Escriba su opción: ")
        if opcion == "1":
            pedido = pedir_cafe()
            if pedido:
                pedidos.append(pedido)
                print("Pedido agregado")
        elif opcion == "2":
            print("Listado de Pedidos")
            for cafe, cant, total in pedidos:
                print(f"{cafe.title()} x{cant} = Su valor es :${total}") #calcula el valor total, segun cantidad
        elif opcion == "3":
            print("Gracias por su visita ☕")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu_cafeteria()