import math
'''### Exercises: Level 1

1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
2. Write a python comment saying 'Day 2: 30 Days of python programming'
3. Declare a first name variable and assign a value to it
4. Declare a last name variable and assign a value to it
5. Declare a full name variable and assign a value to it
6. Declare a country variable and assign a value to it
7. Declare a city variable and assign a value to it
8. Declare an age variable and assign a value to it
9. Declare a year variable and assign a value to it
10. Declare a variable is_married and assign a value to it
11. Declare a variable is_true and assign a value to it
12. Declare a variable is_light_on and assign a value to it
13. Declare multiple variable on one line

### Exercises: Level 2

1. Check the data type of all your variables using type() built-in function
2. Using the _len()_ built-in function, find the length of your first name
3. Compare the length of your first name and your last name
4. Declare 5 as num_one and 4 as num_two
5. Add num_one and num_two and assign the value to a variable total
6. Subtract num_two from num_one and assign the value to a variable diff
7. Multiply num_two and num_one and assign the value to a variable product
8. Divide num_one by num_two and assign the value to a variable division
9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
10. Calculate num_one to the power of num_two and assign the value to a variable exp
11. Find floor division of num_one by num_two and assign the value to a variable floor_division
12. The radius of a circle is 30 meters.
    1. Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
    2. Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
    3. Take radius as user input and calculate the area.
13. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
14. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords'''

first_name = input('Whats your first name ')
last_name = input('Whats your surname ')
full_name = first_name + ' ' + last_name
country =  input('what country are you from ')
city = 'Aberdeen'
age = int(input('what age are you? '))
year = 2004
is_married = False
is_true = True
is_light_on = False
runner, rugby_player = True, False

types = [type(_) for _ in (first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on, runner, rugby_player)]
print(types)

print(len(first_name))

if len(first_name) < len(last_name):
    print('first name is shorter than surname')
elif len(first_name) > len(last_name):
    print('first name is longer than surname')
else :
    print('first and last names are the same length')

num_one, num_two = 5, 4

nums_add = num_one + num_two
nums_subtract= num_one - num_two
nums_multiplied = num_one * num_two
nums_divided = num_one/num_two
nums_modulus = num_one % num_two

variable_exponent = num_one ** num_two
floor_division = num_one // num_two
radius = int(input('Please enter radius '))
area_of_circle = math.pi * (radius**2)
print (area_of_circle)
circumference_of_circle = 2 * math.pi * radius
print (circumference_of_circle)



