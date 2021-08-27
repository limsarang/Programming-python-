from diary import Date

class contents:

    def __init__(self):
        self.diary_list = []

    def write_diary(self):
        print('\n··· 일기 작성 중 ···')
        Title = input("\n일기의 제목을 입력해주세요! : ")
        #다이어리 객체 만들기
        new_diary = Date(Title)
        #다이어리 속성 설정하기
        new_diary.set_diary()
        #다이어리 self.diary_list에 어펜드하기
        self.diary_list.append(new_diary)

    def modify_diary(self):
        for index, diary in enumerate(self.diary_list):
            print(f'\n{index + 1}번 일기\n {diary}')
        deletion = input("\n수정할 일기에 번호를 입력해주세요! : ")
        self.diary_list[int(deletion) - 1].set_title()
        self.diary_list[int(deletion) - 1].set_diary()

    def delete_diary(self):
        for index, diary in enumerate(self.diary_list):
            print(f'\n{index + 1}번 일기\n {diary}')
        deletion = input("\n삭제할 일기에 번호를 입력해주세요! : ")
        del self.diary_list[int(deletion) - 1]

    def show_diary(self):
        for index, diary in enumerate(self.diary_list):
            print(f'\n{index + 1}번 일기')
            print(diary)

    def __str__(self):
        pass