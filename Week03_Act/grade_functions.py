def calculate_average(grade1_smg, grade2_smg, grade3_smg):
    """Calculate the average of three grades"""
    return (grade1_smg + grade2_smg + grade3_smg) / 3

def get_remark(average_smg):
    """Return the remark based on the average grade"""
    if average_smg >= 90:
        return "Excellent"
    elif average_smg >= 85:
        return "Very Good"
    elif average_smg >= 80:
        return "Good"
    elif average_smg >= 75:
        return "Fair"
    else:
        return "Failed"

# Main program
print("----- STUDENT GRADE PROCESSOR -----")
student_name_smg = input("Enter student name: ")
grade1_smg = float(input("Enter first grade: "))
grade2_smg = float(input("Enter second grade: "))
grade3_smg = float(input("Enter third grade: "))

# Calculate average and get remark
average_smg = calculate_average(grade1_smg, grade2_smg, grade3_smg)
remark_smg = get_remark(average_smg)

# Display results
print("\n----- RESULTS -----")
print("Student Name:", student_name_smg)
print("Grade 1:", grade1_smg)
print("Grade 2:", grade2_smg)
print("Grade 3:", grade3_smg)
print("Average:", round(average_smg, 2))
print("Remark:", remark_smg)
