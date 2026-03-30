import tkinter as tk
import json
import os

from gestor_clientes import GestorClientes
from tipos_cliente import ClienteRegular
from cliente import Cliente

gestor = GestorClientes()
archivo_json = "clientes.json"


def guardar_clientes_json():
    datos_cliente = []

    for cliente in gestor.obtener_todos():
        datos_cliente.append(
            {
                "id": cliente.get_id(),
                "nombre": cliente.get_nombre(),
                "email": cliente._Cliente__email,
                "puntos": cliente.get_puntos(),
            }
        )

    with open(archivo_json, "w", encoding="utf-8") as f:
        json.dump(datos_cliente, f, indent=4)


def cargar_clientes_json():
    if not os.path.exists(archivo_json):
        return  # evita error si es primera ejecución

    with open(archivo_json, "r", encoding="utf-8") as f:
        datos_cliente = json.load(f)

    for cliente in datos_cliente:
        nuevo_cliente = ClienteRegular(
            cliente["id"], cliente["nombre"], cliente["email"], cliente["puntos"]
        )
        gestor.agregar(nuevo_cliente)


def crear_cuenta():
    try:
        cliente_id = entry_id.get()
        nombre = entry_nombre.get()
        email = entry_email.get()

        Cliente.validar_email(email)

        cliente = ClienteRegular(cliente_id, nombre, email, 100)  # puntos iniciales
        gestor.agregar(cliente)
        guardar_clientes_json()  # persistencia automática

        etiqueta_mensaje.config(text="Cliente creado correctamente", fg="green")

        entry_id.delete(0, tk.END)
        entry_nombre.delete(0, tk.END)
        entry_email.delete(0, tk.END)

    except ValueError as e:
        etiqueta_mensaje.config(text=str(e), fg="red")


# Tkinter UI
ventana = tk.Tk()
ventana.title("Bienvenido/a a SolutionTech")
ventana.geometry("420x520")
ventana.configure(bg="#EAF2F8")

frame = tk.Frame(ventana, bg="#EAF2F8")
frame.pack(expand=True)

tk.Label(
    frame,
    text="Bienvenido/a a SolutionTech",
    font=("Arial", 18, "bold"),
    bg="#EAF2F8",
    fg="#2E4053",
).pack(pady=10)
tk.Label(
    frame, text="Por favor ingrese o cree su cuenta", font=("Arial", 12), bg="#EAF2F8"
).pack(pady=5)

ancho = 25

tk.Label(frame, text="Cliente_ID", bg="#EAF2F8").pack()
entry_id = tk.Entry(frame, width=ancho)
entry_id.pack(pady=5)

tk.Label(frame, text="Nombre", bg="#EAF2F8").pack()
entry_nombre = tk.Entry(frame, width=ancho)
entry_nombre.pack(pady=5)

tk.Label(frame, text="Email", bg="#EAF2F8").pack()
entry_email = tk.Entry(frame, width=ancho)
entry_email.pack(pady=5)

tk.Button(
    frame,
    text="Crear cuenta",
    command=crear_cuenta,
    width=ancho,
    bg="#197A87",
    fg="white",
).pack(pady=15)

etiqueta_mensaje = tk.Label(frame, text="", bg="#EAF2F8", font=("Arial", 10))
etiqueta_mensaje.pack(pady=10)

cargar_clientes_json()  # carga clientes guardados al iniciar
ventana.mainloop()
