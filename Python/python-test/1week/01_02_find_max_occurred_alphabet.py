def find_max_occurred_alphabet(string):
    count_array = [0] * 26
    for c in string:
        if c.isalpha():
            index = ord(c) - ord("a")
            count_array[index] = count_array[index] + 1

    max_index = 0
    max_count = 0
    for i, cnt in enumerate(count_array):
        if cnt > max_count:
            max_index = i
            max_count = cnt

    return chr(max_index + ord("a"));


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))