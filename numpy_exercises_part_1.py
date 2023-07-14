import numpy as np

# Setup 1
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Use python's built in functionality/operators to determine the following:
en = 1
print(f'##########  EXERCISE {en}  ###############')
en += 1
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
print(sum_of_a)


print(f'##########  EXERCISE {en}  ###############')
en += 1
# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
print(min_of_a)


print(f'##########  EXERCISE {en}  ###############')
en += 1
# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
print(max_of_a)

print(f'##########  EXERCISE {en}  ###############')
en += 1
# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum(a)/len(a)
print(mean_of_a)

print(f'##########  EXERCISE {en}  ###############')
en += 1
# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above
# list together
product_of_a = 1
for n in a:
    product_of_a *= n

print(product_of_a)


# list together
print(f'##########  EXERCISE {en}  ###############')
en += 1
# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = a ** 2
print(squares_of_a)


print(f'##########  EXERCISE {en}  ###############')
en += 1
# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = a % 2 != 0
print(a[odds_in_a])

print(f'##########  EXERCISE {en}  ###############')
en += 1
# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = a % 2 == 0
print(a[evens_in_a])

en = 1
print(f'##########  EXERCISE {en} SETUP 2  ###############')
en += 1
# What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
# Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for
# this list of two lists.
b = np.array([[3, 4, 5],
              [6, 7, 8]])

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make
# sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

print(np.sum(b))

print(f'##########  EXERCISE {en} SETUP 2  ###############')
en += 1
# Exercise 2 - refactor the following to use numpy.
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])
print(np.min(b))

print(f'##########  EXERCISE {en} SETUP 2  ###############')
en += 1
# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

print(np.max(b))

print(f'##########  EXERCISE {en} SETUP 2  ###############')
en += 1
# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

print(np.sum(b)/np.size(b))

print(f'##########  EXERCISE {en} SETUP 2  ###############')
en += 1
# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

print(np.prod(b))

print(f'##########  EXERCISE {en} SETUP 2  ###############')
en += 1
# Exercise 6 - refactor the following to use numpy to find the list of squares
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

print(squares_of_b)
print(np.square(b))
print(np.concatenate(np.square(b)))

print(f'##########  EXERCISE {en} SETUP 2  ###############')
en += 1
# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if number % 2 != 0:
            odds_in_b.append(number)

bb = np.concatenate(b)
print(bb[bb % 2 != 0])

print(f'##########  EXERCISE {en} SETUP 2  ###############')
en += 1
# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if number % 2 == 0:
            evens_in_b.append(number)

bb = np.concatenate(b)
print(bb[bb % 2 == 0])


print(f'##########  EXERCISE {en} SETUP 2  ###############')
en += 1
# Exercise 9 - print out the shape of the array b.

print(np.shape(b))

print(f'##########  EXERCISE {en} SETUP 2  ###############')
en += 1
# Exercise 10 - transpose the array b.
print(np.transpose(b))

print(f'##########  EXERCISE {en} SETUP 2  ###############')
en += 1
# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

print(np.reshape(b, 6))

print(f'##########  EXERCISE {en} SETUP 2  ###############')
en += 1
# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

print(np.reshape(b, (6, 1)))


en = 1
print(f'##########  EXERCISE {en} SETUP 3  ###############')
en += 1
# Setup 3
c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.


print(f'##########  EXERCISE {en} SETUP 3  ###############')
en += 1
# Exercise 2 - Determine the standard deviation of c
print(np.std(c))

print(f'##########  EXERCISE {en} SETUP 3  ###############')
en += 1
# Exercise 3 - Determine the variance of c.

print(np.var(c))

print(f'##########  EXERCISE {en} SETUP 3  ###############')
en += 1
# Exercise 4 - Print out the shape of the array c
print(np.shape(c))

print(f'##########  EXERCISE {en} SETUP 3  ###############')
en += 1
# Exercise 5 - Transpose c and print out transposed result.
print(c)
print(np.transpose(c))

print(f'##########  EXERCISE {en} SETUP 3  ###############')
en += 1
# Exercise 6 - Get the dot product of the array c with c.
print(np.dot(c, c))

print(f'##########  EXERCISE {en} SETUP 3  ###############')
en += 1
# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
print(np.sum(np.transpose(c)*c))

print(f'##########  EXERCISE {en} SETUP 3  ###############')
en += 1
# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
print(np.prod(np.transpose(c)*c))

# Setup 4
d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
])

en = 1
print(f'##########  EXERCISE {en} SETUP 3  ###############')
en += 1
# Exercise 1 - Find the sine of all the numbers in d
print(np.sin(d))

print(f'##########  EXERCISE {en} SETUP 3  ###############')
en += 1
# Exercise 2 - Find the cosine of all the numbers in d
print(np.cos(d))

print(f'##########  EXERCISE {en} SETUP 3  ###############')
en += 1
# Exercise 3 - Find the tangent of all the numbers in d
print(np.tan(d))


print(f'##########  EXERCISE {en} SETUP 3  ###############')
en += 1
# Exercise 4 - Find all the negative numbers in d
negatives = d < 0
n = d[negatives]
print(n)

print(f'##########  EXERCISE {en} SETUP 3  ###############')
en += 1
# Exercise 5 - Find all the positive numbers in d
positives = d > 0
p = d[positives]
print(p)


print(f'##########  EXERCISE {en} SETUP 3  ###############')
en += 1
# Exercise 6 - Return an array of only the unique numbers in d.
print(np.unique(d))


print(f'##########  EXERCISE {en} SETUP 3  ###############')
en += 1
# Exercise 7 - Determine how many unique numbers there are in d.
print(np.size(np.unique(d)))


print(f'##########  EXERCISE {en} SETUP 3  ###############')
en += 1
# Exercise 8 - Print out the shape of d.
print(np.shape(d))


print(f'##########  EXERCISE {en} SETUP 3  ###############')
en += 1
# Exercise 9 - Transpose and then print out the shape of d.
print(np.shape(np.transpose(d)))


print(f'##########  EXERCISE {en} SETUP 3  ###############')
en += 1
# Exercise 10 - Reshape d into an array of 9 x 2


print(np.reshape(d,(9,2)))