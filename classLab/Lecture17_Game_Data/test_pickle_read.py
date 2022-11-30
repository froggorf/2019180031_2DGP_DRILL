import pickle

class NPC:
    def __init__(self,name,x,y):
        self.name, self.x,self.y = name,x,y

    def show(self):
        print(f'Name:{self.name} Pos:({self.x}, {self.y})')


with open('npcs.pickle','rb')as f:
    npc = pickle.load(f)
# yuri.show()
# print(yuri.name)
for n in npc:
    n.show()