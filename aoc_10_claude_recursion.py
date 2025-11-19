from functools import lru_cache


def count_adapter_arrangements(adapters):
    """
    Count the number of distinct ways to arrange adapters using recursion.

    Args:
        adapters: List of adapter joltage ratings

    Returns:
        Number of distinct arrangements
    """
    # Add the charging outlet (0) and device (max + 3)
    adapters = [0] + sorted(adapters)
    device_joltage = adapters[-1] + 3
    adapters.append(device_joltage)

    @lru_cache(maxsize=None)
    def count_paths(index):
        """
        Recursively count the number of paths from current index to the end.

        Args:
            index: Current position in the adapters list

        Returns:
            Number of paths from this index to the device
        """
        # Base case: reached the device
        if index == len(adapters) - 1:
            return 1

        # Count paths by trying all valid next adapters
        total_paths = 0
        for next_idx in range(index + 1, len(adapters)):
            # Check if the jump is valid (within 3 jolts)
            if adapters[next_idx] - adapters[index] <= 3:
                total_paths += count_paths(next_idx)
            else:
                # No point checking further adapters
                break

        return total_paths

    # Start from the outlet (index 0)
    return count_paths(0)


# Test with the first example
test_input_1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
result_1 = count_adapter_arrangements(test_input_1)
print(f"First example: {result_1} arrangements (expected: 8)")

# Test with the second example
test_input_2 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19,
                38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
result_2 = count_adapter_arrangements(test_input_2)
print(f"Second example: {result_2} arrangements (expected: 19208)")

# For your actual puzzle input, replace this with your data
puzzle_input = """
# Paste your puzzle input here, one number per line
""".strip().split('\n')

# Uncomment these lines when you have your puzzle input
# puzzle_adapters = [int(x) for x in puzzle_input if x]
# answer = count_adapter_arrangements(puzzle_adapters)
# print(f"\nPuzzle answer: {answer}")