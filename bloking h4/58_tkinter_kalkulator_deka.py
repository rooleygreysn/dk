import tkinter as tk
from tkinter import ttk

def hitung():
    angka1 = float(angka1_entry.get())
    angka2 = float(angka2_entry.get())
    operator = operator_combobox.get()

    if operator == "+":
        hasil = angka1 + angka2
    elif operator == "-":
        hasil = angka1 - angka2
    elif operator == "*":
        hasil = angka1 * angka2
    elif operator == "/":
        hasil = angka1 / angka2
    else:
        hasil = "Operator Tidak Valid" 

    hasil_label.config(text=str(hasil))

window = tk.Tk()
window.title("Kalkulator")

input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10)

angka1_label = ttk.Label(input_frame, text="Angka Pertama :")
angka1_label.grid(row=0, column=0, sticky="w")
angka1_entry = ttk.Entry(input_frame)
angka1_entry.grid(row=0, column=1)

angka2_label = ttk.Label(input_frame, text="Angka Kedua :")
angka2_label.grid(row=1, column=0, sticky="w")
angka2_entry = ttk.Entry(input_frame)
angka2_entry.grid(row=1, column=1)

operator_combobox = ttk.Combobox(input_frame, values=["+", "-", "*", "/"])
operator_combobox.grid(row=2, column=0, columnspan=2, pady=5)

hitung_button = ttk.Button(input_frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=0, columnspan=2, pady=10)

hasil_label = ttk.Label(input_frame, text="")
hasil_label.grid(row=4, column=0, columnspan=2)

window.mainloop()