class Course():
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __str__(self):
        return "course name=%s, duration=%s" % (self.name, self.duration)

    def __repr__(self):
        return '{}'.format({"name":self.name,"duration":self.duration})

f1 = Course("BDPY資料處理", "35hr")
print(f1)
print([f1])

print("str format=%s, repr format=%r" % (f1, f1))
print("str format={0!s}, repr format={0!r}".format(f1))
print("{0!a}".format(f1))

# a 是沒有辦法顯示中文的 a的顯示方式跟repr一樣

