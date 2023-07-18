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
# print(v.mask(v != 1))
print(v[v == 1])

print()
print()
print()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
i = 1
print('EXERCISES PART 2')
print(f'########## QUESTION {i} #############')
i += 1
# 1. Capitalize all the string values in fruits.
print(fruits.str.capitalize())

print(f'########## QUESTION {i} #############')
i += 1
# 2. Count the letter "a" in all the string values (use string vectorization).
print(fruits.str.count('a'))

print(f'########## QUESTION {i} #############')
i += 1
# 3. Output the number of vowels in each and every string value.
vowels = '[aeiou]'
v = fruits.str.count(vowels)
print(v)

print(f'########## QUESTION {i} #############')
i += 1
# 4. Write the code to get the longest string value from fruits.
# print(fruits.str.len().max())
l = fruits.str.len()
print(fruits[l == l.max()])


print(f'########## QUESTION {i} #############')
i += 1
# 5. Write the code to get the string values with 5 or more letters in the name.
print(fruits[l >= 5])


print(f'########## QUESTION {i} #############')
i += 1
# 6. Find the fruit(s) containing the letter "o" two or more times.
print(fruits[fruits.str.count('o') >= 2])

print(f'########## QUESTION {i} #############')
i += 1
# 7. Write the code to get only the string values containing the substring "berry".
print(fruits[fruits.str.contains('berry')])

print(f'########## QUESTION {i} #############')
i += 1
# 8. Write the code to get only the string values containing the substring "apple".
print(fruits[fruits.str.contains('apple')])

print(f'########## QUESTION {i} #############')
i += 1
# 9. Which string value contains the most vowels?
vowels = '[aeiou]'
print(fruits[v.max() == v])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
i = 1
print('EXERCISES PART 3')
print(f'########## QUESTION {i} #############')
i += 1


# Use pandas to create a Series named letters from the following string. The easiest way to make this string into a
# Pandas series is to use list to convert each individual letter into a single string on a basic Python list.

letters = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))

# 1. Which letter occurs the most frequently in the letters Series?
l = letters.value_counts()
print(l[l.max() == l])

print(f'########## QUESTION {i} #############')
i += 1
# 2. Which letter occurs the Least frequently?
l = letters.value_counts()
print(l[l.min() == l])

print(f'########## QUESTION {i} #############')
i += 1
# 3. How many vowels are in the Series?
vowels = list('aeiou')
vc = letters[letters.isin(vowels)]
print(vc.value_counts().sum())

print(f'########## QUESTION {i} #############')
i += 1
# 4. How many consonants are in the Series?
print(letters.count() - (vc.value_counts().sum()))

print(f'########## QUESTION {i} #############')
i += 1
# 5. Create a Series that has all of the same letters but uppercased.
print(letters.str.upper())

print(f'########## QUESTION {i} #############')
i += 1
# 6. Create a bar plot of the frequencies of the 6 most commonly occurring letters.
top_six = l.head(6)
top_six.name = 'Most common letters'

top_six.plot.bar




i = 1
print(f'########## QUESTION {i} #############')
i += 1

# Use pandas to create a Series named numbers from the following list:
numbers = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3',
                     '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17',
                     '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38',
                     '$2,791,759.67', '$769,681.94', '$452,650.23'])

# 1. What is the data type of the numbers Series?
print('The type of data in the series is string')


print(f'########## QUESTION {i} #############')
i += 1
# 2. How many elements are in the number Series?
print(numbers.count())

print(f'########## QUESTION {i} #############')
i += 1
# 3. Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers
# Series to a numeric data type.
n = numbers.str.replace(',','').str.replace('$','').astype(float)
print(n)

print(f'########## QUESTION {i} #############')
i += 1
# 4. Run the code to discover the maximum value from the Series.
print(n.max())


print(f'########## QUESTION {i} #############')
i += 1
# 5. Run the code to discover the minimum value from the Series.
print(n.min())

print(f'########## QUESTION {i} #############')
i += 1
# 6. What is the range of the values in the Series?
print(n.max(),n.min())

print(f'########## QUESTION {i} #############')
i += 1
# 7. Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
b = pd.cut(n,4)
print(b)

#print(pd.cut(n,4))

print(f'########## QUESTION {i} #############')
i += 1
# 8. Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
print(b.value_counts().plot(kind='bar',title='num distribution'))


i = 1
print(f'########## QUESTION {i} #############')
i += 1
# Use pandas to create a Series named exam_scores from the following list:

exam = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

# 1. How many elements are in the exam_scores Series?
print(exam.count())

print(f'########## QUESTION {i} #############')
i += 1
# 2. Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.

print(f'min {exam.min()}')
print(f'max {exam.max()}')
print(f'mean {exam.mean()}')
print(f'median {exam.median()}')

print(f'########## QUESTION {i} #############')
i += 1
# 3. Plot the Series in a meaningful way and make sure your chart has a title and axis labels.
exam_graph = pd.cut(exam,4,labels=['q1','q2','q3','q4'])
print(exam_graph)
print(exam_graph.value_counts().plot(kind='bar', title='Score distribution'))


print(f'########## QUESTION {i} #############')
i += 1
# 4. Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades.
# Add the necessary points to the highest grade to make it 100, and add the same number of points to every other
# score in the Series as well.
curve = 100 - exam.max()
curved_grades = exam + curve
print(curved_grades)

print(f'########## QUESTION {i} #############')
i += 1
# 5. Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of
# letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.
def get_letter_grade(grade):
    letter_grade = ''   #created local string variable with no value
    if grade >= 90:
        letter_grade = 'A'
    elif grade >= 80:
        letter_grade = 'B'
    elif grade >= 70:
        letter_grade = 'C'    # uses if functions to decide what grade should be based off the given integer
    elif grade >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    return letter_grade   # returns letter grade after it has been assigned a value

letter_grades = curved_grades.apply(get_letter_grade)
print(letter_grades)


print(f'########## QUESTION {i} #############')
i += 1
# 6. Plot your new categorical letter_grades Series in a meaningful way and include a title and axis labels.
lg = letter_grades.value_counts()
print(lg.plot(kind='bar',title='Grade Distribution'))