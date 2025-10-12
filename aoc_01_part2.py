from itertools import combinations

from aoc_tools import read_input_to_nums2

if __name__ == '__main__':
    # nums = read_input_to_nums2('aoc_01_testdata1.txt')
    nums = read_input_to_nums2('aoc_01_data1.txt')

    # comb1 = [item for item in combinations(nums, 2) if item[0] + item[1] < 2020]
    dict1 = {item[0] + item[1]: item for item in combinations(nums, 2) if item[0] + item[1] < 2020}
    # print(comb1)
    # print(len(comb1))
    print(dict1)
    print(len(dict1))

    for num in nums:
        # print(num)
        for k, v in dict1.items():
            if v[0] + v[1] + num == 2020:
                print(v[0] * v[1] * num)
                break
        else:
            continue
        break
