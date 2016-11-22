class Time(object):
    """
    time object 1
    """
t1 = Time()
t1.hour = 12
t1.minute = 45
t1.second = 35

t2 = Time()
t2.hour = 8
t2.minute = 25
t2.second = 15


def is_after(ti, tm):
    return (ti.hour, ti.minute, ti.second) > (tm.hour, tm.minute, tm.second)

print is_after(t1,t2)
