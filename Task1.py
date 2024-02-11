import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def display_tasks(self):
        if not self.tasks:
            messagebox.showinfo("Tasks", "No tasks found.", icon="warning")
        else:
            tasks_str = "Current Tasks:\n"
            for task, status in self.tasks.items():
                tasks_str += f" - {task} [{status}]\n"
            messagebox.showinfo("Tasks", tasks_str, icon="info")

    def add_task(self, task):
        if task not in self.tasks:
            self.tasks[task] = "Pending"
            messagebox.showinfo("Task Added", f"Task '{task}' added successfully.", icon="info")
        else:
            messagebox.showwarning("Task Exists", f"Task '{task}' already exists.", icon="warning")

    def update_task(self, task, status):
        if task in self.tasks:
            self.tasks[task] = status
            messagebox.showinfo("Task Updated", f"Task '{task}' updated to '{status}'.", icon="info")
        else:
            messagebox.showwarning("Task Not Found", f"Task '{task}' not found.", icon="warning")

    def remove_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
            messagebox.showinfo("Task Removed", f"Task '{task}' removed successfully.", icon="info")
        else:
            messagebox.showwarning("Task Not Found", f"Task '{task}' not found.", icon="warning")

def display_menu():
    print("\n===== ToDoList Application =====")
    print("1. Display Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Exit")

def main():
    task_manager = TaskManager()

    def handle_choice():
        choice = choice_var.get()

        if choice == "1":
            task_manager.display_tasks()
        elif choice == "2":
            task = task_entry.get()
            task_manager.add_task(task)
        elif choice == "3":
            task = task_entry.get()
            status = status_entry.get()
            task_manager.update_task(task, status)
        elif choice == "4":
            task = task_entry.get()
            task_manager.remove_task(task)
        elif choice == "5":
            messagebox.showinfo("Exit", "Exiting the ToDoList application, Thank You!!", icon="info")
            root.destroy()
        else:
            messagebox.showerror("Invalid Choice", "Invalid choice. Please enter a number from 1 to 5.", icon="error")

    root = tk.Tk()
    root.title("ToDoList Application")
    root.geometry("400x300")
    root.configure(background="#f0f0f0")

    style = ttk.Style(root)
    style.configure('TButton', background='#1e90ff', foreground='white', font=('Arial', 12))

    choice_var = tk.StringVar(root, "1")

    tk.Label(root, text="ToDo List", font=('Arial', 16, 'bold'), background="#f0f0f0").pack()

    choices = ["Display Tasks", "Add Task", "Update Task", "Remove Task", "Exit"]
    for i, choice in enumerate(choices, start=1):
        tk.Radiobutton(root, text=f"* {choice}", variable=choice_var, value=str(i), font=('Arial', 12), background="#f0f0f0").pack(anchor="w")

    task_entry = tk.Entry(root, width=30, font=('Arial', 12))
    task_entry.pack()
    status_entry = tk.Entry(root, width=30, font=('Arial', 12))
    status_entry.pack()

    result_text = tk.StringVar(root, "")
    result_label = tk.Label(root, textvariable=result_text, font=('Arial', 14, 'bold'), background="#f0f0f0", fg="green")
    result_label.pack()

    submit_button = tk.Button(root, text="Submit", command=handle_choice, width=10, font=('Arial', 12), background='#1e90ff', foreground='white')
    submit_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
