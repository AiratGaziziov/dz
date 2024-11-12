def findmax(b, c):
    a = int(input("Введите число a: "))
    if a > 0:
        return max(a, b, c)
    else:
        return -1
b = 2
c = 8
print(findmax(b, c))
