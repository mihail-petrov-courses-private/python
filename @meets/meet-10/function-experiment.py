# направете функция която пита потребителя за неговото
# първо и второ име 
# и ги връща. 
# > full_name = get_customer_fullname()
def get_customer_fullname():

    firsrt_name = input("първо име")
    last_name   = input("второ име")
    full_name   =  f"{firsrt_name} {last_name}"
    return full_name

# Направете функция която получава две числа 
# и операцията между тях и връща резултата
# подават като аргументи на функция
# '*', '/', '+', '-'
# operation = process_numbers(1, 5, '+')
# print(operation) 6
# operation = process_numbers(1, 5, '*')
# print(operation) 5
# operation = process_numbers(1, 5, '/')
# print(operation) 0.2
# operation = process_numbers(1, 5, '-')
# print(operation) -4
def process_numbers(operand_a, operand_b, operation):

    if operation == "+":
        return operand_a + operand_b
    


def print_5_time(repeat):

    time = 0;
    while time < repeat:
        print(" Time " + str(time + 1))
        time += 1

print_5_time(10)