import math
age = int(24)
height = float(1.74)
complex_num = 2 +3j

base, h = int(input('Please input base ')), int(input('Please input height '))
triagnle_area = .5 * base * h
print(triagnle_area)

a,b,c = int(input('please input the side a ')), int(input('Please input side b ')), int(input('Please input side c '))
perimeter = a + b + c
l,w = float(input('Please enter the length of the rectangle ')), float(input('Please enter the width of the rectangle '))
area_rectangle = l * w
perimeter_rectangle = 2 * (l * w)

r = float(input('Please enter the radius of the circle '))
pi = 3.14
circle_area = pi * (r**2)
circle_circumferance = 2 * pi * r
m = 2
c = -2
slope_1 = m 
y_intercept = (2*0, c)
x_intercept = (-b/m,0)
print( slope_1, x_intercept, y_intercept)
grad = (10-2)/(6-2)
slope_2 = grad
euclidean_distance = math.sqrt((10-6)**2)+((2-10)**2) 
if slope_1 < slope_2:
    print (' slope in task 8 is greater than task 9 ')
elif slope_1 > slope_2:
    print (' slope in task 8 is less than task 9 ')
else:
    print('Both slopes are at the same gradient ')

x = int(input(' Please input a value for x ')) # -3
equation_y = x**2 + 6*x + 9

word_1 = 'Python'
len_python =len(word_1)
word_2 = 'dragon'
len_dragon = len(word_2)
print (len_python < len_dragon)

result_word = 'on' in word_1 and 'on' in word_2

sentence = "I hope this course is not full of jargon"
print("jargon" in sentence)

print('on' not in 'Python' and 'on' not in 'dragon')

length = len(word_1)
length_float = float(length)
length_str = str(length_float)

number_check = 10 # can be any number
if number_check % 2 == 0:
    print('Even number ')
else:
    print('odd number')

print(7//3 == int(2.7))

print(type('10')== type(10))

print(int(float('9.8')) == 10)

hours = float(input('Please enter the number of hours worked '))
hourly= float(input('Please enter number of hours worked'))
total_pay = hours * hourly
print("Weekly pay is ", int(total_pay))

num_years = int(input("Please enter a number of years "))
seconds = num_years * 365 * 24 * 60 * 60 
print ("You have lived for ", seconds , " seconds. ")

for i in range (1, 6):
    print(i,1,i,i**2,i**3)


