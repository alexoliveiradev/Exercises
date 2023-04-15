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
    h = round(seconds // 3600)
    m = round((seconds % 3600) / 60)
    s = round(seconds % 60)
    return f"{h}:{m}:{s}"


print(converter(556))
print(converter(1))
print(converter(140153))
