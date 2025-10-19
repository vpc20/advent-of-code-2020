import re

from aoc_tools import read_input_to_sections

if __name__ == '__main__':
    # sections = read_input_to_sections('aoc_04_testdata1.txt')
    sections = read_input_to_sections('aoc_04_data1.txt')

    valid_ctr = 0
    for section in sections:
        fields_txt = section.replace('\n', ' ')
        print(fields_txt)
        key_set = {field[:3] for field in (fields_txt.split())}
        # print(key_set)
        passport_dict = {field[:3]: field[4:].strip() for field in (fields_txt.split())}
        print(passport_dict)
        dict_count = len(passport_dict)
        if dict_count == 8 or (dict_count == 7 and 'cid' not in key_set):
            if ((1920 <= int(passport_dict['byr']) <= 2002 and
                 2010 <= int(passport_dict['iyr']) <= 2020 <= int(passport_dict['eyr']) <= 2030) and
                    passport_dict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and
                    len(passport_dict['pid']) == 9 and
                    passport_dict['pid'].isdigit() and
                    re.fullmatch(r"^#[0-9a-fA-F]{6}$", passport_dict['hcl']) is not None):
                if passport_dict['hgt'][-2:] == 'cm':
                    if 150 <= int(passport_dict['hgt'][:-2]) <= 193:
                        valid_ctr += 1
                elif passport_dict['hgt'][-2:] == 'in':
                    if 59 <= int(passport_dict['hgt'][:-2]) <= 76:
                        valid_ctr += 1
    print(valid_ctr)

