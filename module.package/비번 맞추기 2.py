import random

def make_answer():
    list_r = random.sample(range(9+1), 3)
    return "".join(map(str, list_r))

def check(guess, answer):
    strike = 0
    ball = 0
    #숫자 하나 꺼내서 정답에 있고 자리가 같으면 strike += 1
    #숫자 하나 꺼내서 정답에 있고 자리가 다르면 ball += 1
    for i, g in enumerate(guess):
        for j, b in enumerate(answer):
            if guess[i] == answer[j]:
                strike += 1
            else:
                ball += 1
    return strike, ball

if __name__ == '__main__':
    answer = make_answer()
    print(answer)
    strike.ball = check