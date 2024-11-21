# We will be making a calculator that
# says hello.

# If the user type in 07734 into the calculator
# a window will pop up that will say hello to the
# user.

import tkinter as tk

root = tk.Tk()

root.geometry("300x500")
root.title("Calculator")

label = tk.Label(root, text="Hello World!", font=('Arial', 18))
label.pack(padx=20, pady=50)

textbox = tk.Text(root, height= 3, font=('Arial', 10))
textbox.pack(padx=10)

# button = tk.Button(root, text="Click Me!", font=('Arial', 18))
# button.pack(padx=10, pady=10)

buttom_frame = tk.Frame(root)
buttom_frame.columnconfigure(0, weight=1)
buttom_frame.columnconfigure(1, weight=1)
buttom_frame.columnconfigure(2, weight=1)
buttom_frame.columnconfigure(3, weight=1)
buttom_frame.columnconfigure(4, weight=1)

def text():
    textbox.insert(0, "1")


btn1 = tk.Button(buttom_frame, text="1", font=('arial', 18), command=text)
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttom_frame, text="2", font=('arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttom_frame, text="3", font=('arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn_divide = tk.Button(buttom_frame, text="/", font=('arial', 18))
btn_divide.grid(row=0, column=3, sticky=tk.W+tk.E)

btn4 = tk.Button(buttom_frame, text="4", font=('arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttom_frame, text="5", font=('arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttom_frame, text="6", font=('arial', 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

btn_multiply = tk.Button(buttom_frame, text="*", font=('arial', 18))
btn_multiply.grid(row=1, column=3, sticky=tk.W+tk.E)

btn7 = tk.Button(buttom_frame, text="7", font=('arial', 18))
btn7.grid(row=2, column=0, sticky=tk.W+tk.E)

btn8 = tk.Button(buttom_frame, text="8", font=('arial', 18))
btn8.grid(row=2, column=1, sticky=tk.W+tk.E)

btn9 = tk.Button(buttom_frame, text="9", font=('arial', 18))
btn9.grid(row=2, column=2, sticky=tk.W+tk.E)

btn_add = tk.Button(buttom_frame, text="+", font=('arial', 18))
btn_add.grid(row=2, column=3, sticky=tk.W+tk.E)

btn_clear = tk.Button(buttom_frame, text="C", font=('arial', 18))
btn_clear.grid(row=3, column=0, sticky=tk.W+tk.E)

btn_clear = tk.Button(buttom_frame, text="0", font=('arial', 18))
btn_clear.grid(row=3, column=2, sticky=tk.W+tk.E)

btn_minus = tk.Button(buttom_frame, text="-", font=('arial', 18))
btn_minus.grid(row=3, column=3, sticky=tk.W+tk.E)

buttom_frame.pack(fill='x')

root.mainloop()



