# 표준 체중을 구하는 프로그램을 작성하시오
#
# 표준체중 = 개인의 키에 적당한 체중
#
# 공식
# 남자 : 키 * 키 * 22
# 여자 : 키 * 키 * 21
#
# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
# 함수명 : std_weight
# 전달값 : height, gender
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시
#
# ex) 키 175cm 남자의 표준 체중은 67.38입니다.

height = int(input("키(cm)를 입력해주세요: "))
gender = input("성별을 입력해주세요: ")
def std_weight(height, gender):
    if gender == "남자":
        return height**2 * 22/10000
    else:
        return height**2 * 21/10000


weight = std_weight(height, gender)
print(f'키 {height}cm {gender}의 표준 체중은 {weight:.2f} 입니다.')