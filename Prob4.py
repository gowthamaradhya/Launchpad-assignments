list_1 = [1, 1, 2, 3, 5, 8, 8, 13, 21, 34, 55, 89]
list_2 = []
for i in list_1:
  if i not in list_2:
    list_2.append(i)
print(list_2)