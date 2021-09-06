#1
import math
bill = 62421
bill = 59827
print(bill//100*100) # 첫 번째 방법
print(bill - bill%100) # 두 번째 방법
print(math.floor(bill/100)*100) # 세 번째 방법
print(int(bill/100)*100) # 네 번째 방법


#2
score = 93
print(round(score/10)*10) # 첫 번째 방법
print(round(score, -1)) # 두 번째 방법


#3
import random
print(random.sample(range(1, 45 + 1), 6))


#4
list_r = random.sample(range(1, 9 + 1), 3)
print(list_r)
# print(str(list_r)) 리스트 그대로 출력되서 X
print("".join(str(n) for n in list_r)) # 첫 번째 방법
print("".join(map(str, list_r))) # 두 번째 방법


#5
import datetime
birthday = datetime.datetime(2004, 2, 21)
now = datetime.datetime.now()
print(now - birthday)


#6
christmas = datetime.datetime(2021, 12, 25)
print(christmas - now)


#7
my_birthday = datetime.datetime(2021, 2, 12)
if my_birthday < now:
    my_birthday = my_birthday.replace(year=2022)
print(my_birthday - now)


#8
#마지막 번호 묻기
last_number = input("마지막 번호는?")
#1~마지막 번호까지 숫자 리스트 만들기
list_class = list(range(1, int(last_number) + 1))
#print(list_class)
#반복
while True:
# 뺄 번호 묻기
    exclude_number = input("뺄 번호는?(enter치면 그만 빼기)")
#다 뺐으면 반복 끝내기
    if exclude_number == '':
        break
# 빼자
    list_class.remove(int(exclude_number))
    print(list_class)
#섞기
random.shuffle(list_class)
#출력
print('자리\t학생번호')
for i, number in enumerate(list_class):
    print(f'{i+1}\t{number}')