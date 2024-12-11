def find_max_plus_or_multiply(array):
    answer = -1
    for num in array:
        if answer == -1:
            answer = num
            continue
        if answer == 0 or answer == 1 or num == 0 or num == 1:
            answer += num
        else:
            answer *= num
    return answer

# 개선
def find_max_plus_or_multiply_v2(array):
    plus_or_multiply_sum = 0
    for num in array:
        if plus_or_multiply_sum <= 1 or num <= 1:
            plus_or_multiply_sum += num
        else:
            plus_or_multiply_sum *= num
    return plus_or_multiply_sum


result = find_max_plus_or_multiply_v2
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))

def fun(value):
    print(value)

test = fun
test(123)