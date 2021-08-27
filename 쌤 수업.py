class Celebrity:
    def __init__(self, name):
        #name
        self.name = name

    def set_name(self, name):
        self.name = name

    def set_entertainment(self, entertainment):
        self.entertainment = entertainment

    def __str__(self): #문자열(string)화 할 때 자동으로 호출되는 메서드
        return f'이름 : {self.name}\t/\t소속사 : {self.entertainment}'

class Talent(Celebrity):
    def __init__(self, name):
        super().__init__(name)  #클래스(부모클래스)의 생성자 호출

    def set_drama(self, drama):
        self.drama = drama

    def __str__(self):
        return super().__str__() + f'\t/\t드라마 : {self.drama}'
        #super().__str__() == 이름 : {self.name}\t/\t소속사 : {self.entertainment}

class singer(Celebrity):
    def __init__(self, name, song):
        super().__init__(name)
        self.song = song

    def __str__(self):
        return super().__str__() + f'\t노래 : {self.song}'

현진 = singer('현진', '신메뉴')
필릭스 = singer('필릭스', 'Back Door')
필릭스.set_entertainment('JYP')
print(필릭스)

스트레이키즈 = []
스트레이키즈.append(현진)
스트레이키즈.append(필릭스)
print(필릭스)
for i in 스트레이키즈:
    print(i)

senku = Celebrity('이시가미 센쿠')
senku.set_entertainment('과학왕국')
print(senku)

이광수 = Talent('이광수')
이광수.set_entertainment('킹콩')
이광수.set_drama('라이브')
print(이광수)


