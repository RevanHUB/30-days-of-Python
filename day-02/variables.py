from math import floor;

# #Day 02#
# string = 'Hi there, my name is David';
# # preparation for the day
# print("Largo en string " + string + " : ", len(string)); # incluye espacios en blanco
# print(type(string));
# numberToString = str(50);
# print(type(numberToString));
# print(float(10));
# # print(input('Enter your name: '))
# print(min(20, 30, 40, 50));
# print(max(20, 30, 40, 50));
# print(min([20, 30, 40, 50]));
# print(max([20, 30, 40, 50]));
# print(sum([20, 30, 40, 50]));
# exit();

# Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
    
    # Done

# Write a python comment saying 'Day 2: 30 Days of python programming'

    # Day 2: 30 days of Python programming

# Declare a first name variable and assign a value to it

firstName = "David";

# Declare a last name variable and assign a value to it

lastName = "Martín";

# Declare a full name variable and assign a value to it

fullName = firstName + " " + lastName;


# Declare a country variable and assign a value to it

country = "Argentina";

# Declare a city variable and assign a value to it

city = "Buenos Aires";

# Declare an age variable and assign a value to it

age = 25;

# Declare a year variable and assign a value to it

year = 2020;

# Declare a variable is_married and assign a value to it

is_married = False;

# Declare a variable is_true and assign a value to it

is_true = True;

# Declare a variable is_light_on and assign a value to it

is_light_on = True

# Declare multiple variable on one line

is_ready, are_you_there = True, False;

#End of day 2 level 01

#Day2 level 02 Start:

# Check the data type of all your variables using type() built-in function

# Declare a first name variable and assign a value to it

firstName = "David"; 
print(type(firstName));

# Declare a last name variable and assign a value to it

lastName = "Martín";
print(type(lastName));

# Declare a full name variable and assign a value to it

fullName = firstName + " " + lastName;
print(type(fullName));


# Declare a country variable and assign a value to it

country = "Argentina";
print(type(country));

# Declare a city variable and assign a value to it

city = "Buenos Aires";
print(type(city));

# Declare an age variable and assign a value to it

age = 25;
print(type(age));

# Declare a year variable and assign a value to it

year = 2020;
print(type(year));

# Declare a variable is_married and assign a value to it

is_married = False;
print(type(is_married));

# Declare a variable is_true and assign a value to it

is_true = True;
print(type(is_true));

# Declare a variable is_light_on and assign a value to it

is_light_on = True
print(type(is_light_on));

# Declare multiple variable on one line

is_ready, are_you_there = True, False;
print(type(is_ready));
print(type(are_you_there));

# Using the len() built-in function, find the length of your first name

print("length of firstName:" , len(firstName))
# Compare the length of your first name and your last name

def compareTwoValues(self, val1 = 3, val2 = 2):
        if (val1 > val2) :
            print("val1 is bigger than val2");
        else :
            print("val2 is bigger than val1");
    
compareTwoValues(3, 2);    
compareTwoValues(3, 10)

# Declare 5 as num_one and 4 as num_two

num_one = int(5);
num_two = int(4);

# Add num_one and num_two and assign the value to a variable total

sum = num_one + num_two;
print(sum);

# Subtract num_two from num_one and assign the value to a variable diff

diff = num_two - num_one;
print(diff);

# Multiply num_two and num_one and assign the value to a variable product

product = num_two * num_one;
print(product);

# Divide num_one by num_two and assign the value to a variable division

division = num_one / num_two;
print(division);

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder

remainder = num_two % num_one;
print(remainder);

# Calculate num_one to the power of num_two and assign the value to a variable exp

exp = num_one ** num_two;
print(exp);

# Find floor division of num_one by num_two and assign the value to a variable floor_division

floor_division = num_one // num_two;
print(floor_division);

# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle

radius_of_circle = 30;
area_of_circle = 3.14 * radius_of_circle ** 2;
print(area_of_circle);

# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle

circum_of_circle = 2 * 3.14 * radius_of_circle;
print(circum_of_circle);

# Take radius as user input and calculate the area.

radius = input("Enter the radius of the circle: ");
radius = int(radius)
area = 3.14 * radius ** 2;
print("The area of the circle is: ", area);

# Use the built-in input function to get first name, last name, country and age from a user and store
# the value to their corresponding variable names

# takeName = input("Enter the name: ");
# takeName = str(takeName)
# print(takeName)
# takeLastName = input("Enter the last name: ");
# takeLastName = str(takeLastName)
# print(takeLastName)
# takeCountry = input("Enter the country: ");
# takeCountry = str(takeCountry)
# print(takeCountry)
# takeAge = input("Enter the age: ");
# takeAge= int(takeAge)
# print(takeAge)

# Run help('keywords') in Python shell or in your file to check for the Python reserved words 
# or keywords

help('keywords');

# 🎉 CONGRATULATIONS ! 🎉