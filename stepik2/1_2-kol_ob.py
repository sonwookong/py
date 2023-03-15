objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]
#objects = [1, 2, 1, 2, 3]
ans = 0
vr = []
for obj in objects:
    if id(obj) not in vr:
#        print(id(obj))
        vr.append(id(obj))
        ans += 1

print(ans)

#print(len(set(map(id, objects))))