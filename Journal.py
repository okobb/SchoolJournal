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

#Function to print the journal whenever necessary.
def print_journal(journal):
    for student in journal:
        student_name = student
        student_grades = class_journal[student]
        print (f"Student name: {student_name}")
        print (f"Student grades: {student_grades}")
        average = round(sum(student_grades)/len(student_grades),2)
        print (f"Student average: {average}\n")


print_journal(class_journal)

#Answering the questions:

#Writing a variable for each question:
highest_average = 0
highest_grade = 0
highest_student = ""
best_performance = 100
best_student = ""
not_passing = []
total_grades = 0
overall_average = 0

def deep_analysis(journal):
    

    for student in class_journal:
        student_name = student
        student_grades = class_journal[student]
        student_average = round(sum(student_grades)/len(student_grades),2)
        student_min = student_grades[0]
        student_max = student_grades[0]
        
        for grade in student_grades:
            #Count the grades for each student
            
            total_grades += 1
            
            #Checking for a grade below 70
            
            if(grade < 70 and student_name not in not_passing):
                not_passing.append(student_name)
            #Find the min and max
            if(grade > student_max):
                student_max = grade
            else:
                student_min = grade
        
        #Find the performance of each student
        student_perfomance = student_max - student_min
        
        #Validating the answer for each question
        if(student_max > highest_grade):
            highest_grade = student_max
            highest_student = student_name
            
        if(student_average > highest_average):
            highest_average = student_average
            
        if(student_perfomance < best_performance):
            best_performance = student_perfomance
            best_student = student_name
        
        overall_average += student_average

    overall_average = overall_average / len(class_journal)

with open("Journal.txt", "w") as file:
    file.write(f"The student who got the highest grade is {highest_student}\n")
    file.write(f"The student who got the most consistent performance is {best_student}\n")
    
    if(len(not_passing) == 0):
        file.write("No students have failed!\n")
    elif(len(not_passing) == 1):
        file.write(f"The student that got at least one grade below 70 is {not_passing}\n")
    else:
        file.write(f"The students that got at least one grade below 70 are {not_passing}\n")

    file.write(f"The total number of grades in this class are {total_grades}\n")
    file.write(f"The overall class average is {overall_average}\n")
    
