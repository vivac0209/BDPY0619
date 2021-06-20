poop = {'name': 'poop', 'field': 'python', 'attendee': 10, 'remote': False}
bdpy = {'name': 'bdpy', 'field': 'python', 'attendee': 15, 'remote': True}
andbiz = {'name': 'andbiz', 'field': 'android', 'attendee': 5, 'remote': False}

#把上面三種課程的字典 裝進list裡
# list
courses = [poop, bdpy, andbiz]

# 把p 改成大寫的P
print(courses)
courses[0]["name"] = "Poop"
print(courses)

# 多加一個課程
# 但在aiocv中 attendee多打一個s attendees
# 用for loop跑 把attendee的print出時會跑出錯誤

aiocv = {'name': 'aiocv', 'field': 'python', 'attendees': 25, 'remote': False}
courses2 = [poop,bdpy, andbiz, aiocv]
for i in range(len(courses2)):
    print(courses2[i]["name"])
for i in range(len(courses2)):
    print(courses2[i]["attendee"])
