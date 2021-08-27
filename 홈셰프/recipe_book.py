from recipe import Recipe

class Recipe_book:
    def __init__(self):
        self.recipe_list = []
        self.init_recipe()

    def add_recipe(self):
        # 추가할 레시피 이름 입력 받기
        global recipe
        name = input("레시피의 이름을 입력해주세용! >> ")
        # 이름 중복 체크
        for recipe in self.recipe_list:
        # 중복되는 레시피 있음
            if recipe.name == name:
            #중복된다고 알려주고 추가안 함
                print('이미 존재하는 레시피 입니다!')
                return
        # 중복되는 레시피 없음(이건 코드가 필요없음)
            # 레시피 객체 생성
        new_recipe = Recipe(name)
        new_recipe.set_recipe()
            # 레시피 리스트에 추가
        self.recipe_list.append(new_recipe)
        return

    def show_recipe(self):
        for index, recipe in enumerate(self.recipe_list):
            print(f'{index + 1}')
            print(recipe)

    # 레시피북에서 레시피 찾기
    def search_recipe(self):
        searched_recipe = []
        #레시피 이름 입력받기(=검색)
        name = input("원하는 레시피를 검색하세요! >> ")
        #내가 찾는 이름 리스트 돌아가면서 찾기
        for recipe in self.recipe_list:
            # 찾는게 있을 때
            if name == recipe.name:
                # 찾은 이름의 레시피를 출력
                print(recipe)
                searched_recipe.append(recipe)
        #찾는게 없을 때(searched_recipe가 비어있다면)
            if len(searched_recipe) == 0:
            # 추가할지 물어보기
                answer = input('찾는 레시피가 없습니다... 추가 하시겠습니까?(1 : 예 / 2 : 아니오) >> ')
            #추가한다고 하면
            elif answer == 1:
                #레시피 추가
                self.add_recipe()
            else:
                return
    # 재료로 해당되는 레시피 찾기
    def search_igdt(self):
        # 빈 셋(set) 생성 > 재료를 중복 제거해서 담은 셋(set)
        all_igdt = set()
        # 페시피 북에 있는 레시피의 재료를 셋에 넣기
        for recipe in self.recipe_list:
            for igdt in recipe.ingredient:
                all_igdt.add(igdt)
        # 다 넣었을때 모든 재료를 보여주기
        for index, igdt in enumerate(all_igdt):
            print(f'{index + 1} : {igdt}')

        #찾을 재료 입력 받기
        search_num = int(input('사용할 재료를 입력해주세요! >> '))
        search_igdt = list(all_igdt)[search_num-1]
        #레시피 리스트의 레시피 -> 레시피 재료 살피기
        for recipe in self.recipe_list:
        # 입력한 재료가 포함되면
            if search_igdt in recipe.ingredient:
            # 해당 레시피 모두 보여주기
                print(recipe)

    def init_recipe(self):
        떡볶이 = Recipe('떡볶이')
        떡볶이.people = 2
        떡볶이.video = 'youtube.com'
        떡볶이.ingredient = {'떡' : '200', '고추장' : '100', '양파' : '300', '물' : '300' }
        self.recipe_list.append(떡볶이)
        
        라면 = Recipe('라면')
        라면.people = 1
        라면.video = 'youtube.com'
        라면.ingredient = {'면': '200', '치즈': '100', '양파': '300', '물': '300'}
        self.recipe_list.append(라면)

        파스타 = Recipe('파스타')
        파스타.people = 2
        파스타.video = 'youtube.com'
        파스타.ingredient = {'면': '200', '로제': '100', '양파': '300', '토마토소스': '300'}
        self.recipe_list.append(파스타)

    def __str__(self):
        pass















