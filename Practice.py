import pandas as pd
import numpy as np

my_list = np.array([1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 6, 5, 4])
uniq = pd.unique(my_list)

# print(uniq)

# What are a couple of attributes from the pandas series?
# Size, dtypes,

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

print(type(df))
print(df)
print(df.info)
print(df.describe())

