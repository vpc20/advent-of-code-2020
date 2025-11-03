from collections import defaultdict

from aoc_tools import read_input_to_text_array


# def search_shiny_gold_bags(k):
#     for item in rule_dict[k]:
#         if item is None:
#             return False
#         elif item.startswith('shiny gold bag'):
#             return True
#         else:
#             if search_shiny_gold_bags(item):
#                 return True


def count_bags(key):
    bag_count = 0
    for k, v in rule_dict[key].items():
        print(k, v)
        if k in rule_dict:
            if k is None:
                return 0
            else:
                bag_count += v + (v * count_bags(k))
    return bag_count


if __name__ == '__main__':
    # rules = read_input_to_text_array('aoc_07_testdata1.txt')
    # rules = read_input_to_text_array('aoc_07_testdata2.txt')
    rules = read_input_to_text_array('aoc_07_data1.txt')

    rule_dict = defaultdict(dict)
    for rule in rules:
        print(rule)
        rule_key, rule_values = rule.split(' contain ')
        print(rule_key)
        print(rule_values)
        if rule_values.startswith('no'):
            rule_dict[rule_key] = {None: None}
        else:
            rule_vals = rule_values[:-1].split(', ')  # rule_values[:-1] used to remove the period at the end
            print(rule_vals)
            for rule_val in rule_vals:
                bag_count = int(rule_val[:1])
                print(bag_count)
                rule_val = rule_val[2:]  # remove the number
                if rule_val.endswith('bag'):
                    rule_val += 's'
                print(rule_val)
                rule_dict[rule_key][rule_val] = bag_count

    print('----------- rule dict ----------------------')
    for k, v in rule_dict.items():
        print(k, v)

    print('------------- count bags -----------------')
    print(count_bags('shiny gold bags'))
