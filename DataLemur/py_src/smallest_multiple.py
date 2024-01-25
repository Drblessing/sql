import math
import time


def smallest_multiple(target: int) -> int:
    """Returns the smallest positive number that is evenly
    divisible by all of the numbers from 1 to target."""

    # Initialize the lowest common multiple (LCM) to 1
    lowest_cm = 1

    # The maximum lcm is the product of all numbers from 1 to target
    max_lcm = math.prod(range(1, target + 1))

    # Iterate through all numbers from 1 to max_lcm
    for i in range(1, max_lcm + 1):
        # Assume the number is the lcm
        is_lcm = True
        # Iterate through all numbers from 1 to target
        for j in range(1, target + 1):
            # If the number is not evenly divisible by any number
            # from 1 to target, it is not the lcm
            if i % j != 0:
                is_lcm = False
                break
        # If the number is the lcm, return it
        if is_lcm:
            return i


def smallest_multiple_fast(target: int) -> int:
    return math.lcm(*range(1, target + 1))


if __name__ == "__main__":
    # Time the function
    start = time.perf_counter()
    smallest_multiple(17)
    end = time.perf_counter()
    slow_time = end - start
    print(f"Slow time: {slow_time:0.6f} seconds")
    start = time.perf_counter()
    smallest_multiple_fast(17)
    end = time.perf_counter()
    fast_time = end - start
    print(f"Fast time: {fast_time:0.6f} seconds")
    print(f"Multiply factor: {slow_time / fast_time:0.2f}")
