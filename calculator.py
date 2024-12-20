# Import tkinter

import tkinter as tk
import SaysHello as sh
# Set the calculation to an empty string
calculation = ""
#str_num = "07734"
# Create function to add calculation
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# Create function evaluate the calculation
def evaluate_calcualtion():
    global calculation
    try:
        calculation = str(eval((calculation)))
        if calculation == "0.7734":
            sh.DisplayMessage()
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "error")

# Create function to clear the textbox field
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


# Create the application page
root = tk.Tk()
root.geometry("300x275")
root.title("Calculator Says Hello")
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

if text_result == int("07734"):
    import SaysHello

# Add all buttons needed for the calculator
btn1 =tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn1.grid(row=2, column=1)
btn2 =tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn2.grid(row=2, column=2)
btn3 =tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn3.grid(row=2, column=3)
btn4 =tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn4.grid(row=3, column=1)
btn5 =tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn5.grid(row=3, column=2)
btn6 =tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn6.grid(row=3, column=3)
btn7 =tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn7.grid(row=4, column=1)
btn8 =tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn8.grid(row=4, column=2)
btn9 =tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn9.grid(row=4, column=3)
btn0 =tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn0.grid(row=5, column=2)
btn_equal =tk.Button(root, text="=", command=evaluate_calcualtion, width=5, font=("Arial", 14))
btn_equal.grid(row=6, column=1)
btn_plus =tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)
btn_minus =tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)
btn_times =tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_times.grid(row=4, column=4)
btn_divide =tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_divide.grid(row=5, column=4)
btn_period =tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font=("Arial", 14))
btn_period.grid(row=6, column=2)
btn_open =tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
btn_open.grid(row=5, column=3)
btn_close =tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
btn_close.grid(row=5, column=1)
btn_clear =tk.Button(root, text="C", command=clear_field, width=5, font=("Arial", 14))
btn_clear.grid(row=6, column=3)
root.mainloop()







