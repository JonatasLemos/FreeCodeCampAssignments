def arithmetic_arranger(problems, solve=False):
    string = top = bottom = result = dashes = ""
    end = ["    "] * (len(problems) - 1)
    end.append("")
    right_operations = ["+", "-"]
    if len(problems) > 5:
        return "Error: Too many problems."

    for i in range(len(problems)):

        operands = problems[i].split(" ")
        if operands[0].isnumeric() == False or operands[2].isnumeric() == False:
            return "Error: Numbers must only contain digits."
        elif operands[1] not in right_operations:
            return "Error: Operator must be '+' or '-'."
        elif len(operands[0]) > 4 or len(operands[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_length = max(len(operands[0]), len(operands[2]))
        top += operands[0].rjust(max_length + 2) + end[i]
        bottom += operands[1] + " " + operands[2].rjust(max_length) + end[i]
        dashes += (max_length + 2) * "-" + end[i]
        result += str(eval(problems[i])).rjust(max_length + 2) + end[i]

    string += top + "\n" + bottom + "\n" + dashes
    if solve:
        string += "\n" + result

    return string
