def count_adapter_arrangements(adapters):
    """
    Count the number of distinct ways to arrange adapters.

    Args:
        adapters: List of adapter joltage ratings

    Returns:
        Number of distinct arrangements
    """
    # Add the charging outlet (0) and device (max + 3)
    adapters = [0] + sorted(adapters)
    device_joltage = adapters[-1] + 3
    adapters.append(device_joltage)

    # Dynamic programming: dp[i] = number of ways to reach adapter i
    dp = [0] * len(adapters)
    dp[0] = 1  # One way to reach the outlet (starting point)

    # For each adapter, count ways to reach it from previous adapters
    for i in range(1, len(adapters)):
        # Check all previous adapters within 3 jolts
        for j in range(i - 1, -1, -1):
            if adapters[i] - adapters[j] > 3:
                break
            dp[i] += dp[j]
            # if adapters[i] - adapters[j] <= 3:
            #     dp[i] += dp[j]
            # else:
            #     # If difference is > 3, earlier adapters won't work either
            #     break

    return dp[-1]


# Test with the first example
test_input_1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
result_1 = count_adapter_arrangements(test_input_1)
print(f"First example: {result_1} arrangements (expected: 8)")

# Test with the second example
test_input_2 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19,
                38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
result_2 = count_adapter_arrangements(test_input_2)
print(f"Second example: {result_2} arrangements (expected: 19208)")

# 3
test_input_3 = ([1,2])
result_3 = count_adapter_arrangements(test_input_3)
print(f"Third example: {result_3} arrangements (expected: x)")

# For your actual puzzle input, replace this with your data
puzzle_input = """
# Paste your puzzle input here, one number per line
""".strip().split('\n')

# Uncomment these lines when you have your puzzle input
# puzzle_adapters = [int(x) for x in puzzle_input if x]
# answer = count_adapter_arrangements(puzzle_adapters)
# print(f"\nPuzzle answer: {answer}")
