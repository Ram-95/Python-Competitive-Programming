from collections import defaultdict


l = ["eat", "tea", "tan", "ate", "nat", "bat"]
k = list(enumerate(l))

k = [(''.join(sorted(x[1])), x[0]) for x in k]
k.sort()
#print(f'{k}')

d = {}
for i in k:
    if i[0] not in d:
        d[i[0]] = [l[i[1]]]
    else:
        d[i[0]].append(l[i[1]])

print(f'{list(d.values())}')



''' Other way using defaultdict from collections module.'''
ans = defaultdict(list)
for word in l:
    ans[''.join(sorted(word))].append(word)

print(ans.values())
