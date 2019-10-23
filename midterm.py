with open('report.txt') as f:
    data = [i.split() for i in f.readlines()]

head = data[0]
head.insert(0, '名次')
head.append('总分')
head.append('平均分')

score = []
for i in data[1:]:
    ls = [int(x) for x in i[1:]]
    ts = sum(ls)
    i.append(ts)
    i.append('%.2f' % (ts / 9))
    score.append(i)
f_score = sorted(score, key=lambda x: x[-1], reverse=True)

each_score = [0, '平均']
for i in range(1, 12):
    j = 0
    k = 0
    for num in f_score:
        j += float(num[i])
        k += 1
    each_score.append('%2.f' % (j / k))

f_score.insert(0, each_score)

x = 1
for i in f_score[1:]:
    i.insert(0, x)
    x += 1

for i in f_score[1:]:
    for j in range(2, len(i)-2):
        if int(i[j]) < 60:
            i[j] = '不及格'

f_score.insert(0, head)

with open('result.txt', 'w', encoding='utf-8') as j:
    for i in f_score:
        for n in i:
            j.write(str(n) + '   ')
        j.write('\n')

