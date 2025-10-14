import re

from aoc_tools import read_input_to_nums2

if __name__ == '__main__':
    # f = open('aoc_02_testdata1.txt')
    f = open('aoc_02_data1.txt')
    valid_password_count = 0
    for line in f:
        rule, password = line.strip().split(': ')
        occ, ch = rule.split()
        pos1, pos2 = [int(item) for item in re.findall(r'\d+', occ)]
        pos1 -= 1
        pos2 -= 1
        print(password, ch, pos1, pos2)
        if password[pos1] == ch and password[pos2] != ch or password[pos2] == ch and password[pos1] != ch:
            valid_password_count += 1
    f.close()
    print(valid_password_count)
