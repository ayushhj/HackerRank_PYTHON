from collections import namedtuple

n = int(input())
fields = input().split()

total_marks = 0
for _ in range(n):
    students = namedtuple('student', fields)
    MARKS, CLASS, NAME, ID = input().split()
    student = students(MARKS, CLASS, NAME, ID)
    total_marks += int(student.MARKS)
avg = (total_marks / n)
print('%.2f'%avg)