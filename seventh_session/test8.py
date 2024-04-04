# EXAM QUESTION IS LIKE THIS

#Program 3.17b: Modify program 3.17 to :
# 1: allow user to enter the credit_limit  and customer_status
# 2: have a variable for approval status and print it at the end of the program

credit_limit = float(input('Enter your credit_limit : '))
customer_status = input('Enter your customer_status : ')
approval = ''
if (credit_limit > 20000 and customer_status == 'good'):
 approval = 'approved'
elif (credit_limit < 20000 and customer_status == 'fair'):
 approval = 'approved with caution'
else:
 approval = 'rejected'

print( ' Your loan application has', approval)