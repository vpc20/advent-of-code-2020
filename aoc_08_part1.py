from aoc_tools import read_input_to_text_array

if __name__ == '__main__':
    # instructions = read_input_to_text_array('aoc_08_testdata1.txt')
    instructions = read_input_to_text_array('aoc_08_data1.txt')

    for instruction in instructions:
        # print(instruction)
        operation, argument = instruction.split()
        argument = int(argument)
        print(operation, argument)

    i = 0
    iset = set()
    accum = 0

    while i not in iset:  # check for infinite loop
        oper, arg = instructions[i].split()
        arg = int(arg)
        iset.add(i)

        if oper == 'nop':
            i += 1
        elif oper == 'acc':
            accum += arg
            i += 1
        elif oper == 'jmp':
            i += arg

    print(accum)

    # i = 0
    # iset = {i}
    # accum = 0
    #
    # while True:
    #     oper, arg = instructions[i].split()
    #     arg = int(arg)
    #
    #     if oper == 'nop':
    #         i += 1
    #     elif oper == 'acc':
    #         accum += arg
    #         i += 1
    #     elif oper == 'jmp':
    #         i += arg
    #
    #     if i in iset:  # infinite loop if instruction repeats
    #         break
    #     else:
    #         iset.add(i)
    #
    # print(accum)
