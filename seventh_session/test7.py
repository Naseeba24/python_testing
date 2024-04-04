#Program 3.17a: Modify program 3.17 to allow user to enter the credit_limit  and customer_status
credit_limit = int(input('Enter your credit_limit : '))
customer_status = str(input('Enter your customer_status : '))
if (credit_limit > 20000 and customer_status == 'good'): # == to check
 print ('Approve')
elif (credit_limit < 20000 and customer_status == 'fair'): # == to check
 print ('Approve with caution')
else:
 print ('Reject')