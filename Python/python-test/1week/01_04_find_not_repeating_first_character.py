# "반복되는 알파벳" 에 대한 체크가 필요하면 아스키 코드를 기억하자

def find_not_repeating_first_character(string):
    answer = "_"

    alpha_arr = [0] * 26
    for char in string:
        char_index = ord(char) - ord("a")
        alpha_arr[char_index] = alpha_arr[char_index] + 1

    for char in string:
        char_index = ord(char) - ord("a")
        if alpha_arr[char_index] == 1:
            return char

    return answer


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))