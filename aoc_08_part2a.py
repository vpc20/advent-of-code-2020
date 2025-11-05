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
    iset1 = set()
    accum = 0

    while i not in iset1:  # check for infinite loop
        oper, arg = instructions[i].split()
        arg = int(arg)
        iset1.add(i)

        if oper == 'nop':
            i += 1
        elif oper == 'acc':
            accum += arg
            i += 1
        elif oper == 'jmp':
            i += arg

    print(accum)

    exit_prog = False

    for set_idx in iset1:
        # change the nop or jmp instruction
        if instructions[set_idx].startswith('nop'):
            instructions[set_idx] = instructions[set_idx].replace('nop', 'jmp')
        else:
            instructions[set_idx] = instructions[set_idx].replace('jmp', 'nop')

        i = 0
        iset2 = set()
        accum = 0

        while -1 < i < len(instructions) and i not in iset2:  # check if instruction index is out of bounds
            oper, arg = instructions[i].split()
            arg = int(arg)
            iset2.add(i)

            if oper == 'nop':
                i += 1
            elif oper == 'acc':
                accum += arg
                i += 1
            elif oper == 'jmp':
                i += arg

        if i > len(instructions) - 1:
            break

        # change the back to original instruction
        if instructions[set_idx].startswith('nop'):
            instructions[set_idx] = instructions[set_idx].replace('nop', 'jmp')
        else:
            instructions[set_idx] = instructions[set_idx].replace('jmp', 'nop')

    print(accum)
