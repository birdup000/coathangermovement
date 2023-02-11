import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk
root = tk.Tk()
root.title("Workout Log")
# Workout list
workout_list = tk.Listbox(root)
workout_list.pack(pady=10)
# Workout icons
icon_path = "workout_icons"
try:
    workout_icons = {
        "Running": ImageTk.PhotoImage(Image.open(os.path.join(icon_path, "running.png"))),
        "Cycling": ImageTk.PhotoImage(Image.open(os.path.join(icon_path, "cycling.png"))),
        "Weightlifting": ImageTk.PhotoImage(Image.open(os.path.join(icon_path, "weightlifting.png"))),
        "Swimming": ImageTk.PhotoImage(Image.open(os.path.join(icon_path, "swimming.png"))),
        "Yoga": ImageTk.PhotoImage(Image.open(os.path.join(icon_path, "yoga.png")))
    }
except FileNotFoundError as e:
    print(f"The file could not be found: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
# Workout dropdown
workout_var = tk.StringVar(value="Running")
workout_dropdown = tk.OptionMenu(root, workout_var, *workout_icons.keys(), image=workout_icons["Running"], compound="left")
workout_dropdown.pack(pady=10)
# Dropdown menu values
workout_types = {
    "Weightlifting": ["Bench Press", "Deadlift", "Squat", "Bicep Curls", "Tricep Dips"],
    "Swimming": ["Freestyle", "Backstroke", "Breaststroke", "Butterfly"],
    "Yoga": ["Vinyasa", "Hatha", "Bikram", "Ashtanga", "Iyengar"]
}
# Subdropdown frames
weightlifting_frame = tk.Frame(root)
swimming_frame = tk.Frame(root)
yoga_frame = tk.Frame(root)
# Subdropdown vars and comboboxes
weightlifting_var = tk.StringVar(value="Bench Press")
weightlifting_dropdown = ttk.Combobox(weightlifting_frame, textvariable=weightlifting_var, values=workout_types["Weightlifting"])
weightlifting_dropdown.pack(pady=10)
swimming_var = tk.StringVar(value="Freestyle")
swimming_dropdown = ttk.Combobox(swimming_frame, textvariable=swimming_var, values=workout_types["Swimming"])
swimming_dropdown.pack(pady=10)
yoga_var = tk.StringVar(value="Vinyasa")
yoga_dropdown = ttk.Combobox(yoga_frame, textvariable=yoga_var, values=workout_types["Yoga"])
yoga_dropdown.pack(pady=10)
# Show relevant subdropdown
def show_dropdown(workout_type):
    weightlifting_frame.pack_forget()
    swimming_frame.pack_forget()
    yoga_frame.pack_forget()
    if workout_type == "Weightlifting":
        weightlifting_frame.pack()
    elif workout_type == "Swimming":
        swimming_frame.pack()
    elif workout_type == "Yoga":
        yoga_frame.pack()
# Triggered on workout type change
def change_workout(*args):
    try:
        workout_type = workout_var.get()
        workout_dropdown.config(image=workout_icons[workout_type])
        show_dropdown(workout_type)
    except KeyError as e:
        print(f"The specified workout type is not an option: {e}")
try:
    workout_var.trace("w", change_workout)
except Exception as e:
    print(f"An unexpected error occurred when tracing the workout variable variable: {e}")
try:
    change_workout()
except Exception as e:
    print(f"An unexpected error occurred when changing the workout variable variable: {e}")
# add workout button
def add_workout():
    workout_name = workout_var.get()
    try:
        sub_workout = locals()[workout_name.lower() + "_var"].get()
        workout_list.insert("end", f"{workout_name}: {sub_workout}")
    except AttributeError as e:
        print(f"An attribute error has occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred when inserting the list item: {e}")
try:
    add_workout_button = tk.Button(root, text="Add Workout", command=add_workout)
    add_workout_button.pack(pady=10)
except Exception as e:
    print(f"An unexpected error occurred when creating the Add Workout button: {e}")
try:
    root.mainloop()
except Exception as e:
    print(f"An unexpected error occurred in mainloop: {e}")
