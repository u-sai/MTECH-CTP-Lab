students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    total_classes = int(input("Enter total classes conducted: "))
    attended_classes = int(input("Enter total classes attended: "))

    if total_classes <= 0:
        print("Total classes must be greater than 0.")
        continue

    if attended_classes < 0 or attended_classes > total_classes:
        print("Invalid attended classes.")
        continue

    attendance_percentage = (attended_classes / total_classes) * 100

    students.append({
        "name": name,
        "total_classes": total_classes,
        "attended_classes": attended_classes,
        "attendance_percentage": attendance_percentage
    })

if len(students) == 0:
    print("\nNo valid student data available.")

else:
    highest_student = students[0]
    total_attendance_percentage = 0

    print("\n========================================")
    print("       STUDENT ATTENDANCE REPORT")
    print("========================================")

    for student in students:
        print("\nStudent Name       :", student["name"])
        print("Total Classes      :", student["total_classes"])
        print("Classes Attended   :", student["attended_classes"])
        print("Attendance %       :", f"{student['attendance_percentage']:.2f}%")

        total_attendance_percentage += student["attendance_percentage"]

        if student["attendance_percentage"] > highest_student["attendance_percentage"]:
            highest_student = student

    average_attendance = total_attendance_percentage / len(students)

    print("\n========================================")
    print("         ATTENDANCE ANALYSIS")
    print("========================================")

    print("\nStudent with Highest Attendance")
    print("Name         :", highest_student["name"])
    print("Attendance % :", f"{highest_student['attendance_percentage']:.2f}%")

    print("\nAverage Class Attendance")
    print("Average      :", f"{average_attendance:.2f}%")

    print("\n========================================")