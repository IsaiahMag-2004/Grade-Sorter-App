# Unit 2 Challange 1 Grade Sorter App
# author (Isaiah Magana)
# Main.py

print("Welcome to The Grade Sorter App\n")

#Get Users Grades and create list
grade = []
first_grade = grade.append(int(input("What is your first grade(0-100): ")))
second_grade = grade.append(int(input("What is your second grade(0-100): ")))
third_grade = grade.append(int(input("What is your third grade(0-100): ")))
fourth_grade = grade.append(int(input("What is your fourth grade(0-100): ")))

#Output
grade.sort(reverse=True)
print()
print(f"Your grades are: {grade}\n")
print(f"Your grades from highest to lowest are: {grade}\n")

#Grade drop
print("The lowest two grades will now be dropped.")
print(f"Removed grade: {grade[3]}")
print(f"Removed grade: {grade[2]}")
#Lowest grades 
low_1 = grade[3]
low_2 = grade[2]
grade.remove(low_1)
grade.remove(low_2)

#Praise for grades
print()
print(f"Your remaining grades are: {grade}")
print(f"Nice Work! Your highest grade is a {grade[0]}")
