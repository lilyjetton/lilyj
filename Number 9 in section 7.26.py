def print_triangular_numbers(n):
    """Returns a list of triangular numbers up to n."""
    for i in range(1, 5 + 1):
        print(i, (i * (i + 1)) // 2)
# Print the list outside the function
for i in print_triangular_numbers(5):
    print(print_triangular_numbers(n))
