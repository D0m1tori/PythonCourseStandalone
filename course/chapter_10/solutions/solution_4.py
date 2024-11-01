firstSrt = input()
firstSet = firstSrt.split()
firstSet = set(firstSet)
secondSrt = input()
secondSet = secondSrt.split()
secondSet = set(secondSet)
sdf = firstSet.union(secondSet) - firstSet.intersection(secondSet)
sdf = list(sdf)
sdf.sort()
print(*sdf)


