from ball2 import make_quiz, check
from custom_error import InvalidLengthError

def save_history(answer, count, name):
    with open('baseball_history.txt', 'a', encoding='utf-8') as f:
        f.write(f'{answer}:{count}:{name}\n')

def load_history(count_name):
    with open('baseball_history.txt', 'r', encoding='utf=8') as f:
        print('====history====')
        while True:
            line = f.readline()     #한 줄 읽기
            if line == '':          #파일 끝이면 끝내기
                break
            print(line.rsplit())    #'\n' 지우기
            line = line.rsplit()        #answer:count:name
            data = line.split(':')      #data[0]: answer, data[1]: count, data[2]: name
            count_name[data[1]] = data[2]   #{3: 'name'}
        #top3
        count_name = sorted(count_name.items()) #정렬하기
        return count_name[:3]                   #top3


answer = make_quiz()
# print(answer)
count = 0
#무한반복
while True:
#  숫자3자리 중복없이 묻자
    guess = input("숫자 세자리는?(t: history, top3) ")
    #t를 입력하면 불러오자, top3
    if guess == 't':
        top3 = load_history()
        print(top3)
        continue
# 숫자인지 아닌지 확인하자
    try:
        guess_int = int(guess)
    except ValueError as e:
        print('숫자를 입력하세요')
        continue
    if len(guess) != len(answer):
        raise InvalidLengthError("정답의 길이와 다른 길이를 입력하셨어요")
        print(f'정답길이와 다른 것 입력 {len(answer)} 문자')
        continue
#  strike, ball 확인하자
    strike, ball = check(guess, answer)
    count += 1
#  출력하자
    print(f'{guess}\tstrike: {strike}\tball: {ball}\t{count}try')
#  strike 가 3일 때, 나가자
if answer == guess:
    print('정답입니다!')
    # 저장하자, 정답, 시도횟수
    name = input('이름은 : ')
    save_history(answer, count, name)
    # 불러오자, top3
    top3 = load_history()
    print(top3)
    break


# 축하해주자
print('축하합니다. 짝짝짝👏👏')