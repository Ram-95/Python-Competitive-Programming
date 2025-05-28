"""
This is an Activity Selection problem where we want to find the maximum number of non-overlapping presentations that can be attended.
Use Greedy approach to solve this problem.
    - Sort the timings in the increasing order of their end times.
    - Iterate through the sorted list and select presentations that start after or at the end of the last selected presentation.
    - Count the number of such presentations.
    - Return the count as the result.
"""

def get_max_presentations(start_times, end_times):
    """
    Calculates the maximum number of non-overlapping presentations that can be attended.

    Args:
        start_times (list of int): List of start times for each presentation.
        end_times (list of int): List of end times for each presentation.

    Returns:
        int: The maximum number of non-overlapping presentations.
    """
    # Sort the presentations by their end times (greedy approach)
    intervals = sorted(zip(start_times, end_times), key=lambda x: x[1])
    count = 0
    prev_end = 0

    # Iterate through each presentation
    for start, end in intervals:
        # If the current presentation starts after or at the end of the last selected one
        if prev_end <= start:
            count += 1
            prev_end = end  # Update the end time to the current presentation's end

    return count

# Example usage
start = [1, 1, 2, 3]
end = [2, 3, 3, 4]
print(get_max_presentations(start, end))