import tkinter as tk

root = tk.Tk()
root.title("Workout Log")
root.geometry("800x600")

# Create a dictionary of workout types and their corresponding exercises
workouts = {
    "Weightlifting": ["Bench Press", "Deadlift", "Squat", "Bicep Curls", "Tricep Dips"],
    "Cardio": ["Running", "Cycling", "Swimming"],
    "Yoga": ["Vinyasa", "Hatha", "Bikram", "Ashtanga", "Iyengar"]
}

# Create a drop-down menu for selecting the workout type
workout_type_var = tk.StringVar(value="Weightlifting")
workout_type_dropdown = tk.OptionMenu(root, workout_type_var, *workouts.keys())
workout_type_dropdown.pack(pady=10)

# Create a drop-down menu for selecting the specific exercise
exercise_var = tk.StringVar(value=workouts[workout_type_var.get()][0])
exercise_dropdown = tk.OptionMenu(root, exercise_var, *workouts[workout_type_var.get()])
exercise_dropdown.pack(pady=10)

# Update the exercise options when the workout type is changed
def update_exercise_options(*args):
    exercise_dropdown["menu"].delete(0, "end")
    for exercise in workouts[workout_type_var.get()]:
        exercise_dropdown["menu"].add_command(label=exercise, command=tk._setit(exercise_var, exercise))

workout_type_var.trace("w", update_exercise_options)

# Create an entry field for specifying the number of sets and reps
sets_var = tk.StringVar(value="1")
sets_label = tk.Label(root, text="Sets:")
sets_label.pack(pady=10)
sets_entry = tk.Entry(root, textvariable=sets_var)
sets_entry.pack(pady=5)

reps_var = tk.StringVar(value="10")
reps_label = tk.Label(root, text="Reps:")
reps_label.pack(pady=10)
reps_entry = tk.Entry(root, textvariable=reps_var)
reps_entry.pack(pady=5)

# Create a list to display the workout history
workout_list = tk.Listbox(root, height=20, width=50)
workout_list.pack(pady=10)

# Create a button to add the workout
def add_workout():
    workout = f"{workout_type_var.get()} - {exercise_var.get()} - {sets_var.get()} sets, {reps_var.get()} reps"
    workout_list.insert(tk.END, workout)

add_button = tk.Button(root, text="Add Workout", command=add_workout)
add_button.pack(pady=10)

root.mainloop()
