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

build_journal(records)

def print_journal(journal):
    for student in journal:
        print (f"Student name: {student}")
        print (f"Student grades: {journal[student]}")
        average = round(sum(journal[student])/len(journal[student]),2)
        print (f"Student average: {average}")



print_journal(class_journal)