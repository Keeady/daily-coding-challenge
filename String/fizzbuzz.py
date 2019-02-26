def print_fizz_buzz(low_range, high_range):
    output = []
    for i in range(low_range, high_range):
        is_div_by_three = i % 3 == 0
        is_div_by_five = i % 5 == 0
        if is_div_by_three and is_div_by_five:
            output.append('fizzbuzz')
        elif is_div_by_three:
            output.append('fizz')
        elif is_div_by_five:
            output.append('buzz')
        else:
            output.append(i)

    return output

def print_fizz_buzz_no_module(low_range, high_range):
    output = []

    for i in range(low_range, high_range):
        num = i // 3
        num2 = i // 5
        is_div_by_three = num * 3 == i
        is_div_by_five = num2 * 5 == i
        if is_div_by_three and is_div_by_five:
            output.append('fizzbuzz')
        elif is_div_by_three:
            output.append('fizz')
        elif is_div_by_five:
            output.append('buzz')
        else:
            output.append(i)

    return output