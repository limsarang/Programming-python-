class Drink:
    _CUPS = ('레귤러', '점보')
    _ICES = ('0%', '50%', '100%', '150%')
    _SUGARS = ('0%', '50%', '100%', '150%')

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cup = 0        #'레귤러'
        self.ice = 2         #'100%'
        self.sugar = 2

    def set_cup(self):
        for index, cup in enumerate(Drink._CUPS):    #컵 종류 보여주기
            print(f'{index + 1} : {cup}')
        cup = input('컵사이즈를 선택해주세요! >> ')      #컵 선택
        if cup == '':
            self.cup = 0
        else:
            cup = int(cup)
            self.cup = cup - 1  #컵 self에 넣기

        if self.cup == 1:       #점보면 +500원
            self.price += 500

    def set_ice(self):
        for index, ice in enumerate(Drink._ICES):               #얼음량 종류 보여주기
            print(f'{index + 1} : {ice}')
        ice = input('얼음량을 선택해주세요! >> ')        #선택
        # if ice == '':
        #     self.ice = 2
        # else:
        #     self.ice = int(ice) - 1                  #self.ice에 넣기
        self.ice = 2 if ice == '' else int(ice) - 1 #위츼 if문과 같은 문장

    def set_sugar(self):
        for index, sugar in enumerate(Drink._SUGARS):          #당도 보여줌
            print(f'{index + 1} : {sugar}')
        sugar = input('당도를 선택해주세요! >> ')      #당도 선택
        self.sugar = 2 if sugar == '' else int(sugar) - 1      #self.sugar에 넣기

    def order(self):
        self.set_cup()
        self.set_ice()
        self.set_sugar()

    def __str__(self):
        return f'\n이름 : {self.name}\n가격 : {self.price}원\n컵 사이즈 : {Drink._CUPS[self.cup]}\n얼음양 : {Drink._ICES[self.ice]}'\
            + f'\n당도 : {Drink._SUGARS[self.sugar]}'

class Coffee(Drink):
    pass

class Bubbletea(Drink):
    _PEARLS = ('타피오카 펄', '화이트 펄', '알로에')

    def __init__(self, name, price):
        super().__init__(name, price)
        self.pearl = 0         #타피오카

    def set_pearl(self):
        for index, pearl in enumerate(Bubbletea._PEARLS):
            print(f'{index + 1} : {pearl}')
        pearl = input('펄을 골라주세요! >> ')
        self.pearl = 0 if pearl == '' else int(pearl) - 1

    def order(self):
        super().order()
        self.set_pearl()

    def __str__(self):
        result = super().__str__()
        return result + f'\n펄 종류 : {Bubbletea._PEARLS[self.pearl]}'


class Order:
    def __init__(self):
        self.menu = []          #self.menu 매장에 있는 음료수 전체
        self.init_menu()        #init_menu()
        self.order_menu = []   #self.order_menu 내가 고른 메뉴들

    def init_menu(self):
        사랑이꺼 = Coffee('카페모카', 2500)
        하람이꺼 = Bubbletea('오레오 쉐이크', 3900)
        에스더꺼 = Bubbletea('말차 우유', 1009)

        self.menu.append(사랑이꺼)
        self.menu.append(하람이꺼)
        self.menu.append(에스더꺼)

    def show_menu(self):
        for index, drink in enumerate(self.menu):
            print(f'{index + 1} : {drink.name} | {drink.price}원')

    def sum_price(self):
        sum_value = 0
        for drink in self.order_menu:
            sum_value += drink.price
        return sum_value

    def order_drink(self):
        while True:
            self.show_menu()                                              #메뉴 보여줌
            drink = input('메뉴를 선택해주세요! >> ')                       #메뉴 선택
            drink = int(drink) - 1
            new_drink = self.menu[drink]
            new_drink.order()                                             #옵션 선택
            self.order_menu.append(new_drink)                             #self.order_menu에 추가
            is_add = input('더 주문하시겠습니까?(n: 종료) >> ')              #더 주문?
            if is_add == 'n':
                break
        print(self)         #주문내역 보여주자


    def __str__(self):
        s = '-' * 20 + ' 주문 내역 ' + '-' * 20               #주문내역 제목 보여주자
        for drink in self.order_menu:                                   #주문한 음료수들 목록 보여주자
            s += str(drink)
        s += f'\n총 금액 >> {self.sum_price()}원'                 #총 합계 가격 보여주자
        return s

# 사랑이꺼 = Bubbletea('우유라뗴', 2500)
# 사랑이꺼.order()
# print(사랑이꺼)

order = Order()
order.order_drink()