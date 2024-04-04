First_name = input('Enter your first name : ')  #input('')  >>> NO SPACE()

Last_name = input('Enter your Last name : ') # for string , NEED TO '' 

# age= int(age) or  int(input('')) #type= int    >>>>TYPE CONVERSION
# age = input('How old are you? ') #type= str
age= int(input('Enter your age: '))

#age = 25 #>>>>> # For numbers No need ''.


# 1::: sentence = 'you are {}'.format(First_name) -----> 'string {}'.format(variable) 
# e.g: variable = 'you are {}'. format(variable x )

sentence = f'you are {First_name} {Last_name}. Your age is {age}' #>> 2::: NEW: f'string {variable}'
#e.g: variable = f'You are {variable 1} {variable 2}. Your age is {variable 3}'

#sentence = f'You are {First_name} {Last_name}. You are {age} years old.'
print(sentence)


# For knowing the type: type(variable)
#print (type(age))
#print (type(First_name))

#cls
# print (age)

