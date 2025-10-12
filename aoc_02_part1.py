import re

from aoc_tools import read_input_to_nums2

if __name__ == '__main__':
    # f = open('aoc_02_testdata1.txt')
    f = open('aoc_02_data1.txt')
    valid_password_count = 0
    for line in f:
        rule, password = line.strip().split(': ')
        occ, ch = rule.split()
        str, end = [int(item) for item in re.findall(r'\d+', occ)]
        print(str, end, ch, password)
        if password.count(ch) in range(str, end + 1):
            valid_password_count += 1
    f.close()
    print(valid_password_count)
