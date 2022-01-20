import random
list = []
for i in range(100):
    ist_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    total = ist_dice + second_dice
    list.append(total)

for i in range(2, 12):
    count = list.count(i)
    print(str(i), " Appeared ", str(count), "times", str(count*"*"))









