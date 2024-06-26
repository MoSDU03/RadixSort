def radix_sort_complexity(n):
    # Range of numbers is [0, n^3)
    # Digits are 3, base is n since range is 0 to n-1 for each digit
    d = 3  # Number of digits
    b = n  # Base (since each digit can be 0 to n-1)
    
    # Calculate the time complexity
    complexity = d * (n + b)
    
    # Display the time complexity in Theta notation
    if complexity == n:
        return "Θ(n)"
    elif complexity == n * (n + n):
        return "Θ(n log n)"
    elif complexity == n * n:
        return "Θ(n^2)"
    else:
        return "Θ(n)"

# Test the function with an example
n = 100  # Example number of integers
print(f"Worst-case time complexity for Radix Sort with n={n}: {radix_sort_complexity(n)}")
