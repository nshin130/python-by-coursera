# List
# -> can include another list / empty

friends = ['Joe', 'Glenn', 'Chris']

for f in friends:
    print('welcome', f)

# Lists : mutable:
# -> we can change an element of a list using the index operator
# strings are immutable
# -> we cannot change the contents of a string
# -> we must make a new string to make any change

# len() : number of elements in the list
# range(): returns a list of number from zero to one less than the parameter

stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

some = [1,9,32,20,26]
9 in some   # True
14 in some  # False

friends.sort()
print(friends)

# len(), max(), min(), sum() -> built in function

total = 0
count = 0
while True:
    inp = input('Enter your number: ')
    if inp == 'done': break
    inp = float(inp)
    total = total + inp
    count = count + 1

print('Average: ', total/count)

num=[]
while True:
    inp = input('Enter your number: ')
    if inp == 'done': break
    inp = float(inp)
    num.append(inp)

total = sum(num)
count = len(num)
print('Average: ', total/count)

# Lists & strings
# split(): breaks a string into parts and produce a list of string
# split(';'): can specify delimiter character

# List summary
# functions: len, min, max, sum
# slicing lists
# method: append, remove
