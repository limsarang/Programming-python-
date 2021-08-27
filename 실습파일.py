def modify_diary(self):
    for index, diary in enumerate(self.diary_list):
        print(f'\n{index + 1}번 일기\n {diary}')
    deletion = input("\n수정할 일기에 번호를 입력해주세요! : ")
    del self.diary_list[int(deletion) - 1]
    self.write_diary()
