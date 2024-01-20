number_of_students = int(input())

students_records = {}
for student in range(number_of_students):
    name,grade = input().split()
    if name not in students_records:
        students_records[name]=[]
    students_records[name].append(float(grade))

for key,value in students_records.items():
    average_grade = sum(value)/len(value)
    formatted_value = f"{' '.join([f'{g:.2f}' for g in value])}"
    print(f'{key} -> {formatted_value} (avg: {average_grade:.2f})')