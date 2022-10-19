# Syntax 

The syntax of a programming language defines the set of rules and symbols that should be used when programming in said language. 
You must adhere to the syntax of a language to write code that will run successfully. 

Example python code: 

```

print("Hello World")

```

## Indentation

This will print "Hello World" to the console.

Python has strict indentation rules. 

Any code that is meant to be within a specific code block must be indented. 

For example: 

```

if 3 > 1 :
  print("3 is greater than 1")

```

Python will show an error if you do not do this. 

## Comments

Comments in python start with a # 

For example: 

```
# This is commented
three = 3 # This line is not (Aside from this comment of course)

```

Multi Line comments are written like this: 

```

"""

This is a multi line comment. 
There can be more than one line and everything inside will be a comment. 

"""

three  = 3

```

## Strings 

Strings must be surrounded by double quotes: 

```

a = "Hello World" 
print(a)
# output: Hello World 

```

You can access the index of a character as such: 

```
# code above

print(a[2])

# Output: l

```

This is because strings are written as arrays of bytes representing Unicode characters. 

## Numbers 

There are three types of numbers in python: 

1. Integer (int)
  - This is a whole number, positive or negative 
  - There are no decimals
2. Floating point (float)
  - This is a number, positive or negative containing 1 or more decimals 
3. Complex Number (complex)
  - This is written with a j' as the imaginary part 

Example variables: 

```

x = 1 # int 
y = 2.43 # float 
zz = 1j # complex 

```

## Type 

To verify the type of any obbject in Python, you can use the type() method: 

```
print(type(x))
# Output: class 'int'
print(type(y))
# Output: class 'float'
print(type(z))
# Output: class 'complex'

