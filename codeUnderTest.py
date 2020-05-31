from funcIOLogger import logIO


def strip_C(s):
    rightTrimmedStr = rstrip_C(s)
    leftTrimmedStr = lstrip_C(rightTrimmedStr)

    return leftTrimmedStr


@logIO
def rstrip_C(s):
    if len(s) == 0:
        return ""

    end = -1
    while s[end].isspace():
        end -= 1

    return s[: (end + 1)]


def lstrip_C(s):
    if len(s) == 0:
        return ""

    start = 0
    while s[start].isspace():
        start += 1

    return s[start:]
