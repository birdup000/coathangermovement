import tkinter as tk

root = tk.Tk()
root.title("Workout Log")
root.geometry("800x600")

workouts = {
    "Weightlifting": ["Bench Press", "Deadlift", "Squat", "Bicep Curls", "Tricep Dips"],
    "Cardio": ["Running", "Cycling", "Swimming"],
    "Yoga": ["Vinyasa", "Hatha", "Bikram", "Ashtanga", "Iyengar"]
}

# Add BMI Calculator
def calculate_bmi():
    try:
        weight = float(weight_var.get())
        height = float(height_var.get())
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive")
        if weight_unit_var.get() == "kg":
            bmi = weight / (height/100)**2
        else:
            bmi = (weight * 703) / height**2
        bmi_var.set(f"{bmi:.2f}")
    except ValueError as e:
        bmi_var.set(str(e))

weight_var, height_var, weight_unit_var, bmi_var = tk.StringVar(), tk.StringVar(), tk.StringVar(value="kg"), tk.StringVar()
tk.Label(root, text="BMI Calculator").pack(pady=10)
tk.Entry(root, textvariable=weight_var).pack(pady=5)
tk.Label(root, text="Weight Unit:").pack(pady=10)
tk.OptionMenu(root, weight_unit_var, "kg", "lbs").pack(pady=5)
tk.Entry(root, textvariable=height_var).pack(pady=5)
tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=5)
tk.Label(root, text="BMI:").pack(pady=10)
tk.Label(root, textvariable=bmi_var).pack(pady=5)

# Add workout log
workout_type_var, exercise_var, sets_var, reps_var = tk.StringVar(value="Weightlifting"), tk.StringVar(), tk.StringVar(value="1"), tk.StringVar(value="10")
tk.OptionMenu(root, workout_type_var, *workouts.keys(), command=lambda _: (exercise_var.set(workouts[workout_type_var.get()][0]), [exercise_dropdown['menu'].add_command(label=exercise, command=lambda exercise=exercise: exercise_var.set(exercise)) for exercise in workouts[workout_type_var.get()]]),).pack(pady=10)
exercise_dropdown = tk.OptionMenu(root, exercise_var, *workouts[workout_type_var.get()])
exercise_dropdown.pack(pady=10)
tk.Label(root, text="Sets:").pack(pady=10)
tk.Entry(root, textvariable=sets_var).pack(pady=5)
tk.Label(root, text="Reps:").pack(pady=10)
tk.Entry(root, textvariable=reps_var).pack(pady=5)
workout_list = tk.Listbox(root, height=20, width=50)
workout_list.pack(pady=10)
tk.Button(root, text="Add Workout", command=lambda: workout_list.insert(tk.END, f"{workout_type_var.get()} - {exercise_var.get()} - {sets_var.get()} sets, {reps_var.get()} reps")).pack(pady=10)

root.mainloop()