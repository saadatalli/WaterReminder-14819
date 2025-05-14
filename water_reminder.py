import tkinter as tk
from tkinter import messagebox

def calculate_water_intake(weight, age):
    if age < 0 or weight < 0:
        raise ValueError("Weight and age must be non-negative.")

    water_intake = weight * 0.033  
    if age < 18:
        interval = 3
    elif age < 50:
        interval = 2
    else:
        interval = 1.5

    if age < 18:
        temp = "cool"
    elif age < 50:
        temp = "room temperature"
    else:
        temp = "lukewarm"

    return round(water_intake, 2), interval, temp

def on_calculate():
    try:
        weight = float(entry_weight.get())
        age = int(entry_age.get())
        water, interval, temp = calculate_water_intake(weight, age)
        result.set(f"Drink {water}L/day.\nReminder: every {interval} hours.\nWater temp: {temp}")
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error: {e}")


root = tk.Tk()
root.title("Water Intake Reminder")

tk.Label(root, text="Enter Weight (kg):").grid(row=0, column=0)
entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1)

tk.Label(root, text="Enter Age:").grid(row=1, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1)

tk.Button(root, text="Calculate", command=on_calculate).grid(row=2, column=0, columnspan=2)

result = tk.StringVar()
tk.Label(root, textvariable=result, fg="blue").grid(row=3, column=0, columnspan=2)

root.mainloop()
