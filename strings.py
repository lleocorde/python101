# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old. (%s)" % (name, age, name));

# https://www.learnpython.org/en/Basic_String_Operations
string1 = 'Hello World!'
print(string1.index('o'));
print(string1.count('l'));

string2 = 'This is a story about a guy named Al'
print(string2[2:20:2]);
print(string2[5:15]);
print(string2[::-1]);

array1 = string2.split(' ');
print(array1);