print("----- GRADE LIST ANALYZER -----")
grades_nbs = []

# Ask user to enter 5 grades
for i in range(1, 6):
    grade = float(input(f"Enter grade {i}: "))
    grades_nbs.append(grade)

# Compute statistics
average_grade_nbs = sum(grades_nbs) / len(grades_nbs)
highest_grade_nbs = max(grades_nbs)
lowest_grade_nbs = min(grades_nbs)

# Display results
print("\n----- RESULTS -----")
print("Grades:", grades_nbs)
print("Average Grade:", round(average_grade_nbs, 1))
print("Highest Grade:", highest_grade_nbs)
print("Lowest Grade:", lowest_grade_nbs)
