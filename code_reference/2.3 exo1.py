#exo1 list et index
L = ["3","2","4","6"]
min = L[0]
for i in range(len(L)):
    if L[i] < min:
        min = L[i]
print(min)

# Solution 2
L = ["3","2","4","6"]
min = L[0]
i = 0
while i < len(L):
    if L[i]<min:
        min = L[i]
        i+=1
print(min)
