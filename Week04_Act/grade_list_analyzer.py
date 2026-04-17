print("----- GRADE LIST ANALYZER -----")
grades_smg = []

# Ask user to enter 5 grades
for i_smg in range(1, 6):
    grade_smg = float(input(f"Enter grade {i_smg}: "))
    grades_smg.append(grade_smg)

# Compute statistics
average_grade_smg = sum(grades_smg) / len(grades_smg)
highest_grade_smg = max(grades_smg)
lowest_grade_smg = min(grades_smg)

# Display results
print("\n----- RESULTS -----")
print("Grades:", grades_smg)
print("Average Grade:", round(average_grade_smg, 1))
print("Highest Grade:", highest_grade_smg)
print("Lowest Grade:", lowest_grade_smg)
