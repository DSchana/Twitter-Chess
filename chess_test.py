from Game import *

p1 = Player("Jim", True)
p2 = Player("Jerome", False)

g = Game(p1, p2)

print(g.getBoard())
print(g.updateBoard("e3f5"))
print(g.updateBoard("e2e4"))
print(g.updateBoard("d7d5"))
