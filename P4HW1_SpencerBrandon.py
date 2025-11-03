# Brandon Spencer
# 11-2-25
# P4HW1
# Changing P2HW2 to use loops and adding validation and letter grades.

num_scores = int(input("How many scores do you want to enter? "))

grades = []

for i in range(num_scores):
    grade = float(input(f"Enter grade for Module {i+1}: "))
    grades.append(grade)
    
    while grade < 0 or grade > 100:
        print("INVALID Score entered ! ! ! !")
        print("Score should be between 0 and 100.")
        grade = float(input(f"Enter grade for Module {i+1}: "))
        grades[-1] = grade

grades_letter = 'A' if (sum(grades) / len(grades)) >= 90 \
                    else 'B' if (sum(grades) / len(grades)) >= 80 \
                    else 'C' if (sum(grades) / len(grades)) >= 70 \
                    else 'D' if (sum(grades) / len(grades)) >= 60 \
                    else 'F'

print("------------Results------------")
print(f"Lowest Score: {min(grades)}")
print(f"Modified List: {grades}")
print(f"Scores Average: {sum(grades) / len(grades):.2f}")
print(f"Grade: {(grades_letter)}")
print("---------------------------------")