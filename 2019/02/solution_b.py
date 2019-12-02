from aoc import AOC


def get_solution(inp: str):
    inp_list = [int(item) for item in inp.split(',')]

    # change the values according to the task
    inp_list[1] = 84
    inp_list[2] = 44

    # slice input into list of commands
    command_list = [inp_list[i:i+4] for i in range(0, len(inp_list), 4)]
    print(command_list)

    add = None
    for command in command_list:

        # first command - OP code
        op_code = command[0]
        if op_code == 99:
            print(first_num)
            print(second_num)
            break
        elif op_code == 1:
            add = True
        elif op_code == 2:
            add = False

        # second and third command - values based on indexes given by the commands are either added or multiplied
        first_num = inp_list[command[1]]
        second_num = inp_list[command[2]]

        if add:
            command_result = first_num + second_num
        else:
            command_result = first_num * second_num

        # fourth command - memory location in which to save the result
        inp_list[command[3]] = command_result

    return inp_list


aoc_data = AOC.get_data(2)
solution = get_solution(aoc_data)

result = 100 * solution[1] + solution[2]
AOC.submit(data=result, part='b', day=2)
