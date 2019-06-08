# https://www.learnpython.org/en/Loops
names = ['Rick','Morty','Summer','Jerry']
for n in names:
    print(n);

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)
    
# Do even numbers from 16
for z in range(16,40,2):
    print(z)

print('New Line')
myCount=2
while myCount <7:
    print(myCount)
    myCount += 2

# break is used to exit a for loop or a while loop, whereas continue is used to skip the current block, and return to the "for" or "while" statement. A few examples:
print('New Line')
# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
print('New Line')
# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)