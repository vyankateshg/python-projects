## we are usinf tkinter to make todo list here 
# and this todo list is connected to database also we have used SQLITE3 database in this small project 
import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkcalendar import Calendar
import sqlite3

# Initialize database
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()

# Create a table for tasks if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    task TEXT NOT NULL
)
""")
conn.commit()

# Functions
def add_task():
    selected_date = calendar.get_date()
    task = task_entry.get().strip()

    if not task:
        messagebox.showwarning("Input Error", "Task cannot be empty!")
        return

    # Insert task into the database
    cursor.execute("INSERT INTO tasks (date, task) VALUES (?, ?)", (selected_date, task))
    conn.commit()

    task_entry.delete(0, tk.END)
    update_task_display(selected_date)


def update_task_display(selected_date):
    task_display.delete(1.0, tk.END)

    # Retrieve tasks for the selected date
    cursor.execute("SELECT task FROM tasks WHERE date = ?", (selected_date,))
    tasks = cursor.fetchall()

    if tasks:
        task_display.insert(tk.END, f"Tasks for {selected_date}:\n")
        for idx, task in enumerate(tasks, 1):
            task_display.insert(tk.END, f"{idx}. {task[0]}\n")
    else:
        task_display.insert(tk.END, f"No tasks for {selected_date}.")


def show_tasks_for_date():
    selected_date = calendar.get_date()
    update_task_display(selected_date)


def delete_task():
    selected_date = calendar.get_date()

    # Retrieve tasks for the selected date
    cursor.execute("SELECT id, task FROM tasks WHERE date = ?", (selected_date,))
    tasks = cursor.fetchall()

    if tasks:
        # Delete the last task for the selected date
        last_task_id = tasks[-1][0]
        cursor.execute("DELETE FROM tasks WHERE id = ?", (last_task_id,))
        conn.commit()

        update_task_display(selected_date)
        messagebox.showinfo("Task Deleted", "Last task for the selected date has been removed.")
    else:
        messagebox.showwarning("No Tasks", "No tasks to delete for the selected date.")


# Main Window
root = tk.Tk()
root.title("To-Do List with Calendar (SQLite Edition)")
root.geometry("500x550")

# Calendar
calendar = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
calendar.pack(pady=20)

# Label for task entry
task_entry_label = tk.Label(root, text="Enter Your Task", font=("Arial", 16, "bold"))
task_entry_label.pack(pady=5)

# Task Entry
task_entry = tk.Entry(root, width=40, font=("Arial", 14))
task_entry.pack(pady=10)
task_entry.insert(0, "Enter your task here...")

# Buttons
add_task_btn = tk.Button(root, text="Add Task", command=add_task, width=20, bg="green", fg="white")
add_task_btn.pack(pady=5)

show_tasks_btn = tk.Button(root, text="Show Tasks", command=show_tasks_for_date, width=20, bg="blue", fg="white")
show_tasks_btn.pack(pady=5)

delete_task_btn = tk.Button(root, text="Delete Last Task", command=delete_task, width=20, bg="red", fg="white")
delete_task_btn.pack(pady=5)

# Label for task display
task_display_label = tk.Label(root, text="Task To-Do", font=("Arial", 16, "bold"))
task_display_label.pack(pady=5)

# Task Display
task_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, font=("Arial", 12))
task_display.pack(pady=10)

# Run the app
root.mainloop()

# Close the database connection on exit
conn.close()
