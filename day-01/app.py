#day-01#
import math;
#Exercise-01#
# Check the python version you are using

    #python --version;

    # para hacerlo en el interactive shell -> import os; pythonV =  os.popen('python --version').read;

# Open the python interactive shell and do the following operations. The operands are 3 and 4.


# addition(+)

print(3 + 4);
print(3 - 4);
print(3 * 4);
print(3 % 4);
print(3 / 4);
print(3**4);
print(3//4);

# Write strings on the python interactive shell. The strings are the following:
# Your name
# Your family name
# Your country
# I am enjoying 30 days of python

"David";
"Martín";
"Spain";
"I am enjoying 30 days of python";

# Check the data types of the following data:
# 10
type(10)
# 9.8
type(9.8)
# 3.14
type(3.14)
# 4 - 4j
type( 4 - 4j)
# ['Asabeneh', 'Python', 'Finland']
type(['Asabeneh', 'Python', 'Finland'])
# Your name
type("David")
# Your family name
type("Martín")
# Your country
type("Spain")
# Exercise: Level 2
# Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file helloworld.py and
# repeat questions 1, 2, 3 and 4. Remember to use print() when you are working on a python file.
# Navigate to the directory where you have saved your file, and run it.

#python --version;

# para hacerlo en el interactive shell -> import os; pythonV =  os.popen('python --version').read();
import os; 
pythonV =  os.popen('python --version').read();
print(pythonV);

# Open the python interactive shell and do the following operations. The operands are 3 and 4.


# addition(+)

print(3 + 4);
print(3 - 4);
print(3 * 4);
print(3 % 4);
print(3 / 4);
print(3**4);
print(3//4);

# Write strings on the python interactive shell. The strings are the following:
# Your name
# Your family name
# Your country
# I am enjoying 30 days of python

"David";
"Martín";
"Spain";
"I am enjoying 30 days of python";

# Check the data types of the following data:
# 10
print(type(10))
# 9.8
print(type(9.8))
# 3.14
print(type(3.14))
# 4 - 4j
print(type( 4 - 4j))
# ['Asabeneh', 'Python', 'Finland']
print(type(['Asabeneh', 'Python', 'Finland']))
# Your name
print(type("David"))
# Your family name
print(type("Martín"))
# Your country
print(type("Spain"))

# Exercise: Level 3
# Write an example for different Python data types such as
# Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

price = 10;
print(price);
print(type(price));
float = 9.6;
print(float);
print(type(float));
complex = 4 - 3j;
print(complex);
print(type(complex));
string = "testing string";
print(string);
print(type(string));
isOnline = True;
print(isOnline);
print(type(isOnline));
frontEnd = ['HTML', 'CSS', 'JavaScript', 'React'];
print(frontEnd);
print(type(frontEnd))
backEndTuple = ('Python', 'NodeJS', 'MySQL');
print(backEndTuple);
print(type(backEndTuple)); 
objectLike = {'David','Martín', 'Spain'};
print(objectLike);
print(type(objectLike));
object = {'name': 'zombie', 'hp': '100', 'attacks': ['bite', 'claw', 'infection']};
print(object)
print(type(object))

# Find an Euclidian distance between (2, 3) and (10, 8)

#d(p, q) = ((p1 - q1) + (p2 - q2) 
def Euclidian(p1, q1, p2, q2):
    distance = math.sqrt(((p1 - q1)**2 + (p2 - q2)**2));
    return distance;

result = Euclidian(2, 3, 10, 8);
print(result);

def distance(p1,q1,p2,q2):
    print(math.sqrt((p1-q1)**2+(p2-q2)**2))

distance(2,3,10,8);
print((distance));
exit();