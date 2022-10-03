"""
The defaultdict tool is a container in the collections class of Python.
It's similar to the usual dictionary (dict) container, but the only difference is that
a defaultdict will have a default value if that key has not been set yet.
If you didn't use a defaultdict you'd have to check to see if that key exists,
and if it doesn't, set it to what you want.
For example:

from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i
This prints:

('python', ['awesome', 'language'])
('something-else', ['not relevant'])
In this challenge, you will be given 2 integers, n and m.
There are n words, which might repeat, in word group A. There are m words belonging to word group B.
For each m words, check whether the word has appeared in group A or not.
Print the indices of each occurrence of m in group A. If it does not appear, print -1.

Example

Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'

For the first word in group B, 'a', it appears at positions 1 and 3 in group A.
The second word, 'c', does not appear in group A, so print .

Expected output:

1 3
-1
Input Format

The first line contains integers, n and m separated by a space.
The next n lines contains the words belonging to group A.
The next m lines contains the words belonging to group B.

Constraints
1 <= n <= 10000
1 <= m <= 100
1 <= length of each word in the input <= 100



Output Format

Output m lines.
The i^{th} line should contain the 1-indexed positions of the occurrences of the i^{th} word separated by spaces.

Sample Input

STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b
Sample Output

1 2 4
3 5
Explanation

'a' appeared 3 times in positions 1, 2 and 4.
'b' appeared 2 times in positions 3 and 5.
In the sample problem, if 'c' also appeared in word group B, you would print -1.
"""
import collections

if __name__ == '__main__':
    default_dict = collections.defaultdict(list)
    n, m = list(map(int, input().split(' ')))
    for i in range(1, n + 1):
        default_dict[input()].append(str(i))
    for i in range(m):
        c = input()
        if c in default_dict:
            print(' '.join(default_dict[c]))
        else:
            print(-1)
