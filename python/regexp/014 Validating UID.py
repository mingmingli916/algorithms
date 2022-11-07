"""
ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits (0 - 9).
It should only contain alphanumeric characters (a - z, A - Z & 0 - 9).
No character should repeat.
There must be exactly 10 characters in a valid UID.
Input Format

The first line contains an integer T, the number of test cases.
The next T lines contains an employee's UID.

Output Format

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

Sample Input

2
B1CD102354
B1CDEF2354
Sample Output

Invalid
Valid
Explanation

B1CD102354: 1 is repeating → Invalid
B1CDEF2354: Valid
"""

import re


def check_uid(s):
    # [a-zA-Z0-9]
    # 10 characters
    if not re.match(r'^[a-zA-Z0-9]{10}$', s):
        return False
    # at least 2 uppercase
    if len(re.findall(r'[A-Z]', s)) < 2:
        return False
    # at least 3 digits
    if len(re.findall(r'[0-9]', s)) < 3:
        return False
    # repeat
    if len(set(s)) < 10:
        return False
    return True


if __name__ == '__main__':
    for _ in range(int(input())):
        if check_uid(input()):
            print('Valid')
        else:
            print('Invalid')