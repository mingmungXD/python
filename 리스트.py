# member = ["유재석", "정형돈", "박명수"]
#
# print(member.index("유재석"))
# member.append("하하")
# print(member)
# member.insert(1, "박명수")
# print(member)
# print(member.pop())
# member.append("유재석")
# print(member.count("유재석"))

num = [5, 2, 4, 3, 1]
num.sort()
print(num)

num.reverse()

# num.clear()

mix = ["조세호", 20, True]
print(mix)

num.extend(mix)
print(num)

# extend() 이 자체는 결과를 내는 것이 아니라 명령이다.
# 그래서 print(num.reverse())의 결과는 none이다.


cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet.get(3))
# print(cabinet[5]) << cabinet에 5라는 키가 없어서 오류가 남
print(cabinet.get(5)) #
print("hi")
print(3 in cabinet) # True

cabinet = {"a-3": "유재석"}
print(cabinet["a-3"])
cabinet["a-30"] = "조세호"
cabinet["a-3"] = "박명수"
print(cabinet)

del cabinet["a-3"]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())