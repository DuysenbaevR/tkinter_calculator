from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import math


def calculate_sqrt():
    resulta = math.sqrt(float(entry.get()))
    resultb = math.sqrt(float(entry2.get()))
    label3.config(text=f"sqrt(a) = {resulta};   sqrt(b) = {resultb}")


def calculate_log():
    result = math.log(int(entry.get()), int(entry2.get()))
    label3.config(text=result)


def calculate_a_b():
    a = float(entry.get())
    b = float(entry2.get())
    result = math.pow(a, b)
    label3.config(text=result)


def calculate_3_sqrt():
    result = math.pow(float(entry.get()), 1/3)
    result2 = math.pow(float(entry2.get()), 1/3)
    label3.config(text=f"cube_root(a) = {result};   cube_root(b) = {result2}")


root = Tk()
root.title("Main App")
root.geometry("400x500")
root.configure(bg='blue')

entry = ttk.Entry()
entry.pack(anchor=SE, padx=6, pady=6)
label1 = ttk.Label(text="a = ", font=("Arial", 16))
label1.pack(anchor=SW, padx=6, pady=1)

entry2 = ttk.Entry()
entry2.pack(anchor=SE, padx=6, pady=6)
label2 = ttk.Label(text="b = ", font=("Arial", 16))
label2.pack(anchor=SW, padx=6, pady=1)

label3 = ttk.Label(text="Answer: ", font=("Arial", 16))
label3.pack(anchor=W, padx=6, pady=1)

imgsqrt = ImageTk.PhotoImage(Image.open("sqrt.jpg"))
btn_sqrt = ttk.Button(image=imgsqrt, command=calculate_sqrt)
btn_sqrt.pack(side=LEFT, padx=6, pady=6)

imglog = ImageTk.PhotoImage(Image.open("log_a_b.jpg"))
btn_log = ttk.Button(image=imglog, command=calculate_log)
btn_log.pack(side=LEFT, padx=6, pady=6)

imgab = ImageTk.PhotoImage(Image.open("a_b.jpg"))
btn_a_b = ttk.Button(image=imgab, command=calculate_a_b)
btn_a_b.pack(side=LEFT, padx=6, pady=6)

imgcuberoot = ImageTk.PhotoImage(Image.open("cube_root.jpg"))
btn_3_sqrt = ttk.Button(image=imgcuberoot, command=calculate_3_sqrt)
btn_3_sqrt.pack(side=LEFT, padx=6, pady=6)

label = ttk.Label()
label.pack(anchor=S, padx=6, pady=6)

root.mainloop()
