class Time(object):

    """
    Represents the time of day.
    attributes: hour, minute, second
    """

t1 = Time()
t1.hour = 11
t1.minute = 18
t1.second = 20

t2 = Time()
t2.hour = 13
t2.minute = 30
t2.second = 20

def times(t1, t2):
    seconds = 0
    seconds.hour = hour * 60 * 60
    seconds.minute = minute * 60
    seconds = seconds


def is_after(time1, time2):
   time1 > time2

print(is_after(t1, t2))
