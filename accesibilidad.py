import tkinter as tk
from tkinter import ttk

# Función para alternar entre modo oscuro y modo claro
def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    
    if dark_mode:
        # Modo oscuro
        root.config(bg="#1a1a1a")
        title_label.config(bg="#1a1a1a", fg="white")
        note1.config(bg="#4a4a4a", fg="white")
        note2.config(bg="#4a4a4a", fg="white")
        note3.config(bg="#4a4a4a", fg="white")
        note4.config(bg="#4a4a4a", fg="white")
        dark_mode_button.config(text="Light Mode", bg="#ff9aa2", fg="black")
    else:
        # Modo claro
        root.config(bg="white")
        title_label.config(bg="white", fg="black")
        note1.config(bg="#ff9aa2", fg="black")
        note2.config(bg="#a2cffe", fg="black")
        note3.config(bg="#87cefa", fg="black")
        note4.config(bg="#ffb347", fg="black")
        dark_mode_button.config(text="Dark Mode", bg="#a2cffe", fg="black")

# Crear ventana principal
root = tk.Tk()
root.title("Mi Página Web Accesible")
root.geometry("500x600")
root.config(bg="white")

# Variable para el modo oscuro
dark_mode = False

# Título
title_label = ttk.Label(
    root,
    text="Mi Página Web Accesible",
    font=("Arial", 20, "bold"),
    background="white",
    foreground="black"
)
title_label.pack(pady=20)

# Botón para alternar entre modos
dark_mode_button = tk.Button(
    root,
    text=" Dark Mode",
    font=("Arial", 12),
    bg="#a2cffe",
    fg="white",
    command=toggle_dark_mode
)
dark_mode_button.pack(pady=10)

# Notas
note1 = tk.Label(
    root,
    text="Proporcionar alternativas textuales para contenido no textual",
    font=("Arial", 12),
    bg="#ff9aa2",
    fg="black",
    wraplength=400,
    padx=10,
    pady=10
)
note1.pack(pady=10)

note2 = tk.Label(
    root,
    text="Diseño y navegación claros y consistentes",
    font=("Arial", 12),
    bg="#a2cffe",
    fg="black",
    wraplength=400,
    padx=10,
    pady=10
)
note2.pack(pady=10)

note3 = tk.Label(
    root,
    text="Compatibilidad con tecnologías de asistencia",
    font=("Arial", 12),
    bg="#87cefa",
    fg="black",
    wraplength=400,
    padx=10,
    pady=10
)
note3.pack(pady=10)

note4 = tk.Label(
    root,
    text="Contraste adecuado y contenido perceptible",
    font=("Arial", 12),
    bg="#ffb347",
    fg="black",
    wraplength=400,
    padx=10,
    pady=10
)
note4.pack(pady=10)

# Ejecutar la interfaz gráfica
root.mainloop()
