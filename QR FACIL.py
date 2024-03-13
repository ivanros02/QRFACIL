import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import qrcode

def validar_numero(input_text):
    if input_text.isdigit() and len(input_text) <= 12:
        return True
    elif input_text == "" or input_text.strip().isdigit():
        return True
    else:
        return False

def validar_parentesco(input_text):
    if input_text.isdigit() and len(input_text) <= 2:
        return True
    elif input_text == "" or input_text.strip().isdigit():
        return True
    else:
        return False

def generar_qr():
    beneficio = entrada_beneficio.get()
    digitos_adicionales = entrada_parentesco.get()

    if not beneficio or not digitos_adicionales:
        messagebox.showwarning("Campos vacíos", "Ambos campos no pueden estar vacíos.")
        return

    data = f"{beneficio}-{digitos_adicionales}"
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=5, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((150, 150))

    img = ImageTk.PhotoImage(img)
    etiqueta_qr.config(image=img)
    etiqueta_qr.image = img

def limpiar_entrada(event):
    event.widget.delete(0, "end")

ventana = tk.Tk()
ventana.title("QR Fácil - Validador de OME")
ventana.iconbitmap("icono.ico")

logo = Image.open("logo.png")
logo = logo.resize((100, 100), Image.BICUBIC)
logo_img = ImageTk.PhotoImage(logo)
logo_label = tk.Label(ventana, image=logo_img)
logo_label.pack()

ventana.geometry("350x460")

frame = tk.Frame(ventana)
frame.pack(pady=20)

etiqueta_beneficio = tk.Label(frame, text="Número de beneficio:")
etiqueta_beneficio.grid(row=0, column=0, padx=10, pady=5)

etiqueta_parentesco = tk.Label(frame, text="Parentesco:")
etiqueta_parentesco.grid(row=1, column=0, padx=10, pady=5)

validacion_numero = ventana.register(validar_numero)
entrada_beneficio = tk.Entry(frame, validate="key", validatecommand=(validacion_numero, "%P"))
entrada_beneficio.bind("<FocusIn>", limpiar_entrada)
entrada_beneficio.grid(row=0, column=1, padx=10, pady=5)

validar_parentesco = ventana.register(validar_parentesco)
entrada_parentesco = tk.Entry(frame, validate="key", validatecommand=(validar_parentesco,"%P"))
entrada_parentesco.bind("<FocusIn>", limpiar_entrada)
entrada_parentesco.grid(row=1, column=1, padx=10, pady=5)

boton_generar_qr = tk.Button(frame, text="Generar QR", command=generar_qr)
boton_generar_qr.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

etiqueta_texto_adicional = tk.Label(ventana, text="Todos los derechos reservados")
etiqueta_texto_adicional.pack(side=tk.BOTTOM)

etiqueta_qr = tk.Label(ventana)
etiqueta_qr.pack(pady=20)

ventana.mainloop()
