def arithmetic_arranger(problems:list, check:bool = False):
    top = ""
    bottom = ""
    line = ""
    result = 0
    result_string = ""

    if len(problems) <= 5:
        for i in problems:
            operations = i.split()
            max_range = (max(len(operations[0]), len(operations[2]))) + 2

            if operations[0].isdigit() and operations[2].isdigit():
                if len(operations[0]) <= 4 and len(operations[2]) <= 4:
                    top += operations[0].rjust(max_range)
                    bottom += operations[1] + operations[2].rjust(max_range-1)
                    line += '-' * max_range
                    if operations[1] == "+":
                        result = str(int(operations[0]) + int(operations[2]))
                        result_string += result.rjust(max_range)
                    elif operations[1] == "-":
                        result = str(int(operations[0]) - int(operations[2]))
                        result_string += result.rjust(max_range)
                    else:
                        return "Error: Operator must be '+' or '-'."

                    if len(problems) > 1:
                        top += '    '
                        bottom += '    '
                        line += '    '
                        result_string += '    '

                    if check == True:
                        arranged_problems = top.rstrip() + "\n" + bottom.rstrip() + "\n" + line.rstrip() + "\n" + result_string.rstrip()
                    else:
                        arranged_problems = top.rstrip() + "\n" + bottom.rstrip() + "\n" + line.rstrip()
                else:
                    return "Error: Numbers cannot be more than four digits."
            else:
                return "Error: Numbers must only contain digits."
    else:
        return "Error: Too many problems."

    return arranged_problems
