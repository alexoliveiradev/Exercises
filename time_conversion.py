"""
Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in
hours:minutes:seconds.

Input
The input file contains an integer N.

Output
Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example.

556         ->      	0:9:16
"""


def converter(seconds):
    h, m, s = 0, 0, 0
    h = seconds // 3600
    m = int(seconds / 3600 * 60)
    s = (seconds % 3600 * 60) * 60
    return f'{h}:{m}:{s}'


print(converter(556))
