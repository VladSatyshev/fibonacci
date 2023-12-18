from argparse import ArgumentTypeError


def range_type(min_val, max_val):
    def inner(str_val):
        value = int(str_val)
        if min_val <= value <= max_val:
            return value
        else:
            raise ArgumentTypeError(f"n is not in range 0..500")

    return inner
