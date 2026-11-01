# University Scholarship Allocation System Using Python

## 1\. Problem Statement

The University Scholarship Allocation System is designed to evaluate students for scholarship eligibility based on their academic performance and financial background.

The system considers the following criteria:

1. **Aggregate Marks:** Students must obtain a minimum aggregate percentage.
2. **Subject-wise Minimum Marks:** Students must score the minimum required marks in every subject.
3. **Attendance:** Students must maintain the minimum attendance percentage.
4. **Family Income:** Students' annual family income must be within the specified limit.

The system identifies eligible students, ranks them according to their academic performance, and allocates scholarships based on predefined tie-breaking rules.

**Tie-breaking rules:**

- First preference: Higher aggregate percentage.
- Second preference: Higher attendance percentage.
- Third preference: Lower annual family income.

The system displays the list of eligible students in rank order along with their scholarship status.

## 2\. Algorithm

1. Start the program.
2. Set the minimum aggregate marks, subject-wise marks, attendance, and maximum family income criteria.
3. Enter the number of students.
4. For each student, input:
   - Student name.
   - Aggregate percentage.
   - Marks in each subject.
   - Attendance percentage.
   - Annual family income.
5. Check whether the student satisfies all eligibility conditions.
6. If all conditions are satisfied, add the student to the eligible list.
7. Otherwise, mark the student as not eligible.
8. Sort eligible students based on:
   - Higher aggregate marks.
   - Higher attendance.
   - Lower family income.
9. Assign ranks to eligible students.
10. Display the eligible students with their ranks.
11. Display the rejected students.
12. Stop the program.

## 3\. Flowchart (Mermaid Code)

Copy the following code into the Mermaid Live Editor to generate the flowchart.

[Mermaid Live Editor](<https://mermaid.live/?utm_source=chatgpt.com>)
```mermaid
flowchart TD
    A([Start]) --> B[Set Scholarship Criteria]
    B --> C[Enter Number of Students]
    C --> D[Enter Student Details]
    D --> E[Check Aggregate Marks]
    E --> F{Aggregate Marks >= Minimum?}
    F -- No --> K[Mark as Not Eligible]
    F -- Yes --> G[Check Subject-wise Marks]
    G --> H{All Subjects Pass?}
    H -- No --> K
    H -- Yes --> I[Check Attendance]
    I --> J{Attendance >= Minimum?}
    J -- No --> K
    J -- Yes --> L[Check Family Income]
    L --> M{Income Within Limit?}
    M -- No --> K
    M -- Yes --> N[Add to Eligible List]
    K --> O{More Students?}
    N --> O
    O -- Yes --> D
    O -- No --> P[Sort Eligible Students]
    P --> Q[Apply Tie-Breaking Rules]
    Q --> R[Assign Ranks]
    R --> S[Display Results]
    S --> T([Stop])
```

## 4\. Python Source Code

The following Python program evaluates scholarship applicants, checks eligibility, ranks students, and resolves ties using predefined rules.

University Scholarship Allocation System - Python Code

python

```python
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
```

## 5\. Sample Input

text

```text
Enter number of students: 4

Enter details of Student 1
Enter student name: Arun
Enter aggregate percentage: 92
Enter marks for 5 subjects:
Subject 1: 90
Subject 2: 95
Subject 3: 88
Subject 4: 92
Subject 5: 95
Enter attendance percentage: 95
Enter annual family income: 200000

Enter details of Student 2
Enter student name: Banu
Enter aggregate percentage: 85
Enter marks for 5 subjects:
Subject 1: 80
Subject 2: 85
Subject 3: 90
Subject 4: 82
Subject 5: 88
Enter attendance percentage: 90
Enter annual family income: 150000

Enter details of Student 3
Enter student name: Charan
Enter aggregate percentage: 72
Enter marks for 5 subjects:
Subject 1: 75
Subject 2: 70
Subject 3: 80
Subject 4: 65
Subject 5: 70
Enter attendance percentage: 85
Enter annual family income: 180000

Enter details of Student 4
Enter student name: Divya
Enter aggregate percentage: 92
Enter marks for 5 subjects:
Subject 1: 95
Subject 2: 90
Subject 3: 92
Subject 4: 90
Subject 5: 93
Enter attendance percentage: 98
Enter annual family income: 250000
```

## 6\. Sample Output

text

```text
========== SCHOLARSHIP ALLOCATION RESULTS ==========

Eligible Students (Rank Wise):

Rank: 1
Name: Divya
Aggregate: 92.0 %
Attendance: 98.0 %
Family Income: Rs. 250000.0
Scholarship Status: SELECTED

Rank: 2
Name: Arun
Aggregate: 92.0 %
Attendance: 95.0 %
Family Income: Rs. 200000.0
Scholarship Status: SELECTED

Rank: 3
Name: Banu
Aggregate: 85.0 %
Attendance: 90.0 %
Family Income: Rs. 150000.0
Scholarship Status: SELECTED

========== NOT ELIGIBLE STUDENTS ==========

Charan

========== END OF PROGRAM ==========
```

## 7\. Explanation of Output

- **Divya:** Secured the first rank because she obtained 92% aggregate marks and 98% attendance.
- **Arun:** Secured the second rank because he obtained the same aggregate as Divya but had lower attendance.
- **Banu:** Secured the third rank with 85% aggregate marks.
- **Charan:** Was rejected because his aggregate percentage (72%) was below the required 75%.

The system successfully identifies eligible students and ranks them according to academic performance, attendance, and family income.

## 8\. Conclusion

The University Scholarship Allocation System automates the scholarship selection process using Python. It checks students' academic marks, subject-wise performance, attendance, and family income. It ranks eligible students using predefined tie-breaking rules, making scholarship allocation easier, faster, and more transparent.Here you have to write the code
