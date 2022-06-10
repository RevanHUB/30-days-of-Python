
# fruits = ['banana', 'orange', 'mango', 'lemon']
# exists =  'naranja' in fruits;
# print(exists);
# fruits.insert(0, 'apple');
# print(fruits);


# Declare an empty list

list = []

# Declare a list with more than 5 items

frutas = ['banana', 'orange', 'mango', 'lemon', 'apple', 'grapes', 'pear']

# Find the length of your list

print("len ", len(frutas))

# Get the first item, the middle item and the last item of the list

print(frutas[0])
print(frutas[len(frutas) - 1])
print(frutas[len(frutas) // 2])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ['David', 30, 1.76, 'Single', 'Calle Luna #123']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies)

# Print the number of companies in the list

print(len(it_companies))

# Print the first, middle and last company

print(it_companies[0])
print(it_companies[len(it_companies) // 2])
print(it_companies[len(it_companies) - 1])

# Print the list after modifying one of the companies

# it_companies[3] = 'Cognito Inc';
# print(it_companies)

# Add an IT company to it_companies

it_companies.insert(1, 'Cognito Inc');
print(it_companies)

# Insert an IT company in the middle of the companies list

it_companies.insert(len(it_companies) // 2, 'Worten Inc');
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)

# it_companies[0] = it_companies[0].upper();
# print(it_companies)

# Join the it_companies with a string '#;  '

string = '#; '.join(it_companies)
print(string)

for companies in it_companies:
    companies = companies + "#;"
    
print(it_companies)

# Check if a certain company exists in the it_companies list.
companySearch = 'Cognito Inc';

print(companySearch +' exists') if it_companies.count(companySearch) == 1 else print(companySearch + ' does not exist');

# Sort the list using sort() method

it_companies.sort();
print(it_companies)

# Reverse the list in descending order using reverse() method

it_companies.sort(reverse = True)
#or 
# it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list

# it_companiesSliced = it_companies[:3]
# it_companies = it_companies[3:len(it_companies)]
# print(it_companies)

# Slice out the last 3 companies from the list

# it_companiesSliced = it_companies[:len(it_companies) - 3]
# print(it_companiesSliced)
# it_companies = it_companies[len(it_companies)-3: len(it_companies)];
# print(it_companies)

# Slice out the middle IT company or companies from the list

# it_companiesSliced = it_companies[:len(it_companies) // 2 ]
# print(it_companiesSliced)
# it_companies = it_companies[len(it_companies) // 2:len(it_companies)];
# print(it_companies)


# Remove the first IT company from the list

# it_companies.pop(0);
# print(it_companies)

# Remove the middle IT company or companies from the list

# it_companies.pop(len(it_companies) // 2)
# print(it_companies) # Google

# Remove the last IT company from the list

# it_companies.pop(len(it_companies) - 1)
# print(it_companies)

# Remove all IT companies from the list

# del it_companies[0:len(it_companies)]
# print(it_companies)

# Destroy the IT companies list

# it_companies = None;
# print(it_companies)
#or 
# it_companies.clear();
# print(it_companies)

# Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

fullstack = front_end + back_end
print(fullstack)

# fullstack = front_end.extend(back_end);
# print(fullstack)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. 
# Then insert Python and SQL after Redux.

full_stack = fullstack.copy()
reduxPos = full_stack.index('Redux') + 1 ;
# print(reduxPos)
full_stack.insert(reduxPos, 'Python');
full_stack.insert(reduxPos, 'SQL');
print(full_stack)

# Exercises: Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age

ages.sort();
print(ages)
min = ages[0]
max = ages[-1];
print(min)
print(max)


# Add the min age and the max age again to the list

ages.insert(0, min)
ages.append(max);
print(ages)

# Find the median age (one middle item or two middle items divided by two)

median = ages[len(ages) // 2]
print(median);

# Find the average age (sum of all items divided by their number )

average = sum(ages) / len(ages)
print(average)

# Find the range of the ages (max minus min)
range = int(max) - int(min);
print(range)

# Compare the value of (min - average) and (max - average), use abs() method

comparation = abs(int(min) - int(average)) - abs(int(max) - int(average));
print(comparation)

# Find the middle country(ies) in the countries list

from config import countries
print(countries[len(countries) // 2])
# Divide the countries list into two equal lists if it is even 
# if not one more country for the first half.
if(len(countries) % 2 == 0):
    print("countries are even")
    countries1 = countries[:len(countries) // 2]
    countries2 = countries[len(countries) // 2:]
    print(len(countries1))
    print(len(countries2))
else:
    print("countries are odd")
    countries1 = countries[:len(countries) // 2 + 1]
    countries2 = countries[len(countries) // 2 + 1:]
    print("list1 " , len(countries1))
    print("list2 " , len(countries2))

unpack = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
# Unpack the first three countries and the rest as scandic countries.

firstThree = unpack[:3];
scandic = unpack[3:];
print(firstThree)
print(scandic)

# End of day 5