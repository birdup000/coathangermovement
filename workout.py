import tkinter as tk

root = tk.Tk()
root.title("Workout Log")
root.geometry("800x600")

units = {"lbs", "kg"}

workouts = {
    "Weightlifting": ["Bench Press", "Deadlift", "Squat", "Bicep Curls", "Tricep Dips"],
    "Cardio": ["Running", "Cycling", "Swimming"],
    "Yoga": ["Vinyasa", "Hatha", "Bikram", "Ashtanga", "Iyengar"]
}

def update_exercise_dropdown(*args):
    exercise_dropdown['menu'].delete(0, 'end')
    for exercise in workouts[workout_type_var.get()]:
        exercise_dropdown['menu'].add_command(label=exercise, command=tk._setit(exercise_var, exercise))

workout_type_var = tk.StringVar(value="Weightlifting")
exercise_var = tk.StringVar(value=workouts[workout_type_var.get()][0])
sets_var = tk.StringVar(value="1")
reps_var = tk.StringVar(value="10")
units_var = tk.StringVar(value="lbs")

workout_type_dropdown = tk.OptionMenu(root, workout_type_var, *workouts.keys(), command=update_exercise_dropdown)
exercise_dropdown = tk.OptionMenu(root, exercise_var, *workouts[workout_type_var.get()])
tk.Label(root, text="Sets:").grid(row=2, column=0, pady=10)
tk.Entry(root, textvariable=sets_var).grid(row=2, column=1, pady=5)
tk.Label(root, text="Reps:").grid(row=3, column=0, pady=10)
tk.Entry(root, textvariable=reps_var).grid(row=3, column=1, pady=5)
units_dropdown = tk.OptionMenu(root, units_var, *units)

for i, widget in enumerate([workout_type_dropdown, exercise_dropdown, units_dropdown]):
    widget.grid(row=i, column=0, pady=10, padx=10)

def add_workout():
    workout_list.insert(tk.END, f"{workout_type_var.get()} - {exercise_var.get()} - {sets_var.get()} sets, {reps_var.get()} reps - {units_var.get()}")

workout_list = tk.Listbox(root, height=20, width=50)
workout_list.grid(row=0, column=1, rowspan=4, padx=10, pady=10)

tk.Button(root, text="Add Workout", command=add_workout).grid(row=4, column=0, pady=10)

def calculate_bmi():
    height = float(height_var.get())
    weight = float(weight_var.get())
    bmi = round(weight / (height / 100) ** 2, 1)
    result_var.set(f"BMI: {bmi}")

height_var = tk.StringVar()
weight_var = tk.StringVar()
result_var = tk.StringVar()

tk.Label(root, text="Height (cm):").grid(row=5, column=0, pady=10)
tk.Entry(root, textvariable=height_var).grid(row=5, column=1, pady=5)
tk.Label(root, text="Weight (kg):").grid(row=6, column=0, pady=10)
tk.Entry(root, textvariable=weight_var).grid(row=6, column=1, pady=5)
tk.Button(root, text="Calculate BMI", command=calculate_bmi).grid(row=7, column=0, pady=10)
tk.Label(root, textvariable=result_var).grid(row=7, column=1, pady=10)

root.mainloop ()