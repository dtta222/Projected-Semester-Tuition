# Projected Semester Tuition
'''
At one college, the tuition for a full-time student is $8,000 per
semester. It has been announced that the tuition will increase by 3
percent each year for the next 5 years. Write a program with a loop
that displays the projected semester tuition amount for the next 5 years.
'''

tuition = 8000
tuition += tuition*.03 
disp_tuition = '$'+(f'{tuition:.2f}')
print("In 1 year, the tuition will be", disp_tuition, end='.\n')
for i in range (2, 6):
    tuition += tuition*.03 
    disp_tuition = '$'+(f'{tuition:.2f}')
    print("In", i, "years, the tuition will be", disp_tuition, end='.\n')
