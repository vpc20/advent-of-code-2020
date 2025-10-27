from collections import Counter

from aoc_tools import read_input_to_sections



if __name__ == '__main__':
    # sections = read_input_to_sections('aoc_06_testdata1.txt')
    sections = read_input_to_sections('aoc_06_data1.txt')

    total_count = 0
    for section in sections:
        print(section)
        person_count = section.count('\n') + 1
        print(person_count)

        sect = section.replace('\n', '')
        print(sect)
        char_counts = Counter(sect)
        print(char_counts)

        everyone_count = len([k for k,v in char_counts.items() if v == person_count])
        total_count += everyone_count
        print()
    print(total_count)