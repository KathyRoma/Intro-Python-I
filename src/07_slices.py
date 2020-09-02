"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print(a[1])

# Output the second-to-last element: 9
print()

# Output the last three elements in the array: [7, 9, 6]
print()

for i in a[-3:]:
    print(i)

# Output the two middle elements in the array: [1, 7]
print()

def print_middle(lst):
    if len(lst)%2 == 0:
        print(lst[int(len(lst)/2) -1], lst[int(len(lst)/2)])
    else:
        print(lst[int(len(lst)/2)])


def print_middle(lst):
    m = int(len(lst)/2)
    if len(lst)%2 == 0:
        print(lst[m -1], lst[m])
    else:
        print(lst[m])
# Output every element except the first one: [4, 1, 7, 9, 6]
print()

print(a[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
print()
print(a[:-1])
# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
l=len('world')
print(s[(-2 -l):-1])

ss = s.split(sep=' ')
print(ss[-1][:-1])