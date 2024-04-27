"""
Decorator library containing software code benchmarking functionalities
"""
import os
import sys
import time

def benchmark(fn):
    """
    Decorator to apply to a function to benchmark
    """
    # Initialize Variables
    result = ""

    def wrapper(*args, **kwargs):
        """
        Benchmark the provided function
        """
        # Start the timer
        start_timer = time.time()
        # Execute function
        result = fn(*args, **kwargs)
        # End the timer
        end_timer = time.time()
        # Calculate elapsed time (time passed)
        time_elapsed = end_timer - start_timer

        # Convert and calculate seconds in various formats using modulus
        hours, rem = divmod(time_elapsed, 3600)
        minutes, seconds = divmod(rem, 60)

        # Display result
        print("[i] Starting Time: {}".format(start_timer))
        print("[i] Ending Time: {}".format(end_timer))
        print("[i] Time taken: {} ({:0>2}:{:0>2}:{:05.2f})".format(time_elapsed, int(hours), int(minutes), seconds))

    # Return
    return wrapper

def benchmark_custom(verbose=True, return_result=False):
    """
    Benchmark a function (with its arguments) and print the start time, end time, and time elapsed, with custom arguments
    """
    # Initialize Variables
    result = ""

    def decorator(fn):
        """
        Decorator to apply to a function to benchmark, with custom options relating to the decorator
        """
        def wrapper(*args, **kwargs):
            """
            Benchmark the provided function
            """
            # Start the timer
            start_timer = time.time()
            # Execute function
            result = fn(*args, **kwargs)
            # End the timer
            end_timer = time.time()
            # Calculate elapsed time (time passed)
            time_elapsed = end_timer - start_timer

            # Convert and calculate seconds in various formats using modulus
            hours, rem = divmod(time_elapsed, 3600)
            minutes, seconds = divmod(rem, 60)

            # Display result
            if verbose == True:
                print("[i] Starting Time: {}".format(start_timer))
                print("[i] Ending Time: {}".format(end_timer))
                print("[i] Time taken: {} ({:0>2}:{:0>2}:{:05.2f})".format(time_elapsed, int(hours), int(minutes), seconds))

            # Check if flag 'return_result' is True
            if return_result == True:
                # True: Return the result; If False: return None
                return result

        # Return nested wrapper function
        return wrapper

    # Return nested decorator function
    return decorator

@benchmark
def main():
    print("Hello World")

if __name__ == "__main__":
    main()

