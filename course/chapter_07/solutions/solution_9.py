a= input()
lst1 = []
while(a != ""):
    lst1.append(int(a))
    a = input()
lst1.sort()
print(f"Минимальная оценка: {lst1[0]}")
print(f"Максимальная оценка: {lst1[len(lst1)-1]}")
print(f"Отсортированные оценки: {lst1}")
