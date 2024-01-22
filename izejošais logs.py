import tkinter as tk

def start_clicked():
    input_text = inputs.get()
    if '-' in input_text:
        calculate_minus(input_text)
    elif '*' in input_text:
        calculate_reiz(input_text)
    elif ':' in input_text or '/' in input_text:
        calculate_dalit(input_text)
    else:
        calculate_sum(input_text)

def clear_clicked():
    inputs.delete(0, tk.END)
    izeja.config(text="")

def calculate_sum(input_text):
    numbers = [int(x) for x in input_text.split('+')]
    result = sum(numbers)
    izeja.config(text=f"Hello {result}")

def calculate_minus(input_text):
    f = input_text.find("-")
    k_puse = int(input_text[:f])
    l_puse = int(input_text[f+1:])
    izeja.config(text=str(k_puse - l_puse))

def calculate_reiz(input_text):
    f = input_text.find("*")
    k_puse = int(input_text[:f])
    l_puse = int(input_text[f+1:])
    izeja.config(text=str(k_puse * l_puse))

def calculate_dalit(input_text):
    if ':' in input_text or '/' in input_text:
        symbol = ':' if ':' in input_text else '/'
        f = input_text.find(symbol)
        k_puse = int(input_text[:f])
        l_puse = int(input_text[f+1:])
        if l_puse == 0:
            izeja.config(text=f"nekorekts ievads")
        else:
            izeja.config(text=str(k_puse // l_puse))

window = tk.Tk()
window.title("Dmitrijs")

window.geometry("640x480")

inputs = tk.Entry(window)
inputs.pack()

start = tk.Button(window, text="Start", command=start_clicked)
start.pack()
clear = tk.Button(window, text="X", command=clear_clicked)
clear.pack()
izeja = tk.Label(window, text="", justify="left", anchor="nw")
izeja.pack()

start.place(x=320, y=240)
clear.place()

window.mainloop()
