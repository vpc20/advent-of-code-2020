from aoc_tools import read_input_to_sections

if __name__ == '__main__':
    # sections = read_input_to_sections('aoc_04_testdata1.txt')
    sections = read_input_to_sections('aoc_04_data1.txt')

    valid_ctr = 0
    for section in sections:
        fields_txt = section.replace('\n', ' ')
        key_set = {field[:3] for field in (fields_txt.split())}
        print(key_set)
        set_count = len(key_set)
        if set_count == 8 or (set_count == 7 and 'cid' not in key_set):
            valid_ctr += 1
    print(valid_ctr)
