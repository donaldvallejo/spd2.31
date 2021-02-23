# by Kami Bigdely 
# Replace magic numbers with named constanst

# First Section
# Given two point charges, calcualte the electric force exerted on them.
COLUMBUS_CONSTANT = 8.9875517923*1e9
question_1 = int(input('Enter a value of charge q1: '))
question_2 = int(input('Enter a value of charge q2: '))
distance = int(input("Enter the distance between two charges: "))
force =  ColumbusConstant * question_1 * question_2/(distance**2)
print ("Electric Force between q1 and q2 is: ", force, "Newton")
# Second Section
num = int(input('Enter an integer number: '))
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")