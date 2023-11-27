# import random
# girls = ['sasha','petra','historia','mikasa']
# boys = ['eren','levi','jan','ervin']
# pairs = []
# pairsboys =[]
# random.shuffle(girls)
# for i in range(len(girls)):
#     pairs.append(girls[i] + ' ' + boys[i])
# print(pairs)
# random.shuffle(boys)
# for j in range(len(girls)):
#     pairsboys.append(boys[j] + ' ' + girls[j])
# print(pairsboys)

# a = str(input("Введите мужское имя: "))
# count=0
# for j in range (len(pairsboys)):
#     tempPair = pairsboys[j].split()
#     if tempPair[0] == a:
#         print(tempPair[1])
#     else:
#         count+=1
#     if count==len(pairsboys):
#         print("takogo net")
# b = str(input("Введите женское имя: "))
# count2=0
# for j in range (len(pairs)):
#     tempPair = pairs[j].split()
#     if tempPair[0] == b:
#         print(tempPair[1])
#     else:
#         count2+=1
#     if count2==len(pairs):
#         print("takogo net")       

import random
girls = ['sasha','petra','historia','mikasa']
boys = ['eren','levi','jan','ervin']
pairs = []
pairsboys =[]
random.shuffle(girls)
for i in range(len(girls)):
    pairs.append(girls[i] + ' ' + boys[i])
print(pairs)
random.shuffle(boys)
for j in range(len(girls)):
    pairsboys.append(boys[j] + ' ' + girls[j])
print(pairsboys)

a = str(input("Введите мужское имя: "))
for j in range (len(pairsboys)):
    tempPair = pairsboys[j].split()
    if tempPair[0] == a:
        print(tempPair[1])
b = str(input("Введите женское имя: "))
for j in range (len(pairs)):
    tempPair = pairs[j].split()
    if tempPair[0] == b:
        print(tempPair[1])

# skolkoraz = int(input('Сколько раз выполнить функцию '))
# arr=[]
# for i in range(skolkoraz):
#     numstoarr = int(input('Цифры которые нужжно отправить '))
#     arr.append(numstoarr)
