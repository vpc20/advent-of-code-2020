from aoc_tools import read_input_to_text_array


def compute_seat_id(text):
    lo = 0
    hi = 127
    left = 0
    right = 7

    for c in text:
        if c == 'F':
            hi = (lo + hi + 1) // 2
        elif c == 'B':
            lo = (lo + hi + 1) // 2
        elif c == 'L':
            right = (left + right + 1) // 2
        elif c == 'R':
            left = (left + right + 1) // 2

    print(lo, left)
    return lo * 8 + left  # seat id


if __name__ == '__main__':
    # text_array = read_input_to_text_array('aoc_05_testdata1.txt')
    text_array = read_input_to_text_array('aoc_05_data1.txt')

    max_seat_id = 0
    for text in text_array:
        print(text)
        seat_id = compute_seat_id(text)
        print(seat_id)
        max_seat_id = max(max_seat_id, seat_id)
    print(max_seat_id)
