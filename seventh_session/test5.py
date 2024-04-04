#Program 3.15a : Modify program 3.15 to allow user to enter the color
color = str(input('Enter a color : '))
if (color == 'red'):
    print ('Stop!')
elif (color == 'green'):
    print ('Go! ')
elif (color == 'yellow'):
    print ('Wait!')
else:
    print ('Invalid color!')