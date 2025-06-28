def count_dgt(number):
    number_str = str(number)
    digit_count = {}
    for current_digit in number_str:
        if current_digit in digit_count:
            digit_count[current_digit] += 1
        else:
            digit_count[current_digit] = 1

    return digit_count

number = 12342341232131
print(count_dgt(number))
