#Program 3.13a --> Modify program 3.13 to allow user to enter the mark and calculate the grade.
mark = float(input('Enter your mark :'))
grade = ''
if (mark >= 90):
 grade = 'A'
elif (mark >= 80):
 grade = "B"
elif (mark >= 70):
 grade = "C"
elif (mark >= 60):
 grade = "D"
elif (mark >= 50):
 grade = "E"
else:
 grade = 'F'
print('You got grade', grade)