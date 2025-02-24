# FILE NAME - convert_C_to_F_01.py

# NAME: Patrick Clark
# DATE: 2/23/2025
# BRIEF DESCRIPTION: This program will ask the user for a temperature in Celsius and output the temperature in farenheight.  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience




    
# Don't forget to cast user input as a float!
    
########## ENTER YER CODE BELOW THIS LINE ##########

celsius = float(input('Enter a temperature in Celsius: '))
conv_1 = 9/5
farenheight = celsius * conv_1 + 32

print(f'{celsius} degrees Celsius is {farenheight} degrees Farenheight.')








########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a temperature in Celsius: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: 1

1 degrees Celsius is 33.8 degrees Fahrenheit.

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What does `float` mean?
# 'float' means floating-point number. It is a decimal value that gets saved in the program.




2. Why do you think it is important to use `float` as opposed to
   a different type of variable type?
#It is important to use 'float' to get a more accurate solution that deals with decimal values. 




'''
