input = 20

# 비효율적 -> n 보다 작은 모든 소수에 대해서만 나누어 떨어지는지 체크하면 된다.
# 소수가 아닌 수는 이미 소수의 곱으로 이루어져있기 때문이다.
def find_prime_list_under_number(number):
    prime_list = []

    # 2~20까지 찾는다
    for n in range(2, number + 1): # 2 ~ number 까지 숫자 범위 반복
        # 해당 숫자들의 소수인지 체크하여 list 에 넣는다.
        for i in range(2, n):   # 2부터 n - 1 까지 반복
            if n % i == 0:  # n = 2, 3, 4, ... 20
                break       # n = 2, i = 1 -> for 문을 못타니 else 를 탄다.
        else:               # n = 3, i = 2 -> 이것도 if 문을 만족하지 못하여 else 를 탄다.
                            # n = 4, i = 2, 3 -> 브레이크문 수행된다.
            prime_list.append(n)

    return prime_list

# 개선 - 자기보다 작은 소수로만 나누어 떨어지는지 확인
def find_prime_list_under_number_v2(number):
    prime_list = []

    for n in range(2, number + 1):
        for i in prime_list:
            if n % i == 0:
                break
        else:
            prime_list.append(n)
    return prime_list

# 개선 2 : N 의 제곱근보다 크지않은 어떤 소수로도 나누어 떨어지지않는다.
def find_prime_list_under_number_v3(number):
    prime_list = []

    for n in range(2, number + 1):
        for i in prime_list:
            if i * i <= n and n % i == 0:
                break
        else:
            prime_list.append(n)
    return prime_list


result = find_prime_list_under_number_v3(input)
print(result)
