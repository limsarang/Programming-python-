class 강원도패키지:
    def __init__(self):
        self.places = ['강릉 경포수욕장', '속조 바다정원 카페']

    def __str__(self):
        return str(self.places)

if __name__ == '__main__':
    gp = 강원도패키지()
    print(gp)