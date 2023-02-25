from tkinter import *

# function to update the display label
def update_display(num):
    display_label.config(text=display_label.cget("text") + str(num))

# function to clear the display label
def clear_display():
    display_label.config(text="")

# function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(display_label.cget("text"))
        display_label.config(text=str(result))
    except:
        display_label.config(text="Error")

# create tkinter window
window = Tk()
window.title("Calculator")

# create label to display the calculator input/output
display_label = Label(window, font=("Arial", 18), width=20, height=2, bg="white", anchor="e")
display_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# create buttons for numbers and operators
num_buttons = []
for i in range(10):
    num_buttons.append(Button(window, text=str(i), font=("Arial", 14), width=4, height=2, command=lambda x=i: update_display(x)))

add_button = Button(window, text="+", font=("Arial", 14), width=4, height=2, command=lambda: update_display("+"))
sub_button = Button(window, text="-", font=("Arial", 14), width=4, height=2, command=lambda: update_display("-"))
mul_button = Button(window, text="*", font=("Arial", 14), width=4, height=2, command=lambda: update_display("*"))
div_button = Button(window, text="/", font=("Arial", 14), width=4, height=2, command=lambda: update_display("/"))

# create buttons for clear and evaluate
clear_button = Button(window, text="C", font=("Arial", 14), width=4, height=2, command=clear_display)
equal_button = Button(window, text="=", font=("Arial", 14), width=4, height=2, command=evaluate_expression)

# place the buttons on the window using grid layout
num_buttons[7].grid(row=1, column=0)
num_buttons[8].grid(row=1, column=1)
num_buttons[9].grid(row=1, column=2)
add_button.grid(row=1, column=3)

num_buttons[4].grid(row=2, column=0)
num_buttons[5].grid(row=2, column=1)
num_buttons[6].grid(row=2, column=2)
sub_button.grid(row=2, column=3)

num_buttons[1].grid(row=3, column=0)
num_buttons[2].grid(row=3, column=1)
num_buttons[3].grid(row=3, column=2)
mul_button.grid(row=3, column=3)

num_buttons[0].grid(row=4, column=0)
clear_button.grid(row=4, column=1)
equal_button.grid(row=4, column=2)
div_button.grid(row=4, column=3)

# run the window
window.mainloop()
