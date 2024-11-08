firstSrt = input()
firstSet = firstSrt.split()
firstSet = set(firstSet)
secondSrt = input()
secondSet = secondSrt.split()
secondSet = set(secondSet)
thirdSrt = input()
thirdSet = thirdSrt.split()
thirdSet = set(thirdSet)
print(*set.difference(firstSet, secondSet, thirdSet))
print(*set.difference(secondSet,firstSet, thirdSet))
print(*set.difference(thirdSet, firstSet, secondSet))


