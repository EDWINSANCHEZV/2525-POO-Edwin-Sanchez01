#Tarea semana 13
# Desarrollar una aplicación de interfaz gráfica de usuario (GUI)

"""
app_gui.py
Aplicación GUI sencilla con Tkinter:
- Agrega datos desde un campo de texto a una tabla (Treeview).
- Botón "Agregar" añade el dato.
- Botón "Limpiar" borra el campo de texto o, si hay una fila seleccionada, la elimina (con confirmación).
- Botón "Eliminar seleccionado" borra la fila seleccionada.
"""

import tkinter as tk
from tkinter import ttk, messagebox


class DataApp(tk.Tk):
    """Aplicación principal que contiene la GUI y la lógica."""
    def __init__(self):
        super().__init__()
        self.title("Aplicación GUI: Gestor de Datos (Tkinter)")
        self.geometry("700x420")
        self.minsize(500, 350)

        # Contador simple para generar IDs de fila
        self.counter = 0

        # Crear widgets y layout
        self.create_widgets()

        # Manejar cierre de ventana
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_widgets(self):
        """Crea y dispone los widgets en la ventana."""
        # --- Encabezado ---
        header = ttk.Label(self, text="Gestor de Datos - Ejemplo", font=("Segoe UI", 14, "bold"))
        header.grid(row=0, column=0, columnspan=4, padx=10, pady=(10, 5), sticky="w")

        # --- Frame de entrada ---
        frm_input = ttk.Frame(self)
        frm_input.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky="ew")
        frm_input.columnconfigure(1, weight=1)  # Entry se expande

        lbl = ttk.Label(frm_input, text="Dato:")
        lbl.grid(row=0, column=0, padx=(0, 5), pady=5, sticky="w")

        self.entry = ttk.Entry(frm_input)
        self.entry.grid(row=0, column=1, padx=(0, 5), pady=5, sticky="ew")
        self.entry.bind("<Return>", lambda e: self.add_item())  # Enter agrega

        btn_add = ttk.Button(frm_input, text="Agregar", command=self.add_item)
        btn_add.grid(row=0, column=2, padx=(5, 0), pady=5)

        btn_clear = ttk.Button(frm_input, text="Limpiar", command=self.clear_action)
        btn_clear.grid(row=0, column=3, padx=(5, 0), pady=5)

        # --- Tabla (Treeview) para mostrar datos ---
        columns = ("ID", "Dato")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", selectmode="browse", height=10)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Dato", text="Dato")
        self.tree.column("ID", width=60, anchor="center")
        self.tree.column("Dato", anchor="w")
        self.tree.grid(row=2, column=0, columnspan=3, padx=10, pady=(5, 10), sticky="nsew")

        # Scrollbar vertical para la tabla
        vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        vsb.grid(row=2, column=3, sticky="ns", padx=(0, 10), pady=(5, 10))
        self.tree.configure(yscrollcommand=vsb.set)

        # --- Pie con acciones y estado ---
        frm_bottom = ttk.Frame(self)
        frm_bottom.grid(row=3, column=0, columnspan=4, sticky="ew", padx=10, pady=(0, 10))
        frm_bottom.columnconfigure(1, weight=1)

        btn_delete = ttk.Button(frm_bottom, text="Eliminar seleccionado", command=self.delete_selected)
        btn_delete.grid(row=0, column=0, sticky="w")

        self.status = tk.StringVar(value="Listo")
        lbl_status = ttk.Label(frm_bottom, textvariable=self.status)
        lbl_status.grid(row=0, column=1, sticky="e")

        # Hacer la fila de la tabla expandible cuando redimensionen la ventana
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        # Población de ejemplo (opcional)
        for sample in ["Manzana", "Banano", "Cereza"]:
            self.add_item(sample)

        # Doble clic para cargar el valor en el entry (edición simple)
        self.tree.bind("<Double-1>", self.on_double_click)

    def add_item(self, value=None):
        """
        Agrega un elemento en la tabla.
        Si value es None toma el contenido del Entry.
        """
        if value is None:
            value = self.entry.get().strip()

        if not value:
            messagebox.showwarning("Advertencia", "Ingrese un dato antes de agregar.")
            return

        self.counter += 1
        # Insertar con un iid (id interno) igual al contador para poder localizarlo luego
        self.tree.insert("", "end", iid=str(self.counter), values=(self.counter, value))
        self.status.set(f"Item #{self.counter} agregado.")
        self.entry.delete(0, tk.END)
        self.entry.focus()

    def clear_action(self):
        """
        Si hay una fila seleccionada pregunta y elimina esa fila.
        Si no hay selección borra el contenido del campo Entry.
        """
        sel = self.tree.selection()
        if sel:
            if messagebox.askyesno("Confirmar", "¿Eliminar el elemento seleccionado?"):
                self.tree.delete(sel)
                self.status.set("Elemento seleccionado eliminado.")
        else:
            self.entry.delete(0, tk.END)
            self.status.set("Campo de texto borrado.")

    def delete_selected(self):
        """Elimina explícitamente el elemento seleccionado (botón separado)."""
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Información", "No hay elemento seleccionado para eliminar.")
            return
        if messagebox.askyesno("Confirmar", "¿Desea eliminar el elemento seleccionado?"):
            self.tree.delete(sel)
            self.status.set("Elemento seleccionado eliminado.")

    def on_double_click(self, event):
        """Carga el valor de la fila seleccionada al Entry para edición rápida."""
        sel = self.tree.selection()
        if not sel:
            return
        item = self.tree.item(sel)
        values = item.get("values", [])
        if len(values) >= 2:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, values[1])
            self.status.set("Editando elemento; presione Agregar para añadir como nuevo.")

    def on_close(self):
        """Confirmación antes de cerrar la ventana."""
        if messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?"):
            self.destroy()


if __name__ == "__main__":
    app = DataApp()
    app.mainloop()