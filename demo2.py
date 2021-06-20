x = 5
print("x=" , x, hex(id(x)))
# 把x=5 改成x=6
x = 6
print("x=" , x, hex(id(x)))

# 值改變 但記憶體位置不會變

l1 = [5]
print("l1[0]=" , l1[0], "l1 id=", hex(id(l1)),"l1[0] id=" , hex(id(l1[0])))
l1[0]= 6
print("l1[0]=" , l1[0], "l1 id=", hex(id(l1)), "l1[0] id=" , hex(id(l1[0])))