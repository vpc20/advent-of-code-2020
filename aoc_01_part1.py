from aoc_tools import read_input_to_nums2

if __name__ == '__main__':
    # nums = read_input_to_nums2('aoc_01_testdata1.txt')
    nums = read_input_to_nums2('aoc_01_data1.txt')

    set1 = set()
    for num in nums:
        print(num)
        x = 2020 - num
        if x in set1:
            break
        else:
            set1.add(num)
    print(x * num)
