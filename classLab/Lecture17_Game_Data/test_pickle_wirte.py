import pickle

class NPC:
    def __init__(self,name,x,y):
        self.name, self.x,self.y = name,x,y

    def show(self):
        print(f'Name:{self.name} Pos:({self.x}, {self.y})')

# yuri = [NPC('Yuugiri',100,200),NPC()
npc = [NPC('Yuugiri',100,200),NPC('Hien',200,300)]
# yuri.show()

with open('npcs.pickle','wb')as f:
    pickle.dump(npc,f)