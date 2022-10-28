"""
You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print True. Otherwise, print False. Try to create a regular expression for a valid Roman numeral.

Input Format

A single line of input containing a string of Roman characters.

Output Format

Output a single line containing True or False according to the instructions above.

Constraints

The number will be between 1 and 3999 (both included).

Sample Input

CDXXI
Sample Output

True
References

Regular expressions are a key concept in any programming language. A quick explanation with Python examples is available here. You could also go through the link below to read more about regular expressions in Python.

https://developers.google.com/edu/python/regular-expressions
"""

"""
number  = a * 1000 + b * 100 + c * 10 + d
for a:
M{0,3}

for b:
0-3: C{0,3}
4: CD
5-8: DC{0,3}
9: CM
D?C{0,3}|C[DM]

for c:
0-3: X{0,3}
4: XL
5-8: LX{0,3}
9: XC
L?X{0,3}|X[LC]

for d:
0-3: I{0,3}
4: IV
5-8: VI{0,3}
9: IX
V?I{0,3}|I[VX]
"""

regex_pattern = r"{}{}{}{}$".format('M{0,3}', '(D?C{0,3}|C[DM])', '(L?X{0,3}|X[LC])', '(V?I{0,3}|I[VX])')
# Do not delete 'r'.

import re

print(str(bool(re.match(regex_pattern, input()))))
