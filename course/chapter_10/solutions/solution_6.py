firstSrt = input()
firstSet = firstSrt[::]
firstSet = set(firstSet)
secondSrt = input()
secondSet = secondSrt[::]
secondSet = set(secondSet)
sdf = firstSet.intersection(secondSet)
sdf = list(sdf)
sdf.sort()
print(*sdf)


