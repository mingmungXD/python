# 동네에 치킨집
# 대기 손님 치킨 요리 시간을 줄이고자 자동 주문 시스템 제작
#
# 조건1 : 1보다 작거나 숫자가 아닌 값이 들어올 때는 ValueError
# 출력 메시지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 치킨량은 10마리로 한정
# 치킨 소진시 사용자 정의 에러[Soldouterror]를 발생시키고 프로그램 종료
# 출력메시지 : 재고가 소진되어 더이상 주문을 받지 않습니다:

class Soldouterror(Exception):
    pass

chicken = 10
waiting = 1
while True:
    try:
        print(f'[남은 치킨] : {chicken}')
        order = int(input("몇 마리 주문하실건가요? : "))
        if order < 1:
            raise ValueError
        elif order > chicken:
            print("재고가 부족합니다.")
        else:
            print(f'대기번호 {waiting}번, 치킨 {order}마리 주문 완료되었습니다.')
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise Soldouterror
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except Soldouterror:
        print("재고가 소진되어 더이상 주문을 받지 않습니다")
        break