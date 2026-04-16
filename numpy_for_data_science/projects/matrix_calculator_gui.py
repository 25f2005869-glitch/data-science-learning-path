"""
Author: Saloni Tiwari
Topic: NumPy Matrix Calculator (GUI)
Week: Practice Project
Description: GUI-based matrix calculator using Tkinter and NumPy
"""

import tkinter as tk
import numpy as np

# Function to convert text input into matrix
def get_matrix(text):
    try:
        rows = text.strip().split("\n")
        matrix = [list(map(int, row.split())) for row in rows]
        return np.array(matrix)
    except:
        return None

# Function to perform operation
def calculate(operation):
    A = get_matrix(text_A.get("1.0", tk.END))
    B = get_matrix(text_B.get("1.0", tk.END))

    if A is None or B is None:
        result_label.config(text="❌ Invalid matrix input")
        return

    try:
        if operation == "add":
            result = A + B
        elif operation == "sub":
            result = A - B
        elif operation == "mul":
            if A.shape[1] != B.shape[0]:
                result_label.config(text="❌ Multiplication not possible")
                return
            result = np.dot(A, B)

        result_label.config(text=f"Result:\n{result}")
    except:
        result_label.config(text="❌ Error occurred")

# Create window
root = tk.Tk()
root.title("Matrix Calculator GUI")
root.geometry("500x600")

# Title
tk.Label(root, text="Matrix Calculator", font=("Arial", 16, "bold")).pack(pady=10)

# Matrix A input
tk.Label(root, text="Matrix A (rows separated by newline)").pack()
text_A = tk.Text(root, height=5, width=40)
text_A.pack()

# Matrix B input
tk.Label(root, text="Matrix B (rows separated by newline)").pack()
text_B = tk.Text(root, height=5, width=40)
text_B.pack()

# Buttons
tk.Button(root, text="Add", width=15, command=lambda: calculate("add")).pack(pady=5)
tk.Button(root, text="Subtract", width=15, command=lambda: calculate("sub")).pack(pady=5)
tk.Button(root, text="Multiply", width=15, command=lambda: calculate("mul")).pack(pady=5)

# Result
result_label = tk.Label(root, text="Result will appear here", font=("Arial", 12))
result_label.pack(pady=20)

# Run app
root.mainloop()