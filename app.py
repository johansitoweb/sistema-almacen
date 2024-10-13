import tkinter as tk
from tkinter import messagebox, simpledialog

class Almacen:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Almacén")
        self.root.geometry("500x500")

        self.productos = {}
        self.proveedores = {}

        # Frame para la entrada de productos
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.label_nombre = tk.Label(self.frame, text="Nombre del Producto:")
        self.label_nombre.grid(row=0, column=0)

        self.entry_nombre = tk.Entry(self.frame)
        self.entry_nombre.grid(row=0, column=1)

        self.label_cantidad = tk.Label(self.frame, text="Cantidad:")
        self.label_cantidad.grid(row=1, column=0)

        self.entry_cantidad = tk.Entry(self.frame)
        self.entry_cantidad.grid(row=1, column=1)

        self.label_categoria = tk.Label(self.frame, text="Categoría:")
        self.label_categoria.grid(row=2, column=0)

        self.entry_categoria = tk.Entry(self.frame)
        self.entry_categoria.grid(row=2, column=1)

        # Frame para los botones
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(pady=10)

        # Botones
        self.btn_agregar = tk.Button(self.frame_botones, text="Agregar Producto", command=self.agregar_producto)
        self.btn_agregar.grid(row=0, column=0, padx=5)

        self.btn_eliminar = tk.Button(self.frame_botones, text="Eliminar Producto", command=self.eliminar_producto)
        self.btn_eliminar.grid(row=0, column=1, padx=5)

        self.btn_mostrar = tk.Button(self.frame_botones, text="Mostrar Inventario", command=self.mostrar_inventario)
        self.btn_mostrar.grid(row=0, column=2, padx=5)

        self.btn_agregar_proveedor = tk.Button(self.frame_botones, text="Agregar Proveedor", command=self.agregar_proveedor)
        self.btn_agregar_proveedor.grid(row=0, column=3, padx=5)

        self.btn_mostrar_proveedores = tk.Button(self.frame_botones, text="Mostrar Proveedores", command=self.mostrar_proveedores)
        self.btn_mostrar_proveedores.grid(row=0, column=4, padx=5)

    def agregar_producto(self):
        nombre = self.entry_nombre.get()
        cantidad = self.entry_cantidad.get()
        categoria = self.entry_categoria.get()

        if nombre and cantidad.isdigit() and categoria:
            cantidad = int(cantidad)
            if cantidad < 0:
                messagebox.showerror("Error", "La cantidad no puede ser negativa.")
                return
            
            if nombre in self.productos:
                self.productos[nombre]['cantidad'] += cantidad
            else:
                self.productos[nombre] = {'cantidad': cantidad, 'categoria': categoria}
            messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado con cantidad {cantidad}.")
            self.entry_nombre.delete(0, tk.END)
            self.entry_cantidad.delete(0, tk.END)
            self.entry_categoria.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Por favor, ingrese un nombre válido, cantidad y categoría.")

    def eliminar_producto(self):
        nombre = simpledialog.askstring("Eliminar Producto", "Ingrese el nombre del producto a eliminar:")
        if nombre in self.productos:
            del self.productos[nombre]
            messagebox.showinfo("Éxito", f"Producto '{nombre}' eliminado.")
        else:
            messagebox.showerror("Error", "Producto no encontrado.")

    def mostrar_inventario(self):
        inventario = "\n".join([f"{nombre} (Categoría: {info['categoria']}): {info['cantidad']}" for nombre, info in self.productos.items()])
        if not inventario:
            inventario = "El inventario está vacío."
        messagebox.showinfo("Inventario", inventario)

    def agregar_proveedor(self):
        nombre = simpledialog.askstring("Agregar Proveedor", "Ingrese el nombre del proveedor:")
        contacto = simpledialog.askstring("Agregar Proveedor", "Ingrese el contacto del proveedor:")
        if nombre and contacto:
            self.proveedores[nombre] = contacto
            messagebox.showinfo("Éxito", f"Proveedor '{nombre}' agregado.")
        else:
            messagebox.showerror("Error", "Por favor, ingrese un nombre y un contacto válidos.")

    def mostrar_proveedores(self):
        proveedores_list = "\n".join([f"{nombre}: {contacto}" for nombre, contacto in self.proveedores.items()])
        if not proveedores_list:
            proveedores_list = "No hay proveedores registrados."
        messagebox.showinfo("Proveedores", proveedores_list)

if __name__ == "__main__":
    root = tk.Tk()
    app = Almacen(root)
    root.mainloop()
