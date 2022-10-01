"""
ABC is a right triangle, 90 degree at B.


Point M is the midpoint of hypotenuse AC.

You are given the lengths AB and BC.
Your task is to find angle MBC (angle theta, as shown in the figure) in degrees.

Input Format

The first line contains the length of side AB.
The second line contains the length of side BC.

Constraints
0 < AB <= 100
0 < BC <= 100

Lengths AB and BC are natural numbers.
Output Format

Output angle MBC in degrees.

Note: Round the angle to the nearest integer.

Examples:
If angle is 56.5000001°, then output 57°.
If angle is 56.5000000°, then output 57°.
If angle is 56.4999999°, then output 56°.
0 < theta < 90

Sample Input

10
10
Sample Output

45°
"""
import math

if __name__ == '__main__':
    ab = int(input())
    bc = int(input())
    ac = math.sqrt(ab ** 2 + bc ** 2)
    mc = ac / 2
    cos_c = bc / ac
    bm = math.sqrt((bc ** 2 + mc ** 2) - 2 * bc * mc * cos_c)
    cos_theta = (bm ** 2 + bc ** 2 - mc ** 2) / (2 * bm * bc)
    theta = math.acos(cos_theta)
    degree_theta = round(math.degrees(theta))
    print(f'{degree_theta}{chr(176)}')
