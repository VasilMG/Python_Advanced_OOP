number_of_students = int(input())
students_grades = {}
for st in range(number_of_students):
    student, grade = input().split()
    if student not in students_grades:
        students_grades[student] = []
    
    students_grades[student].append(float(grade))
           
    
for k, v in students_grades.items():
    average = sum(v) / len(v)
    formatted_grades = ' '.join(f"{g:.2f}" for g in v) 
    print(f"{k} -> {formatted_grades} (avg: {average:.2f})")