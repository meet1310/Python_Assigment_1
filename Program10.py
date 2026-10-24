import tkinter as tk

FILE = "assignments.txt"


def add_assignment():
    assignment = entry.get()

    if assignment:
        with open(FILE, "a") as f:
            f.write(assignment + "\n")

        listbox.insert(tk.END, assignment)
        entry.delete(0, tk.END)


def load_assignments():
    try:
        with open(FILE, "r") as f:
            for assignment in f:
                listbox.insert(tk.END, assignment.strip())
    except FileNotFoundError:
        pass


# GUI
root = tk.Tk()
root.title("Assignment Tracker")
root.geometry("400x300")

tk.Label(root, text="Assignment Name").pack(pady=10)

entry = tk.Entry(root, width=35)
entry.pack()

tk.Button(root, text="Add Assignment",
          command=add_assignment).pack(pady=10)

listbox = tk.Listbox(root, width=45, height=10)
listbox.pack()

load_assignments()

root.mainloop()