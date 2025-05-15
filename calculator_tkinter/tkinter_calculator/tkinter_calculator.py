# import tkinter as tk

# # Function to update the input field
# def update_input(value):
#     current_text = input_field.get()
#     input_field.delete(0, tk.END)
#     input_field.insert(0, current_text + value)

# # Function to clear the input field
# def clear_input():
#     input_field.delete(0, tk.END)

# # Function to evaluate the expression
# def calculate():
#     try:
#         result = eval(input_field.get())
#         input_field.delete(0, tk.END)
#         input_field.insert(0, str(result))
#     except Exception as e:
#         input_field.delete(0, tk.END)
#         input_field.insert(0, "Error")

# # Create the main window
# root = tk.Tk()
# root.title("Calculator")

# # Create an input field
# input_field = tk.Entry(root, width=35, borderwidth=5)
# input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# # Define buttons
# buttons = [
#     ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
#     ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
#     ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
#     ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
#     ('=', 5, 0)
# ]

# # Create and place buttons
# for (text, row, col) in buttons:
#     if text == '=':
#         button = tk.Button(root, text=text, padx=40, pady=20, command=calculate)
#         button.grid(row=row, column=col, columnspan=4)
#     elif text == 'C':
#         button = tk.Button(root, text=text, padx=40, pady=20, command=clear_input)
#         button.grid(row=row, column=col)
#     else:
#         button = tk.Button(root, text=text, padx=40, pady=20, command=lambda t=text: update_input(t))
#         button.grid(row=row, column=col)

# # Run the application
# root.mainloop()


