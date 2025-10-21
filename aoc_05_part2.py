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

    # print(lo, left)
    return lo * 8 + left  # seat id


if __name__ == '__main__':
    # text_array = read_input_to_text_array('aoc_05_testdata1.txt')
    text_array = read_input_to_text_array('aoc_05_data1.txt')

    seat_ids = []
    for text in text_array:
        # print(text)
        seat_id = compute_seat_id(text)
        # print(seat_id)
        seat_ids.append(seat_id)

    # for e in sorted(seat_ids):
    #     print(e)

    sorted_seat_ids = sorted(seat_ids)
    # print(sorted_seat_ids)
    # for i, e in enumerate(sorted_seat_ids):
    #     if e != sorted_seat_ids[i - 1] + 1:
    #         print(e - 1)

    for i in range(1, len(sorted_seat_ids)):
        print(sorted_seat_ids[i])
        if sorted_seat_ids[i] != sorted_seat_ids[i - 1] + 1:
            print(sorted_seat_ids[i] - 1)
            break