class Player:
    name = 'Player'     #클래스변수

    def __init__(self):
        self.x = 100

    def where(self):
        print(self.x)


    def __int__(self):
        print('aaa')
        return 1

player = Player()

print(Player.name)
print(player.name)  #name 이라는 객체 변수가 없으면 같은 이름의 클래스 변수가 선택됨

print(Player.name)
print(player.name)


# Player.where(player)      #원칙적인 파이썬에서의 멤버 함수 호출
# player.where()            #-> Player.where(player)
