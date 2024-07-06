def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance+money

def withdraw(balance, money):
    if balance >= money :
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

balance = 0

balance = deposit(balance,1000)

balance = withdraw(balance, 2000)

commission, balance = withdraw_night(balance,500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))

gun= 10
def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))


print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))



def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end="")
    for lang in language:
        print(lang, end="")
    print()

profile("유재석", 20, "python", "java", "c", "c++")
profile("김태호", 25, "kotlin", "swift")