from decimal import Decimal as Dec

x1 = Dec(2.968)
print(x1)
x2 = Dec('2.968')
print(x2)
x3 = Dec(0.001)*Dec(2968)-Dec(2.968)
print(x3)
x4 = Dec('0.001')*Dec(2968)-Dec('2.968')
print(x4)
