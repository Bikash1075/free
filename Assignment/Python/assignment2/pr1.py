# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

# Print the expected output - 50
# SampList : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

#   Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

SampList = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in range(len(SampList)):
    for j in range(len(SampList)):
        if SampList[i][1]>SampList [j][1]:
            SampList[i],SampList[j]=SampList[j],SampList[i]
            print(SampList[i],SampList[j])
print(SampList)


SampList = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in range(len(SampList)):
    for j in range(len(SampList)):
        if SampList[i][1]<SampList [j][1]:
            SampList[i],SampList[j]=SampList[j],SampList[i]
            print(SampList[i],SampList[j])
print(SampList)


