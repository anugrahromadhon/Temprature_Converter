from tkinter import *
from tkinter.messagebox import *
from tkinter import Tk

root = Tk()
root.title("Temperature Converter")
root.geometry("900x500+50+50")
root.config(bg="#f0f8ff")

t = ("Century", 40, "bold", "italic")
f = ("Arial", 20, "bold", "italic")

# Title Label
labTitle = Label(root, text="Temperature Converter", font=t, fg="#FF6347", bg="#f0f8ff")
labTitle.pack(pady=50)

# Celsius Label
labCel = Label(root, text="Enter Temperature in Celsius:", font=f, fg="#4682B4", bg="#f0f8ff")
labCel.place(x=50, y=200)

# Celsius Entry
entCel = Entry(root, font=f, bd=2, relief=SUNKEN, bg="#fff8dc", fg="#000080")
entCel.place(x=500, y=200)

# Result Label
labAns = Label(root, font=f, fg="#32CD32", bg="#f0f8ff")
labAns.place(x=250, y=400)

def show():
    cel = entCel.get()

    if len(entCel.get()) == 0:
        showerror("Issue", "You did not enter Celsius amount")
        entCel.focus()
        return
    
    if cel.isalpha():
        showerror("Issue", "Celsius amount cannot be text")
        entCel.delete(0, END)
        entCel.focus()
        return

    if cel.isspace():
        showerror("Issue", "Celsius amount cannot be spaces")
        entCel.delete(0, END)
        entCel.focus()
        return
    
    try:
        cel = float(entCel.get())
        if 0 <= cel <= 100:
            fah = (cel * 9 / 5) + 32
            msg = round(fah, 2)
            labAns.configure(text=f"{msg} °F")
            entCel.delete(0, END)
            entCel.focus()
        else:
            showerror("Issue", "Enter Temperature in range 0 to 100 only")
            entCel.delete(0, END)
            entCel.focus()

    except ValueError:
        showerror("Issue", "Celsius amount cannot be special characters")
        entCel.delete(0, END)
        entCel.focus()

# Convert Button
btn = Button(root, text="Convert", font=f, command=show, bg="#FFD700", fg="#000080", relief=RAISED, bd=5)
btn.place(x=500, y=300)

# Exit Confirmation
def confirmExit():
    if askyesno('Exit', 'Do you want to exit?'):
        root.destroy()

root.protocol('WM_DELETE_WINDOW', confirmExit)
root.mainloop()
