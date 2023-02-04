#exo 3
def sortedornot(S):
    for i in range(len(S)-1):
        if S[i+1]>S[1]:
            print('False')
            break
    print('True')
S= ['5','3','2','2']
sortedornot(S)

#exo4
def comparelength():
    L = ['yes','no','wow','shuanqu','allez']
    Total_len = 0
    i = 0
    while i < len(L):
        Total_len = Total_len + len(L[i])
        i=i+1
    Aver_len = Total_len / len(L)
    count = 0
    for j in range(len(L)):
        if len(L[j]) >= int(Aver_len):
            count+=1
    return Aver_len,count
comparelength()