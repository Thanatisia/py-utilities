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

def benchmark_loops(iter_count=0, results=None):
    """
    Benchmark N iterations/loops of the function

    :: Params
    - iter_count : Specify the number of iterations/loops to run the provided function
        + Type: Integer
        + Default: 0

    - results : Pass a dictionary (key-value mapping) variable from the caller that you want to store the results into
        + Type: Dictionary
        + Default: None
    """
    def decorator(fn):
        """
        Decorator to apply to a function to benchmark, with custom options relating to the decorator
        """
        def wrapper(*args, **kwargs):
            # Initialize Variables
            results = {
                "benchmark" : {
                    "time-start" : "",
                    "time-end" : "",
                    "time-elapsed" : "",
                },
                "function" : { "results" : [] },
            }

            # Get starting time
            timer_start = time.time()
    
            # Iterate iter_count number of times
            for i in range(iter_count):
                # Execute the function and its arguments
                result = fn(*args, **kwargs)
         
                # Store the current result
                results["function"]["results"].append(result)

            # Get ending time
            timer_end = time.time()

            # Calculate time passed
            time_elapsed = timer_end - timer_start

            # Store the start time
            results["benchmark"]["time-start"] = timer_start

            # Store the end time
            results["benchmark"]["time-end"] = timer_end

            # Store the elapsed time
            results["benchmark"]["time-elapsed"] = time_elapsed

            # Return the results
            return results

        # Return the wrapper object
        return wrapper

    # Return the decorator object
    return decorator

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

