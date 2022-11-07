#Zad 7
import random
lst=[]
for i in range(10):
    lst.append(random.randint(1,100))
if lst[1]>lst[0]:
    highest=lst[1]
    nextHighest=lst[0]
    pos0=0
    pos1=1
else:
    highest=lst[0]
    nextHighest=lst[1]
    pos0=1
    pos1=0

for i in range(2,len(lst)):
    if lst[i]>=highest:
        pos0=pos1
        pos1=i
        nextHighest = highest
        highest = lst[i]
    elif lst[i]>=nextHighest:
        nextHighest=lst[i]
        pos0=i
print(lst,highest, "&", pos1, nextHighest, "&", pos0)
    
