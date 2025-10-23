from aoc_tools import read_input_to_sections



if __name__ == '__main__':
    # sections = read_input_to_sections('aoc_06_testdata1.txt')
    sections = read_input_to_sections('aoc_06_data1.txt')

    yes_count = 0
    for section in sections:
        print(section)
        sect = section.replace('\n', '')
        yes_set = set(sect)
        yes_count += len(yes_set)
        print()
    print(yes_count)