import random


def make_quiz():
    list = random.sample(range(1, 9 + 1), 3)
    return "".join(map(str, list))


def check(guess, answer):
    strike = 0
    ball = 0

    for i, g in enumerate(guess):
        for j, a in enumerate(answer):
            if g == a:
                if i == j:
                    strike += 1
                else:
                    ball += 1
    return strike, ball

if __name__ == '__main__':
    answer = make_quiz()
    print(answer)
    strike, ball = check("238, 241")