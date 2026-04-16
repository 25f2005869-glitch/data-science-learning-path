"""
Author: Saloni Tiwari
Topic: Advanced Matrix Calculator GUI
Week: Practice Project
Description: Colorful GUI with NumPy operations + Save + Determinant + Inverse
"""

import tkinter as tk
from tkinter import filedialog
import numpy as np

# Convert text to matrix
def get_matrix(text):
    try:
        rows = text.strip().split("\n")
        matrix = [list(map(float, row.split())) for row in rows]
        return np.array(matrix)
    except:
        return None

# Format result as table
def format_matrix(mat):
    return "\n".join(["\t".join([f"{val:.2f}" for val in row]) for row in mat])

# Save result to file
def save_result():
    data = result_label["text"]
    file = filedialog.asksaveasfilename(defaultextension=".txt")
    if file:
        with open(file, "w") as f:
            f.write(data)

# Operations
def calculate(op):
    A = get_matrix(text_A.get("1.0", tk.END))
    B = get_matrix(text_B.get("1.0", tk.END))

    if A is None:
        result_label.config(text="❌ Invalid Matrix A")
        return

    try:
        if op == "add":
            result = A + B
        elif op == "sub":
            result = A - B
        elif op == "mul":
            if A.shape[1] != B.shape[0]:
                result_label.config(text="❌ Multiplication not possible")
                return
            result = np.dot(A, B)
        elif op == "det":
            result = np.linalg.det(A)
            result_label.config(text=f"Determinant: {result:.2f}")
            return
        elif op == "inv":
            result = np.linalg.inv(A)
        
        result_label.config(text="Result:\n" + format_matrix(result))

    except Exception as e:
        result_label.config(text="❌ Error: " + str(e))

# GUI Window
root = tk.Tk()
root.title("Advanced Matrix Calculator")
root.geometry("550x650")
root.config(bg="#1e1e2f")

# Title
tk.Label(root, text="Matrix Calculator", font=("Arial", 18, "bold"),
         bg="#1e1e2f", fg="#00ffcc").pack(pady=10)

# Matrix A
tk.Label(root, text="Matrix A", bg="#1e1e2f", fg="white").pack()
text_A = tk.Text(root, height=5, width=45, bg="#2e2e3f", fg="white")
text_A.pack(pady=5)

# Matrix B
tk.Label(root, text="Matrix B", bg="#1e1e2f", fg="white").pack()
text_B = tk.Text(root, height=5, width=45, bg="#2e2e3f", fg="white")
text_B.pack(pady=5)

# Buttons Frame
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=10)

btn_style = {"width":12, "bg":"#00ffcc", "fg":"black", "font":("Arial", 10, "bold")}

tk.Button(frame, text="Add", command=lambda: calculate("add"), **btn_style).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame, text="Subtract", command=lambda: calculate("sub"), **btn_style).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame, text="Multiply", command=lambda: calculate("mul"), **btn_style).grid(row=0, column=2, padx=5, pady=5)

tk.Button(frame, text="Determinant", command=lambda: calculate("det"), **btn_style).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame, text="Inverse", command=lambda: calculate("inv"), **btn_style).grid(row=1, column=1, padx=5, pady=5)
tk.Button(frame, text="Save Result", command=save_result, **btn_style).grid(row=1, column=2, padx=5, pady=5)

# Result Label
result_label = tk.Label(root, text="Result will appear here",
                        bg="#1e1e2f", fg="white", font=("Consolas", 11), justify="left")
result_label.pack(pady=20)

# Run
root.mainloop()