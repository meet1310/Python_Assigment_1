students = []

# Number of students
n = int(input("Enter number of students: "))

# Taking student details
for i in range(n):
    print("\nEnter details for Student", i + 1)

    enrollment = input("Enrollment No: ")
    name = input("Name: ")
    semester = int(input("Semester: "))
    cpi = float(input("CPI: "))

    # Taking subject marks
    marks = []
    subjects = int(input("Enter number of subjects: "))

    for j in range(subjects):
        mark = float(input(f"Enter marks for Subject {j + 1}: "))
        marks.append(mark)

    # Tuple for student record
    student = (enrollment, name, semester, cpi, marks)

    # Store tuple inside list
    students.append(student)


# Number of top students required
k = int(input("\nEnter K (number of top students): "))


# Group students semester-wise using dictionary
semester_data = {}

for student in students:
    semester = student[2]

    if semester not in semester_data:
        semester_data[semester] = []

    semester_data[semester].append(student)


# Display semester-wise results
print("\n========== CAMPUS MERIT ANALYZER ==========")

for semester in sorted(semester_data):

    print(f"\n--- Semester {semester} ---")

    # Sort students according to CPI
    sorted_students = sorted(
        semester_data[semester],
        key=lambda x: x[3],
        reverse=True
    )

    print(f"Top {k} Students:")

    for rank, student in enumerate(sorted_students[:k], start=1):

        enrollment = student[0]
        name = student[1]
        cpi = student[3]
        marks = student[4]

        average_marks = sum(marks) / len(marks)

        print(
            f"{rank}. {name} "
            f"(Enrollment: {enrollment}) "
            f"- CPI: {cpi:.2f}, "
            f"Average Marks: {average_marks:.2f}"
        )


# Overall statistics
print("\n========== OVERALL STATISTICS ==========")

total_students = len(students)

print("Total Students:", total_students)

# Average CPI
total_cpi = sum(student[3] for student in students)
average_cpi = total_cpi / total_students

print(f"Average CPI: {average_cpi:.2f}")


# Highest CPI student
highest_student = max(students, key=lambda x: x[3])

print(
    "Highest CPI Student:",
    highest_student[1],
    f"({highest_student[3]:.2f})"
)