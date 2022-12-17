SampList = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in range(len(SampList)):
    for j in range(len(SampList)-1):
        if SampList[i][1]==SampList [j][1]:
            SampList[i],SampList[j]=SampList[j],SampList[i]
            print(SampList[i],SampList[j])
print(SampList)