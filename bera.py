class Icecream:
    def __init__(self, name):   #생성자, 주로 변수 초기화
        self.name = name
    #이름 : name
    #설명 : explanation
    def set_explanation(self, explanation):
        self.explanation = explanation

    def __str__(self):          #우리가 알아보기 쉽게 문자열로 리턴, 주로 print()에서 호출
        return f'이름 : {self.name}'

# 민트초코 = Icecream('민트 초코')
# 민트초코.set_explanation('민트맛 아이스 크림과 초콜릿칩이 쏙쏙')
# print(민트초코)
# print(set_explanation)
#
# 이상한나라의솜사탕 = Icecream('이상한나라의솜사탕')
# print(이상한나라의솜사탕)
#
# 요거트31 = Icecream('31요거트')
# print(요거트31)
#
# 블랙소르베 = Icecream('블랙소르베')
# print(블랙소르베)


class Order:
    _CATEGORIES = ['싱글 레귤러', '더블 레귤러', '파인트']
    _PRICES = [3200, 6200, 8200]
    def __init__(self):
        # 종류 : 콘, 파인트 ...
        self.set_cateries()
        #메뉴
        self.menu = []
        self.init_menu()
        #주문한 메뉴
        self.order_menu = []

    def __str__(self):
        pass
    def set_cateries(self):
        for index, category in enumerate(Order._CATEGORIES):
            print(index+1, category)
        category_num = input('먹고 싶은 아이스크림의 종류를 골라주세요! >> ')
        self.category = int(category_num)
    def init_menu(self):
        self.menu.append(Icecream('민트초코'))
        self.menu.append(Icecream('31요거트'))
        self.menu.append(Icecream('체리쥬빌레'))
    def show_menu(self):
        for index, icecream in enumerate(self.menu):
            print(f'{index + 1}번째 아이스크림 {icecream}')

    def order(self):
        self.show_menu()            #아이스크림 보여주기
        for _ in range(self.category): #종류의 따라 반복
            # 메뉴 선택
            icecream = input('먹고 싶은 아이스크림의 종류를 골라주세요! >> ')
            icecream = int(icecream)
            #주문한 메뉴의 추가
            self.order_menu.append(self.menu[icecream - 1])
        #종류 출력
        print('-'*10 + '주문 내역입니다!' + '-'*10)
        print(order._CATEGORIES[self.category - 1])
        print (str(Order._PRICES[self.category - 1]) + '원')
        #주문 메뉴 출력
        for icecream in self.order_menu:
            print(icecream)
order = Order()
order.order()