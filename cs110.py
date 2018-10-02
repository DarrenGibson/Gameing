#
# Example 1
#

print()
print('Example 1:')
first = 4
second = first
print('first: {}'.format(first))
print('second: {}'.format(second))
# Do first and second point to the same place in memory,
# or are they two distinct things that happen to be the same?

first = first + 3
print('first: {}'.format(first))
print('second: {}'.format(second))
# What do you think now?
# Do first and second point to the same place in memory,
# or are they two distinct things that happen to be the same?

#
# Example 2
#

print()
print('Example 2:')
first = 'Erez'
second = first
print('first: {}'.format(first))
print('second: {}'.format(second))
# Do first and second point to the same place in memory,
# or are they two distinct things that happen to be the same?

first = first + ' Morag'
print('first: {}'.format(first))
print('second: {}'.format(second))
# What do you think now?
# Do first and second point to the same place in memory,
# or are they two distinct things that happen to be the same?

#
# Example 3
#

print()
print('Example 3:')
first = [ 'Erez', 'is', 'a' ]
second = first
print('first: {}'.format(first))
print('second: {}'.format(second))
# Do first and second point to the same place in memory,
# or are they two distinct things that happen to be the same?

first.append('teacher.')
print('first: {}'.format(first))
print('second: {}'.format(second))
# What do you think now?
# Do first and second point to the same place in memory,
# or are they two distinct things that happen to be the same?

#
# Example 4
#

print()
print('Example 4:')
first = 'Hello.'
second = first
print('first: {}'.format(first))
print('second: {}'.format(second))
# Do first and second point to the same place in memory,
# or are they two distinct things that happen to be the same?

# Try this line of code by removing the # and running the code:
# first[5] = '!'
# It will fail. Why?
# What does "TypeError: 'str' object does not support item assignment" mean?
# When you are done, add the # back in front of the bad code.
first = first.replace('.', '!')
print('first: {}'.format(first))
print('second: {}'.format(second))
# What do you think now?
# Do first and second point to the same place in memory,
# or are they two distinct things that happen to be the same?

#
# Example 5
#

print()
print('Example 5:')
first = [ 'Erez', 'is', 'a', 'teacher.' ]
second = first
print('first: {}'.format(first))
print('second: {}'.format(second))
# Do first and second point to the same place in memory,
# or are they two distinct things that happen to be the same?

first[3] = 'instructor.'
second[3] = 'engineer.'
print('first: {}'.format(first))
print('second: {}'.format(second))
# What do you think now?
# Do first and second point to the same place in memory,
# or are they two distinct things that happen to be the same?






























