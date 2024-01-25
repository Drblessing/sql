def largest_prime_factor(target: int) -> int:
    """Returns the largest prime factor of target."""

    # Check that target is an integer
    if not isinstance(target, int):
        raise TypeError("target must be an integer.")

    # Check that target is positive
    if target < 1:
        raise ValueError("target must be positive.")

    # Find the largest prime factor of target
    i = 2
    while i * i <= target:
        if target % i:
            i += 1
        else:
            target //= i
    return target
