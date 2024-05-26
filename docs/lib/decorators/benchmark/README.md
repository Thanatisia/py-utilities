# Decorators - benchmark

## Information

### Module
+ Type: Decorator

### Description
+ Library containing various benchmark-related decorator functions and utilities to make benchmarking easier

## Documentations

### Packages
- pyutils.decorators

### Modules
- pyutils.decorators
    - `.benchmark`

### Classes

### Data Types/Objects

### Functions
- `benchmark(fn)`: Decorator to apply to a function to benchmark
    - Usage
        ```python
        @benchmark
        def function():
            print("Hello World")
        ```
- `benchmark_custom(verbose=True, return_result=False)`: Benchmark a function (with its arguments) and print the start time, end time, and time elapsed, with custom arguments
    - Parameters Signature/Headers
        - verbose : Enable/Disable verbose message output
            + Type: Boolean
            + Default: True
            - Values
                + True = Verbose
                + False = Not Verbose
        - return_result: Enable/Disable returning of result from function; Set True if your function has a result to return
            + Type: Boolean
            + Default: False
            - Values
                + True = return result
                + False = no return/return None

### Attributes/Variables

### Usage
- Enable/Disable verbose
    ```python
    @benchmark_custom(verbose={True|False})
    def function():
        print("Hello World")
    ```
- Enable/Disable returning of result
    - Results to return
        ```python
        @benchmark_custom(return_result=True)
        def function():
            return "Hello World"

        def main():
            msg = function()
            print(msg)
        ```
    - No results to return
        ```python
        @benchmark_custom(return_result=False)
        def function():
            print("Hello World")

        def main():
            function()
        ```

## Wiki

## Resources

## References

## Remarks

