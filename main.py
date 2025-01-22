import tkinter as tk
from tkinter import messagebox

# Functions for the app
def add_task():
    task = task_entry.get()
    if task.strip():
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Please enter a task.")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Error", "Please select a task to delete.")

def mark_done():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, f"✅ {task}")
    else:
        messagebox.showwarning("Error", "Please select a task to mark as done.")

def clear_tasks():
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?")
    if confirm:
        task_listbox.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("Task Manager")

# Layout
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Title
title_label = tk.Label(frame, text="My Task Manager", font=("Arial", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Task input field
task_label = tk.Label(frame, text="New task:")
task_label.grid(row=1, column=0, sticky="e", pady=5)

task_entry = tk.Entry(frame, width=40)
task_entry.grid(row=1, column=1, pady=5)

# Task management buttons
add_button = tk.Button(frame, text="Add Task", command=add_task, width=15)
add_button.grid(row=2, column=0, pady=5, sticky="e")

delete_button = tk.Button(frame, text="Delete Task", command=delete_task, width=15)
delete_button.grid(row=2, column=1, pady=5, sticky="w")

mark_done_button = tk.Button(frame, text="Mark as Done", command=mark_done, width=20)
mark_done_button.grid(row=3, column=0, columnspan=2, pady=5)

clear_button = tk.Button(frame, text="Clear All", command=clear_tasks, width=20, bg="red", fg="white")
clear_button.grid(row=4, column=0, columnspan=2, pady=5)

# Task list
task_listbox = tk.Listbox(frame, width=50, height=15, selectmode=tk.SINGLE)
task_listbox.grid(row=5, column=0, columnspan=2, pady=10)

# Start the tkinter loop
root.mainloop()
