# 자료형
from Tools.scripts.var_access_benchmark import A

print(5)
print(-10)
print(3.14)
print(1000)
print(5 + 3)
print(2 * 8)
print(3 * (3 + 1))

print("================================")

# 문자형
print('풍선')
print('나비')
print("ㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ" * 9)

print("================================")

# 참/거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))  # 이 답은 거짓인데 not이 들어가 반대인 false가 나온다

print("================================")

# 변수
# 애완동물 소개
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

# 플러스 말고도 , 로 써도 상관이 없다. 대신 빈 칸이 생긴다.
print("우리집 " + animal + "의 이름은 " + name + "예요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

print("================================")

# 주석
''' 이렇게 하면 
    여러 문장이 
    주석처리 됩니다.'''
# 여러문장 편하게 주석으로 바꾸기 (전체 선택 + 컨트롤 + 슬러쉬)

# ================================

# 연산자
print(1 + 1)  # 2
print(3 - 2)  # 1
print(5 * 2)  # 10
print(6 / 3)  # 2

print(2 ** 3)  # 2^3 = 8
print(5 % 3)  # 나머지 2
print(10 % 3)  # 1
print(5 // 3)  # 1
print(10 // 3)  # 3

print(10 > 3)  # T
print(4 >= 7)  # F
print(10 < 3)  # F
print(5 <= 5)  # T

print(3 == 3)  # T
print(4 == 2)  # F
print(3 + 4 == 7)  # T

print(1 != 3)  # T
print(not (1 != 3))  # F

print((3 > 0) and (3 < 5))  # T
print((3 > 0) & (3 < 5))  # T

print((3 > 0) or (3 < 5))  # T
print((3 > 0) | (3 < 5))  # T

print(5 > 4 > 3)  # T
print(5 > 4 > 7)  # F

print("================================")

# 간단한 수식
print(2 + 3 * 4)  # 14
print((2 + 3) * 4)  # 20
number = 2 + 3 * 4  # 14
print(number)
number = number + 2  # 16
print(number)
number += 2  # 18
print(number)
number *= 2  # 36
print(number)
number /= 2  # 18
print(number)
number -= 2  # 16
print(number)

number %= 5  # 0
print(number)

print("================================")

# 숫자 처리 함수
print(abs(-5))  # 5
print(pow(4, 2))  # 4^2 = 4*4 = 16
print(max(5, 12))  # 12
print(min(5, 12))  # 5
print(round(3.14))  # 3
print(round(4.99))  # 5

from math import *

print(floor(4.99))  # 내림. 4
print(ceil(3.14))  # 올림. 4
print(sqrt(16))  # 제곱근. 4

print("================================")

# 랜덤 함수
from random import *

print(random())  # 말 글대로 랜덤(0.0 ~ 1.0 미만의 임의의 값 생성)
print(random() * 10)  # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))  # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10))  # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10))  # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1)  # 1 ~ 10 이하의 임의의 값 생성
print(randrange(1, 10))  # 1 ~ 10 미만의 임의의 값 생성
print(randint(1, 10))  # 1 ~ 10 이하의 임의의 값 생성

print("================================")

# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = '파이썬은 쉬워요'
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

print("================================")

# 슬라이싱
jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])  # 0부터 2 직전까지 (0, 1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])  # 처음부터 6직전까지
print("뒤 7자리 : " + jumin[7:])  # 7부터 끝까지
print("뒤 7자리(뒤에 부터) : " + jumin[-7:])  # 맨 뒤에서 7번째부터 끝까지

print("================================")

# 문자열 처리함수
python = "Python is Amazing"
print(python.lower())  # 소문자로 반환
print(python.upper())  # 대문자로 반환
print(python[0].isupper())  # [n]의 값이 대문자인지 확인
print(len(python))  # 길이 반환
print(python.replace("Python", "Java"))  # 특정 문자를 찾아 바꾸고 싶은 문자로 반환

index = python.index("n")  # 문자 위치
print(index)
index = python.index("n", index + 1)  # 그 다음 n의 위치를 알려줌
print(index)

print(python.find("n"))  # 원하는 값이 없을 때 -1을 내보내고 프로그램은 계속 진행됨
print(python.index("n"))  # 원하는 값이 없을 때 오류를 내버림
print("hi")

print(python.count("n"))  # n이 몇 번 등장하는지 알려줌

print("================================")

# 문자열 포멧

# 방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")

print("나는 %s색과 %s색을 좋아해요." % ("분홍", "노란"))

# 방법 2
print("나는 {}살입니다.".format((20)))
print("나는 {}색과 {}색을 좋아해요.".format("분홍", "노란"))
print("나는 {0}색과 {1}색을 좋아해요.".format("분홍", "노란"))
print("나는 {1}색과 {0}색을 좋아해요.".format("분홍", "노란"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="노란"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="노란", age=20))

# 방법 4 (v3.6 이상)
age = 20
color = "노란"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

print("================================")

# 탈출문자
print("백문이 불여일견 \n 백견이 불여일타")

print("저는 '나도 코딩'입니다.")
print('저는 "나도 코딩"입니다.')
print("저는 \"나도코딩\"입니다.")  # \", \' 문장내에서 따옴표 사용 가능

# \\ 문장 내에서 \ 사용 가능
print("\\fdfd\\dfdf\\")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

print("================================")

# 리스트[]

# 지하철 칸별로 10, 20, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway1)

subway1 = ["유재석", "조세호", "박명수"]
print(subway)

print("================================")

# #리스트 []
#
# # 지하철 칸별로 10, 20, 30명
# # subway1 = 10
# # subway2 = 20
# # subway3 = 30
#
# subway = [10, 20, 30]
# print(subway)
#
# subway = ["유재석", "조세호", "박명수"]
# print(subway)
#
# #조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))
#
# #하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")
# print(subway)
#
# #정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1, "정형돈")
# print(subway)
#
# #지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)
#
# # print(subway.pop())
# # print(subway)
# #
# # print(subway.pop())
# # print(subway)
#
# #같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
mix_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]
# print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

