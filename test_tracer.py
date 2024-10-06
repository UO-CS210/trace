"""Unit tests for tracer.trace decorator.
Why is this in the top-level directory?  Because Python's import machinery
is obtuse and won't allow a relative import from a parent or sibling without a bunch of
extra hackery.  C'mon Python, this has been a mess for way too long.
"""
import sys
import itertools

from tracer import trace




with open("test_results/actual/fact4", "w") as result:
    @trace(result)
    def fact(n: int) -> int:
        if n > 1:
            return n * fact(n-1)
        else:
            return 1
    fact(4)


with open("test_results/actual/gcd_12_10", "w") as result:
    @trace(result)
    def gcd(m: int, n: int) -> int:
        if n > 0:
            return gcd(n, m % n)
        return m
    gcd(12,10)


with open("test_results/actual/fib_5", "w") as result:
    @trace(result)
    def fib(m: int) -> int:
        if m > 1:
            return fib(m-1) + fib(m-2)
        else:
            return m
    fib(5)


def compare_results(actual: str, expected: str) -> bool:
    """Returns True if file contents are identical.
    Otherwise returns False AND prints a diff.
    """
    try:
        actual_file = open(actual, "r")
    except Exception:
        f"Unable to open {actual}"
        return False

    snip =35  # Length of displayed prefixes of actual and expected

    expected_file = open(expected, "r")
    actual_text = [line.rstrip().ljust(snip, ' ') for line in actual_file.readlines()]
    expected_text = [line.rstrip().ljust(snip, ' ') for line in expected_file.readlines()]
    actual_file.close()
    expected_file.close()
    if actual_text == expected_text:
        return True
    # Diagnostic output
    pairs = itertools.zip_longest(actual_text, expected_text, fillvalue=" " * snip)
    print("---")
    print(f"Actual output in {actual} doesn't match expected", file=sys.stderr)
    print(f"  {'Actual':35} | {'Expected':35}", file=sys.stderr)
    filler = " "
    for actual_line, expected_line in pairs:
        mark = " " if actual_line == expected_line else "X"
        print(f"{mark} {actual_line} . {expected_line}",
              file=sys.stderr)
    print()


if __name__ == "__main__":
    ok = compare_results("test_results/actual/fact4",
                         "test_results/expected/fact4")
    ok = compare_results("test_results/actual/gcd_12_10",
                         "test_results/expected/gcd_12_10") and ok
    ok = compare_results("test_results/actual/fib_5",
                         "test_results/expected/fib_5") and ok
    if ok:
        print("All tests passed", file=sys.stderr)
    else:
        print("Some tests failed", file=sys.stderr)







