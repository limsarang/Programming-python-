class Recipe:

    def __init__(self, name):
        #재료, 재료의 개수
        self.ingredient = {}    #중괄호로 빈 딕셔너리 생성(딕셔너리는 key값으로 접근함)
                                # key = value 형태의 값으로 자료를 저장할 수 있는 자료구조
        #내용
        self.contents = ''
        #이름
        self.name = name
        #몇 인분 인지
        self.people = 1
        #url(요리영상링크)
        self.video = ''

    def set_contents(self):
        contents = input('레시피 내용을 입력해주세요 >> ')
        self.contents = '입력된 정보가 없습니다..' if contents == '' else contents

    def set_people(self):
        people = input('몇 인분 인가요? >> ')
        self.people = 1 if people == '' else people

    def set_video(self):
        video = input('레시피 영상 주소를 입력해주세요 >> ')
        self.video = '입력된 링크가 없습니다..' if video == '' else video

    def set_ingredient(self):
        while True:
            ingredient = input("재료를 입력 해주세요! >> (입력예시 : '감자 100')\n재료 입력이 끝났으면 엔터를 눌러주세요~ >> ")
            if ingredient == '':
                break
            ingredient_name, ingredient_gram = ingredient.split()
            #기준을 정하여 문자열을 나누는 함수
            # ex) 강아지 = '강아지는+귀엽다' => 강아지.split('+') == 강아지는, 귀엽다

            self.ingredient[ingredient_name] = ingredient_gram
            #{'감자 ' : '200', '당근' : '100' }

    def __str__(self):
        return  f'==================레시피=====================\n레시피 : {self.name}\n양 : {self.people}인분\n정보 : {self.contents}\n영상 링크 : {self.video}\n재료 : {self.ingredient}'

    def set_recipe(self):
        self.set_people()
        self.set_ingredient()
        self.set_video()
        self.set_contents()

# 카레 = Recipe('카레')
# 카레.set_recipe()
# print(카레)