print("====================================")

# 사전
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet[5])
print(cabinet.get(5))
print(cabinet.get(5, "사용 가능"))
print("hi")

# print(3 in cabinet) #T
# print(5 in cabinet) #F
# cabinet{"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"  # 업데이트
cabinet["C-20"] = "조세호"  # 추가
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)

print("====================")

# 튜플
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

print("======================")

# 세트 = 집합(중복이 안돼고 순서가 없음)
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (자바와 파이썬을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (자바도 할 수 있거나 파이썬도 할 수 있는 개발자
print(java | python)
print(java.union(python))

# 차집합 (자바는 할 수 있지만 파이썬은 못하는 개발자
print(java - python)
print(java.difference(python))

# 파이썬을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# 자바를 잊었어요
java.remove("김태호")
print(java)

print("=========================")

# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

print("=========================")

# if
# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or weather =="눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

temp = int(input("기온은 어때요"))
if 30 <= temp:
    print("temp: int . 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")

print("=========================")

# for
for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다".format(customer))

print("=========================")

# while
customer = "토르"
person = "Unknown"
while person != customer:
    print("{0}, 커피가 준비 되었습니다".format(customer))
    person = input("이름이 어떻게 되세요? ")

print("=========================")

# continue 와 break
students = [1, 2, 3, 4, 5]
print(students)
students = [i + 100 for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

print("=========================")


# 합수
def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balance, money):  # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원 입니다".format(balance + money))
    return balance + money


def withdraw(balance, money):  # 출금
    if balance >= money:
        print("출금이 완료 되었습니다. 잔액은 {0}원 입니다".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance


def withdraw_night(balance, money):  # 저녁에 출금
    commission = 100  # 수수료 100원
    return commission, balance - money - commission


balance = 0  # 잔액
balance = deposit(balance, 1000)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원 입니다.".format(commission, balance))

print("=========================")


# 기본값
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))


profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")


def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))


profile("유재석")
profile("김태호")

print("=========================")


# 키워드 값
def profile(name, age, main_lang):
    print(name, age, main_lang)


profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")

print("=========================")


# 가변인자
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)


def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile("유재석", 20, "파이썬", "자바", "C", "C++", "C#")
profile("김태호", 25, "코틴", "스와프")

print("=========================")

# 지역변수와 전역변수
gun = 10
gun: int


def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 중 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

print("=========================")

# 클래스
# class Unit:
#     def __init__(self, name, hp, damage):  #self 빼고 동일한 갯수 만큼 값을 던져줘야함
#         self.name = name  #맴버변수
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 : {0}, 공격력 : {1}".format(self.hp, self.damage))
#
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱커", 150, 35)
#
# print("=========================")
#
# #멤버변수
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
#
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True  # 변수를 이렇게 새로 추가(확장)하는 것도 가능
#                          # 하지만 기존에 있는 다른 객체에는 적용X(그 객체에서만 사용 가능)
#
# if wraith2.clocking == True:
#     print("{0}은 현재 클로킹 상태 입니다.".format(wraith2.name))

print("=========================")

# 상속
# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name  # 맴버변수
        self.hp = hp


# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)

print("=========================")

# 다중상속
class Flyble:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyble):  #다중 상속 할 땐 컴마사용
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyble.__init__(self, flying_speed)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

print("=========================")

# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name  # 맴버변수
#         self.hp = hp
#         self.speed = speed
#
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#               .format(self.name, location, self.speed))
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#               .format(self.name, location, self.damage))
#
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))
#
# class Flyble:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

#메서드 오버라이딩
class FlyableAttackUnit(AttackUnit, Flyble):  #다중 상속 할 땐 컴마사용
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyble.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

vulture = AttackUnit("벌쳐", 80, 10, 20)

battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("5시")

print("=========================")

#pass
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()

print("=========================")

#super
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location

        #super를 사용하면 맨 처음에 상속 받는 클래스에 대해서만 임의 함수가 호출됨
        #다 초기화하고 싶으면 따로 명시적으로

print("=========================")

#게임 완성

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name  # 맴버변수
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
              .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
              .format(self.name, location, self.damage))


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True

        if self.seize_mode == False:
            print("{0} : 시즈모드를 해제제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

#나는 기능
class Flyble:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyble):  #다중 상속 할 땐 컴마사용
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyble.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocked(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("플레이어 : gg")
    print("플레이어 님이 게임에서 퇴장하셨습니다.")

print("=========================")

#퀴즈 8
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.completion_year = completion_year
        self.price = price
        self.deal_type = deal_type
        self.house_type = house_type
        self.location = location

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "아빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()