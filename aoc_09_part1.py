import sys

from aoc_tools import read_input_to_nums2


def valid_num(target_sum, nums):
    print(target_sum, nums)
    seen = {nums[0]}
    for num in nums[1:]:
        if target_sum - num in seen:
            return True
        else:
            seen.add(num)
    return False


if __name__ == '__main__':
    # nums = read_input_to_nums2('aoc_09_testdata1.txt')
    nums = read_input_to_nums2('aoc_09_data1.txt')
    print(nums)

    start = 0
    end = 25

    for num in nums[25:]:
        if not valid_num(num, nums[start:end]):
            print(num)
            break
        start += 1
        end += 1
