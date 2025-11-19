from functools import lru_cache

from aoc_tools import read_input_to_nums2


@lru_cache(maxsize=None)
def count_paths(nums, idx):
    count = 0
    if idx == 0:
        return 1

    if idx >= 1 and nums[idx] - nums[idx - 1] <= 3:
        count += count_paths(nums, idx - 1)
    if idx >= 2 and nums[idx] - nums[idx - 2] <= 3:
        count += count_paths(nums, idx - 2)
    if idx >= 3 and nums[idx] - nums[idx - 3] <= 3:
        count += count_paths(nums, idx - 3)
    return count


if __name__ == '__main__':
    # nums = sorted(read_input_to_nums2('aoc_10_testdata1.txt'))
    # nums = sorted(read_input_to_nums2('aoc_10_testdata2.txt'))
    # nums = sorted(read_input_to_nums2('aoc_10_testdata3.txt'))
    nums = sorted(read_input_to_nums2('aoc_10_data1.txt'))

    nums = [0] + nums + [nums[-1] + 3]
    print(count_paths(tuple(nums), len(nums) - 1))

# 1973822685184
