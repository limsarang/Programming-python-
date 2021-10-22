# 1
# 2
# 3
# 4

'''
 02
 24
 17
'''

import random
반4 = list(range(1, 20))
반4.remove(3)
print(반4)
print(random.choice(반4))  #반4에서 랜덤으로 숫자

id_number = "040212"
print("출생 년도 끝 두자리: " + id_number[0:2] + "\n")
print("출생 년도 끝 두자리: " + id_number[:2] + "\n")
print("출생 년도 끝 두자리: " + id_number[-6:-4] + "\n")

print("출생 년도 끝 두자리: " + id_number[2:] + "\n")
print("출생 년도 끝 두자리: " + id_number[2:6] + "\n")
print("출생 년도 끝 두자리: " + id_number[-4:] + "\n")

# 뒤에서 보는건 -가 편하고 앞에서 보는건 +가  편하다

year = id_number[:2]
month_day = id_number[-4:]
print(month_day)
print(int(year) * int(month_day))
print('곱한결과 : ' + str(int(year) * int(month_day)))


# f-string
name = '임사랑'
age = 17
# %-formatting
print('안녕 나는 %s이야, 내 나이는 %d살이야' % (name, age)) # 외따옴표든 쌍따옴표든 상관 X
# str.format()
print('안녕 나는 {}이야, 내 나이는 {}살이야'.format(name, age))
# f-string
print(f'안녕 나는 {name}이야, 내 나이는 {age}살이야')

print(name * 10) # 문자열 + 문자열, 문자열 + 정수형

student_number = "2417"

print(student_number[:2])
print(student_number[2:])
print(student_number[-2:][1]) #'17' [1]
print(int(student_number[-2:])) # int('03') 숫자 0은 그냥 안나 옴

print("----------------------------------------------------")


#휴대폰 번호를 입력할 때 빼기 있든 없든 없이 출력하기
Phone_Number1 = '010-9386-7908'
Phone_Number2 = '010 3498 4950'
Phone_Number3 = '01038590475'

#1
phoneNumber = Phone_Number1
result = Phone_Number1.replace('-', ' ').replace('-', ' ')
print(result)

#2
result1 = Phone_Number1.replace('-', ' ')
result2 = Phone_Number2.replace('-', ' ')
result3 = Phone_Number3.replace('-', ' ')
print("전화번호 1 : {0}\n전화번호 2 : {1}\n전화번호 3 : {2}\n".format(result1, result2, result3))

print("----------------------------------------------------")


