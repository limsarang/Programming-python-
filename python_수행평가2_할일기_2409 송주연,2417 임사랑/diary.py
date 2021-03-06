class Date:
    _IMOJI = ('๐ฐ', '๐ฅ', '๐ค', 'โบ', '๐คฉ')

    def __init__(self, Title):
        #์ผ๊ธฐ ์ ๋ชฉ
        self.Title = Title
        #์ผ๊ธฐ๋ฅผ ์ด ๋ ์ง
        self.date = ''
        #์ผ๊ธฐ๋ฅผ ์ด ๋ ์ ๋ ์จ
        self.weather = ''
        #์ผ๊ธฐ ๋ด์ฉ
        self.dairy = ''
        #์ผ๊ธฐ๋ฅผ ์ฐ๊ณ  ๋ ๋ค ๋ด ๊ธฐ๋ถ (ex:์ต๊ณ ๋ก ์ข๋ค๋ฉด 5๋ฅผ ์๋ ฅ, ๋ง์ด ์ฐ์ธํ๋ค๋ฉด 1์ ์๋ ฅ)
        self.mood = 3

    def set_title(self):
        Title = input("\n์ผ๊ธฐ์ ์ ๋ชฉ์ ์๋ ฅํด์ฃผ์ธ์! : ")
        self.Title = '์๋ ค์ฃผ์ธ์...' if Title == '' else Title

    def set_date(self):
        date = input('์ค๋ ๋ ์ง๋? (ex 2021. 1. 1.) : ')
        self.date = '์๋ ค์ฃผ์ธ์...' if date == '' else date

    def set_weather(self):
        weather = input('๋ ์จ๋ ์ด์ผ๊ธฐ ํด์ฃผ์ธ์! : ')
        self.weather = '์๊ธฐํด์ฃผ์จ์ผ๋ฉด ์ข๊ฒ ๋ค...!!' if weather == '' else weather

    def set_dairy(self):
        dairy = input('์ค๋ ๋์ ํ๋ฃจ๋ฅผ ์ญ๋ฃจ๋ฃฉ ์ ์ด๋ด๋ ค๊ฐ๋ด์ ๐ : ')
        self.dairy = '...์จ ์ฐ ๊ฑฐ๋ผ๋ ์ ์ด์ฃผ์ธ์ ๐ข' if dairy == '' else dairy

    def set_mood(self):
        for index, mood in enumerate(Date._IMOJI):
            print(f'{index + 1} : {mood}')
        mood = input('๋ง์ง๋ง ์ง๋ฌธ!! ์ค๋์ ๊ธฐ๋ถ์?!(ex:์ต๊ณ ๋ก ์ข๋ค๋ฉด 5๋ฅผ ์๋ ฅ, ๋ง์ด ์ฐ์ธํ๋ค๋ฉด 1์ ์๋ ฅํด์ฃผ์ธ์โจ) : ')
        if mood == '':
            self.mood = 0
        else:
            mood = int(mood)
            self.mood = mood - 1

    def __str__(self):
        return f'โจ====๐น====๐๋ด๊ฐ ์ ์ ๋์ ํ๋ฃจ๐====๐น====โจ\n์ ๋ชฉ : [ {self.Title} ]\n๊ทธ ๋  ๋ ์ง [ {self.date} ]\n๊ทธ ๋  ๋ ์จ [ {self.weather} ]\n์ญ๋ฃจ๋ฃฉ ์ ์ด๋ณธ ํ๋ฃจ [ {self.dairy} ]' \
               f'\n๊ทธ๋ ๋์ ๊ธฐ๋ถ [ {Date._IMOJI[self.mood]} ]\n=========================================='

    def set_diary(self):
        f'{self.date} ๋ ์ผ๊ธฐ'
        self.set_date()
        self.set_weather()
        self.set_dairy()
        self.set_mood()