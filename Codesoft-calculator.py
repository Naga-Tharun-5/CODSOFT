import tkinter as tk
# In this program we used a GUI interface based method to exhibit a simple calculator 
#this function is used to calculate the result of the given operators with mentioned operation and set the answer to the result
def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operation"#If in case the given operation is not a valid operation then 'Invalid Operation' will be displayed

    result_label.config(text="Result: " + str(result))


root = tk.Tk()
root.title("Simple Calculator")


entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

operations = ["+", "-", "*", "/"]#these are the only basic arithematic operators used in the program
operation_var = tk.StringVar(root)
operation_var.set("+")  # by default '+' operator is set to the (operation_var) opearation variable

operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=5)

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

root.mainloop()