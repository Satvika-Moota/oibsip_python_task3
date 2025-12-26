import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

root = tk.Tk()
root.title("Secure Password Generator")
root.state("zoomed")
root.configure(bg="#0f172a")
root.resizable(False, False)

# ================= Background =================
bg_frame = tk.Frame(root, bg="#0f172a")
bg_frame.pack(fill="both", expand=True)

# ================= Header =================
header = tk.Frame(bg_frame, bg="#020617", height=90)
header.pack(fill="x")

tk.Label(header, text="🔐 Secure Password Generator", bg="#020617",
         fg="#e0e7ff", font=("Segoe UI", 24, "bold")).pack(pady=25)

# ================= Main Card =================
card = tk.Frame(bg_frame, bg="#020617", width=520, height=630)
card.place(relx=0.5, rely=0.53, anchor="center")
card.pack_propagate(False)

# ================= Input =================
tk.Label(card, text="Password Length", fg="#a5b4fc",
         bg="#020617", font=("Segoe UI", 16, "bold")).pack(pady=(25, 6))

length_entry = tk.Entry(card, font=("Segoe UI", 17), justify="center",
                        bg="#1e293b", fg="white", insertbackground="white",
                        relief="flat")
length_entry.pack(ipady=10, fill="x", padx=35)
length_entry.insert(0, "12")

# ================= Options =================
upper = tk.IntVar(value=1)
lower = tk.IntVar(value=1)
digits = tk.IntVar(value=1)
symbols = tk.IntVar(value=1)
exclude = tk.IntVar()

def make_check(text, var):
    tk.Checkbutton(card, text=text, variable=var, fg="#e0e7ff", bg="#020617",
                   activebackground="#020617", activeforeground="#e0e7ff",
                   selectcolor="#020617", font=("Segoe UI", 11)).pack(anchor="w", padx=60, pady=5)

make_check("Uppercase Letters", upper)
make_check("Lowercase Letters", lower)
make_check("Numbers", digits)
make_check("Symbols", symbols)
make_check("Exclude Similar (O, 0, l, 1)", exclude)

# ================= Result =================
tk.Label(card, text="Generated Password", fg="#a5b4fc",
         bg="#020617", font=("Segoe UI", 16)).pack(pady=(18, 6))

result_entry = tk.Entry(card, font=("Segoe UI", 17), justify="center",
                        bg="#020617", fg="#c8dbe3",
                        insertbackground="white", relief="flat")
result_entry.pack(ipady=12, fill="x", padx=35)

# ================= Functions =================
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password must be at least 4 characters")
            return

        chars = ""
        if upper.get(): chars += string.ascii_uppercase
        if lower.get(): chars += string.ascii_lowercase
        if digits.get(): chars += string.digits
        if symbols.get(): chars += string.punctuation

        if exclude.get():
            for ch in "O0l1":
                chars = chars.replace(ch, "")

        if not chars:
            messagebox.showerror("Error", "Select at least one option!")
            return

        pwd = "".join(random.choice(chars) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, pwd)

    except:
        messagebox.showerror("Error", "Enter valid number")

def copy_password():
    if result_entry.get():
        pyperclip.copy(result_entry.get())
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "Generate password first!")

# ================= Buttons =================
btn_style = {"font":("Segoe UI",12,"bold"),"relief":"flat","fg":"white"}

tk.Button(card, text="Generate Password", command=generate_password,
          bg="#6366f1", **btn_style).pack(fill="x", padx=35, pady=(22,6), ipady=12)

tk.Button(card, text="Copy to Clipboard", command=copy_password,
          bg="#22c55e", **btn_style).pack(fill="x", padx=35, pady=(0,10), ipady=12)

root.mainloop()
