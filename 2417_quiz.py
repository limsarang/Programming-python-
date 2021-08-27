# Quiz 1)

station = "사당"  # , "신도림", "인천공항"

print(station + "행 열차가 들어오고 있습니다.")

print("--------------------------")

# Quiz 2)

from random import *

day = (randint(4, 28))
print("오프라인 스터디 모임 날짜는 매월 " + str(day) + "일로 선정되었습니다.")

print("--------------------------")

# Quiz 3)

url = "http://naver.com"
my_pw = url.replace("http://", "")
my_pw = my_pw[:my_pw.index(".")]
password = my_pw[:3] + str(len(my_pw)) + str(my_pw.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))

print("--------------------------")

# Quiz 4)
from random import *

users = range(1, 21)
users = list(users)

print(users)
shuffle(users)
print(users)

winners = sample(users, 4)

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 -- ")

print("--------------------------")

# Quiz 5)
from random import *

cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print("총 탑승 승객 : {0} 분".format(cnt))

print("--------------------------")

# Quiz 5)
from random import *

cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번쨰 손님 (소요시간 : {1}분)".format(i, time))

print("총 찹승객 수 : {0} 분".format(cnt))

print("==========선생님 퀴즈==========")

id_number = "020316"

print("출생년도 끝 두자리 : " + id_number[:2] + "\n")
print("출생 월일 : " + id_number[2:] + "\n")
print("그 두 개의 합 " + (id_number[:2] + id_number[2:]))

print("--------------------------")

id_number = "020316"
print("출생 년도 끝 두자리: " + id_number[:2] + "\n")
print("출생 월일: " + id_number[2:] + "\n")
print("두 개 합 : {0}".format(int(id_number[:2]) + int(id_number[2:])))

phone_number = "023-1234-5678"
print("지역 번호 : " + phone_number[:phone_number.index("-")] + "\n맨 끝 네 자리 : " + phone_number[-4:])

print("--------------------------")

student_number = 2417
Number = student_number[1]
Number = int(Number)
majors = ['0', '뉴소과', '뉴소과', '뉴웹과', '뉴웹과', '뉴디과', '뉴디과']
if 1 <= Number and Number <= 6:
    print(f"{Number}반 {majors[Number - 1]}")  # -1인 이유 : 1->0 2->1
else:
    print('잘못 입력하셨습니다')

print("--------------------------")


def get_major(student_number):
    majors = ['소', '소', '솔', '솔', '디', '디']
    grade = student_number[0]
    classroom = int(student_number[1])
    return grade, majors[classroom - 1]


grade, major = get_major('2100')  # 빨간 줄 나올 때 (ALT + ENTER) 누르면 도움줌
print(major, grade)  # 뉴미디어소프트웨어과 2

print("--------------------------")


# 1
def average1(*numbers):
    count = 0
    sum_value = 0
    for number in numbers:
        sum_value += numbers
        count += 1
    return sum_value / count


# 2
def average2(*number):
    return sum(number) / len(number)


print("--------------------------")


def get_bmi(height, weight):
    height /= 100
    bmi = weight / height ** 2  # 제곱 연산자 ** 그냥 곱 *
    return round(bmi, 1)


bmi = get_bmi(176, 69)
print(bmi)  # 22.3

print("--------------------------")


def get_bmi(height, weight):
    height /= 100
    bmi = weight / height

    if bmi < 18.5:
        print('저체중')
    elif bmi < 23:
        print('정상')
    elif bmi < 25.00:
        print('과체중')
    else:
        print('비만')

    return


bmi = get_bmi(176, 69)

print("--------------------------")


# Quiz3-1. n_sum() 함수를 만든다.
# 함수의 인수(argument)로 10자리 숫자보다 작은 숫자를 넣으면,
# 각 자리의 숫자의 합계를 리턴한다. 10자리 이상이면 -1 리턴한다.

def n_sum(argument):
    new = str(argument)
    add = 0
    for i in range(len(new)):
        if len(new) < 10:
            add += int(new[i])
        elif len(new) >= 10:
            return -1
    return add


result = n_sum(10)
print(result)  # 1
result = n_sum(331)
print(result)  # 7
result = n_sum(408)
print(result)  # 12
result = n_sum(1000000000)
print(result)  # -1
print("--------------------------")

# Quiz3-2. get_subway_fare() 함수를 만든다.
# 이 함수는 인수로 가는 거리(km)를 숫자로 넣으면, 요금을 리턴한다.
# * 지하철 요금계산법 10km 이내: 720원(청소년),
# 10~50km: 5km마다 100원, 50km 초과 시 8km마다 100원

import math


def get_subway_fare(km):
    money = 720
    if km > 10 and km <= 50:
        money += math.ceil((km - 10) / 5) * 100  # math.ceil은 반올림(남는 km가 있는 것을 대비)
    elif km > 50:
        money += 800  # 기본적으로 50km 갔을 때 800원임
        money += math.ceil((km - 50) / 8) * 100

    return money


fare = get_subway_fare(5)
print(fare)  # 720
fare = get_subway_fare(26)
print(fare)  # 1120
fare = get_subway_fare(61)
print(fare)  # 1720

print("--------------------------")


