import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid Operation")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x200")


tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

operation_var = tk.StringVar(value="+")
tk.Label(root, text="Select operation:").pack()
tk.OptionMenu(root, operation_var, "+", "-", "*", "/").pack()


tk.Button(root, text="Calculate", command=calculate).pack(pady=10)


result_label = tk.Label(root, text="Result:")
result_label.pack()


root.mainloop()
