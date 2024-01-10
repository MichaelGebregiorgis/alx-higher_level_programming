#!/usr/bin/python3
"""computes metrics"""


def print_stats(size, status_codes):
    """Print accumulated metrics"""
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

    if __name__ == "__main__":
        import sys

        size = 0
        status_codes = {}
        code = {'200', '301', '400', '401', '403', '404', '405', '500'}
        cnt = 0
        try:
            for ln in sys.stdin:
                if cnt == 10:
                    print_stats(size, status_codes)
                    cnt = 1
                else:
                    cnt += 1
                ln = ln.split()

                try:
                    size += int(ln[-1])
                except (IndexError, ValueError):
                    pass
                try:
                    if ln[-2] in code:
                        status_codes[ln[-2]] = status_codes.get(line[-2], 0) + 1
                except IndexError:
                    pass
            print_stats(size, code)
        except KeyboardInterrupt:
            print_stats(size, code)
            raise
        except BrokenPipeError:
            pass
