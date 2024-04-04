#Program 3.13c modify program 3.13a 
#1. to allow user to enter Assignment marks and FinalExam marks 
#2. if both marks are 50 and above, result is PASS
#3. if any of the marks below 50, result is RESIT
#4. if both marks below 50, result is FAIL 

mark = float(input('Enter your mark: '))
final_exam_mark = float(input('Enter your final exam marks : '))
if (mark >= 50 and final_exam_mark >= 50): 
 print ('Congrats - you passed the test! ')
elif (mark < 50 and final_exam_mark > 50 ):
 print('Your result is Resit')
elif (mark < 50 and final_exam_mark < 50 ):
 print('Your result is FAIL')
else:
 print ('Sorry, WRONG INPUT! ')