# Calculator App using Tkinter (Works in VS Code)

from tkinter import *

# Create main window
root = Tk()
root.title("Calculator")
root.geometry("350x500")
root.configure(bg="#2c3e50")

# Function to calculate result
def calculate():
    try:
        num1 = float(first_number.get())
        num2 = float(second_number.get())
        op = operator.get()

        if op == "+":
            result = num1 + num2

        elif op == "-":
            result = num1 - num2

        elif op == "*":
            result = num1 * num2

        elif op == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero"

        else:
            result = "Invalid Operator"

        result_label.config(text="Result = " + str(result))

    except:
        result_label.config(text="Enter valid numbers")


# Heading
heading = Label(
    root,
    text="CALCULATOR",
    font=("Arial", 24, "bold"),
    bg="#2c3e50",
    fg="white"
)
heading.pack(pady=20)

# First number entry
first_number = Entry(
    root,
    font=("Arial", 18),
    width=15,
    justify="center",
    bd=5
)
first_number.pack(pady=15)

# Operator dropdown
operator = StringVar()
operator.set("+")

dropdown = OptionMenu(root, operator, "+", "-", "*", "/")
dropdown.config(font=("Arial", 16), bg="#3498db", fg="white")
dropdown.pack(pady=15)

# Second number entry
second_number = Entry(
    root,
    font=("Arial", 18),
    width=15,
    justify="center",
    bd=5
)
second_number.pack(pady=15)

# Calculate button
button = Button(
    root,
    text="Calculate",
    font=("Arial", 18, "bold"),
    bg="#1abc9c",
    fg="white",
    padx=20,
    pady=10,
    command=calculate
)
button.pack(pady=25)

# Result label
result_label = Label(
    root,
    text="Result = ",
    font=("Arial", 20, "bold"),
    bg="#2c3e50",
    fg="yellow"
)
result_label.pack(pady=20)

# Run application
root.mainloop()