from random import *

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f'{self.name}유닛이 생성되었습니다.')

    def move(self, location):
        print("[지상 유닛 이동]")
        print(f'{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]')


class Attackunit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        print(f'체력 {self.hp}, 공격력 {self.damage}')

    def attack(self, location):
        print(f'{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]')

    def damaged(self, damage):
        print(f'{self.name} : {damage}데미지를 입었습니다.')
        self.hp -= damage
        print(f'{self.name} : 현재 체력은 {self.hp} 입니다.')
        if self.hp <= 0:
            print(f'{self.name} : 파괴되었습니다.')

class Flyable:
    def __init__(self, name, flyingspeed):
        self.name = name
        self.flyingspeed = flyingspeed

    def fly(self, location):
        print(f'{self.name} : {location} 방향으로 날아갑니다. 속도 : {self.flyingspeed}')

class flyableAttackUnit(Attackunit, Flyable):
    def __init__(self, name, hp, damage, flyingspeed):
        Attackunit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, name, flyingspeed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(location)

class Buildingunit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0)
        self.location = location

class Marine(Attackunit):
    def __init__(self):
        Attackunit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (hp 10 감소)".format(self.name))
        else:
            print(f'{self.name} : 체력이 부족하여 스팀팩을 사용하지 않습니다.')


class Tank(Attackunit):
    seize_developed = False

    def __init__(self):
        Attackunit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:
            print(f'{self.name} : 시즈모드로 전환합니다.')
            self.damage *= 2
            self.seize_mode = True
        else:
            print(f'{self.name} : 시즈모드를 해제합니다.')
            self.damage /= 2
            self.seize_mode = False

class Wraith(flyableAttackUnit):
    def __init__(self):
        flyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print(f'{self.name} : 클로킹 모드를 해제합니다..')
            self.clocked = False
        else:
            print(f'{self.name} : 클로킹 모드를 설정합니다..')
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("player : gg")

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for Unit in attack_units:
    Unit.move("1시")

Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

for Unit in attack_units:
    if isinstance(Unit,Marine):
        Unit.stimpack()
    elif isinstance(Unit, Tank):
        Unit.set_seize_mode()
    elif isinstance(Unit, Wraith):
        Unit.clocking()

for Unit in attack_units:
    Unit.attack("1시")

for Unit in attack_units:
    Unit.damaged(randint(5,21))

game_over()






        




