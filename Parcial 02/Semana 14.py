#!/usr/bin/env python3
# agenda.py
"""
Agenda Personal con Tkinter y tkcalendar (DateEntry).
Características:
- TreeView con columnas: Fecha, Hora, Descripción.
- DatePicker (tkcalendar.DateEntry).
- Añadir, eliminar (con confirmación) y ver detalles con doble-clic.
- Persistencia simple en JSON (events.json).
"""

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import json
import os
from datetime import datetime

DATA_FILE = "events.json"

class AgendaApp:
    def __init__(self, master):
        self.master = master
        master.title("Agenda Personal")
        master.geometry("700x420")

        # ----------------- Frames -----------------
        self.frame_list = ttk.Frame(master)
        self.frame_form = ttk.Frame(master, padding=8)
        self.frame_actions = ttk.Frame(master, padding=8)

        self.frame_list.pack(fill='both', expand=True)
        self.frame_form.pack(fill='x')
        self.frame_actions.pack(fill='x')

        # ----------------- TreeView (lista de eventos) -----------------
        cols = ("fecha", "hora", "descripcion")
        self.tree = ttk.Treeview(self.frame_list, columns=cols, show="headings", selectmode="browse")
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")
        self.tree.column("fecha", width=110, anchor="center")
        self.tree.column("hora", width=80, anchor="center")
        self.tree.column("descripcion", width=440, anchor="w")

        vsb = ttk.Scrollbar(self.frame_list, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.pack(side="left", fill="both", expand=True)
        vsb.pack(side="right", fill="y")

        # ----------------- Formulario (entrada de datos) -----------------
        lbl_fecha = ttk.Label(self.frame_form, text="Fecha:")
        lbl_hora = ttk.Label(self.frame_form, text="Hora (HH:MM):")
        lbl_desc = ttk.Label(self.frame_form, text="Descripción:")

        lbl_fecha.grid(row=0, column=0, padx=6, pady=6, sticky="e")
        lbl_hora.grid(row=0, column=2, padx=6, pady=6, sticky="e")
        lbl_desc.grid(row=1, column=0, padx=6, pady=6, sticky="ne")

        # DateEntry proporciona un DatePicker (get_date() -> datetime.date).
        self.date_entry = DateEntry(self.frame_form, width=12)
        self.time_entry = ttk.Entry(self.frame_form, width=12)
        self.desc_entry = ttk.Entry(self.frame_form, width=60)

        self.date_entry.grid(row=0, column=1, padx=6, pady=6, sticky="w")
        self.time_entry.grid(row=0, column=3, padx=6, pady=6, sticky="w")
        self.desc_entry.grid(row=1, column=1, columnspan=3, padx=6, pady=6, sticky="we")

        # ----------------- Botones -----------------
        btn_add = ttk.Button(self.frame_actions, text="Agregar Evento", command=self.add_event)
        btn_delete = ttk.Button(self.frame_actions, text="Eliminar Evento Seleccionado", command=self.delete_event)
        btn_exit = ttk.Button(self.frame_actions, text="Salir", command=self.on_exit)

        btn_add.pack(side="left", padx=10, pady=8)
        btn_delete.pack(side="left", padx=10, pady=8)
        btn_exit.pack(side="right", padx=10, pady=8)

        # Doble clic para ver detalles
        self.tree.bind("<Double-1>", self.on_show_event)

        # Cargar eventos guardados (si existen)
        self.load_events()

    # ----------------- Lógica -----------------
    def add_event(self):
        # Obtener fecha desde DateEntry (objeto datetime.date)
        try:
            date_obj = self.date_entry.get_date()
            fecha_guardar = date_obj.strftime("%Y-%m-%d")  # formato ISO para almacenar
            fecha_mostrar = date_obj.strftime("%d/%m/%Y")  # formato más humano para mostrar (opcional)
        except Exception:
            messagebox.showerror("Fecha inválida", "Por favor selecciona una fecha válida.")
            return

        hora = self.time_entry.get().strip()
        descripcion = self.desc_entry.get().strip()

        if not hora or not descripcion:
            messagebox.showwarning("Datos incompletos", "Completa la hora y la descripción.")
            return

        # Validar formato de hora HH:MM (24h)
        try:
            datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showerror("Hora inválida", "La hora debe tener formato HH:MM (ej. 14:30).")
            return

        # Insertar en la TreeView (mostramos fecha en formato dd/mm/YYYY)
        self.tree.insert("", "end", values=(fecha_mostrar, hora, descripcion))

        # Guardar persistente
        self.save_events()

        # Limpiar campos (excepto fecha)
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def delete_event(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Sin selección", "Selecciona un evento para eliminar.")
            return
        # Diálogo de confirmación (opcional solicitado)
        if messagebox.askyesno("Confirmar eliminación", "¿Deseas eliminar el evento seleccionado?"):
            for iid in sel:
                self.tree.delete(iid)
            self.save_events()

    def on_show_event(self, event):
        sel = self.tree.selection()
        if not sel:
            return
        iid = sel[0]
        fecha, hora, descripcion = self.tree.item(iid, "values")
        messagebox.showinfo("Detalles del evento", f"Fecha: {fecha}\nHora: {hora}\nDescripción: {descripcion}")

    def save_events(self):
        events = []
        for child in self.tree.get_children():
            fecha, hora, descripcion = self.tree.item(child, "values")
            # Convertir fecha a ISO (si se quiere consistencia al guardar)
            # Aquí asumimos fecha en dd/mm/YYYY -> convertir a YYYY-MM-DD
            try:
                dt = datetime.strptime(fecha, "%d/%m/%Y")
                fecha_iso = dt.strftime("%Y-%m-%d")
            except Exception:
                fecha_iso = fecha
            events.append({"fecha": fecha_iso, "hora": hora, "descripcion": descripcion})
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(events, f, ensure_ascii=False, indent=2)
        except Exception as e:
            messagebox.showerror("Error al guardar", str(e))

    def load_events(self):
        if not os.path.exists(DATA_FILE):
            return
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                events = json.load(f)
            for ev in events:
                fecha_iso = ev.get("fecha", "")
                hora = ev.get("hora", "")
                descripcion = ev.get("descripcion", "")
                # Mostrar fecha en dd/mm/YYYY si es posible
                try:
                    dt = datetime.strptime(fecha_iso, "%Y-%m-%d")
                    fecha_mostrar = dt.strftime("%d/%m/%Y")
                except Exception:
                    fecha_mostrar = fecha_iso
                self.tree.insert("", "end", values=(fecha_mostrar, hora, descripcion))
        except Exception as e:
            messagebox.showwarning("No se pudieron cargar eventos", str(e))

    def on_exit(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
