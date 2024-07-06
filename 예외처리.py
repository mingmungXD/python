try:
    print("나누기 전용 계산기")
    nums = []
    nums.append(int(input("첫번째 숫자")))
    nums.append(int(input("두번째 숫자")))
    # nums.append(int(nums[0]/nums[1]))
    print(f'{nums[0]} / {nums[1]} = {nums[2]}')

except ValueError:
    print("에러 발생")

except ZeroDivisionError as err:
    print(err)

except Exception as err:
    print("알 수 없는 에러 발생")
    print(err)


try:
    print("한 자리 숫자 나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자: "))
    num2 = int(input("두 번째 숫자: "))

    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print(f'{num1} / {num2} = {int(num1/num2)}')

except ValueError:
    print("한자리 숫자를 입력해주세요")

