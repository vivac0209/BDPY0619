# radius半徑
radius = 2.0
area = radius * radius * 3.14
print(radius, area)

print("radius=%f, area=%f" % (radius, area))
#只顯示到小數點後兩位
print("radius=%.2f, area=%.2f" % (radius, area))

print("radius=%(r).2f, area=%(a).2f" % {'r': radius, 'a': area})
print("radius=%(r).2f, area=%(a).2f" % {'a': area, 'r': radius})
print("radius={}, area={}".format(radius, area))
print("radius={:.2f}, area={:.2f}".format(radius, area))

print("radius={0:.2f}, area={1:.2f}".format(radius, area))
print("radius={1:.2f}, area={0:.2f}".format(area, radius))

print("radius={r:.2f}, area={a:.2f}".format(r=radius, a=area))


print(f"radius={radius}, area={area}")