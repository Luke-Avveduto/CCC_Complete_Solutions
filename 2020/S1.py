"""
Senior 1: Surmising a Sprinter’s Speed

Problem Description:
Trick E. Dingo is trying, as usual, to catch his nemesis the Street Sprinter. His past attempts
using magnets, traps and explosives have failed miserably, so he’s catching his breath to gather
observational data and learn more about how fast Street Sprinter is.
Trick E. Dingo and Street Sprinter both inhabit a single straight west-east road with a particularly
famous rock on it known affectionately as The Origin. Positions on this straight road are measured
numerically according to the distance from The Origin, and using negative numbers for positions
west of The Origin and positive numbers for positions east of The Origin.
The observations by Trick E. Dingo each contain two numbers: a time, and the value of Street
Sprinter’s position on the road at that time. Given this information, what speed must Street Sprinter
must be capable of?

Input Specification:
The first line contains a number 2 ≤ N ≤ 100 000, the number of observations that follow. The
next N lines each contain an integer 0 ≤ T ≤ 1 000 000 000 indicating the time, in seconds, of
when a measurement was made, and an integer −1 000 000 000 ≤ X ≤ 1 000 000 000 indicating
the position, in metres, of the Street Sprinter at that time. No two lines will have the same value
of T.

Output Specification
Output a single number X, such that we can conclude that Street Sprinter’s speed was at least X
metres/second at some point in time, and such that X is as large as possible. If the correct answer
is C, the grader will view X as correct if |X − C|/C < 10−5.

See https://cemc.uwaterloo.ca/contests/computing/2020/ccc/seniorEF.pdf
for more information.

Solution is copyright Luke Avveduto, 2021.
"""

n = int(input())

pairs = []
for _ in range(0, n):
    input_list = input().split(' ')
    pairs.append((int(input_list[0]), int(input_list[1])))

pairs.sort(key=lambda s: s[0])

speeds = [abs((pairs[i][1] - pairs[i - 1][1])/(pairs[i][0] - pairs[i - 1][0]))
          for i in range(1, len(pairs))]

print(max(speeds))
