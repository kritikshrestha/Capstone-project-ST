import tkinter as tk

from CVD_model import *
# create the main window
root = tk.Tk()
root.title("Student Performance Predictor")

# Load the student scores dataset
data = pd.read_csv('exams.csv')



# create labels for each form field
gender_label = tk.Label(root, text="Gender:")
race_label = tk.Label(root, text="Race/Ethnicity:")
parental_education_label = tk.Label(root, text="Parental Level of Education:")
lunch_label = tk.Label(root, text="Lunch:")
math_score_label = tk.Label(root, text="Math Score:")
reading_score_label = tk.Label(root, text="Reading Score:")
writing_score_label = tk.Label(root, text="Writing Score:")

# create dropdown menus for each form field
gender_options = ["Male", "Female"]
gender_var = tk.StringVar(root)
gender_dropdown = tk.OptionMenu(root, gender_var, *gender_options)

race_options = ["Group A", "Group B", "Group C", "Group D", "Group E"]
race_var = tk.StringVar(root)
race_dropdown = tk.OptionMenu(root, race_var, *race_options)

education_options = ["Some High School", "High School", "Some College", "Associate's Degree", "Bachelor's Degree", "Master's Degree"]
education_var = tk.StringVar(root)
education_dropdown = tk.OptionMenu(root, education_var, *education_options)

lunch_options = ["Standard", "Free/Reduced"]
lunch_var = tk.StringVar(root)
lunch_dropdown = tk.OptionMenu(root, lunch_var, *lunch_options)

# create entry widgets for each form field
math_score_entry = tk.Entry(root)
reading_score_entry = tk.Entry(root)
writing_score_entry = tk.Entry(root)


# create a function to handle form submission
def predict():
    gender = gender_var.get()
    if (gender == "Male"):
        gender = 1
    else:
        gender = 0
    race = race_var.get()
    education = education_var.get()
    lunch = lunch_var.get()
    math_score = int(math_score_entry.get())
    if math_score>=50:
        print("you have higher chance of passing the exam")
    elif math_score<=50:
        print("you have higher chance of failing the exam")
    reading_score = int(reading_score_entry.get())
    if reading_score>=50:
        print("you have higher chance of passing the exam")
    elif reading_score<=50:
        print("you have higher chance of failing the exam")
    writing_score = int(writing_score_entry.get())
    if writing_score>=50:
        print("you have higher chance of passing the exam")
    elif writing_score<=50:
        print("you have higher chance of failing the exam")

# create a button to submit the form
submit_button = tk.Button(root, text="Predict", command=predict)

# arrange the form elements on the grid
gender_label.grid(row=0, column=0)
gender_dropdown.grid(row=0, column=1)
race_label.grid(row=1, column=0)
race_dropdown.grid(row=1, column=1)
parental_education_label.grid(row=2, column=0)
education_dropdown.grid(row=2, column=1)
lunch_label.grid(row=3, column=0)
lunch_dropdown.grid(row=3, column=1)
math_score_label.grid(row=4, column=0)
math_score_entry.grid(row=4, column=1)
reading_score_label.grid(row=5, column=0)
reading_score_entry.grid(row=5, column=1)
writing_score_label.grid(row=6, column=0)
writing_score_entry.grid(row=6, column=1)
submit_button.grid(row=7, column=1)

# start the main event loop
root.mainloop()
