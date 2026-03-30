class GestorClientes():
    def __init__(self):
        self.__clientes = []
        
    def agregar(self,cliente):  
        self.__clientes.append(cliente) #Agrego a la lista los clientes
        
    def obtener_todos(self):
        return self.__clientes  # necesario para guardar en JSON
        
    def listar(self):
        for cliente in self.__clientes:
            print (f"{cliente.get_nombre()} Descuento: {cliente.calcular_descuento()}")
    
    def buscar(self, id__cliente):  
        for cliente in self.__clientes:
            if cliente.get_id() == id__cliente: #buscar cliente que coincida de la lista
                return cliente
        return None
    
    def eliminar(self, id__cliente): 
        nueva_lista = []
        
        for cliente in self.__clientes: 
            if cliente.get_id() != id__cliente: #buscar cliente que  no coincida de la lista
                nueva_lista.append(cliente)     #se eliminara y no quedará en la nueva lista
        
        self.__clientes = nueva_lista  