records = [
["Layla", 89], ["Tariq", 77], ["Layla", 91], ["Jana", 100], ["Tariq", 84],
["Ziad", 62], ["Jana", 97], ["Tariq", 73], ["Ziad", 71], ["Layla", 86],
["Jana", 94], ["Ziad", 75]
]

class_journal = {}

#Function to Fill the journal whenever necessary.

def build_journal (records):
    for student in records:
        student_name = student[0] 
        student_grade = student[1] 
        if(student_name) not in class_journal:
            class_journal[student_name] = []
            class_journal[student_name].append(student_grade)
        else:
            class_journal[student_name].append(student_grade)
    print("\n")

build_journal(records)

#Function to print the journal whenever necessary.
def print_journal(journal):
    for student in journal:
        student_name = student
        student_grades = class_journal[student]
        print (f"Student name: {student_name}")
        print (f"Student grades: {student_grades}")
        average = round(sum(student_grades)/len(student_grades),2)
        print (f"Student average: {average}")
    print("\n")

print_journal(class_journal)

#Answering the questions:

#Writing a variable for each question:
highest_average = 0
highest_grade = 0
highest_student = ""
best_performance = 0
best_student = ""
not_passing = []
total_grades = 0
overall_average = 0
