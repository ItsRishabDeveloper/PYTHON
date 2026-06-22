for i in range(1,6):
    print(i)
for i in range(1,11,2):
    print(i)
for i in range(10,0,-1):
    print(i)
sum = 0
for i in range(15):
    sum = sum + i
print(sum)
name = "Rishab"
for ch in name:
    print(ch)
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()
fruits = ["Apple", "Mango", "Banana"]
for index, fruit in enumerate(fruits):
    print(index, fruit)