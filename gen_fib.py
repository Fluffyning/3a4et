def gen_fib(number):
    first_num = 0
    second_num = 1
    for index in range(number):
        yield first_num
        first_num, second_num = second_num, first_num + second_num

for current_num in gen_fib(11):
    print(current_num)
