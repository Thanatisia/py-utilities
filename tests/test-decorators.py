"""
Unit Test for decorators
"""
import os
import sys
from pyutils.libraries.utils import pprint_info, pprint_error, pprint_warning
from pyutils.decorators.benchmark import benchmark, benchmark_loops, benchmark_custom

@benchmark
def test_benchmark():
    print("Hello World")

result = {}
@benchmark_loops(iter_count=4, results=result)
def test_benchmark_iter():
    print("Hello World")
    return result

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

        pprint_info("Unit Test Target: test_benchmark_iter()", fmt_str="[*]")
        result = test_benchmark_iter()
        # Get result values
        start_timer = result["benchmark"]["time-start"]
        end_timer = result["benchmark"]["time-end"]
        time_elapsed = result["benchmark"]["time-elapsed"]
        # Convert and calculate seconds in various formats using modulus
        hours, rem = divmod(time_elapsed, 3600)
        minutes, seconds = divmod(rem, 60)
        # Print results
        print("[i] Starting Time: {}".format(start_timer))
        print("[i] Ending Time: {}".format(end_timer))
        print("[i] Time taken: {} ({:0>2}:{:0>2}:{:05.2f})".format(time_elapsed, int(hours), int(minutes), seconds))
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

