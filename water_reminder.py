import tkinter as tk
from tkinter import messagebox

def calculate_water_intake(weight, age):
    if age <= 0 or weight <= 0:
        raise ValueError("Weight and age must be greater than zero.")

    water_intake = weight * 0.033  
    if age < 18:
        interval = 3
    elif age < 50:
        interval = 2
    else:
        interval = 1.5

    return round(water_intake, 2), interval

def on_calculate():
    weight_input = entry_weight.get().strip()
    age_input = entry_age.get().strip()

    if not weight_input or not age_input:
        messagebox.showerror("Input Error", "Please enter both weight and age.")
        return

    try:
        weight = float(weight_input)
        age = int(age_input)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter numeric values for weight and age.")
        return

    if weight <= 0 or age <= 0:
        messagebox.showerror("Input Error", "Weight and age must be greater than zero.")
        return

    try:
        water, interval = calculate_water_intake(weight, age)
        result.set(f"Drink {water}L/day.\nReminder: every {interval} hours.")
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error: {e}")

root = tk.Tk()
root.title("Water Intake Reminder")

tk.Label(root, text="Enter Weight (kg):").grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter Age:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Calculate", command=on_calculate).grid(row=2, column=0, columnspan=2, pady=10)

result = tk.StringVar()
tk.Label(root, textvariable=result, fg="blue").grid(row=3, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
