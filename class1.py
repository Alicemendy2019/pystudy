import functools

class Player:
    LEVEL_LIMIT = 10
    @property
    def level(self):
        return self.__level

    @level.setter

    def level(self,value):
        if value > Player.LEVEL_LIMIT :
            self.__level = Player.LEVEL_LIMIT
        else:
            self.__level = value

p1 = Player()
p1.level = 100
print(p1.level)
# print(p1.level)
# p1.level_show()
