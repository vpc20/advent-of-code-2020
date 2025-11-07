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


def find_contiguous_subarray(nums, target_sum):
    l, r, current_sum = 0, 0, 0

    while l <= r:
        if current_sum > target_sum:
            current_sum -= nums[l]
            l += 1
        else:
            current_sum += nums[r]
            r += 1
        if current_sum == target_sum:
            return nums[l: r]

    return None  # No such subarray found


if __name__ == '__main__':
    # nums = read_input_to_nums2('aoc_09_testdata1.txt')
    nums = read_input_to_nums2('aoc_09_data1.txt')
    print(nums)

    # for aoc_09_testdata1.txt
    # preamble_len = 5

    # for aoc_09_data1.txt
    preamble_len = 25

    start = 0
    end = preamble_len

    for num in nums[preamble_len:]:
        if not valid_num(num, nums[start:end]):
            print(num)
            break
        start += 1
        end += 1

    sub_arr = find_contiguous_subarray(nums, num)
    print(sub_arr)
    print(min(sub_arr) + max(sub_arr))
