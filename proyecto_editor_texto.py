from tkinter import *
from tkinter import filedialog as FileDialog
from io import open # Obligatorio en script (no en Jupyter)

ruta = "" # La usaremos para almacenar la ruta del fichero.

# Definimos las funciones que impactarán sobre el monitor inferior del editor

def nuevo():
    global ruta # Para hacer referencia a la variable definida fuera
    mensaje.set("New file")
    ruta = "" # Vacío.
    texto.delete(1.0,"end") #Se indica con float. Borra desde el primer caracter hasta el final. 
    # Actualizamos el título como la ruta del fichero asignada
    root.title(ruta + " | My Editor")

def abrir():
    global ruta 
    mensaje.set("Open file")
    ruta = FileDialog.askopenfilename(initialdir='.',filetypes=(("Ficheros de texto", "*.txt"),),title="Open file") # Nos abre un cuadro de dialogo para guardar un fichero.
    
    # Si la ruta está establecida:
    if ruta != "": 
        fichero = open(ruta,'r') 
        contenido = fichero.read()
        # Vemos si está vacío el texto e insertar el contenido:
        texto.delete(1.0, "end")
        texto.insert("insert", contenido)
        fichero.close()
        # Actualizamos el título como la ruta del fichero asignada
        root.title(ruta + " | My Editor")

def guardar():
    global ruta 
    mensaje.set("Save file")

    # Esta opción es solo para cuando tenemos un fichero ya abierto (no para uno nuevo)
    if ruta != "":
        contenido = texto.get(1.0,"end-1c") # Guardamos desde el primer caracter hasta el final. Nota: end -1c es recuperar todo menos el último caracter (es un salto de línea que añadía).
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("File saved successfully")
    else:
        guardar_como() # Llamará a la función guardar_como() cuando guardo a partir de un fichero nuevo.

def guardar_como():
    global ruta
    mensaje.set("Save file as...")
    fichero = FileDialog.asksaveasfile(title="Save file as...", mode="w", defaultextension=".txt") 
    
    if fichero is not None:
        ruta = "fichero.name" # Ruta total del fichero.
        # Recuperamos el contenido:
        contenido = texto.get(1.0,"end-1c") # Guardamos desde el primer caracter hasta el final. Nota: end -1c es recuperar todo menos el último caracter (es un salto de línea que añadía).
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("File saved successfully")
    else: # Cancelamos el proceso.
        mensaje.set("File not saved")
        ruta = ""

# Raíz
root = Tk()
root.title("My Editor")

# Configuración del menú superior
menubar = Menu(root)
root.config(menu=menubar)

# Primer submenú
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(menu=filemenu,label="File")

filemenu.add_command(label="New",command=nuevo) 
filemenu.add_command(label="Open",command=abrir) 
filemenu.add_command(label="Save",command=guardar) 
filemenu.add_command(label="Save as...",command=guardar_como) 
filemenu.add_separator() 
filemenu.add_command(label="Exit", command=root.quit) 


# Configuración del espacio de texto
texto = Text(root)
texto.pack(fill="both",expand=1)
texto.config(bd=0,padx=6,pady=4,font=("Consolas",14))

# Monitor inferior para mostrar información
mensaje = StringVar()
mensaje.set("Welcome to My Editor")
monitor = Label(root,textvar=mensaje)
monitor.pack(side="left")



# Finalización del bucle
root.mainloop()