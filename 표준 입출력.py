import sys
print("python", "java", sep=",", end="?")
print("무엇이 더 재밌을까요?")

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4),sep=":")

# 은행 대기순번표

for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))

# answer = input("아무값이나 입력하세요 : ")
# print(type(answer))
# # print("입력하신 값은 "+  answer + "입니다.")

print("{0: >10}".format(500))

print("{0: >+10}".format(-500))
print("{0: >+10}".format(500))
print("{0:_<10}".format(500))
print("{0:,}".format(1000000000))
print("{0:+,}".format(1000000000))
print("{0:+,}".format(-1000000000))
print("{0:^>+30,}".format(1000000000))
