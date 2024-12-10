age = 20
isAdult = age > 19

man = "M"
isMan = man == "M"


def checkAdultMan(m, a):
    return m and a


if checkAdultMan(isMan, isAdult):
    print("adult man")
else:
    print("false")

arr = [1, 2, 3]
for index, value in zip(range(5), arr):
    print(index, value)

arr = [1, 2, 3]
for index, value in enumerate(arr):
    print(index, value)