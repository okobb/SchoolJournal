records = [
["Layla", 89], ["Tariq", 77], ["Layla", 91], ["Jana", 100], ["Tariq", 84],
["Ziad", 62], ["Jana", 97], ["Tariq", 73], ["Ziad", 71], ["Layla", 86],
["Jana", 94], ["Ziad", 75]
]

class_journal = {}

#Function to Fill the journal whenever necessary.

def BuildJournal (records):
    for student in records:
        student_name = student[0] 
        student_grade = student[1] 
        if(student_name) not in class_journal:
            class_journal[student_name] = []
            class_journal[student_name].append(student_grade)
        else:
            class_journal[student_name].append(student_grade)
    print(class_journal)

BuildJournal(records)