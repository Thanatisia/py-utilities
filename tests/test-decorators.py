"""
Unit Test for decorators
"""
import os
import sys
from pyutils.libraries.utils import pprint_info, pprint_error, pprint_warning
from pyutils.decorators.benchmark import benchmark, benchmark_custom

@benchmark
def test_benchmark():
    print("Hello World")

@benchmark_custom(verbose=True)
def test_benchmark_verbose_true():
    print("Hello World")

@benchmark_custom(verbose=False)
def test_benchmark_verbose_false():
    print("Hello World")

def main():
    try:
        pprint_info("Unit Test Target: test_benchmark()", fmt_str="[*]")
        test_benchmark()
        pprint_info("Status: Success", fmt_str="[+]")

        print("")

        pprint_info("Unit Test Target: test_benchmark_verbose_true()", fmt_str="[*]")
        test_benchmark_verbose_true()
        pprint_info("Status: Success", fmt_str="[+]")

        print("")

        pprint_info("Unit Test Target: test_benchmark_verbose_false()", fmt_str="[*]")
        test_benchmark_verbose_false()
        pprint_info("Status: Success", fmt_str="[+]")
    except Exception as ex:
        pprint_error("Error detected: {}".format(ex))

if __name__ == "__main__":
    main()

