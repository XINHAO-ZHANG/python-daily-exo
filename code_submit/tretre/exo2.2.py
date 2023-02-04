#exo1 list et index
L = ["3","2","4","6"]
min = L[0]
for i in range(len(L)):
    if L[i] < min:
        min = L[i]
print(min)

#exo2 list et index
L = ["5","3","6","7"]
min = L[0]
for i in L[1:]:
    if i < min:
        print('not ok')
        break
    else:
        print("OK")