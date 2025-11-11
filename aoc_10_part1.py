from aoc_tools import read_input_to_nums2

if __name__ == '__main__':
    # nums = sorted(read_input_to_nums2('aoc_10_testdata1.txt'))
    # nums = sorted(read_input_to_nums2('aoc_10_testdata2.txt'))
    nums = sorted(read_input_to_nums2('aoc_10_data1.txt'))
    print(nums)

    curr_jolt = 0
    ctr1 = 0
    ctr3 = 0
    nums.append(nums[-1] + 3)  # include the highest jolt rating

    for num in nums:
        if num - curr_jolt == 1:
            ctr1 += 1
        elif num - curr_jolt == 3:
            ctr3 += 1
        curr_jolt = num

    print(ctr1, ctr3)
    print(ctr1 * ctr3)
