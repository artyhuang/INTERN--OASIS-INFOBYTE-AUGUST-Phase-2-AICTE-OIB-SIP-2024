import tkinter as tk
from tkinter import messagebox

def calculate_bmi(height, weight):
    if height <= 0:
        return None
    bmi = weight / (height ** 2)
    return round(bmi, 1)

def bmi_classification(bmi):
    if bmi is None:
        return "Invalid input"
    elif bmi <= 18.4:
        return "Underweight"
    elif bmi <= 24.9:
        return "Normal"
    elif bmi <= 39.9:
        return "Overweight"
    else:
        return "Obese"

def on_calculate():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        bmi = calculate_bmi(height, weight)
        classification = bmi_classification(bmi)
        messagebox.showinfo("BMI Result", f"Your BMI is: {bmi}\n You are {classification} person")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

app = tk.Tk()
app.title("BMI Calculator")
tk.Label(app, text="Height (m):").grid(row=0, column=0, padx=10, pady=10)
height_entry = tk.Entry(app)
height_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Label(app, text="Weight (kg):").grid(row=1, column=0, padx=10, pady=10)
weight_entry = tk.Entry(app)
weight_entry.grid(row=1, column=1, padx=10, pady=10)
calculate_button = tk.Button(app, text="Calculate BMI", command=on_calculate)
calculate_button.grid(row=2, columnspan=2, pady=20)
app.mainloop()
