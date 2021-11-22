import string
from string import punctuation

#avt = ([[3,0], [9,1], [4,10], [12,2], [6,1], [7,10]])#результат: 17
avt = (input().replace("(", ""))
avt = avt.replace(")", "")
avt = avt.replace("]", "")
avt = avt.replace("[", "")
avt = avt.split(", ") #знаю, что можно это организовать более компактно, позже переделаю
avt = list(avt)
j = 0
while(j < len(avt)):
    avt[j] = list(avt[j].split(","))
    avt[j] = tuple(avt[j])
    j += 1

tul = tuple(avt)
print(tul)
sum_in = 0
sum_out = 0
i = 0

while(i < len(tul)):
    np = int(tul[i][0])
    sum_in += np
    nm = int(tul[i][1])
    sum_out += nm
    i += 1


print(sum_in - sum_out)