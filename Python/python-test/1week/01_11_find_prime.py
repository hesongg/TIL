input = 20


def find_prime_list_under_number(number):
    prime_list = []

    for n in range(2, number + 1):
        if check_prime(n):
            prime_list.append(n)

    return prime_list


def check_prime(number):
    if number == 2:
        return True

    remain = number % 2
    if remain == 0:
        return False

    medium = int(number / 2)
    for n in range(2, medium):
        if number % n == 0:
            return False

    return True


result = find_prime_list_under_number(input)
print(result)
