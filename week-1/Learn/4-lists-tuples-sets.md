# Lists, Tuples and Sets

Lists, tuples and sets are common data types in python used to store multiple items within. 

## Lists 

Lists are used to store multiple items in a single variable.
They are one of 4 built in data types in Python whose usecase is to store data.

Lists syntax: 

```

my_list = ["Tomato", "Broccoli", "Spinach"]
print(my_list)
# Output: my_list = ["Tomato", "Broccoli", "Spinach"]

```

You can access the length of any list using the length function: 

```

print(len(my_list)) # Output: 3

```

List items can be of any data type. 

## Tuples 

As with lists, tuples are used to store multiple items in a single variable. 
Unlike lists, tuples are ordered and immutable. 

Tuples are written with round brackets: 

```

my_tuple = ("Luton", "Leeds", "Newcastle")
print(my_tuple)
# Output: my_tuple = ("Luton", "Leeds", "Newcastle")

```

To reiterate, tuples are immutable which means they cannot be changed. 
They can be accessed by their index. 

To create tuple that has only 1 item you must add a comma after the first item else Python will not consider it as a tuple

``` 
my_tuple = ("Luton",)
print(type(my_tuple))
# Output: class 'tuple'

not_a_tuple = ("Luton")
print(type(not_a_tuple))
# Output: class 'string'

```

## Sets

As with lists and tuples, Sets are used to store multiple items into a single variable. 
Unlike lists and tuples, a set is a collection that is both: 

- Unordered 
- Unindexed

Sets are written within curly braces: 

```

my_set = {"Hello", "World", "Bitch"}
print(my_set)
# Output: my_set = {"Hello", "World", "Bitch"}

```

A quirk about sets is that they dissallow duplicate values. 
Also due to the fact that they are unnordered, sets can appear in a differe4nt order every time.

If you enter a duplicate value into a set, it will be ignored: 

```
my_set = {"Hello", "World", "Bitch", "World"}
print(my_set)
# Output: my_set = {"Hello", "World", "Bitch"}
```