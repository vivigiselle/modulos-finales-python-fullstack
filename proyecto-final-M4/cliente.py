class Cliente:
    def __init__(self, cliente_id, nombre, email):
        self.__id = cliente_id
        self.__nombre = nombre
        self.__email = email

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre  # faltaba asignación
        
    # Validaciones
    @staticmethod
    def validar_email(email): 
        if "@" not in email:
            raise ValueError("Falta el @")
        if ".com" not in email:
            raise ValueError("Falta el .com en su correo electronico")
        return True
    
    @staticmethod
    def validar_telefono(telefono):
        if len(telefono) < 8:
            raise ValueError("Faltan numeros")
        if not telefono.isdigit():
            raise ValueError("Telefono solo deben ser numeros")
        return True
    
    @staticmethod
    def validar_direccion(direccion):
        if "," not in direccion:
            raise ValueError("Falta la , despues de la direccion e indicar la comuna")       
        return True

    @staticmethod  # metodo pertenece a la clase
    def calcular_descuentos(clientes):
        resultados = []
        for cliente in clientes:
            resultados.append(f"{cliente.get_nombre()}: {cliente.calcular_descuento()}%")
        return resultados
    