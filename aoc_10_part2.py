from functools import lru_cache

from aoc_tools import read_input_to_nums2

@lru_cache(maxsize=None)
def count_paths(nums):
    count = 0
    if len(nums) == 1:
        return 1

    if len(nums) >= 2 and nums[-1] - nums[-2] <= 3:
        count += count_paths(nums[:-1])
    if len(nums) >= 3 and nums[-1] - nums[-3] <= 3:
        count += count_paths(nums[:-2])
    if len(nums) >= 4 and nums[-1] - nums[-4] <= 3:
        count += count_paths(nums[:-3])
    return count


if __name__ == '__main__':
    # nums = sorted(read_input_to_nums2('aoc_10_testdata1.txt'))
    # nums = sorted(read_input_to_nums2('aoc_10_testdata2.txt'))
    # nums = sorted(read_input_to_nums2('aoc_10_testdata3.txt'))
    nums = sorted(read_input_to_nums2('aoc_10_data1.txt'))

    nums = [0] + nums + [nums[-1] + 3]
    print(count_paths(tuple(nums)))

# 1973822685184