# Quiz3-3. get_three_six_nine() 함수를 만든다.
# 이 함수에 숫자를 입력하면 369 게임에  해당하는 답변을 리턴한다.
# * 369게임: 숫자의 어느 자리든 3 또는 6 또는 9가 있다면 그 갯수만큼 '짝'을 외치고,
# 아니면 그냥 숫자를 외친다.
# 힌트: 문자열 함수 중에 특정 글자를 세는 함수가 있음

def get_three_six_nine(n):
    number = str(n)
    data = list(number)
    count_3 = n.count('3')
    count_6 = n.count('6')
    count_9 = n.count('9')

    for date in number:
        if "3" in date or "6" in data or "9" in data:
            return (count_3 + count_6 + count_9) * "짝"
        return n


result = get_three_six_nine(1)
print(result)  # 1
result = get_three_six_nine(3)
print(result)  # 짝
result = get_three_six_nine(16)
print(result)  # 짝
result = get_three_six_nine(36)
print(result)  # 짝짝

# def get_three_six_nine(n):
#     number = str(n)
#     data = list(number)
#     count_3 = n.count('3')
#     count_6 = n.count('6')
#     count_9 = n.count('9')
#
#     for date in number:
#         if "3" in date or "6" in data or "9" in data:
#             return (count_3 + count_6 + count_9) * "짝"
#         return n
#
#
# result = get_three_six_nine(1)
# print(result)  # 1
# result = get_three_six_nine(3)
# print(result)  # 짝
# result = get_three_six_nine(16)
# print(result)  # 짝
# result = get_three_six_nine(36)
# print(result)  # 짝짝

print("--------------------------")


# Quiz3-4.팩토리얼을 구하는 함수
# 함수 이름은 factorial 인수 k에 정수를 넣고(인수 1개)
# 그 인수의 팩토리얼을 구하고 리턴
# 아래는 출력 예시
# 숫자 입력 >> 5
# 120

# 답
def factorial(k):
    result = 1
    for i in range(1, k + 1):
        result *= i
    return result


k = int(input("숫자 입력 >> "))
print(factorial(k))

print("--------------------------")

# 친구들 퀴즈
'''
Quiz4-1. [학생퀴즈] 소수판별하기(소수: 1이나 자기자신으로만 나누어 떨어지는 수)
is_prime() 함수를 만든다.
인수로 1개의 숫자를 받는다.
인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면, "소수 아님" 리턴한다.
'''
def is_prime(prime_number):
    num = 0
    for i in range(2, prime_number):
        if prime_number%i==0:
           num = 1

    if num == 0:
        return print("{0}는 소수입니다.".format(prime_number))
    else:
        return print("{0}은 소수가 아닙니다.".format(prime_number))

result = is_prime(2)
print(result)  # 소수
result = is_prime(13)
print(result)  # 소수
result = is_prime(36)
print(result)  # 소수 아님

'''
Quiz4-2. [학생퀴즈] get_compliment() 함수를 만든다. 이 함수에 '고구마' 또는 '맛있는'이 들어가는 말을 입력하면 그에 해당하는 답변을 리턴한다.
'고구마'가 들어가는 말을 입력하면 '왓쇼이!', '맛있는'이 들어가는 말을 입력하면 '우마이!',
'놀랄 만한', '황당한', '굉장한'이 들어가는 말을 입력하면 '요모야..!', 특정 단어가 하나라도 들어가지 않는다면 '으무!'를 리턴한다.
'''

def get_compliment(rengoku):
    if rengoku.find('고구마'):
        return print("왓쇼이!")
    elif rengoku.find('맛있는'):
        return print("우마이!")
    elif rengoku.find('놀랄 만한') and rengoku.find('황당한') and rengoku.find('굉장한'):
        return print("요모야..!")
    else:
        return print("으무!")

result = get_compliment('고구마 된장국')
print(result) # 왓쇼이!
result = get_compliment('맛있는 크레이프')
print(result) # 우마이!
result = get_compliment('놀랄 만한 상황')
print(result) # 요모야..!
result = get_compliment('좋은 마음가짐이다!')
print(result) # 으무!

#------------------------------------------------------

# Quiz5-1. 모듈이란?
#필요한 것들끼리 부품처럼 잘 만들어진 파일같은 것

# Quiz5-2. 패키지란?
#묘둘들을 모아놓은 집합

# Quiz5-3. theater_module.py 모듈(파일)의 price 함수를 p학번 라는 이름으로 호출 하도록 import문을 작성하세요
#import theater_module as p2417
#p2417.price
#
# Quiz5-4. __all__의 역할은?
#이 변수는 정의한 모듈만 쓸 수 있게 해주는 역할
#
# Quiz5-5. 지금 파이썬 파일을 직접실행할 때만 실행되고, 다른 모듈에서 import할 때는 실행되지 않도록 하는 제어문은?
#if __name__ == "__main__":
# Quiz5-6. travel 패키지(폴더) 안에 vietnam.py 모듈(파일) 안의 ThailandPackage
# 클래스를 생성하고 detail 함수를 호출하는 < 가 >, < 나 >, < 다 > 에 들어갈 각 방법은?
# import travel.vietnam
# < 가 >
#trip_to = travel.vietnam.ThailandPackage()
#trip_to.detail()
# from travel import vietnam
# < 나 >
#trip_to = vietnam.ThailandPackage()
#trip_to.detail()
# from travel.vietnam import ThailandPackage
# < 다 >
#trip_to = ThailandPackage()
#trip_to.detail()