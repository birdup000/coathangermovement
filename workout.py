import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title("Workout Log")

def add_workout():
    workout_type = workout_var.get()
    if workout_type == "Weightlifting":
        weightlifting_type = weightlifting_var.get()
        workout_list.insert(tk.END, f"{workout_type}: {weightlifting_type}")
    elif workout_type == "Swimming":
        swimming_type = swimming_var.get()
        workout_list.insert(tk.END, f"{workout_type}: {swimming_type}")
    elif workout_type == "Yoga":
        yoga_type = yoga_var.get()
        workout_list.insert(tk.END, f"{workout_type}: {yoga_type}")
    else:
        workout_list.insert(tk.END, workout_var.get())
    save_workouts()

def remove_workout():
    workout_list.delete(tk.ANCHOR)
    save_workouts()

def save_workouts():
    with open("workouts.txt", "w") as f:
        for item in workout_list.get(0, tk.END):
            f.write(f"{item}\n")

def load_workouts():
    if os.path.exists("workouts.txt"):
        with open("workouts.txt") as f:
            for item in f:
                workout_list.insert(tk.END, item.strip())

# Create a dictionary of workout icons
icon_path = "workout_icons"
workout_icons = {
    "Running": ImageTk.PhotoImage(Image.open(os.path.join(icon_path, "running.png"))),
    "Cycling": ImageTk.PhotoImage(Image.open(os.path.join(icon_path, "cycling.png"))),
    "Weightlifting": ImageTk.PhotoImage(Image.open(os.path.join(icon_path, "weightlifting.png"))),
    "Swimming": ImageTk.PhotoImage(Image.open(os.path.join(icon_path, "swimming.png"))),
    "Yoga": ImageTk.PhotoImage(Image.open(os.path.join(icon_path, "yoga.png")))
}

# Create a drop-down menu for selecting the workout type
workout_var = tk.StringVar(value="Running")
workout_dropdown = tk.OptionMenu(root, workout_var, *workout_icons.keys(), image=workout_icons["Running"], compound="left")
workout_dropdown.pack(pady=10)

# Create a drop-down menu for selecting the weightlifting type
weightlifting_frame = tk.Frame(root)
weightlifting_var = tk.StringVar(value="Bench Press")
weightlifting_types = [    "Bench Press",    "Deadlift",    "Squat",    "Bicep Curls",    "Tricep Dips"]
weightlifting_dropdown = ttk.Combobox(weightlifting_frame, textvariable=weightlifting_var, values=weightlifting_types)
weightlifting_dropdown.pack(pady=10)
weightlifting_frame.pack()

# Create a drop-down menu for selecting the swimming type
swimming_frame = tk.Frame(root)
swimming_var = tk.StringVar(value="Freestyle")
swimming_types = [    "Freestyle",    "Backstroke",    "Breaststroke",    "Butterfly"]
swimming_dropdown = ttk.Combobox(swimming_frame, textvariable=swimming_var, values=swimming_types)
swimming_dropdown.pack(pady=10)
swimming_frame.pack()

# Create a drop-down menu for selecting the yoga type
yoga_frame = tk.Frame(root)
yoga_var = tk.StringVar(value="Vinyasa")
yoga_types = [    "Vinyasa",    "Hatha",    "Bikram",    "Ashtanga",    "Iyengar"]
yoga_dropdown = ttk.Combobox(yoga_frame, textvariable=yoga_var, values=yoga_types)
yoga_dropdown.pack(pady=10)
yoga_frame.pack()

# Show only the relevant drop-down menu
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

workout_var.trace("w", lambda *args: show_dropdown(workout_var.get()))

# Create a list to display the workout history
workout_list = tk.Listbox(root)
workout_list.pack(pady=10)

# Create buttons to add and remove workouts
add_button = tk.Button(root, text="Add Workout", command=add_workout)
add_button.pack(pady=10)
remove_button = tk.Button(root, text="Remove Workout", command=remove_workout)
remove_button.pack(pady=10)

load_workouts()
root.mainloop()
