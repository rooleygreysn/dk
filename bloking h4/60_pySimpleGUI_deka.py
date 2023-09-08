import tkinter as tk

layout = [[tk.Button('KLIK SAYA')]]

window = tk.Window('contoh program PySimpleGUI', layout)

while True:
    event, values = window.read()
    if event == tk.WINDOW_CLOSED:
        break
    elif event == 'klik saya':
        print('tombol diklik')

window.close()