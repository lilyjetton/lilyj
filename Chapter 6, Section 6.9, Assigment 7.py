# Name:        Section 6.9 Question 7
# Purpose:
#
# Author:      Lilyj
#
# Created:     02/08/2025
# Copyright:   (c) Lilyj 2025
# Licence:     <your licence>



def to_secs(hours, minutes, seconds):
    """
    Converts hours, minutes, and seconds into a total number of seconds.

    Parameters:
        hours (int): Number of hours (non-negative).
        minutes (int): Number of minutes (non-negative, less than 60).
        seconds (int): Number of seconds (non-negative, less than 60).

    Returns:
        int: Total number of seconds.
    """
    # Input validation
    if not (isinstance(hours, int) and isinstance(minutes, int) and isinstance(seconds, int)):
        raise ValueError("All inputs must be integers.")
    if hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError("Hours, minutes, and seconds must be non-negative.")
    if minutes >= 60 or seconds >= 60:
        raise ValueError("Minutes and seconds must be less than 60.")

    # Calculate total seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

# Example usage
if __name__ == "__main__":
    # Test cases
    test_cases = [
        {"hours": 2, "minutes": 30, "seconds": 10, "expected": 9010},  # Standard case
        {"hours": 0, "minutes": 45, "seconds": 15, "expected": 2715},  # No hours
        {"hours": 1, "minutes": 0, "seconds": 0, "expected": 3600},    # Only hours
        {"hours": 0, "minutes": 0, "seconds": 0, "expected": 0},       # All zero
        {"hours": 0, "minutes": 59, "seconds": 59, "expected": 3599},  # Edge case
    ]

    try:
        # Test the function with mock data
        for case in test_cases:
            result = to_secs(case["hours"], case["minutes"], case["seconds"])
            print(f"Input: {case} -> Output: {result} (Expected: {case['expected']})")
            assert result == case["expected"], f"Test failed for input: {case}"
        print("All tests passed!")
    except ValueError as e:
        print(f"Error: {e}")
    except AssertionError as e:
        print(f"Assertion Error: {e}")
