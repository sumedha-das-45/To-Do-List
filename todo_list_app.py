import tkinter as tk
from tkinter import messagebox, filedialog
import os

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x450")

        tk.Label(root, text="To-Do List", font=("Arial", 18, "bold")).pack(pady=10)

        self.task_entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.task_entry.pack(pady=5)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Add Task", width=10, command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Delete Task", width=10, command=self.delete_task).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Save Tasks", width=10, command=self.save_tasks).grid(row=0, column=2, padx=5)

        self.task_listbox = tk.Listbox(root, width=45, height=15, font=("Arial", 12))
        self.task_listbox.pack(pady=10)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        try:
            selected = self.task_listbox.curselection()
            self.task_listbox.delete(selected[0])
        except IndexError:
            messagebox.showwarning("Select Task", "Please select a task to delete.")

    def save_tasks(self):
        tasks = self.task_listbox.get(0, tk.END)
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(task + "\n")
        messagebox.showinfo("Saved", "Tasks saved successfully!")

    def load_tasks(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as f:
                for line in f:
                    self.task_listbox.insert(tk.END, line.strip())

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
