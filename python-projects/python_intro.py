print("hello world!")

# this is one line of comments

'''
this is one line
this is another
'''


#Variables
x = 10 #python is dynamically typed - don't have to declare variable type
print(x)
x = 'hello!'
print(x)
s = 'hello world'

x = 100
y = 10
r = x / y # can cast as r as an int as r = int(x / y)
print(r) # r printed as a float as 10.0
r = x // y # floor division for int
print(r)

# math functions
m = min(100,20)
print(m)
p = pow(2,4)
print(p)
p = 2**4 # shortcut for power exponent

# if statements
x = -1
y = 1

if x < 0: #no parenthesis, use colon, block of code is indented
	x = 1
	x += 10
	

print("outside of if statement")

if x < 0 and y == 1:
	print('x negative and y is 1')

if x < 0 or y == 1:
	print('x negative or y is 1')

if x < 0:
	print('x is less than 0')
elif x == 0:
	print(x)
else:
	print('x is greater than 0')

# Loops
counter = 0
while counter < 10: #while loop
	print(counter)
	counter += 1

nums = [10,20,30,40,50] #array
for i in range(5): #iteration for loop - this goes from 0 to 4
	print(nums[i])
for i in range(2, len(nums)): #starts at index 2 to last index in array
	print(nums[i])

for num in nums: # for each loop
	num += 5
	print(num)
print(nums) # for each loop does not modify values in array

for index, val in enumerate(nums): #not working
	print("i is, ",i, "and val is ", val)

dogs = ["boomer","rocky","daisy"]

index = 0
while index < len(dogs):
	print(dogs[index])
	index += 1

for i in range(3):
	print(dogs[i])

for index, val in enumerate(dogs):
	print(i, val)

nums = [1,2,3,4,5]
sum_nums = 0
for val in nums:
	sum_nums += val
print("The sum of nums is " + str(sum_nums))
#print(f"The sum of nums is {sum_nums}")

def hello(name):
	print('hello!',name)
hello('Bob')

def hello(name="friend"):
	print("hello!",name)
hello()

fname = "Anna"
lname = "Shirley"
print("she's a great dancer.")
print('He said "Hi" to his friend.')
fullname = fname + " " + lname
print(fullname)
f_initial = fname[0]
print(f_initial)

title = 'Rephactor Python'
print('Last character:', title[-1])
name3 = fullname * 3
print(name3)

name = 'John'
name_in_uppercase = name.upper()
print(name_in_uppercase)
print(name)

course = "Platform Computing"
Platform = course[0:8] #up to not including last index
print(Platform)
Computing = course[9:18]
print(Computing)

# Exercise
swap = [0,3,8,5,4]
temp = swap[2]
swap[2] = swap[4]
swap[4] = temp
print(swap)




