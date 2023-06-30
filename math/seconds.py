"""
Make a function that takes three integers as parameters representing hours, minutes and seconds,
and convert them to seconds.
"""


def convert(hours, minutes, seconds):
    """
    The function transforms hours, minutes and seconds into seconds
    :param hours: Receive the number of hours
    :param minutes: Receive the number of minutes
    :param seconds: Receive the number of seconds
    :return: Return total seconds
    """
    hours = hours * 3600
    minutes = minutes * 60
    total = hours + minutes + seconds
    return f"Total of seconds: {total}"


print(convert(2, 30, 45))
