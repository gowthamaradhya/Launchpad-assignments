list_1 = [1, 3, 4, 3, 6, 7]
list_2 = []
for i in range(0, len(list_1)):
  if list_1[i] == 3 :
    list_2.append(i)
print(list_2)