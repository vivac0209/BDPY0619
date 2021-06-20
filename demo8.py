class Person:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age


p1 = Person(35)
p2 = Person(35)
p3 = p1
print(p1, p2, p3, p1.age, p2.age, p3.age)
print(p1 is p2, p1 is p3)
print(p1 == p2, p1 == p3)
# is 代表p1是不是p2的實例

# 加上def __eq__ 會讓 == 成立

print("before age={}, p1 id={}".format(p1.age, hex(id(p1))))
print("p1.age id={}".format(hex(id(p1.age))))
p1.age = 36
print("before age={}, p1 id={}".format(p1.age, hex(id(p1))))
print("p1.age id={}".format(hex(id(p1.age))))
x = 35
print(hex(id(x)))
x = 36
print(hex(id(x)))
# immutable 這邊重新assgine值 值的會改變記憶體位置