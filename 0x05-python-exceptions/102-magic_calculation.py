#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for inc in range(1, 3):
        try:
            if inc > a:
                raise Exception('Too far')
            result += a ** b / inc
        except Exception:
            result = b + a
            break
    return (result)
