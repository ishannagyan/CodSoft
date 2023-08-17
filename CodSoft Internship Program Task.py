'''#Simple Calculator
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y
print("Please select the operation:")
print(" 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide")

selection = input("Enter selection (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if selection == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif selection == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif selection == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif selection == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")

#WAP to do list
import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task: task_listbox.insert(tk.END, task), task_entry.delete(0, tk.END)
    else: messagebox.showwarning("Warning", "Please enter a task!")

def remove_task():
    selected_index = task_listbox.curselection()
    if selected_index: task_listbox.delete(selected_index)

def clear_tasks(): task_listbox.delete(0, tk.END)
app = tk.Tk()
app.title("To-Do List")
tk.Label(app, text="Enter the Task:").pack()
task_entry = tk.Entry(app); task_entry.pack()
tk.Button(app, text="Add New Task", command=add_task).pack()
tk.Button(app, text="Remove Task", command=remove_task).pack()
tk.Button(app, text="Clear All Tasks", command=clear_tasks).pack()
task_listbox = tk.Listbox(app); task_listbox.pack()
app.mainloop()'''

#WAP for generating password
import tkinter as tk
import random
import string

def generate_pass():
    password_length = int(length_entry.get())
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for _ in range(password_length))
    generate_pass_label.config(text="Generated Password: " + password)
window = tk.Tk()
window.title("Password Generator")

username_label = tk.Label(window, text="Enter username:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

length_label = tk.Label(window, text="Select Password Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

generate_button = tk.Button(window, text="Click here to Generate the Password", command=generate_pass)
generate_button.pack()
generate_pass_label = tk.Label(window, text="")
generate_pass_label.pack()
window.mainloop()

















