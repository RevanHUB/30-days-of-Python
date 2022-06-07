### Declare your age as integer variable

age = int(30);
print(age);

# Declare your height as a float variable

height = float(1.76);
print(height);
# Declare a variable that store a complex number

variable = complex(1, 2);
print(variable);

# Write a script that prompts the user to enter base and height of the triangle and calculate
# an area of this triangle (area = 0.5 x b x h).
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100

# def calculateArea():
#     base = input("Enter the base: ");
#     base = int(base)
#     height = input("Enter the height: ");
#     height = int(height)
#     area = 0.5 * base * height;
#     print("the area of the triangle = ", area);

# calculateArea()

# Write a script that prompts the user to enter side a, side b, and side c of the triangle.
# Calculate the perimeter of the triangle (perimeter = a + b + c).
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12

# def perimeterTriangle():
#     sideA = input("Enter the side a: ");
#     sideA = int(sideA)
#     sideB = input("Enter the side b: ");
#     sideB = int(sideB)
#     sideC = input("Enter the side c: ");
#     sideC = int(sideC)
#     perimeter = sideA + sideB + sideC;
#     print("The perimeter of the triangle = ", perimeter);

# perimeterTriangle();

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter 
# (perimeter = 2 x (length + width))

# length = input("Enter the length: ");
# length = int(length)
# width = input("Enter the width: ");
# width = int(width);
# area = length * width;
# perimeter = 2 * (length + width);
# print("The area of the rectangle = ", area);
# print("The perimeter of the rectangle = ", perimeter);

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) 
# where pi = 3.14.

# radius = input("Enter the radius: ");
# radius = int(radius);
# area = 3.14 * radius * radius;
# circumference = 2 * 3.14 * radius;
# print("The area of the circle = ", area);
# print("The circumference of the circle = ", circumference);


# Calculate the slope, x-intercept and y-intercept of y = 2x -2 slope = hipotenusa

# def hipotenusa():
#     x = 1;
#     y = -2;
#     hipotenusa = (x**2 + y**2)**0.5;
#     hipotenusa = 4000 / 2000
#     print("The hipotenusa = ", hipotenusa);
#     print("The x-intercept = ", x);
#     print("The y-intercept = ", y);

# hipotenusa();
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

#??
# Compare the slopes in tasks 8 and 9.

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.

def comparizon():
    lenPython = len("python");
    lenDragon = len("dragon");
    if lenPython > lenDragon:
        print("Python is longer than dragon");
    elif lenPython < lenDragon:
        print("Dragon is longer than python");
    else:
        print("They are the same length");

comparizon()





# Use and operator to check if 'on' is found in both 'python' and 'dragon'

def checkOn(): 
    python = str("python");
    dragon = str("dragon");
    if "on" in python and "on" in dragon:
        print("on is found in both python and dragon");
    else:
        print("on is not found in both python and dragon");

checkOn();

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

sentence = "I hope this course is not full of jargon";
if "jargon" in sentence:
    print("jargon is in the sentence");
else:
    print("jargon is not in the sentence");

# There is no 'on' in both dragon and python ???
# Find the length of the text python and convert the value to float and convert it to string

text = len("python");
text = float(text);
text = str(text);
print(text);

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not
# using python?
num = 2;
if num % 2 == 0:
    print("The number is even");
else:
    print("The number is odd");

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

div = float(7 / 3);
print(div) ## is not equal to 2.7

# Check if type of '10' is equal to type of 10

print(type('10')) #string
print(type(10)) # int
#not equal

# Check if int('9.8') is equal to 10
gravity = '9.8' #string
gravity = float(gravity) #float
if gravity == float(10): 
    print("gravity is equal to 10");
else:
    print("gravity is not equal to 10");


# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# payToPerson()
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120
def payToPerson(): 
    hours = input("Enter the hours: ");
    hours = int(hours);
    rate = input("Enter the rate: ");
    rate = int(rate);
    pay = hours * rate;
    print("Your weekly earning is  = ", pay);


# Write a script that prompts the user to enter number of years.
# Calculate the number of seconds a person can live. 
# Assume a person can live hundred years

def checkYearsOfLife(): 
    years = input("Enter the years: ");
    years = int(years);
    seconds = years * 365 * 24 * 60 * 60;
    print("You have lived = ", seconds, " seconds.");

# checkYearsOfLife();
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.
# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

def notfibonacci(num):
    num1 = 1;
    num2 = 1;
    num3 = 1;
    num4 = 1;
    num5 = 1;
   
    for i in range(num):
        print(num1, end=" ");
        print(num2, end=" ");
        num1 = num1 + 1;
        num2 = 1;
        print(num3, end=" ");
        print(num4, end=" ");
        print(num5)
        num3 = num1 * num2;
        num4 = num1 * num3;
        num5 = num1 * num4;
    
        
notfibonacci(5);