# creating the calculator 

from tkinter import *

a = Tk()
a.geometry("400x500")
a.title("Calculator")
a.config(bg="#1e1e2f")

x = Entry(a, width=20, font=("Arial", 20), bd=5, relief=RIDGE, justify=RIGHT,
          bg="#ffffff", fg="#000000")
x.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

def click(num):
    current = x.get()
    x.delete(0, END)
    x.insert(0, str(current) + str(num))

def clear():
    x.delete(0, END)

def equal():
    try:
        res = eval(x.get())
        x.delete(0, END)
        x.insert(0, res)
    except:
        x.delete(0, END)
        x.insert(0, "Error")

# Number buttons
Button(a, text="1", width=5, height=2, bg="#4CAF50", fg="white",
       activebackground="#45a049", activeforeground="white",
       command=lambda: click(1)).grid(row=1, column=0, padx=5, pady=5)

Button(a, text="2", width=5, height=2, bg="#4CAF50", fg="white",
       activebackground="#45a049", activeforeground="white",
       command=lambda: click(2)).grid(row=1, column=1, padx=5, pady=5)

Button(a, text="3", width=5, height=2, bg="#4CAF50", fg="white",
       activebackground="#45a049", activeforeground="white",
       command=lambda: click(3)).grid(row=1, column=2, padx=5, pady=5)

Button(a, text="+", width=5, height=2, bg="#ff9800", fg="white",
       activebackground="#e68900", activeforeground="white",
       command=lambda: click("+")).grid(row=1, column=3, padx=5, pady=5)

Button(a, text="4", width=5, height=2, bg="#4CAF50", fg="white",
       activebackground="#45a049", activeforeground="white",
       command=lambda: click(4)).grid(row=2, column=0, padx=5, pady=5)

Button(a, text="5", width=5, height=2, bg="#4CAF50", fg="white",
       activebackground="#45a049", activeforeground="white",
       command=lambda: click(5)).grid(row=2, column=1, padx=5, pady=5)

Button(a, text="6", width=5, height=2, bg="#4CAF50", fg="white",
       activebackground="#45a049", activeforeground="white",
       command=lambda: click(6)).grid(row=2, column=2, padx=5, pady=5)

Button(a, text="-", width=5, height=2, bg="#ff9800", fg="white",
       activebackground="#e68900", activeforeground="white",
       command=lambda: click("-")).grid(row=2, column=3, padx=5, pady=5)

Button(a, text="7", width=5, height=2, bg="#4CAF50", fg="white",
       activebackground="#45a049", activeforeground="white",
       command=lambda: click(7)).grid(row=3, column=0, padx=5, pady=5)

Button(a, text="8", width=5, height=2, bg="#4CAF50", fg="white",
       activebackground="#45a049", activeforeground="white",
       command=lambda: click(8)).grid(row=3, column=1, padx=5, pady=5)

Button(a, text="9", width=5, height=2, bg="#4CAF50", fg="white",
       activebackground="#45a049", activeforeground="white",
       command=lambda: click(9)).grid(row=3, column=2, padx=5, pady=5)

Button(a, text="*", width=5, height=2, bg="#ff9800", fg="white",
       activebackground="#e68900", activeforeground="white",
       command=lambda: click("*")).grid(row=3, column=3, padx=5, pady=5)

Button(a, text="C", width=5, height=2, bg="#f44336", fg="white",
       activebackground="#d32f2f", activeforeground="white",
       command=clear).grid(row=4, column=0, padx=5, pady=5)

Button(a, text="0", width=5, height=2, bg="#4CAF50", fg="white",
       activebackground="#45a049", activeforeground="white",
       command=lambda: click(0)).grid(row=4, column=1, padx=5, pady=5)

Button(a, text="=", width=5, height=2, bg="#2196F3", fg="white",
       activebackground="#1976D2", activeforeground="white",
       command=equal).grid(row=4, column=2, padx=5, pady=5)

Button(a, text="/", width=5, height=2, bg="#ff9800", fg="white",
       activebackground="#e68900", activeforeground="white",
       command=lambda: click("/")).grid(row=4, column=3, padx=5, pady=5)

a.mainloop()