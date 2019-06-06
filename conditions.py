# https://www.learnpython.org/en/Conditions
name = 'Sanchez'
if name in ['John','Rick']:
    print('Your name is either John or Rick.');
elif name == 'Morty':
    print('Your name is MooooRRRtttYYYY');
else:
    print('Oh jeeze');

# Unlike the double equals operator "==", the "is" operator does not match the values of the variables, but the instances themselves. For example:
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

print(not False) # Prints out True
print((not False) == (False)) # Prints out False

# Exercise
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")