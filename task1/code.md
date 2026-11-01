# University Scholarship Allocation System

# Scholarship Eligibility Criteria
MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 40
MIN_ATTENDANCE = 75
MAX_INCOME = 300000

eligible_students = []
rejected_students = []

# Input number of students
n = int(input("Enter number of students: "))

for i in range(n):

    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")

    aggregate = float(input("Enter aggregate percentage: "))

    print("Enter marks for 5 subjects:")
    subjects = []

    for j in range(5):
        mark = float(input(f"Subject {j+1}: "))
        subjects.append(mark)

    attendance = float(input("Enter attendance percentage: "))

    income = float(input("Enter annual family income: "))

    # Check eligibility conditions
    if (aggregate >= MIN_AGGREGATE and
        all(mark >= MIN_SUBJECT_MARKS for mark in subjects) and
        attendance >= MIN_ATTENDANCE and
        income <= MAX_INCOME):

        student = {
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        }

        eligible_students.append(student)

    else:
        rejected_students.append(name)


# Sort students using tie-breaking rules
eligible_students.sort(
    key=lambda x: (
        -x["aggregate"],
        -x["attendance"],
        x["income"]
    )
)

# Display eligible students
print("\n========== SCHOLARSHIP ALLOCATION RESULTS ==========")

if eligible_students:

    print("\nEligible Students (Rank Wise):")

    for rank, student in enumerate(eligible_students, start=1):

        print("\nRank:", rank)
        print("Name:", student["name"])
        print("Aggregate:", student["aggregate"], "%")
        print("Attendance:", student["attendance"], "%")
        print("Family Income: Rs.", student["income"])
        print("Scholarship Status: SELECTED")

else:
    print("\nNo students are eligible for scholarship.")

# Display rejected students
print("\n========== NOT ELIGIBLE STUDENTS ==========")

if rejected_students:
    for name in rejected_students:
        print(name)
else:
    print("No rejected students.")

print("\n========== END OF PROGRAM ==========")
In this you have to write the alroithm,flowchart,python source code,samplce input,sample output,and the flow chart in mermaid
