import pandas as pd

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato",
                    "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry",
                    "gooseberry", "papaya"])

i = 1
print(f'########## QUESTION {i} #############')
i += 1
# 1. Determine the number of elements in fruits.
print(fruits.count())

print(f'########## QUESTION {i} #############')
i += 1
# 2. Output only the index from fruits.
print(fruits.index)

print(f'########## QUESTION {i} #############')
i += 1
# 3. Output only the values from fruits.
print(fruits.values)

print(f'########## QUESTION {i} #############')
i += 1
# 4. Confirm the data type of the values in fruits.
print(fruits.dtype)

print(f'########## QUESTION {i} #############')
i += 1
# 5. Output only the first five values from fruits. Output the last three values. Output two random values from fruits.
print(fruits.head())
print(fruits.tail(3))
print(fruits.sample(2))

print(f'########## QUESTION {i} #############')
i += 1
# 6. Run the .describe() on fruits to see what information it returns when called on a Series with string values.
print(fruits.describe())

print(f'########## QUESTION {i} #############')
i += 1
# 7. Run the code necessary to produce only the unique string values from fruits.
print(fruits.unique())

print(f'########## QUESTION {i} #############')
i += 1
# 8. Determine how many times each unique string value occurs in fruits.
print(fruits.value_counts())

print(f'########## QUESTION {i} #############')
i += 1
# 9. Determine the string value that occurs most frequently in fruits.
print(fruits.mode())

print(f'########## QUESTION {i} #############')
i += 1
# 10. Determine the string value that occurs least frequently in fruits.
v = fruits.value_counts()
#print(v.mask(v != 1))
print(v[v == 1])


