import sys


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def merge_d(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs): # If xs list is finished,
            result.extend(ys[yi:]) # Add remaining items from ys
            break

        if yi >= len(ys): # Same again, but swap roles
            result.extend(xs[xi:])
            break

        # Both lists still have items, copy smaller item to result.
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] > ys[yi]:
            result.append(ys[yi])
            yi += 1
        else:
            result.append(xs[xi])
            xi += 1
            yi += 1
    return result


def merge_a(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):  # If xs list is finished,
            break

        if yi >= len(ys):  # Same again, but swap roles
            break

        # Both lists still have items, copy smaller item to result.
        if xs[xi] < ys[yi]:
            xi += 1
        elif xs[xi] > ys[yi]:
            yi += 1
        else:
            result.append(xs[xi])
            xi += 1
            yi += 1

    return result


def merge_b(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):  # If xs list is finished,
            break

        if yi >= len(ys):  # Same again, but swap roles
            result.extend(xs[xi:])
            break

        # Both lists still have items, copy smaller item to result.
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] > ys[yi]:
            yi += 1
        else:
            xi += 1
            yi += 1

    return result


def merge_c(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):  # If xs list is finished,
            result.extend(ys[yi:])
            break

        if yi >= len(ys):  # Same again, but swap roles
            break

        # Both lists still have items, copy smaller item to result.
        if ys[yi] < xs[xi]:
            result.append(ys[yi])
            yi += 1
        elif ys[yi] > xs[xi]:
            xi += 1
        else:
            xi += 1
            yi += 1

    return result


def merge_e(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs): # If xs list is finished,
            # result.extend(ys[yi:]) # Add remaining items from ys
            break

        if yi >= len(ys): # Same again, but swap roles
            result.extend(xs[xi:])
            break

        # Both lists still have items, copy smaller item to result.
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] > ys[yi]:
            yi += 1
        else:
            xi += 1
            yi += 1
    return result


# test(merge_a([], []) == [])
# test(merge_a(["a", "b"], []) == [])
# test(merge_a([], ["a", "b"]) == [])
# test(merge_a(["a", "b", "c"], ["A", "a", "b"]) == ["a", "b"])
# test(merge_a(["a", "b", "c"], ["d", "e", "f"]) == [])
#
# test(merge_b([], []) == [])
# test(merge_b(["a", "b"], []) == ["a", "b"])
# test(merge_b([], ["a", "b"]) == [])
# test(merge_b(["a", "b", "c"], ["A", "a", "b"]) == ["c"])
# test(merge_b(["a", "b", "c"], ["d", "e", "f"]) == ["a", "b", "c"])
#
# test(merge_c([], []) == [])
# test(merge_c([], ["a", "b"]) == ["a", "b"])
# test(merge_c(["a", "b"], []) == [])
# test(merge_c(["A", "a", "b"], ["a", "b", "c"]) == ["c"])
# test(merge_c(["d", "e", "f"], ["a", "b", "c"]) == ["a", "b", "c"])
#
# test(merge_d([], []) == [])
# test(merge_d([], ["a", "b"]) == ["a", "b"])
# test(merge_d(["a", "b"], []) == ["a", "b"])
# test(merge_d(["A", "a", "b"], ["a", "b", "c"]) == ["A", "a", "b", "c"])
# test(merge_d(["d", "e", "f"], ["a", "b", "c"]) == ["a", "b", "c", "d", "e", "f"])

test(merge_e([5, 7, 11, 11, 11, 12, 13], [7, 8, 11]) == [5, 11, 11, 12, 13])
