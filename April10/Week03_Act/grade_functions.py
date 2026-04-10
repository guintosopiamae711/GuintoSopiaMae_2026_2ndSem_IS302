def calculate_average(grade1_nbs, grade2_nbs, grade3_nbs):
    """Calculate the average of three grades"""
    return (grade1_nbs + grade2_nbs + grade3_nbs) / 3

def get_remark(average_nbs):
    """Return the remark based on the average grade"""
    if average_nbs >= 90:
        return "Excellent"
    elif average_nbs >= 85:
        return "Very Good"
    elif average_nbs >= 80:
        return "Good"
    elif average_nbs >= 75:
        return "Fair"
    else:
        return "Failed"

# Main program
print("----- STUDENT GRADE PROCESSOR -----")
student_name = input("Enter student name: ")
grade1_nbs = float(input("Enter first grade: "))
grade2_nbs = float(input("Enter second grade: "))
grade3_nbs = float(input("Enter third grade: "))

# Calculate average and get remark
average_nbs = calculate_average(grade1_nbs, grade2_nbs, grade3_nbs)
remark_nbs = get_remark(average_nbs)

# Display results
print("\n----- RESULTS -----")
print("Student Name:", student_name)
print("Grade 1:", grade1_nbs)
print("Grade 2:", grade2_nbs)
print("Grade 3:", grade3_nbs)
print("Average:", round(average_nbs, 2))
print("Remark:", remark_nbs)
