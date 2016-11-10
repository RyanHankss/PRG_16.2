class Time(object):

    """
    Represents the time of day.
    attributes: hour, minute, second
    """

t = Time()
hour = 11
minute = 18
second = 20


def is_after(t1, t2):
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

print(is_after(11,12))
