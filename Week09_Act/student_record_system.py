# Ask the user to input student name and course
name_smg = input("Enter student name: ")
course_smg = input("Enter course: ")

# Save the record to students.txt in append mode
with open("students.txt", "a") as file_smg:
    file_smg.write(name_smg + "," + course_smg + "\n")

# Display all student records
print("\nStudent Records:")
with open("students.txt", "r") as file_smg:
    for line_smg in file_smg:
        print(line_smg.strip())