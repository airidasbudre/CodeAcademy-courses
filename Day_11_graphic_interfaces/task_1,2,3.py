from tkinter import *


# Sukurti programą su grafine sąsaja, kuri:

# Turėtų laukelį su užrašu "Įveskite vardą", kuriame vartotojas galėtų įvesti vardą
# Turėtų mygtuką su užrašu "Patvirtinti", kurį nuspaudus, programa po lauku atspausdintų "Labas, {vardas}!"
# Atspausdintų pasisveikinimą ne tik nuspaudus mygtuką, bet ir paspaudus mygtuką "Enter"

window = Tk()

def print1(event):
    inputx = None
    inputx = input1.get(f"Hello {inputx}!")
    rezult["text"] = inputx
    
def clearToTextInput():
   rezult.delete("1.0","end")  

sign1 = Label(window, text="Input name")
window.geometry("400x400")
input1 = Entry(window)
button1 = Button(window, text="Print")
meniu = Menu(window)
window.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)
submeniu1 = Menu(meniu, tearoff = 0)
submeniu2 = Menu(meniu, tearoff = 0)
submeniu3 = Menu(meniu, tearoff = 0)
rezult = Label(window, text="")

meniu.add_cascade(label="Menu", menu=submeniu)
submeniu1.add_command(label="Clear", command = clearToTextInput)
submeniu2.add_command(label="Return last")
submeniu.add_separator()
submeniu3.add_command(label="Exit")
input1 = 


button1.bind("<Button-1>", print1)
window.bind("<Return>", print1)
rezult.bind("<Return>", print1)

sign1.grid(row=0, column=0)
input1.grid(row=0, column=1)
button1.grid(row=0, column=2)
rezult.grid(row=1, columnspan=3)

window.mainloop()