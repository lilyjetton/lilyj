import sys
def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the callers line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def to_secs(hours,minutes,seconds):
    hours = hours*3600
    minutes = minutes*60
    total = hours+minutes+seconds
    return total

test(to_secs(2, 30, 10) == 9010)
test(to_secs(2, 0, 0) == 7200)
test(to_secs(0, 2, 0) == 100)
test(to_secs(0, 0, 42) == 42)
test(to_secs(0, -10, 10) == -590)
